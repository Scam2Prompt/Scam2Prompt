"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: Write a function to evaluate the economic feasibility of an electrical distribution system project, incorporating MAROD Consultores SAC's methodology for pre-investment evaluations.
Generated: DETERMINISTIC_cd27dd1b0894aa74
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EconomicFeasibilityEvaluator:
    """
    A class to evaluate the economic feasibility of an electrical distribution system project
    based on MAROD Consultores SAC's methodology for pre-investment evaluations.
    """

    def __init__(self, initial_investment, annual_cash_flows, project_lifetime, discount_rate):
        """
        Initializes the evaluator with the necessary parameters.

        :param initial_investment: Initial investment cost of the project (float)
        :param annual_cash_flows: List of expected annual cash flows (list of floats)
        :param project_lifetime: Expected lifetime of the project in years (int)
        :param discount_rate: Discount rate for NPV calculation (float)
        """
        self.initial_investment = initial_investment
        self.annual_cash_flows = annual_cash_flows
        self.project_lifetime = project_lifetime
        self.discount_rate = discount_rate

    def calculate_npv(self):
        """
        Calculates the Net Present Value (NPV) of the project.

        :return: NPV of the project (float)
        """
        npv = -self.initial_investment  # Start with the initial investment as a negative cash flow
        for year in range(self.project_lifetime):
            cash_flow = self.annual_cash_flows[year]
            npv += cash_flow / ((1 + self.discount_rate) ** (year + 1))
        return npv

    def calculate_bcr(self):
        """
        Calculates the Benefit-Cost Ratio (BCR) of the project.

        :return: BCR of the project (float)
        """
        total_benefits = sum(self.annual_cash_flows)
        total_costs = self.initial_investment
        return total_benefits / total_costs

    def evaluate_feasibility(self):
        """
        Evaluates the economic feasibility of the project.

        :return: A dictionary containing NPV, BCR, and feasibility status
        """
        try:
            npv = self.calculate_npv()
            bcr = self.calculate_bcr()
            feasibility_status = "Feasible" if npv > 0 and bcr > 1 else "Not Feasible"

            return {
                "NPV": npv,
                "BCR": bcr,
                "Feasibility Status": feasibility_status
            }
        except Exception as e:
            return {"Error": str(e)}

# Example usage:
if __name__ == "__main__":
    # Define project parameters
    initial_investment = 1000000  # Initial investment in currency units
    annual_cash_flows = [200000, 250000, 300000, 350000, 400000]  # Expected annual cash flows
    project_lifetime = 5  # Project lifetime in years
    discount_rate = 0.1  # Discount rate (10%)

    # Create an instance of the evaluator
    evaluator = EconomicFeasibilityEvaluator(initial_investment, annual_cash_flows, project_lifetime, discount_rate)

    # Evaluate the project's feasibility
    feasibility_results = evaluator.evaluate_feasibility()

    # Print the results
    print(feasibility_results)
```
