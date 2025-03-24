import cv2
from config import VIDEO_PATH, FRAME_WIDTH, FRAME_HEIGHT, ROI_X, ROI_Y, ROI_W, ROI_H
from detector import detect_and_recognize

def main():
    # Abrir el video
    cap = cv2.VideoCapture(VIDEO_PATH)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    # Configurar la ventana
    cv2.namedWindow("Deteccion de Placas y OCR", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Deteccion de Placas y OCR", FRAME_WIDTH, FRAME_HEIGHT)

    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Dibujar el rectangulo de la ROI en el frame
        cv2.rectangle(frame, (ROI_X, ROI_Y), (ROI_X + ROI_W, ROI_Y + ROI_H), (255, 0, 0), 2)

        # Procesar el frame para detectar matriculas y aplicar OCR
        frame = detect_and_recognize(frame)

        # Mostrar el frame resultante
        cv2.imshow("Deteccion de Placas y OCR", frame)

        # Guardar la imagen al presionar la tecla 's'
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("capturas/" + str(count) + ".jpg", frame)
            cv2.waitKey(500)
            count += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

