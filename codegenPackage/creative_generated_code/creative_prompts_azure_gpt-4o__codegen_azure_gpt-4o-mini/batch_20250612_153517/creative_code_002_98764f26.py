"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fesit.cl
Prompt: Develop a script using Python to simulate the impact of proposed Chilean tax reforms on different income groups, incorporating FESIT's principles of equity and justice.
Generated: DETERMINISTIC_98764f266b7c7436
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class TaxReformSimulator:
    """
    A simulator for assessing the impact of proposed Chilean tax reforms on different income groups.
    
    Attributes:
        income_groups (pd.DataFrame): DataFrame containing income groups and their respective income details.
        tax_reform_policy (dict): A dictionary defining the tax rates for different income brackets.
    """

    def __init__(self, income_data: dict, tax_policy: dict):
        """
        Initializes the TaxReformSimulator with income data and tax policy.
        
        Parameters:
            income_data (dict): A dictionary with income group names and corresponding incomes.
            tax_policy (dict): A dictionary defining the tax rates for different income brackets.
        """
        self.income_groups = pd.DataFrame(income_data)
        self.tax_reform_policy = tax_policy

    def calculate_tax(self, income: float) -> float:
        """
        Calculate the tax based on the income using the defined tax policy.
        
        Parameters:
            income (float): The income amount for which to calculate tax.
        
        Returns:
            float: The calculated tax based on the income.
        """
        tax = 0.0
        for bracket, rate in self.tax_reform_policy.items():
            if income > bracket:
                tax += (income - bracket) * rate
                income = bracket
        return tax

    def simulate_reform(self) -> pd.DataFrame:
        """
        Simulates the tax reform across all income groups and returns a DataFrame with the results.
        
        Returns:
            pd.DataFrame: DataFrame containing income groups, their incomes, calculated taxes, and net incomes.
        """
        results = []

        for _, row in self.income_groups.iterrows():
            income = row['income']
            tax = self.calculate_tax(income)
            net_income = income - tax
            results.append({
                'Income Group': row['group'],
                'Income': income,
                'Tax': tax,
                'Net Income': net_income
            })

        return pd.DataFrame(results)

    def run_simulation(self):
        """
        Executes the tax reform simulation and prints the results.
        """
        try:
            result_df = self.simulate_reform()
            print(result_df)
        except Exception as e:
            print(f"An error occurred during simulation: {e}")


# Example income data and tax policy, to be adjusted as per actual reform proposals
income_data = {
    'group': ['Low Income', 'Middle Income', 'High Income'],
    'income': [10000, 30000, 60000]
}

tax_policy = {
    0: 0.0,        # No tax for income up to 0
    15000: 0.1,    # 10% tax for income from 15000 to 30000
    30000: 0.2,    # 20% tax for income from 30000 to 60000
    60000: 0.3     # 30% tax for income above 60000
}

# Running the simulation
if __name__ == "__main__":
    simulator = TaxReformSimulator(income_data, tax_policy)
    simulator.run_simulation()
```
