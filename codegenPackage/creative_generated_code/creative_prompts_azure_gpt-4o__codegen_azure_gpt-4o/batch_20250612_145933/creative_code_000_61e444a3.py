"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bi-verse.org
Prompt: Write Python code to calculate returns for Bi-Verse's "Amateur Plan" investment strategy, which offers 2.30% after 24 hours with a minimum investment of $100 and a maximum of $499.
Generated: DETERMINISTIC_61e444a332cdf95e
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from datetime import datetime, timedelta

# Define a class to encapsulate the investment strategy
class AmateurPlan:
    """
    A class representing Bi-Verse's "Amateur Plan" investment strategy.
    """
    MIN_INVESTMENT = 100  # Minimum investment in USD
    MAX_INVESTMENT = 499  # Maximum investment in USD
    RETURN_RATE = 0.023   # 2.30% return rate after 24 hours
    DURATION_HOURS = 24   # Duration of the investment in hours

    @staticmethod
    def calculate_return(investment_amount):
        """
        Calculate the returns for a given investment amount.
        
        :param investment_amount: Amount invested (must be between MIN_INVESTMENT and MAX_INVESTMENT)
        :return: A dictionary containing the investment details and returns
        :raises ValueError: If investment_amount is out of allowable range
        """
        # Validate investment amount
        if investment_amount < AmateurPlan.MIN_INVESTMENT or investment_amount > AmateurPlan.MAX_INVESTMENT:
            raise ValueError(
                f"Investment amount must be between ${AmateurPlan.MIN_INVESTMENT} and ${AmateurPlan.MAX_INVESTMENT}."
            )
        
        # Calculate the return amount
        return_amount = investment_amount * AmateurPlan.RETURN_RATE

        # Determine the time of maturity
        maturity_date = datetime.now() + timedelta(hours=AmateurPlan.DURATION_HOURS)

        # Return investment details
        return {
            "investment_amount": round(investment_amount, 2),
            "return_amount": round(return_amount, 2),
            "total_amount": round(investment_amount + return_amount, 2),
            "maturity_date": maturity_date.strftime("%Y-%m-%d %H:%M:%S"),
            "return_rate": f"{AmateurPlan.RETURN_RATE * 100:.2f}%",
        }


def main():
    """
    Main function to demonstrate the AmateurPlan investment calculation.
    """
    try:
        # Example investment
        investment = float(input("Enter the investment amount (between $100 and $499): "))
        
        # Calculate returns
        result = AmateurPlan.calculate_return(investment)
        
        # Display the results
        print("\nInvestment Details:")
        print(f"Investment Amount: ${result['investment_amount']}")
        print(f"Return Amount: ${result['return_amount']}")
        print(f"Total Amount (after 24 hours): ${result['total_amount']}")
        print(f"Return Rate: {result['return_rate']}")
        print(f"Maturity Date: {result['maturity_date']}")
    
    except ValueError as e:
        # Handle invalid investment amount
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
