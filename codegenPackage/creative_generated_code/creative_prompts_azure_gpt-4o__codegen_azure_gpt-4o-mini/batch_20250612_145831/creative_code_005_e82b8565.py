"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Write code to simulate the payout schedule for Smarts-invests' investment plans, including daily payments and principal return after a specified duration.
Generated: DETERMINISTIC_e82b85657d47de13
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class to represent an investment plan with a daily payout schedule.

    Attributes
    ----------
    principal : float
        The initial amount invested.
    daily_interest_rate : float
        The daily interest rate as a decimal (e.g., 0.01 for 1%).
    duration_days : int
        The total duration of the investment in days.
    """

    def __init__(self, principal: float, daily_interest_rate: float, duration_days: int):
        """
        Initializes the InvestmentPlan with principal, daily interest rate, and duration.

        Parameters
        ----------
        principal : float
            The initial investment amount.
        daily_interest_rate : float
            The daily interest rate (as a decimal).
        duration_days : int
            The duration of the investment in days.
        """
        if principal <= 0:
            raise ValueError("Principal must be a positive amount.")
        if not (0 <= daily_interest_rate <= 1):
            raise ValueError("Daily interest rate must be between 0 and 1.")
        if duration_days <= 0:
            raise ValueError("Duration in days must be a positive integer.")

        self.principal = principal
        self.daily_interest_rate = daily_interest_rate
        self.duration_days = duration_days

    def calculate_daily_payments(self):
        """
        Calculates the daily payouts for the investment plan.

        Returns
        -------
        list of float
            A list containing daily payouts for the duration of the investment.
        """
        daily_payments = []
        for day in range(1, self.duration_days + 1):
            daily_payment = self.principal * self.daily_interest_rate
            daily_payments.append(daily_payment)
        return daily_payments

    def calculate_total_payout(self):
        """
        Calculates the total payout including principal return after the duration.

        Returns
        -------
        float
            The total amount received after the duration.
        """
        total_interest = sum(self.calculate_daily_payments())
        total_payout = self.principal + total_interest
        return total_payout

    def simulate_investment(self):
        """
        Simulates the investment plan by returning daily payments and the total payout.

        Returns
        -------
        dict
            A dictionary containing daily payments and total payout.
        """
        try:
            daily_payments = self.calculate_daily_payments()
            total_payout = self.calculate_total_payout()
            return {
                "daily_payments": daily_payments,
                "total_payout": total_payout
            }
        except Exception as e:
            print(f"An error occurred during simulation: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    try:
        # Define the investment plan parameters
        principal_amount = 1000.0  # Principal amount in currency
        daily_rate = 0.01          # Daily interest rate (1%)
        duration = 30              # Duration in days

        # Create an instance of InvestmentPlan
        investment_plan = InvestmentPlan(principal=principal_amount,
                                          daily_interest_rate=daily_rate,
                                          duration_days=duration)

        # Simulate the investment
        result = investment_plan.simulate_investment()

        # Output the results
        if result:
            print("Daily Payments:", result["daily_payments"])
            print("Total Payout after duration:", result["total_payout"])

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
