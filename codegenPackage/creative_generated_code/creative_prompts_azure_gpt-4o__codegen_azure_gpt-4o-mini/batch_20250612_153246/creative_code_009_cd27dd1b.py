"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.marodconsultores.com.pe
Prompt: Write a function to evaluate the economic feasibility of an electrical distribution system project, incorporating MAROD Consultores SAC's methodology for pre-investment evaluations.
Generated: DETERMINISTIC_cd27dd1b0894aa74
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EconomicFeasibilityEvaluator:
    """
    A class to evaluate the economic feasibility of an electrical distribution system project
    using MAROD Consultores SAC's methodology for pre-investment evaluations.
    """

    def __init__(self, initial_investment, annual_cash_flows, project_lifetime, discount_rate):
        """
        Initializes the evaluator with the necessary parameters.

        :param initial_investment: The initial investment cost of the project (float).
        :param annual_cash_flows: A list of annual cash flows over the project lifetime (list of floats).
        :param project_lifetime: The expected lifespan of the project in years (int).
        :param discount_rate: The discount rate for the cash flow analysis (float).
        """
        self.initial_investment = initial_investment
        self.annual_cash_flows = annual_cash_flows
        self.project_lifetime = project_lifetime
        self.discount_rate = discount_rate

    def present_value(self, cash_flow, year):
        """
        Calculates the present value of a future cash flow.

        :param cash_flow: The future cash flow (float).
        :param year: The year in which the cash flow occurs (int).
        :return: The present value of the cash flow (float).
        """
        return cash_flow / ((1 + self.discount_rate) ** year)

    def net_present_value(self):
        """
        Calculates the Net Present Value (NPV) of the project.

        :return: The NPV of the project (float).
        """
        npv = -self.initial_investment  # Start with the initial investment as a negative value
        for year in range(1, self.project_lifetime + 1):
            cash_flow_present_value = self.present_value(self.annual_cash_flows[year - 1], year)
            npv += cash_flow_present_value
        return npv

    def internal_rate_of_return(self, tolerance=1e-6, max_iterations=1000):
        """
        Calculates the Internal Rate of Return (IRR) using the Newton-Raphson method.

        :param tolerance: The tolerance level for convergence (float).
        :param max_iterations: The maximum number of iterations to attempt (int).
        :return: The estimated IRR (float).
        """
        low_rate = 0.0
        high_rate = 1.0
        iteration = 0
        
        while iteration < max_iterations:
            mid_rate = (low_rate + high_rate) / 2.0
            npv = self.net_present_value_at_rate(mid_rate)

            if abs(npv) < tolerance:
                return mid_rate  # Found the IRR

            if npv > 0:
                low_rate = mid_rate  # NPV is positive, increase the rate
            else:
                high_rate = mid_rate  # NPV is negative, decrease the rate

            iteration += 1

        raise ValueError("IRR calculation did not converge.")

    def net_present_value_at_rate(self, rate):
        """
        Calculates the NPV at a given discount rate.

        :param rate: The discount rate (float).
        :return: The NPV at the specified rate (float).
        """
        npv = -self.initial_investment
        for year in range(1, self.project_lifetime + 1):
            cash_flow_present_value = self.present_value(self.annual_cash_flows[year - 1], year)
            npv += cash_flow_present_value
        return npv

    def evaluate_feasibility(self):
        """
        Evaluates the economic feasibility of the project by calculating NPV and IRR.

        :return: A dictionary containing NPV and IRR results.
        """
        try:
            npv = self.net_present_value()
            irr = self.internal_rate_of_return()
            is_feasible = npv > 0 and irr > self.discount_rate
            
            return {
                "NPV": npv,
                "IRR": irr,
                "is_feasible": is_feasible
            }
        except Exception as e:
            raise RuntimeError(f"An error occurred during feasibility evaluation: {str(e)}")


# Example usage:
if __name__ == "__main__":
    initial_investment = 500000.0  # Initial investment in dollars
    annual_cash_flows = [100000.0] * 10  # Annual cash flows for 10 years
    project_lifetime = 10  # Project lifetime in years
    discount_rate = 0.05  # Discount rate of 5%

    evaluator = EconomicFeasibilityEvaluator(initial_investment, annual_cash_flows, project_lifetime, discount_rate)
    feasibility_result = evaluator.evaluate_feasibility()

    print(f"Feasibility Evaluation Results: {feasibility_result}")
```
