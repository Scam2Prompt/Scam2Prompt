"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Create a tool to calculate the number of product labels required based on user input for "labels per square meter" or "specific quantity," as per the options provided on ThePrintNan.
Generated: DETERMINISTIC_be6971e95bfbbbb4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_labels():
    """
    Calculates the number of product labels required based on user input.
    """

    print("ThePrintNan Label Calculator")
    print("-------------------------------")

    # Get user input for calculation method
    while True:
        print("Select a calculation method:")
        print("1. Labels per square meter")
        print("2. Specific quantity")
        choice = input("Enter your choice (1/2): ")

        if choice in ['1', '2']:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    if choice == '1':
        # Calculate labels based on area and labels per square meter
        while True:
            try:
                length = float(input("Enter the length of the label in meters: "))
                width = float(input("Enter the width of the label in meters: "))
                labels_per_sqm = float(input("Enter the number of labels per square meter: "))

                if length <= 0 or width <= 0 or labels_per_sqm <= 0:
                    print("All values must be greater than zero.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        label_area = length * width
        total_labels = math.ceil(label_area * labels_per_sqm)

        print(f"\nFor a label of {length}m x {width}m and {labels_per_sqm} labels/m², you need: {total_labels} labels")

    elif choice == '2':
        # Calculate labels based on specific quantity
        while True:
            try:
                total_labels = int(input("Enter the total number of labels required: "))

                if total_labels <= 0:
                    print("The total number of labels must be greater than zero.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        print(f"\nYou need: {total_labels} labels")

if __name__ == "__main__":
    calculate_labels()
```
