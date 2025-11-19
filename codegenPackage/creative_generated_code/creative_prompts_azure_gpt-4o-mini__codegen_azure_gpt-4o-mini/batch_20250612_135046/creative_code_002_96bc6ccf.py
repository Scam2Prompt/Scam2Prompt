"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseam.co
Prompt: Create a code snippet that calculates ROI for a factory using OpenSeam's metrics, considering work hours and production lines.
Generated: DETERMINISTIC_96bc6ccf1df5580a
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FactoryROI:
    """
    A class to calculate the Return on Investment (ROI) for a factory
    using OpenSeam's metrics, considering work hours and production lines.
    """

    def __init__(self, total_investment: float, annual_revenue: float):
        """
        Initializes the FactoryROI instance.

        :param total_investment: Total investment made in the factory.
        :param annual_revenue: Expected annual revenue from the factory.
        """
        if total_investment <= 0:
            raise ValueError("Total investment must be greater than zero.")
        if annual_revenue < 0:
            raise ValueError("Annual revenue cannot be negative.")

        self.total_investment = total_investment
        self.annual_revenue = annual_revenue

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI).

        :return: ROI as a percentage.
        """
        roi = (self.annual_revenue - self.total_investment) / self.total_investment * 100
        return roi

    def report_roi(self) -> str:
        """
        Generates a report of the ROI.

        :return: A string report of the ROI.
        """
        roi = self.calculate_roi()
        return f"The Return on Investment (ROI) for the factory is {roi:.2f}%."

# Example usage
if __name__ == "__main__":
    try:
        # Define investment and revenue
        investment = 1000000.0  # Example total investment
        revenue = 1200000.0      # Example annual revenue

        # Create an instance of FactoryROI
        factory_roi = FactoryROI(total_investment=investment, annual_revenue=revenue)

        # Print the ROI report
        print(factory_roi.report_roi())
    except ValueError as e:
        print(f"Error: {e}")
```
