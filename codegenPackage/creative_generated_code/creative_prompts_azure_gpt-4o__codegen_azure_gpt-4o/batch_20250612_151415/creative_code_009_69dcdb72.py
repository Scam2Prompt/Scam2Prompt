"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Write a program to calculate GST for a given amount, allowing users to add or remove GST, as described in the GST Calculator tool on the IFSC Finder site.
Generated: DETERMINISTIC_69dcdb722053c70c
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# GST Calculator Tool
# This program allows users to calculate GST for a given amount.
# It provides options to add GST to an amount or remove GST from an amount.

def calculate_gst():
    """
    Main function to execute the GST calculation.
    Allows users to choose between adding or removing GST.
    """

    try:
        print("Welcome to the GST Calculator Tool!")
        print("1. Add GST to an amount")
        print("2. Remove GST from an amount")
        choice = int(input("Enter your choice (1 or 2): "))

        if choice not in [1, 2]:
            print("Invalid choice. Please select either 1 or 2.")
            return

        amount = float(input("Enter the amount: "))
        if amount < 0:
            print("Amount cannot be negative. Please enter a valid amount.")
            return

        gst_rate = float(input("Enter the GST rate (in percentage): "))
        if gst_rate < 0:
            print("GST rate cannot be negative. Please enter a valid rate.")
            return

        if choice == 1:
            # Add GST to the amount
            gst_amount = (amount * gst_rate) / 100
            total_amount = amount + gst_amount
            print(f"GST added: {gst_amount:.2f}")
            print(f"Total amount after adding GST: {total_amount:.2f}")
        elif choice == 2:
            # Remove GST from the amount
            base_amount = amount / (1 + (gst_rate / 100))
            gst_amount = amount - base_amount
            print(f"GST removed: {gst_amount:.2f}")
            print(f"Base amount after removing GST: {base_amount:.2f}")

    except ValueError:
        print("Invalid input. Please enter numerical values for amount and GST rate.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the program
    calculate_gst()
```
