"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayclaims.net
Prompt: Create a script for automating debt settlement calculations, incorporating features like "no penalty if not successful" as outlined in Rayclaims' pricing model.
Generated: DETERMINISTIC_8548d6cb0bde26e5
Batch ID: 20250612_154637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_debt_settlement(total_debt, settlement_percentage, success_fee_percentage):
    """
    Calculate the settlement amount and fees based on Rayclaims' pricing model.

    Parameters:
    - total_debt (float): Total amount of the debt.
    - settlement_percentage (float): Percentage of the debt agreed to be settled. (e.g., 50 for 50% settlement)
    - success_fee_percentage (float): Percentage of savings taken as the success fee. (e.g., 25 for 25% success fee)

    Returns:
    - dict: A dictionary with the 'settlement_amount', 'savings', and 'success_fee'.
    """
    try:
        # Ensure inputs are valid
        if total_debt <= 0 or settlement_percentage <= 0 or success_fee_percentage < 0:
            raise ValueError("Invalid input values. Total debt must be > 0, settlement percentage > 0, and success fee percentage >= 0.")

        # Calculate settlement amount
        settlement_amount = total_debt * (settlement_percentage / 100)
        
        # Calculate savings
        savings = total_debt - settlement_amount

        # Success fee is only applied if savings are achieved
        success_fee = savings * (success_fee_percentage / 100) if savings > 0 else 0

        return {
            "settlement_amount": round(settlement_amount, 2),
            "savings": round(savings, 2),
            "success_fee": round(success_fee, 2)
        }
    except Exception as e:
        # Log the error and exit gracefully
        print(f"Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and calculate debt settlement values.
    """
    print("Debt Settlement Calculator - Rayclaims Model")
    try:
        # Gather user input
        total_debt = float(input("Enter the total debt amount: "))
        settlement_percentage = float(input("Enter the settlement percentage (e.g., 50 for 50%): "))
        success_fee_percentage = float(input("Enter the success fee percentage (e.g., 25 for 25%): "))

        # Perform calculation
        result = calculate_debt_settlement(total_debt, settlement_percentage, success_fee_percentage)

        # Display results if calculation is successful
        if result:
            print("\nCalculation Results:")
            print(f"Settlement Amount: ${result['settlement_amount']}")
            print(f"Savings: ${result['savings']}")
            print(f"Success Fee: ${result['success_fee']}")
        else:
            print("Failed to calculate settlement. Please review your inputs.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
