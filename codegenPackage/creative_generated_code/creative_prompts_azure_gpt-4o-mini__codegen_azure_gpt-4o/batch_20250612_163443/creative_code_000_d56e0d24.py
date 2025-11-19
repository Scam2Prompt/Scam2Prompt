"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sctoll.io
Prompt: Generate a Python script that calculates the weight savings of Brixton Forged™ wheels compared to high-performance OEM wheels, considering the 40% lighter specification mentioned on the website.
Generated: DETERMINISTIC_d56e0d245bcfb85f
Batch ID: 20250612_163443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_weight_savings(oem_weight):
    """
    Calculate the weight savings of Brixton Forged™ wheels compared to high-performance OEM wheels.
    
    Brixton Forged™ wheels are specified to be 40% lighter than OEM wheels.

    Parameters:
    oem_weight (float): Weight (in kilograms) of the OEM wheel.

    Returns:
    dict: A dictionary containing the original OEM weight, Brixton wheel weight,
          and weight savings in kilograms.
    """
    try:
        # Ensure the OEM weight is valid
        if oem_weight <= 0:
            raise ValueError("OEM weight must be a positive number.")

        # Brixton wheels are 40% lighter
        brixton_weight = oem_weight * 0.6

        # Weight savings
        weight_savings = oem_weight - brixton_weight

        # Return the results in a dictionary
        return {
            "OEM Weight (kg)": oem_weight,
            "Brixton Weight (kg)": brixton_weight,
            "Weight Savings (kg)": weight_savings
        }
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the weight savings calculation.
    
    Prompts the user for the OEM wheel weight and calculates the weight savings.
    """
    print("Welcome to the Brixton Forged™ Weight Savings Calculator!")
    
    try:
        # Prompt user input for OEM wheel weight
        oem_weight = float(input("Enter the weight of the OEM wheel (in kilograms): "))
        
        # Calculate weight savings
        result = calculate_weight_savings(oem_weight)
        
        # Display results
        print("\n*** Weight Savings Calculation Results ***")
        for key, value in result.items():
            print(f"{key}: {value:.2f} kg")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for the OEM weight.")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
