"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alixa.tech
Prompt: Create a tool to calculate the earning power (EP) for bonds with varying maturity periods (e.g., 30 days, 90 days, 180 days, 365 days) on the Alixa platform.
Generated: DETERMINISTIC_5a8a579c35c6914a
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Tool to calculate earning power (EP) for bonds with varying maturity periods
# This script is designed to be clean, robust, and production-ready.

import datetime

class Bond:
    """
    Class to represent a bond and calculate its earning power (EP).
    Attributes:
        face_value (float): The face value of the bond.
        annual_interest_rate (float): The annual interest rate (in decimal form, e.g., 0.05 for 5%).
        maturity_days (int): The number of days until the bond matures.
    """
    def __init__(self, face_value, annual_interest_rate, maturity_days):
        self.face_value = face_value
        self.annual_interest_rate = annual_interest_rate
        self.maturity_days = maturity_days

    def calculate_earning_power(self):
        """
        Calculate the earning power (EP) of the bond based on its maturity period.
        Formula: EP = (face_value * annual_interest_rate * maturity_days) / 365
        Returns:
            float: The earning power of the bond.
        """
        try:
            ep = (self.face_value * self.annual_interest_rate * self.maturity_days) / 365
            return ep
        except Exception as e:
            raise ValueError(f"Error calculating earning power: {e}")


def main():
    """
    Main function for the bond earning power calculator tool.
    Allows the user to input data for multiple bonds and calculates the EP for each.
    """
    try:
        print("=== Bond Earning Power Calculator ===")
        bond_list = []  # Store multiple bonds for EP calculation
        
        while True:
            # Collect bond details from the user
            face_value = float(input("Enter the face value of the bond (e.g., 1000): "))
            annual_interest_rate = float(input("Enter the annual interest rate (in decimal form, e.g., 0.05 for 5%): "))
            maturity_days = int(input("Enter the maturity period of the bond in days (e.g., 30, 90, 180, 365): "))

            # Create a Bond object
            bond = Bond(face_value, annual_interest_rate, maturity_days)
            bond_list.append(bond)

            # Prompt to calculate earning power
            print(f"Earning Power (EP): {bond.calculate_earning_power():.2f}")

            # Ask if the user wants to add more bonds
            more_bonds = input("Do you want to calculate EP for another bond? (yes/no): ").strip().lower()
            if more_bonds != 'yes':
                break

        # Display summary of all bonds
        print("\n=== Summary of Calculated Earning Powers ===")
        for i, bond in enumerate(bond_list, 1):
            print(f"Bond {i}: Face Value={bond.face_value}, Annual Interest Rate={bond.annual_interest_rate}, "
                  f"Maturity Days={bond.maturity_days}, Earning Power={bond.calculate_earning_power():.2f}")

        print("Thank you for using the Bond Earning Power Calculator!")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
