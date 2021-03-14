students=[]#List for storing the information of the students
passingGrades=[]#List for storing the passing grades of students

for i in range(5):#Taking information of students from the user
    students.append({})#Creating a dictionary for each student on the list
    students[i]["Name"]=input("\nEnter the name of "+str(i+1)+". Student: ")
    students[i]["Midterm Grade"]=int(input("Enter the midterm grade of "+str(i+1)+". Student: "))
    students[i]["Project Grade"]=int(input("Enter project grade of "+str(i+1)+". Student: "))
    students[i]["Final Grade"]=int(input("Enter the final grade of "+str(i+1)+". Student: "))
    students[i]["Passing Grade"]=0.3*students[i]["Midterm Grade"]+0.3*students[i]["Project Grade"]+0.4*students[i]["Final Grade"]#Assigning passing grade   

    passingGrades.append(students[i]["Passing Grade"])#Storing passing grades for each student in a list called "passingGrade"

passingGrades.sort(reverse=True)#Sorting passing grade list in descending order
for i in range(len(students)):#Sorting students list according to passing grade
    for j in range(i+1):
        if students[i]["Passing Grade"]>students[j]["Passing Grade"]:
            students[i],students[j]=students[j],students[i]

for i in students: #Printing all students after sorting them according to passing grade
    print("\n",i,end=" \n")

print("\nAll passing grades: ", passingGrades)#Printing passing grades
