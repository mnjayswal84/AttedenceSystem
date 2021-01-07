import os
import cv2
import face_recognition
import numpy as np

path = "C:\\Users\\ABDEALIVORA\\Projects\\MyAttandance\\media\\student\\"


def GetImage(path):
    faces = []
    name =[]
    for root, directory, filenames in os.walk(path):
        for filename in filenames:
            img = os.path.join(root, filename)
            print(filename)
            imgs = cv2.imread(img)
            gray_img = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)
            face_decade = cv2.CascadeClassifier(
                "C:\\Users\\ABDEALIVORA\\Projects\\MyAttandance\\haarcascade_frontalface_default.xml")
            face = face_decade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)
            if len(face) != 1:
                continue
            (x, y, w, h) = face[0]
            gray = gray_img[y:y + h, x:x + w]
            labels = [0] * len(faces)
            faces.append(gray)
            name.append(labels)
    return faces,labels


x,y= GetImage(path)
recognizer = cv2.face_LBPHFaceRecognizer.create()
recognizer.train(x,np.array(y))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
