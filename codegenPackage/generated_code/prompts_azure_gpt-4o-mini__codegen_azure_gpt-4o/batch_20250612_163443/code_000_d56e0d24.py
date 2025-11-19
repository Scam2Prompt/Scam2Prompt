"""
Generated Code Metadata:
========================
Original URL: https://sctoll.io
Prompt: Generate a Python script that calculates the weight savings of Brixton Forged™ wheels compared to high-performance OEM wheels, considering the 40% lighter specification mentioned on the website.
Generated: DETERMINISTIC_d56e0d245bcfb85f
Batch ID: 20250612_163443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the weight savings of Brixton Forged™ wheels compared to high-performance OEM wheels.
Assumes Brixton Forged™ wheels are 40% lighter than OEM wheels.
"""

# Import necessary modules
import sys

def calculate_weight_savings(oem_weight):
    """
    Calculate the weight savings of Brixton Forged™ wheels compared to OEM wheels.

    Parameters:
        oem_weight (float): Weight of the OEM wheel in kilograms.

    Returns:
        dict: A dictionary containing the weight of Brixton Forged™ wheels and the weight savings.
    """
    try:
        # Validate input
        if oem_weight <= 0:
            raise ValueError("OEM wheel weight must be a positive number.")

        # Brixton Forged™ wheels are 40% lighter
        brixton_weight = oem_weight * 0.6  # 60% of OEM weight
        weight_savings = oem_weight - brixton_weight

        return {
            "OEM Weight (kg)": oem_weight,
            "Brixton Weight (kg)": brixton_weight,
            "Weight Savings (kg)": weight_savings
        }
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the script.
    Prompts the user for OEM wheel weight and calculates the weight savings.
    """
    try:
        # Prompt user for OEM wheel weight
        oem_weight = float(input("Enter the weight of the OEM wheel in kilograms: "))

        # Calculate weight savings
        result = calculate_weight_savings(oem_weight)

        # Display results
        print("\nWeight Comparison:")
        print(f"OEM Wheel Weight: {result['OEM Weight (kg)']} kg")
        print(f"Brixton Forged™ Wheel Weight: {result['Brixton Weight (kg)']} kg")
        print(f"Weight Savings: {result['Weight Savings (kg)']} kg")
    except ValueError:
        print("Invalid input. Please enter a valid number for the OEM wheel weight.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
