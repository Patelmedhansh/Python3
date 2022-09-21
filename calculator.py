# Bulding basic calculator 
def add(n1, n2):
    return  n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
  
def calc():

    operators = {"+": add, "-":subtract, "*":multiply, "/": divide}

    n1 = float(input("What is the first number?: "))

    for symbols in operators:
        print(symbols)
    should_continue = True


    while should_continue:
        operations = input("Choose an operation from above: ")
        n2 = float(input("What is the second number?: "))

        calculation = operators[operations]
        answer = round(calculation(n1, n2) ,3)

        print(f"{n1} {operations} {n2} = {answer}")

        if input(f"Type 'y' to continue with the calculation, or type 'n' to start a new calculatio: ") == "y":
            n1 = answer
        else:
            should_continue = False
            calc()
 
calc()

# num1 = int (input ("Enter a number :- ") )
# num2  = int (input ("Enter a number :- ") )  

# result = num1 + num2

# print(result) 

# Here when we take input from a user , by default python converts it into string 
# so here we need to define it as int ( integer ) 

# when you use int function it only accepts the whole numbers , so instead of int you can use float function as well 
# if you want to enter decimal  values 
