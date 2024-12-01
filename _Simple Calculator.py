def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter the number corresponding to the operation (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue
            if choice == '1':
                print(f"The result of addition: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"The result of subtraction: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"The result of multiplication: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"The result of division: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Division by zero is not allowed.")

        else:
            print("Invalid choice. Please choose a valid operation.")
        another = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the Simple Calculator. Goodbye!")
            break
calculator()
