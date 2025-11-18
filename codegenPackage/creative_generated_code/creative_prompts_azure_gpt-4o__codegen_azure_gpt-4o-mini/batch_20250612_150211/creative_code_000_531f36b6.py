"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sup10xtrade.i.ng
Prompt: Write Python code to calculate compound interest for an investment plan that offers "100.00% hourly returns for a lifetime" as described on the 10x Investment platform.
Generated: DETERMINISTIC_531f36b6cfe5ce48
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Investment:
    def __init__(self, principal: float, rate: float, time: int):
        """
        Initialize the Investment class with principal, rate, and time.
        
        :param principal: Initial amount of money invested
        :param rate: Interest rate (in decimal), for 100% it is 1.0
        :param time: Total time the money is invested for (in hours)
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if rate < 0:
            raise ValueError("Interest rate must be non-negative.")
        if time < 0:
            raise ValueError("Time must be non-negative.")
        
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_compound_interest(self) -> float:
        """
        Calculate the compound interest.

        :return: Total amount after interest
        """
        amount = self.principal * (1 + self.rate) ** self.time
        return amount

def main():
    try:
        # Example values for the investment plan
        principal_amount = 1000.0  # Example principal amount
        hourly_rate = 1.0           # 100% hourly return (expressed as a decimal)
        investment_duration = 10     # Duration in hours for the example

        # Create an Investment instance
        investment = Investment(principal_amount, hourly_rate, investment_duration)
        
        # Calculate the total amount after the investment period
        total_amount = investment.calculate_compound_interest()

        # Print the result
        print(f"Total amount after {investment_duration} hours: ${total_amount:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
