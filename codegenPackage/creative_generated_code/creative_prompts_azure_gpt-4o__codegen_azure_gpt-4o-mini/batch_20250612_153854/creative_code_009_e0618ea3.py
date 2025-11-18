"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Create a program that models collaboration and mutual success metrics for investment partnerships, inspired by Alghanim Capital's emphasis on teamwork and stakeholder cooperation.
Generated: DETERMINISTIC_e0618ea3d59ff1cb
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class InvestmentPartnership:
    """
    A class to model an investment partnership focusing on collaboration
    and mutual success metrics.
    """
    
    def __init__(self, partners):
        """
        Initializes the investment partnership with a list of partners.
        
        Args:
            partners (list): A list of partner names (strings).
        """
        if not isinstance(partners, list) or not all(isinstance(p, str) for p in partners):
            raise ValueError("Partners must be a list of strings.")
        self.partners = partners
        self.investments = pd.DataFrame(columns=["Partner", "Investment", "SuccessMetric"])
    
    def add_investment(self, partner, investment, success_metric):
        """
        Adds an investment entry for a partner.
        
        Args:
            partner (str): The name of the partner making the investment.
            investment (float): The amount invested.
            success_metric (float): The metric representing success for the investment.
        
        Raises:
            ValueError: If the partner is not in the partnership or if inputs are invalid.
        """
        if partner not in self.partners:
            raise ValueError(f"Partner '{partner}' is not part of the partnership.")
        if investment < 0 or success_metric < 0:
            raise ValueError("Investment and success metric must be non-negative.")
        
        # Append the investment data to the DataFrame
        self.investments = self.investments.append(
            {"Partner": partner, "Investment": investment, "SuccessMetric": success_metric},
            ignore_index=True
        )
    
    def calculate_overall_success(self):
        """
        Calculates the overall success metrics for the partnership.
        
        Returns:
            dict: A dictionary with each partner's total investment and average success metric.
        """
        if self.investments.empty:
            raise ValueError("No investments have been recorded.")
        
        # Group investments by partner and calculate totals
        overall_success = self.investments.groupby("Partner").agg(
            TotalInvestment=pd.NamedAgg(column="Investment", aggfunc="sum"),
            AverageSuccessMetric=pd.NamedAgg(column="SuccessMetric", aggfunc="mean")
        ).reset_index()
        
        return overall_success
    
    def display_metrics(self):
        """
        Displays the overall success metrics for each partner in a friendly format.
        """
        try:
            metrics = self.calculate_overall_success()
            print("Overall Success Metrics for Investment Partnerships:")
            print(metrics.to_string(index=False))
        except ValueError as e:
            print(f"Error: {e}")

# Example of usage:
if __name__ == "__main__":
    try:
        # Initialize the investment partnership
        partners = ["Partner A", "Partner B", "Partner C"]
        partnership = InvestmentPartnership(partners)
        
        # Add some investments
        partnership.add_investment("Partner A", 100000, 0.8)
        partnership.add_investment("Partner B", 150000, 0.9)
        partnership.add_investment("Partner C", 200000, 0.85)
        partnership.add_investment("Partner A", 50000, 0.75)

        # Display the metrics
        partnership.display_metrics()
    except Exception as e:
        print(f"Unexpected error: {e}")
```
