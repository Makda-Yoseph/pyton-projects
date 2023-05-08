def calculator():
    num1=float(input("Enter the first number \n"))
    operator=input("Enter one of the four operators these are +,-,*,/ \n")
    if operator in {"+","*","-","/"}:
        num2= float(input("Enter the second number\n"))
        addition=num1+num2
        substruction=num1 - num2
        multiplication=num1*num2
        
        if type(num1) == float:
            if operator =="+":
               print("result: " , addition)
            elif operator =="-":
                print ("result: " , substruction)
            elif operator =="*":
                print("result: " , multiplication)
            elif operator == "/":
                if num2 == 0:
                    print("Error: Division by zero is invalid")
                else:
                    print("result: " , num1/num2) 
    else:
        print("you have entered the wrong input")
calculator()
response=input("Would you like to calculate other numbers ? if yes type yes if no type no \n")
while response =="yes":
    calculator()


