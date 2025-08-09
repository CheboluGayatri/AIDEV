#function to add numbers
def add(x,y):
    return x+y

#functions to substract two numbers
def substract(x,y):
    return x-y

#function mul two numbers
def multiply(x,y):
    return x*y

#functions to div two numbers
def divide(x,y):
    if y==0:
        return "Error! Division by zero not allowed."
    else:
        return x/y 
    
def calculator():
    print("Select operator:")
    print("1. add")
    print("2. substract")
    print("3. multiply")
    print("4. divide")
    while True:
        #Take input from user
        choice=input("Enter choices(1/2/3/4):")

        #check if the input is one of the four options 
        if choice in['1','2','3','4']:
            num1=float(input("Enter the first number"))
            num2=float(input("Enter the first number"))
            if choice == '1':
               print(f"{num1} + {num2} = {add(num1, num2)}")

            if choice == '2':
               print(f"{num1} - {num2} = {substract(num1, num2)}")

            if choice == '3':
               print(f"{num1} * {num2} = {multiply(num1, num2)}")

            if choice == '4':
               print(f"{num1} / {num2} = {divide(num1, num2)}")

                
        # option to exit the loop
        next_calculation =input("Do want to perform another calculation ? (yes/no)")
        if next_calculation.lower() !='yes':
           break

print("exiciting calculator.goodbye!")
#call the calculator function
calculator()