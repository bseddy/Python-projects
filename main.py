#Basic Calculator by Akinbiyi Adegoke

# This function adds both numbers
def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

#This function subtracts both numbers
def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))

#This function multiplies both numbers
def mul(a,b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))

#This function divides both numbers
def div(a,b):
    
    # validation for dividing by zero
    if b == 0:
        print("Can't divide by 0, try another number")
        return
    
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))
    
# added while loop to allow for multiple calculator operations

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit ")

    #Choice aids users to define function per functions listed prior
    choice = input("Input your choice:")
    
    # restructured choices with exit condition choice first
    if choice == "e" or choice == "E":
        print("Program has ended")
        break
    
    # input validation for any input not defined
    if choice not in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']:
        print("Invalid choice, please select again.")
        continue
    
    # float conversion with input validation on user number inputs
    try:
        a = float(input("Input the first number:"))
        b = float(input("Input the second number:"))
    except ValueError:
        print("Invalid input, please use a valid number.")
        continue

    if choice == "a" or choice == "A":
        print("Addition")
        add(a,b)
        
    elif choice == "b" or choice == "B":
        print("Subtraction")
        sub(a,b)
        
    elif choice == "c" or choice == "C":
        print("Multiplication")
        mul(a,b)
        
    elif choice == "d" or choice == "D":
        print("Division")
        div(a,b)
        
    # see if user wants to perform another operation or quit
    
    calc_continue = input("Do you want to perform another calculation? (y/n): ")
    if calc_continue == "y" or calc_continue == "Y":
    # loop will start again
        pass
    # any other input other than y or Y will result in program termination
    else:
        print("Program has ended")
        break
    



