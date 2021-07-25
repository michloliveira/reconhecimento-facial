import cv2

xml_haar_cascade = 'haarcascade_frontalface_alt.xml'

#Carregando Classificador
cv2.CascadeClassifier(xml_haar_cascade)

#Inicializando Camera
camera = cv2.VideoCapture(0)

#Definindo Resolucao Camera
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while not cv2.waitKey(20) & 0xff == ord("q"):
    ret, frame = camera.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", frame_gray)
    cv2.imshow("color", frame)