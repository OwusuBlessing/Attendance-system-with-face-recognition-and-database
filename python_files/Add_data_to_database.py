# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:14:21 2023

@author: ME
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
firebase_admin.delete_app(firebase_admin.get_app())

cred = credentials.Certificate(r"C:/Users/ME/Desktop/Blessing_AI/Face_attendance/python_files/Service_account_key.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://face-attendance-system-c9176-default-rtdb.firebaseio.com/'})

ref = db.reference("Students")
data = {"1233":{
    "Name":"Onanuga Oreoluwa",
    "Major":"Electrical Engineering",
    "Starting Year":2019,
    "Total attendance":5,
    "Level":400,
    "Last time attended":"2023-2-23 13:34:10"},
    "1234":{
        "Name":"Owusu Samuel",
        "Major":"Electrical Engineering",
        "Starting Year":2019,
        "Total attendance":5,
        "Level":400,
        "Last time attended":"2023-2-23 13:35:10"},
    "1236":{
        "Name":"Abdulkareem Sikirulahi",
        "Major":"Mechatronics Engineering",
        "Starting Year":2019,
        "Total attendance":5,
        "Level":400,
        "Last time attended":"2023-2-23 12:34:10"},
    "1238":{
        "Name":"Abulmatin Mato",
        "Major":"Electrical Engineering",
        "Starting Year":2019,
        "Total attendance":5,
        "Level":400,
        "Last time attended":"2023-2-23 14:34:10"},
    "1239":{
        "Name":"Akinyemi Olusegun",
        "Major":"Marketing",
        "Starting Year":2019,
        "Total attendance":5,
        "Level":400,
        "Last time attended":"2023-2-23 11:34:12"}
        
        
        
        
    
        }

for key,value in data.items():
    ref.child(key).set(value)