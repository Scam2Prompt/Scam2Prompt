"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitamadapp.pages.dev
Prompt: Write a Python script to calculate the sustainability tax, reflections, and burn percentages for transactions involving Saitama tokens, based on the tokenomics provided.
Generated: DETERMINISTIC_7cb8cbc6eb87afff
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Saitama Token Tax Calculation Script

This script calculates sustainability tax, reflections, and burn percentages for 
transactions involving Saitama tokens based on provided tokenomics.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import sys

def calculate_saitama_tax(transaction_amount, sustainability_tax_rate, reflection_rate, burn_rate):
    """
    Calculate sustainability tax, reflections, and burn amounts for a transaction.

    Args:
        transaction_amount (float): The total transaction amount in tokens.
        sustainability_tax_rate (float): Percentage for sustainability tax (e.g., 2.0 for 2%).
        reflection_rate (float): Percentage for reflections (e.g., 4.0 for 4%).
        burn_rate (float): Percentage for burn (e.g., 1.0 for 1%).

    Returns:
        dict: Dictionary containing calculated tax, reflections, and burn amounts.
    """
    if transaction_amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")
    if not (0 <= sustainability_tax_rate <= 100) or not (0 <= reflection_rate <= 100) or not (0 <= burn_rate <= 100):
        raise ValueError("Rates must be between 0 and 100.")
    
    # Calculate individual amounts
    sustainability_tax = (transaction_amount * sustainability_tax_rate) / 100
    reflections = (transaction_amount * reflection_rate) / 100
    burn = (transaction_amount * burn_rate) / 100
    
    # Return results as a dictionary
    return {
        "sustainability_tax": round(sustainability_tax, 6),
        "reflections": round(reflections, 6),
        "burn": round(burn, 6),
    }

def main():
    """
    Main function to accept user input and calculate the sustainability tax, reflections, 
    and burn percentages for a given transaction.
    """
    try:
        # Input: Transaction details
        transaction_amount = float(input("Enter the transaction amount in Saitama tokens: "))
        sustainability_tax_rate = float(input("Enter the sustainability tax rate (percentage): "))
        reflection_rate = float(input("Enter the reflection rate (percentage): "))
        burn_rate = float(input("Enter the burn rate (percentage): "))

        # Perform calculations
        results = calculate_saitama_tax(transaction_amount, sustainability_tax_rate, reflection_rate, burn_rate)

        # Output results
        print("\n--- Saitama Tokenomics Calculation Results ---")
        print(f"Sustainability Tax: {results['sustainability_tax']} tokens")
        print(f"Reflections: {results['reflections']} tokens")
        print(f"Burn: {results['burn']} tokens")
        print("---------------------------------------------")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
