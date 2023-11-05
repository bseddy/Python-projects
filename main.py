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
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))


print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit ")

#Choice aids users to define function per functions listed prior
choice = input("Input your choice:")

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("Input the first number:"))
    b = int(input("Input the second number:"))
    add(a,b)

elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("Input the first number:"))
    b = int(input("Input the second number:"))
    sub(a,b)

elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("Input the first number:"))
    b = int(input("Input the second number:"))
    mul(a,b)

elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("Input the first number:"))
    b = int(input("Input the second number:"))
    div(a,b)

elif choice == "e" or choice == "E":
    print("Program has ended")
    quit()
