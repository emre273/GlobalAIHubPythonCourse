#Creating Cvs of 5 people:
cv1={"Name": "Emre", "Surname": "Öztürk",
    "Education": "MSc in Civil Engineering",
    "CGPA": 3.05, "Computer Skills":["Javascript","C++","Python","C#"]}

cv2={"Name": "Civan", "Surname": "Odabaşı",
    "Education": "BSc in Civil Engineering",
    "CGPA": 2.5, "Computer Skills":["MATLAB","Autocad","MathCAD"]}

cv3={"Name": "Burak", "Surname": "Kayaalp",
    "Education": "BSc in Computer Engineering",
    "CGPA": 2.7, "Computer Skills":["PHP","C++","C#"]}

cv4={"Name": "Onur", "Surname": "Öztürk",
    "Education": "MSc in Information Management",
    "CGPA": 2.65, "Computer Skills":["MS Office","PHP",]}

cv5={"Name": "Enes", "Surname": "Yılmazsoy",
    "Education": "Bsc in Architecture",
    "CGPA": 2.4, "Computer Skills":["AutoCad","Revit","SketchUp"]}

CV=[cv1,cv2,cv3,cv4,cv5]#Creating a list containing all the CVs
for i in CV:
    print("\nCV"+str(CV.index(i)+1)+":\n",i,end=" \n") #Printing all the information in each CV