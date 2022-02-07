salary=int(input("Enter the salary: "))
year=int(input("Enter years of service: "))
if year>10:
  bonus=salary*0.1
  print("bonus",bonus)
if year>=6 and year<=10:
    bonus=salary*0.08
    print("bonus",bonus)
if year<6:
      bonus=salary*0.05
      print("bonus",bonus)