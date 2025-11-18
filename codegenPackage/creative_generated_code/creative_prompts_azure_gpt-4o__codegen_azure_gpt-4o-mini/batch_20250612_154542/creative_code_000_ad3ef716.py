"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcoinners.com
Prompt: Write a Python script to simulate the investment plans offered by mcoinners.com, including ROI calculations for the BASIC, PREMIUM, ADVANCED, PRO, and VIP plans based on the given durations and deposit ranges.
Generated: DETERMINISTIC_ad3ef716313c8a75
Batch ID: 20250612_154542
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
    A class to represent an investment plan.
    """

    def __init__(self, name, min_deposit, max_deposit, roi_percentages):
        """
        Initialize an investment plan.

        :param name: Name of the investment plan
        :param min_deposit: Minimum deposit amount for the plan
        :param max_deposit: Maximum deposit amount for the plan
        :param roi_percentages: Dictionary of ROI percentages keyed by duration
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.roi_percentages = roi_percentages

    def calculate_roi(self, deposit, duration):
        """
        Calculate the return on investment.

        :param deposit: Amount deposited
        :param duration: Duration of the investment
        :return: Calculated ROI amount
        :raises ValueError: If deposit is out of valid range or duration is not valid
        """
        if not (self.min_deposit <= deposit <= self.max_deposit):
            raise ValueError(f"Deposit amount must be between {self.min_deposit} and {self.max_deposit}.")
        
        if duration not in self.roi_percentages:
            raise ValueError(f"Invalid duration. Allowed durations are: {list(self.roi_percentages.keys())}")

        roi_percentage = self.roi_percentages[duration]
        return deposit * (roi_percentage / 100)


# Define investment plans with their respective parameters
plans = {
    "BASIC": InvestmentPlan("BASIC", 100, 999, {30: 5, 60: 10, 90: 15}),
    "PREMIUM": InvestmentPlan("PREMIUM", 1000, 4999, {30: 7, 60: 12, 90: 20}),
    "ADVANCED": InvestmentPlan("ADVANCED", 5000, 9999, {30: 10, 60: 15, 90: 25}),
    "PRO": InvestmentPlan("PRO", 10000, 49999, {30: 12, 60: 18, 90: 30}),
    "VIP": InvestmentPlan("VIP", 50000, 1000000, {30: 15, 60: 25, 90: 40}),
}

def simulate_investment(plan_name, deposit, duration):
    """
    Simulate the investment and calculate the returns based on the selected plan.

    :param plan_name: Name of the investment plan
    :param deposit: Amount to invest
    :param duration: Duration of the investment
    :return: Total amount after ROI
    :raises ValueError: If the plan name is invalid
    """
    if plan_name not in plans:
        raise ValueError(f"Invalid plan name. Available plans are: {list(plans.keys())}")

    plan = plans[plan_name]
    roi = plan.calculate_roi(deposit, duration)
    total_amount = deposit + roi
    return total_amount


# Example usage
def main():
    try:
        plan_name = "PREMIUM"
        deposit = 2000
        duration = 60
        
        total_amount = simulate_investment(plan_name, deposit, duration)
        print(f"Total amount after ROI for {plan_name} plan: ${total_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
