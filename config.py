import cv2
import pytesseract

# Configuracion de pytesseract (Cambiar segun corresponda)
pytesseract.pytesseract.tesseract_cmd = r'/bin/tesseract'

# Rutas (Cambiar segun corresponda)
CASCADE_PATH = "/home/hisui/Escritorio/EquipoU2/iti-271362_eq_07_u2/iti-271362_eq_07_u2_source/dataset/haarcascade_matriculas.xml"
#VIDEO_PATH = "/home/hisui/Escritorio/EquipoU2/iti-271362_eq_07_u2/iti-271362_eq_07_u2_source/pruebas/pruebamini.mp4"
#video_path alternativo:
VIDEO_PATH = "/home/hisui/Descargas/manana.mp4"

# Parámetros de video
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

# Región de interés (ROI) para búsqueda de matrículas
ROI_X = 0
ROI_Y = 950
ROI_W = 3900
ROI_H = 1100
#ROI alternativo, para "pruebamini":
#ROI_X = 0
#ROI_Y = 420
#ROI_W = 1200
#ROI_H = 350

# Area minima para considerar una deteccion valida
MIN_AREA = 1300

