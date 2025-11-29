age=int(input("Enter your age:"))
if(age<12):
  print("Original Price is 100")
  a=input("Are you a Student[Y/N]?:")
  if(a=="y"):
    print("Price is 80(Rs.20 discount)")
  else:
    print("Sorry NO DISCOUNT!")
elif(age>=12 and age<=18):
  print("Original Price is 150")
  a=input("Are you a Student[Y/N]?:")
  if(a=="y"):
    print("Price is 130(Rs.20 discount)")
  else:
    print("Sorry NO DISCOUNT!")
elif(age>=18):
  print("Original Price is 200")
  a=input("Are you a Student[Y/N]?:")
  if(a=="y"):
    print("Price is 180(Rs.20 discount)")
  else:
    print("Sorry NO DISCOUNT!")
else:
  print("INVALID")
