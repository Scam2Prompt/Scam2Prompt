"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchsheelbank.com
Prompt: Write a function to calculate overdraft limits against fixed deposits, based on the loan offerings described by Panchsheel Mercantile Co-op. Bank Ltd.
Generated: DETERMINISTIC_a24118334765b88a
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OverdraftCalculator:
    """
    A class to calculate overdraft limits against fixed deposits based on bank offerings.
    """

    def __init__(self, fixed_deposit_amount: float, interest_rate: float):
        """
        Initialize the overdraft calculator with a fixed deposit amount and interest rate.
        
        :param fixed_deposit_amount: The total amount of the fixed deposit.
        :param interest_rate: The annual interest rate applicable on the fixed deposit (in percentage).
        """
        if fixed_deposit_amount <= 0:
            raise ValueError("Fixed deposit amount must be greater than zero.")
        if not (0 <= interest_rate <= 100):
            raise ValueError("Interest rate must be between 0 and 100.")
        
        self.fixed_deposit_amount = fixed_deposit_amount
        self.interest_rate = interest_rate

    def calculate_overdraft_limit(self) -> float:
        """
        Calculate the overdraft limit based on the fixed deposit amount and interest rate.
        
        The overdraft limit is assumed to be a percentage of the fixed deposit amount. 
        In this case, we will assume a limit of 90% of the fixed deposit amount.

        :return: The overdraft limit calculated.
        """
        overdraft_limit_percentage = 0.90  # Assuming overdraft limit is 90% of FD amount
        overdraft_limit = self.fixed_deposit_amount * overdraft_limit_percentage
        
        return overdraft_limit

    def display_overdraft_limit(self):
        """
        Display the calculated overdraft limit in a formatted manner.
        """
        try:
            limit = self.calculate_overdraft_limit()
            print(f"The overdraft limit against a fixed deposit of ₹{self.fixed_deposit_amount:.2f} "
                  f"at an interest rate of {self.interest_rate:.2f}% is: ₹{limit:.2f}")
        except Exception as e:
            print(f"Error calculating overdraft limit: {e}")


# Example usage
if __name__ == "__main__":
    try:
        fd_amount = 1000000  # Example fixed deposit amount
        interest_rate = 5.0  # Example interest rate
        
        calculator = OverdraftCalculator(fd_amount, interest_rate)
        calculator.display_overdraft_limit()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
