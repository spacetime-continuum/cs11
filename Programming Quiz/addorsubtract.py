print("Do you want to add or subtract?")
choice = input("Type 1 for add 2 for subtract ")

num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second number "))

if choice == "1":
    add = num1 + num2
    print(add)
elif choice == "2":
    subtract = num1 - num2
    print(subtract)
else:
    print("Invalid choice.")