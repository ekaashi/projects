# # image recognition
# # steps-
# # read-open-hold
import cv2
import cv2.data
modelpath = cv2.data.haarcascades +"haarcascade_frontalface_default.xml"
trained =cv2.CascadeClassifier(modelpath)
img = cv2.imread("image1.jpg")
#img2= cv2.rectangle(img,(100,100),(200,200),(255,0,0),2) #rectangle oveer img
#img_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convrting to gray

#cv2.imshow("new img",img2)
# 0 kyunki bo hr millisecond khulega

faces = trained.detectMultiScale(img,1.3,2)
for face in faces:
    x,y,w,h =face
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
cv2.imshow("new img",img)
cv2.waitKey(0)