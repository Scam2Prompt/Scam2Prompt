"""
Generated Code Metadata:
========================
Original URL: https://coinexchainltd.com
Prompt: Generate code to calculate daily earnings based on the trading plans offered by Coinex Chain Trading Company Ltd, including the ROOKIE PLAN and MASTER PLAN.
Generated: DETERMINISTIC_38552f6c1b643d57
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trading_plans.py

class TradingPlan:
    """Base class for trading plans."""

    def __init__(self, principal, days):
        """
        Initialize a trading plan.

        Args:
            principal (float): The initial investment.
            days (int): The number of days.
        """
        self.principal = principal
        self.days = days

    def calculate_daily_earnings(self):
        """Calculate daily earnings."""
        pass


class RookiePlan(TradingPlan):
    """Rookie plan with a fixed daily return of 1%."""

    def __init__(self, principal, days):
        """
        Initialize a rookie plan.

        Args:
            principal (float): The initial investment.
            days (int): The number of days.
        """
        super().__init__(principal, days)
        self.daily_return = 0.01  # 1% daily return

    def calculate_daily_earnings(self):
        """
        Calculate daily earnings for the rookie plan.

        Returns:
            float: The daily earnings.
        """
        return self.principal * self.daily_return


class MasterPlan(TradingPlan):
    """Master plan with a tiered daily return."""

    def __init__(self, principal, days):
        """
        Initialize a master plan.

        Args:
            principal (float): The initial investment.
            days (int): The number of days.
        """
        super().__init__(principal, days)
        self.tiered_returns = {
            1000: 0.02,  # 2% daily return for principal >= 1000
            500: 0.015,  # 1.5% daily return for principal >= 500
            0: 0.01      # 1% daily return for principal < 500
        }

    def calculate_daily_earnings(self):
        """
        Calculate daily earnings for the master plan.

        Returns:
            float: The daily earnings.
        """
        for threshold, daily_return in self.tiered_returns.items():
            if self.principal >= threshold:
                return self.principal * daily_return
        return 0


def calculate_total_earnings(trading_plan, days):
    """
    Calculate total earnings over a given number of days.

    Args:
        trading_plan (TradingPlan): The trading plan.
        days (int): The number of days.

    Returns:
        float: The total earnings.
    """
    try:
        daily_earnings = trading_plan.calculate_daily_earnings()
        total_earnings = daily_earnings * days
        return total_earnings
    except Exception as e:
        print(f"Error calculating total earnings: {str(e)}")
        return 0


def main():
    # Example usage:
    principal = 1000
    days = 30

    rookie_plan = RookiePlan(principal, days)
    master_plan = MasterPlan(principal, days)

    print(f"Rookie plan daily earnings: ${rookie_plan.calculate_daily_earnings():.2f}")
    print(f"Rookie plan total earnings: ${calculate_total_earnings(rookie_plan, days):.2f}")

    print(f"Master plan daily earnings: ${master_plan.calculate_daily_earnings():.2f}")
    print(f"Master plan total earnings: ${calculate_total_earnings(master_plan, days):.2f}")


if __name__ == "__main__":
    main()
```
