"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Write a script to calculate the target profit for a REIT portfolio based on the investment range ($2 million - $20 million) and secure income policies described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_dfa0fb931452635a
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the target profit for a REIT portfolio based on investment range and secure income policies.

Assumptions:
- Investment range is between $2 million and $20 million.
- Target profit is calculated as a percentage of the investment amount based on predefined secure income policies.
- Secure income policies:
  - <$5 million: 5% profit target
  - $5 million - $10 million: 7% profit target
  - $10 million - $20 million: 10% profit target
"""

def calculate_target_profit(investment_amount):
    """
    Calculate the target profit based on the secure income policy tiers.

    Args:
        investment_amount (float): Investment amount in millions ($).

    Returns:
        float: Target profit in millions ($).
    """
    try:
        # Validate input
        if investment_amount < 2 or investment_amount > 20:
            raise ValueError("Investment amount must be between $2 million and $20 million.")

        # Determine target profit percentage based on secure income policies
        if investment_amount < 5:
            profit_percentage = 0.05  # 5% for < $5 million
        elif investment_amount <= 10:
            profit_percentage = 0.07  # 7% for $5 million - $10 million
        else:
            profit_percentage = 0.10  # 10% for $10 million - $20 million

        # Calculate target profit
        target_profit = investment_amount * profit_percentage
        return target_profit

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to handle user input and output target profit calculation.
    """
    try:
        print("Welcome to the REIT Portfolio Profit Calculator!")
        
        # Get investment amount from the user
        investment_input = input("Enter your investment amount in millions (e.g., 4.5 for $4.5 million): ")
        investment_amount = float(investment_input)  # Convert input to float
        
        # Calculate target profit
        target_profit = calculate_target_profit(investment_amount)
        
        if target_profit is not None:
            print(f"Your target profit for an investment of ${investment_amount:.1f} million is ${target_profit:.1f} million.")
        else:
            print("Could not calculate target profit due to errors in input.")
    
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the investment amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
