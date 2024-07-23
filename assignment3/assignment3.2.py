score = int(input("write your score from 1 to 100 "))
if(score<60):
    grade = "F"
elif(59<score<70):
    grade = "D"
elif(69<score<80):
    grade = "C"
elif(79<score<90):
    grade = "B"
else:
    grade = "A"
    
print(grade)