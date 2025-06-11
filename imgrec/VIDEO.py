




import cv2
import cv2.data
modelpath = cv2.data.haarcascades +"haarcascade_frontalface_default.xml"
trained =cv2.CascadeClassifier(modelpath)
camera = cv2.VideoCapture(0)

while True:
    status, frame = camera.read()
    faces = trained.detectMultiScale(frame,1.3,2)
    for face in faces:
        x,y,w,h =face
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),2) 
        cv2.imshow("new img",frame)
        cv2.waitKey(1)

   # frame = cv2.imread("image1.jpg")
   
   


