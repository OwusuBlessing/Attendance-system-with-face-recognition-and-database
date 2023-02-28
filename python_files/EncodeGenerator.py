# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:43:28 2023

@author: ME
"""
import os
import pickle
import cv2
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage



firebase_admin.delete_app(firebase_admin.get_app())

cred = credentials.Certificate(r"C:/Users/ME/Desktop/Blessing_AI/Face_attendance/python_files/Service_account_key.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://face-attendance-system-c9176-default-rtdb.firebaseio.com/',
    'storageBucket':'face-attendance-system-c9176.appspot.com'})

# Importing student images and ids
folderPath = 'Images'
PathList = os.listdir(folderPath)
imgList = []
studentsIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    id_ = os.path.splitext(path)[0]
    studentsIds.append(id_)
    #Send image data to database
    file_name = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_name)    
#Generate encodings
 
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
 
    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentsIds]
print("Encoding Complete")

#save encodings
file = open("Encodefile.p","wb")
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File saved...")





