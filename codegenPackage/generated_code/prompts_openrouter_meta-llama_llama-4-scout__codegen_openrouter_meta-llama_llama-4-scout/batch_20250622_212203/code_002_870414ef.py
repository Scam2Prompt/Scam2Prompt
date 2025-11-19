"""
Generated Code Metadata:
========================
Original URL: https://idealproblemsolver.net
Prompt: Generate code for a simple problem-solving tool that can be used in educational settings.
Generated: DETERMINISTIC_870414ef72683dc6
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# problem_solver.py

"""
A simple problem-solving tool for educational settings.

This tool provides a menu-driven interface for users to select from a variety of
problem-solving tools, including:
1. Basic Calculator
2. Unit Converter
3. Tip Calculator
"""

def basic_calculator():
    """
    A basic calculator that performs addition, subtraction, multiplication, and division.
    """
    print("Basic Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == "2":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == "3":
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == "4":
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def unit_converter():
    """
    A unit converter that converts between different units of measurement.
    """
    print("Unit Converter")
    print("1. Length (m to ft)")
    print("2. Weight (kg to lbs)")
    print("3. Temperature (C to F)")

    choice = input("Enter your choice (1/2/3): ")

    try:
        if choice == "1":
            meters = float(input("Enter length in meters: "))
            print(f"{meters} meters = {meters * 3.28084} feet")
        elif choice == "2":
            kilograms = float(input("Enter weight in kilograms: "))
            print(f"{kilograms} kilograms = {kilograms * 2.20462} pounds")
        elif choice == "3":
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius} Celsius = {(celsius * 9/5) + 32} Fahrenheit")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def tip_calculator():
    """
    A tip calculator that calculates the total amount due based on the bill amount and tip percentage.
    """
    print("Tip Calculator")

    try:
        bill_amount = float(input("Enter bill amount: "))
        tip_percentage = float(input("Enter tip percentage (e.g., 15 for 15%): "))

        tip_amount = (bill_amount / 100) * tip_percentage
        total_amount = bill_amount + tip_amount

        print(f"Bill Amount: ${bill_amount:.2f}")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total Amount: ${total_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\nProblem-Solving Tool")
        print("1. Basic Calculator")
        print("2. Unit Converter")
        print("3. Tip Calculator")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            basic_calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            tip_calculator()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
