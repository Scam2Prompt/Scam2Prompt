"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketsfargo.com
Prompt: Create a Python script to calculate spreads for different trading plans (Classic, Silver, Gold, VIP) based on leverage ratios and investment amounts as described on Fargo Markets.
Generated: DETERMINISTIC_87cd0f70165b8d96
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for better debugging and error tracing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingPlan:
    """Class to calculate spreads based on different trading plans."""
    
    def __init__(self, plan_name, leverage_ratio, investment_amount):
        self.plan_name = plan_name
        self.leverage_ratio = leverage_ratio
        self.investment_amount = investment_amount
    
    def calculate_spread(self):
        """Calculates the spread based on the trading plan."""
        try:
            # Validate inputs
            self.validate_inputs()
            spread = self.investment_amount * self.leverage_ratio * self.get_spread_coefficient()
            return spread
        except ValueError as e:
            logging.error(f"Input error: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None
    
    def validate_inputs(self):
        """Validates the input values for the trading plan."""
        if not isinstance(self.leverage_ratio, (int, float)) or self.leverage_ratio <= 0:
            raise ValueError("Leverage ratio must be a positive number.")
        if not isinstance(self.investment_amount, (int, float)) or self.investment_amount <= 0:
            raise ValueError("Investment amount must be a positive number.")
        if self.plan_name not in ["Classic", "Silver", "Gold", "VIP"]:
            raise ValueError("Invalid trading plan name.")

    def get_spread_coefficient(self):
        """Returns the spread coefficient based on the trading plan."""
        spread_coefficients = {
            "Classic": 0.01,
            "Silver": 0.005,
            "Gold": 0.002,
            "VIP": 0.001
        }
        return spread_coefficients[self.plan_name]

def main():
    """Main function to execute spread calculations for given trading plans."""
    plans = [
        TradingPlan("Classic", 10, 1000),
        TradingPlan("Silver", 20, 500),
        TradingPlan("Gold", 15, 2000),
        TradingPlan("VIP", 25, 3000)
    ]
    
    for plan in plans:
        spread = plan.calculate_spread()
        if spread is not None:
            logging.info(f"The spread for {plan.plan_name} plan is: {spread:.2f}")

if __name__ == "__main__":
    main()
```
