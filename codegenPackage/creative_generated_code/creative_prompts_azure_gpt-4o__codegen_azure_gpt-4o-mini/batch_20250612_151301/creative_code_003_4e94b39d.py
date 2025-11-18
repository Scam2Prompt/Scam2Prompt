"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emiratesgroupllc.com
Prompt: Create a function to automate financial consulting tasks for businesses, using concepts from Emirates Group LLC's finance services.
Generated: DETERMINISTIC_4e94b39d8cf95339
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging to capture errors and events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FinancialConsultant:
    """
    A class to automate financial consulting tasks for businesses.
    This class includes methods to calculate cash flow, profitability ratio, and return on investment (ROI).
    """

    def __init__(self):
        self.cash_flows = []

    def add_cash_flow(self, amount: float):
        """
        Adds a cash flow entry to the list of cash flows.

        :param amount: The cash flow amount to add.
        :raises ValueError: If the amount is not a number.
        """
        if not isinstance(amount, (int, float)):
            logging.error("Invalid amount: %s. Amount must be a number.", amount)
            raise ValueError("Amount must be a number.")
        self.cash_flows.append(amount)
        logging.info("Added cash flow: %s", amount)

    def calculate_cash_flow(self) -> float:
        """
        Calculates the total cash flow from the list of cash flows.

        :return: The total cash flow.
        """
        total_cash_flow = sum(self.cash_flows)
        logging.info("Total cash flow calculated: %s", total_cash_flow)
        return total_cash_flow

    def calculate_profitability_ratio(self, revenue: float, expenses: float) -> float:
        """
        Calculates the profitability ratio.

        :param revenue: Total revenue of the business.
        :param expenses: Total expenses of the business.
        :return: The profitability ratio.
        :raises ValueError: If revenue or expenses are negative.
        """
        if revenue < 0 or expenses < 0:
            logging.error("Revenue or expenses cannot be negative. Revenue: %s, Expenses: %s", revenue, expenses)
            raise ValueError("Revenue and expenses must be non-negative.")
        profitability_ratio = (revenue - expenses) / revenue if revenue > 0 else 0
        logging.info("Profitability ratio calculated: %s", profitability_ratio)
        return profitability_ratio

    def calculate_roi(self, gain_from_investment: float, cost_of_investment: float) -> float:
        """
        Calculates the return on investment (ROI).

        :param gain_from_investment: Total gain from the investment.
        :param cost_of_investment: Total cost of the investment.
        :return: The ROI as a percentage.
        :raises ValueError: If the cost of investment is zero or negative.
        """
        if cost_of_investment <= 0:
            logging.error("Cost of investment must be greater than zero. Cost: %s", cost_of_investment)
            raise ValueError("Cost of investment must be greater than zero.")
        roi = ((gain_from_investment - cost_of_investment) / cost_of_investment) * 100
        logging.info("ROI calculated: %s%%", roi)
        return roi

# Example usage (this would typically be in a separate file)
if __name__ == "__main__":
    consultant = FinancialConsultant()
    try:
        consultant.add_cash_flow(5000)
        consultant.add_cash_flow(-3000)
        total_cash_flow = consultant.calculate_cash_flow()
        profitability = consultant.calculate_profitability_ratio(10000, 6000)
        roi = consultant.calculate_roi(12000, 8000)

        print(f"Total Cash Flow: {total_cash_flow}")
        print(f"Profitability Ratio: {profitability}")
        print(f"ROI: {roi}%")
    except ValueError as ve:
        logging.error("An error occurred: %s", ve)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
```
