#Creating dictionary for questions and answers.
Qs={"What is the capital of Turkey: ": "Ankara",
    "Which planet is closest to the sun: ":"Mercury",
    "What is the largest country in the world: ": "Russia",
    "Alberta is a province of which country: ":"Canada",
    "How many elements are there in the periodic table: ":"118",
    "Name the fictional city Batman calls home: ":"Gotham",
    "In what year did World War II end: ":"1945",
    "Which chess piece can't move in a straight line: ":"Knight",
    "In Greek mythology, who is the God of the sea: ":"Poseidon",
    "The largest desert of the World is: ": "Sahara"}

checker=[]#"checker" is to check wheter the corresponding question is true or not.
answers=[]#This list will store the answer that the user will give.
totalPoints=0#"totalPoints" is representing the the total point that the user get

for i in Qs: #Asking all the question to the user
    ans=str((input("\n"+i))) #Taking the answer
    answers.append(ans)#Storing each answer
    if ans.lower()==Qs[i].lower():#Checking the answer considering case sensitivity
        checker.append(True)
        totalPoints += 10
    else:
        checker.append(False)

print("\nYou can see the answers below: ")
j=0
for i in Qs:#Printing questions and the correct answers.
    print("\n"+str(j+1)+"."+i+" Correct answer: "+Qs[i]+"/// Your Answer: "+answers[j])
    j += 1
    
if totalPoints>50:#Checking total points and informing the user
    print("\nYou have "+str(checker.count(False))+" wrong answer. Therefore you have "+str(totalPoints)+" Points ==> SUCCESSFUL") 
else:
    print("\nYou have "+str(checker.count(False))+" wrong answer. Therefore you have "+str(totalPoints)+" Points ==> UNSUCCESSFUL") 