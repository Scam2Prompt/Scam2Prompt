"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerlab.org
Prompt: Create a program to compare MinerLab's mining plans for different cryptocurrencies, calculating the most profitable option based on user input.
Generated: DETERMINISTIC_43ee262175c42b8d
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class MiningPlan:
    def __init__(self, name: str, hash_rate: float, power_consumption: float, cost_per_kwh: float, monthly_costs: float, coin_price: float, block_reward: float):
        """
        Initializes a MiningPlan object.

        :param name: Name of the mining plan
        :param hash_rate: Hash rate of the mining plan (in TH/s)
        :param power_consumption: Power consumption of the mining plan (in kW)
        :param cost_per_kwh: Cost of electricity per kWh
        :param monthly_costs: Other monthly costs associated with the mining operation
        :param coin_price: Current price of the mined cryptocurrency
        :param block_reward: Current block reward for the mined cryptocurrency
        """
        self.name = name
        self.hash_rate = hash_rate
        self.power_consumption = power_consumption
        self.cost_per_kwh = cost_per_kwh
        self.monthly_costs = monthly_costs
        self.coin_price = coin_price
        self.block_reward = block_reward

    def monthly_profit(self) -> float:
        """
        Calculates the monthly profit from the mining plan.

        :return: The monthly profit after deducting costs
        """
        # Calculate monthly power cost
        energy_cost = self.power_consumption * 24 * 30 * self.cost_per_kwh
        total_costs = energy_cost + self.monthly_costs
        
        # Calculate monthly revenue from mining
        # Assuming the mining efficiency is proportional to hash rate
        monthly_mined_coins = (self.hash_rate / 1000) * (self.block_reward * 30)  # TH/s to GH/s
        monthly_revenue = monthly_mined_coins * self.coin_price
        
        # Calculate profit
        profit = monthly_revenue - total_costs
        return profit

def compare_mining_plans(plans: list) -> pd.DataFrame:
    """
    Compares different mining plans and determines the most profitable option.

    :param plans: A list of MiningPlan objects
    :return: A DataFrame containing the profitability of each plan
    """
    results = []

    for plan in plans:
        profit = plan.monthly_profit()
        results.append({'Plan Name': plan.name, 'Monthly Profit': profit})

    return pd.DataFrame(results)

def main():
    # Example mining plans
    try:
        plans = [
            MiningPlan("Plan A", hash_rate=100, power_consumption=1.5, cost_per_kwh=0.10, monthly_costs=200, coin_price=2500, block_reward=6.25),
            MiningPlan("Plan B", hash_rate=200, power_consumption=2.0, cost_per_kwh=0.10, monthly_costs=300, coin_price=2500, block_reward=6.25),
            MiningPlan("Plan C", hash_rate=150, power_consumption=1.8, cost_per_kwh=0.10, monthly_costs=250, coin_price=2500, block_reward=6.25),
        ]

        # Compare mining plans
        comparison_results = compare_mining_plans(plans)
        print(comparison_results)

        # Identify the most profitable plan
        most_profitable_plan = comparison_results.loc[comparison_results['Monthly Profit'].idxmax()]
        print(f"The most profitable mining plan is: {most_profitable_plan['Plan Name']} with a profit of {most_profitable_plan['Monthly Profit']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
