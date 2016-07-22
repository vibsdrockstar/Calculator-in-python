print("Welcome to my calculator")
typeofoperation=str(input("Would you like Addition(a),Subtraction(s) or Multiplication(m)")) 
if typeofoperation=="a":
num1 = int(input("Please enter the first number"))
num2=int(input("Please enter the second  number"))
print(num1+num2)
elif typeofoperation=="s":
 num1= int(input("Please enter the first number"))
num2=int(input("Please enter the second  number"))
print(num1-num2)                   
elif typeofoperation=="m":
 num1= int(input("Please enter the first number"))
num2=int(input("Please enter the second  number"))
print(num1*num2)
else:
print("Sorry i don't have that sum")
                    
input("Press enter to exit")
