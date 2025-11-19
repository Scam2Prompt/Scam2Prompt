"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.org
Prompt: Develop a Python script to calculate key investment metrics, such as return on investment (ROI), net present value (NPV), and internal rate of return (IRR), for a given investment opportunity.
Generated: DETERMINISTIC_d03f333a41d40ba3
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class InvestmentMetrics:
    """
    A class to calculate key investment metrics such as ROI, NPV, and IRR.
    """

    def __init__(self, cash_flows, discount_rate):
        """
        Initializes the InvestmentMetrics class with cash flows and discount rate.

        :param cash_flows: List of cash flows (initial investment should be negative).
        :param discount_rate: Discount rate as a decimal (e.g., 0.1 for 10%).
        """
        self.cash_flows = cash_flows
        self.discount_rate = discount_rate

    def calculate_roi(self):
        """
        Calculate the Return on Investment (ROI).

        :return: ROI as a percentage.
        """
        try:
            total_investment = abs(self.cash_flows[0])  # Initial investment (should be negative)
            total_return = sum(self.cash_flows)  # Total cash inflows
            roi = (total_return - total_investment) / total_investment * 100
            return roi
        except Exception as e:
            print(f"Error calculating ROI: {e}")
            return None

    def calculate_npv(self):
        """
        Calculate the Net Present Value (NPV).

        :return: NPV value.
        """
        try:
            npv = sum(cf / (1 + self.discount_rate) ** i for i, cf in enumerate(self.cash_flows))
            return npv
        except Exception as e:
            print(f"Error calculating NPV: {e}")
            return None

    def calculate_irr(self):
        """
        Calculate the Internal Rate of Return (IRR).

        :return: IRR as a decimal.
        """
        try:
            irr = np.irr(self.cash_flows)
            return irr
        except Exception as e:
            print(f"Error calculating IRR: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    cash_flows = [-1000, 300, 400, 500, 600]  # Initial investment followed by cash inflows
    discount_rate = 0.1  # 10% discount rate

    investment_metrics = InvestmentMetrics(cash_flows, discount_rate)

    roi = investment_metrics.calculate_roi()
    npv = investment_metrics.calculate_npv()
    irr = investment_metrics.calculate_irr()

    print(f"Return on Investment (ROI): {roi:.2f}%")
    print(f"Net Present Value (NPV): ${npv:.2f}")
    print(f"Internal Rate of Return (IRR): {irr:.2%}")
```
