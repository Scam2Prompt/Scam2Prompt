"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Create a tool to calculate the number of product labels required based on user input for "labels per square meter" or "specific quantity," as per the options provided on ThePrintNan.
Generated: DETERMINISTIC_be6971e95bfbbbb4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_labels():
    """
    Tool to calculate the number of product labels required.
    The user can select between "labels per square meter" or "specific quantity."
    """
    print("Welcome to the Product Label Calculator!")
    print("Choose an option:")
    print("1. Calculate labels based on 'Labels per Square Meter'")
    print("2. Calculate labels based on 'Specific Quantity'")
    
    try:
        option = int(input("Enter 1 or 2: "))
        if option not in [1, 2]:
            raise ValueError("Invalid option selected. Please choose 1 or 2.")
        
        if option == 1:
            # Option 1: Labels per Square Meter
            try:
                area = float(input("Enter total area in square meters: "))
                if area <= 0:
                    raise ValueError("Area must be a positive number.")
                
                labels_per_square_meter = int(input("Enter the number of labels per square meter: "))
                if labels_per_square_meter <= 0:
                    raise ValueError("Labels per square meter must be a positive number.")
                
                total_labels = math.ceil(area * labels_per_square_meter)
                print(f"Total labels required: {total_labels}")
            except ValueError as ve:
                print(f"Error: {ve}")
        
        elif option == 2:
            # Option 2: Specific Quantity
            try:
                quantity = int(input("Enter the specific quantity of labels needed: "))
                if quantity <= 0:
                    raise ValueError("Quantity must be a positive number.")
                
                print(f"Total labels required: {quantity}")
            except ValueError as ve:
                print(f"Error: {ve}")

    except ValueError as ve:
        print(f"Error: {ve}")
    finally:
        print("Thank you for using the Product Label Calculator!")

if __name__ == "__main__":
    calculate_labels()
```
