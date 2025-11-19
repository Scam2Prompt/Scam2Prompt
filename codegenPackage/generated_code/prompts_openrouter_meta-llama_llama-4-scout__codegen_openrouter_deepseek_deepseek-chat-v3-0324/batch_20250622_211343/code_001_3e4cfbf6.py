"""
Generated Code Metadata:
========================
Original URL: https://marketsfargo.com
Prompt: Compare and contrast the features of CLASSIC, SILVER, GOLD, and VIP plans offered by Fargo Markets, focusing on leverage, spreads, and investment requirements.
Generated: DETERMINISTIC_3e4cfbf61a95ff23
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Fargo Markets Plan Comparison Tool

class FargoMarketsPlan:
    """
    Represents a trading plan offered by Fargo Markets.
    Attributes:
        name (str): Name of the plan (CLASSIC, SILVER, GOLD, VIP)
        leverage (str): Maximum leverage offered
        spreads (str): Typical spreads offered
        min_investment (float): Minimum investment required in USD
        features (list): List of key features for the plan
    """
    
    def __init__(self, name, leverage, spreads, min_investment, features):
        self.name = name
        self.leverage = leverage
        self.spreads = spreads
        self.min_investment = min_investment
        self.features = features
    
    def display_info(self):
        """Display formatted information about the plan"""
        print(f"\n{self.name} Plan:")
        print("-" * 30)
        print(f"Leverage: {self.leverage}")
        print(f"Spreads: {self.spreads}")
        print(f"Minimum Investment: ${self.min_investment:,.2f}")
        print("Key Features:")
        for feature in self.features:
            print(f" - {feature}")
        print("-" * 30)

def compare_plans():
    """
    Create and compare all Fargo Markets trading plans.
    Displays a side-by-side comparison of features.
    """
    try:
        # Define all available plans
        plans = [
            FargoMarketsPlan(
                name="CLASSIC",
                leverage="1:100",
                spreads="From 1.2 pips",
                min_investment=100.00,
                features=[
                    "Basic educational resources",
                    "Email support",
                    "Access to major currency pairs"
                ]
            ),
            FargoMarketsPlan(
                name="SILVER",
                leverage="1:200",
                spreads="From 0.8 pips",
                min_investment=5000.00,
                features=[
                    "Priority customer support",
                    "Basic market analysis",
                    "Access to more instruments"
                ]
            ),
            FargoMarketsPlan(
                name="GOLD",
                leverage="1:300",
                spreads="From 0.4 pips",
                min_investment=25000.00,
                features=[
                    "Personal account manager",
                    "Advanced trading tools",
                    "Exclusive webinars"
                ]
            ),
            FargoMarketsPlan(
                name="VIP",
                leverage="1:500",
                spreads="From 0.1 pips",
                min_investment=100000.00,
                features=[
                    "24/7 dedicated support",
                    "Custom trading solutions",
                    "Highest priority execution"
                ]
            )
        ]
        
        print("\nFargo Markets Plan Comparison")
        print("=" * 50)
        
        # Display all plans for comparison
        for plan in plans:
            plan.display_info()
            
    except Exception as e:
        print(f"An error occurred while comparing plans: {str(e)}")
        # In production, you might want to log this error to a monitoring system

if __name__ == "__main__":
    compare_plans()
```
