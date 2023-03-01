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
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

firebase_admin.delete_app(firebase_admin.get_app())
cred = credentials.Certificate(r"C:/Users/ME/Desktop/Blessing_AI/Face_attendance/python_files/Service_account_key.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://face-attendance-system-c9176-default-rtdb.firebaseio.com/',
    'storageBucket':'face-attendance-system-c9176.appspot.com'})

bucket = storage.bucket()
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

mode_type = 0
counter = 0
id_ = -1
while True:
    success,img = cap.read()

    #resize image to make it smaller
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    #find location and encodings of current frame
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

    imgBackground[162:162 + 480,55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[mode_type]
    
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
                        id_ = studentsIds[match_index]
                        print(id_)
                        
                        if counter == 0:
                            # cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                           # cv2.imshow("Face Attendance", imgBackground)
                            # cv2.waitKey(1)
                            counter = 1
                            mode_type = 1
        if counter != 0:
            if counter == 1:
                student_info = db.reference(f'Students/{id_}').get()
                
                #get image data from storage
                blob = bucket.get_blob(f'Images/{id_}.jpg')
                array = np.frombuffer(blob.download_as_string(),np.uint8)
                img_student = cv2.imdecode(array,cv2.COLOR_BGRA2BGR)
                #update attendance data
                date_time_object = datetime.strptime(student_info['Last time attended'],'%Y-%m-%d %H:%M:%S')
                sec_elap = (datetime.now() - date_time_object).total_seconds()
                if sec_elap > 240:
                    ref = db.reference(f'Students/{id_}')
                    student_info['Total attendance'] += 1
                    ref.child('Total attendance').set(student_info['Total attendance'])
                    ref.child('Last time attended').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    mode_type = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[mode_type]
 
                
        if mode_type != 3:
           
              if 30 < counter < 60:
                mode_type = 2
              imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[mode_type]
            
      
            
                
              if counter <= 30:
                    
                        cv2.putText(imgBackground,str(student_info['Total attendance']),(861,125),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                        cv2.putText(imgBackground,str(student_info['Major']),(1006,550),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                        cv2.putText(imgBackground,str(id_),(1006,493),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),1)
                        cv2.putText(imgBackground,str(student_info['Level']),(1025,625),cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                        cv2.putText(imgBackground,str(student_info['Starting Year']),(1125,625),cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                        
                        #Centre name on graphic
                        (w,h),_ = cv2.getTextSize(student_info["Name"],cv2.FONT_HERSHEY_COMPLEX,1,1)
                        offset = (414 - w)//2
                        cv2.putText(imgBackground,str(student_info['Name']),(808 + offset,445),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,50),1)
                          
                        imgBackground[175 : 175 + 216,909:909 + 216] = img_student
                            
                        
                    
                    
                    
                    
              counter += 1
              if counter >= 60 :
                    counter = 0
                    mode_type = 0
                    studuent_info = []
                    img_student = []
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[mode_type]
                    
                
    else:
       mode_type = 0
       counter = 0
    cv2.imshow("Face attendance",imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
# Releasing camera
cap.release()
# Destroying all opened OpenCV windows
cv2.destroyAllWindows()
    