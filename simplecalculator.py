a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("CHOOSE YOUR OPERATOR")
print("1.ADD, 2.SUB, 3.MULTIPLY, 4.DIVIDE")
c=input("Choose any one:")
if(c=="1"):
  add=a+b
  print("Result =",a,"+",b,"=",add)
elif(c=="2"):
  sub=a-b
  print("Result =",a,"-",b,"=",sub)
elif(c=="3"):
  mul=a*b
  print("Result =",a,"×",b,"=",mul)
elif(c=="4"):
  if(b==0):
    print("Division by Zero is not possible")
  else:
    div=a/b
    print("Result =",a,"/",b,"=",div)
else:
  print("INVALID")
