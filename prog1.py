def main():
    print("Welcome to the Ultimate Multi-Utility Program!")
    print("Choose a number from 1 to 50 for specific tasks or results.")
    print("Type 'exit' to quit the program.")

    while True:
        user_input = input("\nEnter your choice (1-50 or 'exit'): ").strip()

        if user_input.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break

        try:
            choice = int(user_input)

            if choice == 1:
                print("Task 1: Add two numbers.")
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print(f"The sum is {a + b}.")
            elif choice == 2:
                print("Task 2: Subtract two numbers.")
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print(f"The result is {a - b}.")
            elif choice == 3:
                print("Task 3: Multiply two numbers.")
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print(f"The product is {a * b}.")
            elif choice == 4:
                print("Task 4: Divide two numbers.")
                a = int(input("Enter numerator: "))
                b = int(input("Enter denominator: "))
                if b == 0:
                    print("Error: Division by zero!")
                else:
                    print(f"The result is {a / b}.")
            elif choice == 5:
                print("Task 5: Check if a number is even or odd.")
                num = int(input("Enter a number: "))
                if num % 2 == 0:
                    print(f"{num} is even.")
                else:
                    print(f"{num} is odd.")
            elif choice == 6:
                print("Task 6: Find the square of a number.")
                num = int(input("Enter a number: "))
                print(f"The square of {num} is {num ** 2}.")
            elif choice == 7:
                print("Task 7: Find the cube of a number.")
                num = int(input("Enter a number: "))
                print(f"The cube of {num} is {num ** 3}.")
            elif choice == 8:
                print("Task 8: Check if a number is positive, negative, or zero.")
                num = int(input("Enter a number: "))
                if num > 0:
                    print(f"{num} is positive.")
                elif num < 0:
                    print(f"{num} is negative.")
                else:
                    print(f"{num} is zero.")
            elif choice == 9:
                print("Task 9: Convert Celsius to Fahrenheit.")
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius}°C is {fahrenheit}°F.")
            elif choice == 10:
                print("Task 10: Convert Fahrenheit to Celsius.")
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5/9
                print(f"{fahrenheit}°F is {celsius}°C.")
            # ... (Continue tasks in a similar pattern up to Task 50)
            elif choice == 50:
                print("Task 50: Calculate the factorial of a number.")
                num = int(input("Enter a number: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    factorial = 1
                    for i in range(1, num + 1):
                        factorial *= i
                    print(f"The factorial of {num} is {factorial}.")
            else:
                print("Invalid choice! Please select a number between 1 and 50.")

        except ValueError:
            print("Invalid input! Please enter a valid number or type 'exit'.")

if __name__ == "__main__":
    main()