while True:
    print("""
1. Addition
2. Subtraction
3. Multiplication 
4. Division
5. Exit 
""")
    choice = input("Choose b/w (1 to 5): ")

    if choice == "1":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("Addition is", num1 + num2)

    elif choice == "2":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("Subtraction is", num1 - num2)

    elif choice == "3":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("Multiplication is", num1 * num2)

    elif choice == "4":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Division is", num1 / num2)

    elif choice == "5":
        print("Thanks for using the calculator!")
        break   

    else:
        print("Invalid choice. Try again.")
