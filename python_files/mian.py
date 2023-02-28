# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 19:15:36 2023

@author: ME
"""
import numpy as np
import face_recognition
import pickle
import cv2
import cvzone
import os
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
#Set graphics and read background image
modefolder = r'C:/Users/ME/Desktop/Blessing_AI/Face_attendance/Resources/background.png'
imgBackground = cv2.imread(modefolder)

# Importing the mode images into a list
folderModePath = r'C:/Users/ME/Desktop/Blessing_AI/Face_attendance/Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

#import encoding file
print("Loading encode file...")
file = open(r"C:/Users/ME/Desktop/Blessing_AI/Face_attendance/EncodeFile.p","rb")
encodeListKnownWithIds = pickle.load(file)
encodeListKnown, studentsIds = encodeListKnownWithIds
file.close()

print(encodeListKnown)
print("Encoded file loaded completely")


while True:
    success,img = cap.read()

    #resize image to make it smaller
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    #find location and encodings of current frame
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

    imgBackground[162:162 + 480,55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[1]
    
    print(faceCurFrame)
    # print(encodeCurFrame)
    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                match_index = np.argmin(faceDis) 
                #print(faceDis)
                print(" Match index:",match_index)
                if matches[match_index]:
                        y1, x2, y2, x1 = faceLoc
                        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                        bbox = 55 + x1, 162 + y1, x2 - x1 , y2 - y1
                        imgBackground = cvzone.cornerRect(imgBackground,bbox,rt=0)
                        
                
                
    
    cv2.imshow("Face attendance",imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
# Releasing camera
cap.release()
# Destroying all opened OpenCV windows
cv2.destroyAllWindows()
    