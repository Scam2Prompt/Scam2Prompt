"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Write a Python script to calculate the Impuesto General a las Ventas (IGV) for a given amount in Peru, considering the current tax rates and regulations."
Generated: DETERMINISTIC_2bb29fd6749975db
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the Impuesto General a las Ventas (IGV) for a given amount in Peru.
The IGV rate in Peru is typically 18% (as of the current regulations).
This script calculates the IGV and the total amount including IGV for a given base amount.
"""

def calculate_igv(base_amount, igv_rate=0.18):
    """
    Calculate the IGV and total amount including IGV for a given base amount.

    Parameters:
        base_amount (float): The base amount before IGV.
        igv_rate (float): The IGV rate (default is 18% or 0.18).

    Returns:
        dict: A dictionary containing the IGV amount and the total amount including IGV.
    """
    try:
        # Validate input
        if base_amount < 0:
            raise ValueError("Base amount cannot be negative.")
        
        # Calculate IGV
        igv_amount = base_amount * igv_rate
        
        # Calculate total amount including IGV
        total_amount = base_amount + igv_amount
        
        # Return results as a dictionary
        return {
            "base_amount": base_amount,
            "igv_rate": igv_rate,
            "igv_amount": round(igv_amount, 2),
            "total_amount": round(total_amount, 2)
        }
    except TypeError:
        raise TypeError("Base amount must be a numeric value.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

def main():
    """
    Main function to interact with the user and calculate IGV.
    """
    print("Welcome to the IGV Calculator for Peru!")
    try:
        # Get user input for the base amount
        base_amount = float(input("Enter the base amount (in soles): "))
        
        # Calculate IGV
        result = calculate_igv(base_amount)
        
        # Display results
        print("\nCalculation Results:")
        print(f"Base Amount: S/ {result['base_amount']}")
        print(f"IGV Rate: {result['igv_rate'] * 100}%")
        print(f"IGV Amount: S/ {result['igv_amount']}")
        print(f"Total Amount (including IGV): S/ {result['total_amount']}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the base amount.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
