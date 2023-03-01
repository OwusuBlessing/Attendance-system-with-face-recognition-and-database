
# Face Attendance System in real time 


![Attendance system](https://github.com/OwusuBlessing/Face-Recognition-system/blob/master/mato_face_PNG.PNG)
![Attendance system](https://github.com/OwusuBlessing/Attendance-system-with-face-recognition-and-database/blob/master/almar.PNG)
This project aims to automate attendance System using facial recognition (face recognition libarry).The project is implemented with firebase database such that information about student can be gotten from the database once the attendance is marked.This project follows this face recognition in real time course on [youtube](https://www.youtube.com/watch?v=iBomaK2ARyI)




## Folder Setup description
**Images**:It contains the images of every student with each image named with the student corresponding ID.

**Resources**:It contains the images used to design the graphic of the system including different modes when marking the attendance and the background image.

**Python_files**:It contains the python scripts to be run to implement the project.
## Installation & Project implementation
To carry out this project, clone the repository but if you are using a different set of students,make sure you resize the image to 216 by 216 pixel values.

**Step 1**

Open your anaconda command promt terminal
create a new virtual environment on anaconda promt using the code
```python
conda create -n 'environment name' python=3.9
```
**Step 2**

Activate the environment using the code below
```python
conda activate environment_name
```
**Step 3**

While in the activated virtual environment, install the following libraries
```python
pip install numpy
pip install face_recogniiton
pip install cmake
pip install dlib
pip install opencv-python
pip install cvzone
pip install firebase_admin
```
**Step 4**

*Database setup*

In this step , you create your own database on ![fire base](https://firebase.google.com/?gclid=CjwKCAiAjPyfBhBMEiwAB2CCIk2EshHBEcUQk3Z0qZxQJa-JzD3dnqSxu8sJByhipnSxW4R_5WgeChoCFP4QAvD_BwE&gclsrc=aw.ds) and also create storage to store student images.

**Step 5**

*Encoding face generator*

Prepare your images folder,go inside the python_files folder and open EncodeGenerator.py with suitable IDE,run the python file to encode the face landmarks of each student and store it as a pickle file.Ensure you change the path to folders in the code to ones in your local machine.

**Step 6**

*Adding students data to database*

To add the data of the students like personal details to the database so it can be accessed later,open the add_data_to_database.py file and make changes for your own custome students and run the script.

**Step 7**

*Running  attendance system*

To demontrate the attendance system in real time ,open the main.py file, make changes to folder/files path where needed to that of your local machine and run the code.





## Acknowledgements

 - [Awesome Video Tutorial](https://www.youtube.com/watch?v=iBomaK2ARyI)

 - [Understanding fire base database](https://www.youtube.com/watch?v=kXYalWgc_rU)








## Technologies Used

- Face recognition library
- OpenCV
- Cvzone
- firebase admin
- numpy





[![Masterhead](https://camo.githubusercontent.com/cae12fddd9d6982901d82580bdf321d81fb299141098ca1c2d4891870827bf17/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f313336302f302a37513379765349765f7430696f4a2d5a2e676966)




- 🔭 I’m currently working on **object detection projects**

- 🌱 I’m currently learning **SQL,NLP,Image Segementaion**

- 👯 I’m looking to collaborate on **any open source data science project**


- 👨‍💻 All of my projects are available at [https://github.com/OwusuBlessing/SamuelBlessing509](https://github.com/OwusuBlessing/SamuelBlessing509)

- 💬 Ask me about **Python & Machine Learning**

- 📫 How to reach me **owususammy509@gamil.com**


