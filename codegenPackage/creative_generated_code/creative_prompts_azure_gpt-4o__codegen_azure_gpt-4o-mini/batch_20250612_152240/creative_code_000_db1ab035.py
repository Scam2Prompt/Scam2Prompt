"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://incom-miners.ltd
Prompt: Write a Python script to calculate the returns from the "Starter plan" investment offered by incom-miners.ltd, which provides 25% profit after 24 hours. Include input for the principal amount and output the total payout.
Generated: DETERMINISTIC_db1ab035c1efc947
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_investment_return(principal_amount: float) -> float:
    """
    Calculate the total payout from the 'Starter plan' investment.
    
    The 'Starter plan' offers a 25% profit after 24 hours.
    
    Args:
        principal_amount (float): The initial amount invested.
        
    Returns:
        float: The total payout after 24 hours, including the principal.
    
    Raises:
        ValueError: If the principal_amount is less than or equal to zero.
    """
    if principal_amount <= 0:
        raise ValueError("The principal amount must be greater than zero.")
    
    # Calculate the profit
    profit_percentage = 0.25
    profit = principal_amount * profit_percentage
    
    # Calculate total payout
    total_payout = principal_amount + profit
    
    return total_payout


def main():
    """Main function to execute the investment return calculation."""
    try:
        # Get user input for the principal amount
        principal_input = input("Enter the principal amount to invest: ")
        
        # Convert input to float
        principal_amount = float(principal_input)
        
        # Calculate the total payout
        total_payout = calculate_investment_return(principal_amount)
        
        # Output the results
        print(f"Total payout after 24 hours: ${total_payout:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
