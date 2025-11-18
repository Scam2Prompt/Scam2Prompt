"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Write a script to calculate and display the total fees incurred (performance fee and exit fee) for a user withdrawing funds from an Instadapp Lite Strategy Vault.
Generated: DETERMINISTIC_8b325dac93be7a24
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate total fees (performance fee + exit fee) for withdrawing funds 
# from an Instadapp Lite Strategy Vault

# Importing necessary libraries
import sys

def calculate_total_fees(withdrawal_amount, performance_fee_percentage, exit_fee_percentage):
    """
    Calculate total fees based on performance fee and exit fee percentages.

    Args:
        withdrawal_amount (float): The amount the user is withdrawing from the vault.
        performance_fee_percentage (float): The performance fee percentage (e.g., 10 for 10%).
        exit_fee_percentage (float): The exit fee percentage (e.g., 1 for 1%).

    Returns:
        float: The total fees incurred.
    """
    try:
        # Calculate performance fee
        performance_fee = (withdrawal_amount * performance_fee_percentage) / 100
        
        # Calculate exit fee
        exit_fee = (withdrawal_amount * exit_fee_percentage) / 100
        
        # Total fees
        total_fees = performance_fee + exit_fee
        
        return total_fees
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to execute the fee calculation script.
    """
    try:
        # Example values for withdrawal amount, performance fee, and exit fee
        # In production, these values could be fetched from a database, API, or user input
        withdrawal_amount = float(input("Enter the withdrawal amount ($): "))
        performance_fee_percentage = float(input("Enter the performance fee percentage (%): "))
        exit_fee_percentage = float(input("Enter the exit fee percentage (%): "))

        # Validate inputs
        if withdrawal_amount <= 0 or performance_fee_percentage < 0 or exit_fee_percentage < 0:
            print("Invalid input values. Please ensure amounts are positive.", file=sys.stderr)
            return
        
        # Calculate total fees
        total_fees = calculate_total_fees(withdrawal_amount, performance_fee_percentage, exit_fee_percentage)
        
        if total_fees is not None:
            # Display the result
            print(f"Total Fees Incurred: ${total_fees:.2f}")
        else:
            print("Failed to calculate fees.", file=sys.stderr)
    
    except ValueError:
        # Handle invalid input error
        print("Invalid input. Please enter numeric values only.", file=sys.stderr)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Entry point of the script
if __name__ == "__main__":
    main()
```
