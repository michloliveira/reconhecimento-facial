import cv2

xml_haar_cascade = 'haarcascade_frontalface_alt.xml'

#Carregando Classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

#Inicializando Camera
camera = cv2.VideoCapture(0)

#Definindo Resolucao Camera
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while not cv2.waitKey(20) & 0xff == ord("q"):
    ret, frame_color = camera.read()
    frame_gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
    faces = faceClassifier.detectMultiScale(frame_gray)

    for x, y, w, h in faces:
        cv2.rectangle(frame_color, (x,y), (x + w, y + h), (0,255,0),2) #desenha retangulo

    #cv2.imshow("gray", frame_gray)
    cv2.imshow("color", frame_color)