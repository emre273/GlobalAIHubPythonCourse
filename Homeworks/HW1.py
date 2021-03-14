firstList=[x for x in range(20) if x%2!=0]#Assigning odd numbers up to 20
secondList=[x for x in range(20) if x%2==0] #Assigning even numbers up to 20
mergedList=firstList+secondList #Merging above two lists
mergedList.sort() #Sorting the merged list in ascending order

finalMergedList=[i*2 for i in mergedList] #Multiplying all the values in merged List

for i in finalMergedList:
    print(i, " TYPE ==> ", type(i))#Printing the values in the merged list and the data type of them