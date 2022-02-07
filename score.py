subject1=int(input("Enter the first subject: "))
subject2=int(input("Enter the second subject: "))
subject3=int(input("Enter the third subject: "))
subject4=int(input("Enter the fourth subject: "))
subject5=int(input("Enter the fifth subject: "))

average=(subject1+subject2+subject3+subject4+subject5)//5
print("average",average)

score=int(input("enter your score: "))

if score >=70 and score <=100:
  print("Grade A")
elif score>=60 and score <=69:
  print("Grade B")
elif score>=50 and score <=59:
  print("Grade c")
elif score>=40 and score <49:
  print("Grade D")
elif score <39:
  print("FAIL")