import cv2
import pytesseract
from config import CASCADE_PATH, MIN_AREA, ROI_X, ROI_Y, ROI_W, ROI_H

# Cargar el clasificador Haar cascade
plate_cascade = cv2.CascadeClassifier(CASCADE_PATH)

def process_plate(frame, x, y, w, h):
    """
    Dibuja el rectángulo de la matrícula detectada y extrae la ROI para preprocesamiento.
    """
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(frame, "Matricula detectada", (x, y - 5),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

    # Extraer la ROI correspondiente a la matricula
    roi_plate = frame[y:y+h, x:x+w]

    # Preprocesamiento: convertir a gris, aplicar mediana y umbralizacion
    roi_gray = cv2.cvtColor(roi_plate, cv2.COLOR_BGR2GRAY)
    roi_blur = cv2.medianBlur(roi_gray, 3)
    _, roi_thresh = cv2.threshold(roi_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return roi_thresh

def detect_and_recognize(frame):
    """
    Procesa el frame para detectar matrículas dentro de la ROI, realiza OCR y muestra el texto reconocido.
    """
    # Convertir a escala de grises para la deteccion
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    plate_text = ""

    for (x, y, w, h) in plates:
        area = w * h
        if area > MIN_AREA:
            # Verificar que la deteccion esté completamente dentro de la ROI definida
            if x >= ROI_X and y >= ROI_Y and (x + w) <= (ROI_X + ROI_W) and (y + h) <= (ROI_Y + ROI_H):
                roi_thresh = process_plate(frame, x, y, w, h)
                config = "--psm 7"  # Asume que el texto es una sola linea
                texto = pytesseract.image_to_string(roi_thresh, config=config)
                plate_text = texto.strip().replace(" ", "").replace("\n", "")

                # Validar que la matricula tenga 9 caracteres
                if len(plate_text) == 9:
                    cv2.putText(frame, plate_text, (x, y + h + 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    print("Caracteres detectados en la matrícula:", plate_text)
                else:
                    plate_text = ""
                # Mostrar la ROI procesada
                cv2.imshow("ROI", roi_thresh)
    return frame

