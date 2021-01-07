import glob
from datetime import datetime

import cv2
import face_recognition
import numpy
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import faculty, student


def index(request):
    return render(request, 'index.html')


def studentData(request):
    if request.method == 'POST' and request.FILES['studentimage']:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        image = request.FILES.get('studentimage')
        if password1 == password2:
            if student.objects.filter(email=email).exists():
                return HttpResponse("email taken")
            else:
                student.objects.create(username=username, email=email, studentimage=image,
                                       password1=make_password(password1, salt=None, hasher='default'))
                return redirect('index')
        else:
            return HttpResponse("Password Not Match")
    return render(request, 'student.html')


def facultyData(request):
    if request.method == "POST" and request.FILES['facultyimage']:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        image = request.FILES.get('facultyimage')
        if password1 == password2:
            if faculty.objects.filter(email=email).exists():
                return HttpResponse("email taken")
            else:
                faculty.objects.create(username=username, email=email, facultyimage=image,
                                       password1=make_password(password1, salt=None, hasher='default'))
                return redirect('index')
    return render(request, 'faculty.html')


def loginstudent(request):
    folders = glob.glob('student\\*')
    image_list = []
    for folder in folders:
        for f in glob.glob(folder + '/*.jpg'):
            image_list.append(f)
    print(image_list)

    read_images = []
    for image in image_list:
        read_images.append(cv2.imread(image, cv2.IMREAD_GRAYSCALE))
    print(read_images)

    def Encodings(read_images):
        encodeList = []
        for img in read_images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def Attandance(name):
        with open('StudentAttandance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                datestring = now.strftime("%m/%d/%Y, %H:%M:%S")
                f.writelines(f'\n{name},{datestring}')

    encodeListKnown = Encodings(read_images)
    print(encodeListKnown)
    print("Programing Complete")
    webcam = cv2.VideoCapture(0)
    key = cv2.waitKey(1)
    while True:
        successful_frame_read, frame = webcam.read()
        imgS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        Face_cur_frame = face_recognition.face_locations(imgS)
        encode_cur_frame = face_recognition.face_encodings(imgS, Face_cur_frame)

        for encodeFace, FaceLoc in zip(encode_cur_frame, Face_cur_frame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchindex = numpy.argmin(faceDis)

            if matches[matchindex]:
                name = image_list[matchindex].upper()

                y1, x2, y2, x1 = FaceLoc
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                Attandance(name)

        cv2.imshow('Hey You Look Beautiful Keep Watch In Camera', frame)
        key = cv2.waitKey(1)
        if key == 65 or key == 97:
            break


def loginfaculty(request):
    folders = glob.glob('faculty\\*')
    image_list = []
    for folder in folders:
        for f in glob.glob(folder + '/*.jpg'):
            image_list.append(f)
    print(image_list)

    read_images = []
    for image in image_list:
        read_images.append(cv2.imread(image, cv2.IMREAD_GRAYSCALE))
    print(read_images)

    def Encodings(read_images):
        encodeList = []
        for img in read_images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def Attandance(name):
        with open('FacultyAttandance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                datestring = now.strftime("%m/%d/%Y, %H:%M:%S")
                f.writelines(f'\n{name},{datestring}')

    encodeListKnown = Encodings(read_images)
    print(encodeListKnown)
    print("Programing Complete")
    webcam = cv2.VideoCapture(0)
    key = cv2.waitKey(1)
    while True:
        successful_frame_read, frame = webcam.read()
        imgS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        Face_cur_frame = face_recognition.face_locations(imgS)
        encode_cur_frame = face_recognition.face_encodings(imgS, Face_cur_frame)

        for encodeFace, FaceLoc in zip(encode_cur_frame, Face_cur_frame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchindex = numpy.argmin(faceDis)

            if matches[matchindex]:
                name = image_list[matchindex].upper()

                y1, x2, y2, x1 = FaceLoc
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
                Attandance(name)

        cv2.imshow('Hey You Look Beautiful Keep Watch In Camera', frame)
        key = cv2.waitKey(1)
        if key == 65 or key == 97:
            break
