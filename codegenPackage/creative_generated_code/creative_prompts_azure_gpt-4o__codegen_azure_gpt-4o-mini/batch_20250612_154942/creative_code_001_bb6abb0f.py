"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libertyaid.co
Prompt: Generate code to calculate potential savings on Medicare Advantage plans, including options like PFFS, HMO, and PPO plans, based on user input for premium and out-of-pocket costs.
Generated: DETERMINISTIC_bb6abb0f3da16087
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MedicareAdvantageCalculator:
    """
    A class to calculate potential savings on Medicare Advantage plans including PFFS, HMO, and PPO plans.
    """

    def __init__(self):
        self.plans = {
            'PFFS': {'premium': 0, 'out_of_pocket': 0},
            'HMO': {'premium': 0, 'out_of_pocket': 0},
            'PPO': {'premium': 0, 'out_of_pocket': 0}
        }

    def input_plan_data(self):
        """
        Input the premium and out-of-pocket costs for each Medicare Advantage plan.
        """
        for plan in self.plans.keys():
            try:
                premium = float(input(f"Enter the monthly premium for {plan} plan: "))
                out_of_pocket = float(input(f"Enter the annual out-of-pocket costs for {plan} plan: "))
                self.plans[plan]['premium'] = premium
                self.plans[plan]['out_of_pocket'] = out_of_pocket
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                return self.input_plan_data()  # Recursive call for valid input

    def calculate_total_costs(self):
        """
        Calculate the total annual costs for each plan.
        Returns a dictionary of total costs for each plan.
        """
        total_costs = {}
        for plan, costs in self.plans.items():
            yearly_cost = (costs['premium'] * 12) + costs['out_of_pocket']
            total_costs[plan] = yearly_cost
        return total_costs

    def find_best_plan(self, total_costs):
        """
        Determine which plan has the lowest total cost.
        Returns the plan with the lowest cost and its associated value.
        """
        best_plan = min(total_costs, key=total_costs.get)
        return best_plan, total_costs[best_plan]

    def display_results(self, total_costs, best_plan):
        """
        Display the total costs for each plan and the best plan option.
        """
        print("\nTotal Annual Costs for Medicare Advantage Plans:")
        for plan, cost in total_costs.items():
            print(f"{plan} Plan: ${cost:.2f}")
        
        print(f"\nBest Plan: {best_plan[0]} with a total cost of ${best_plan[1]:.2f}")

    def run(self):
        """
        Execute the calculator workflow.
        """
        self.input_plan_data()
        total_costs = self.calculate_total_costs()
        best_plan = self.find_best_plan(total_costs)
        self.display_results(total_costs, best_plan)


if __name__ == "__main__":
    calculator = MedicareAdvantageCalculator()
    calculator.run()
```
