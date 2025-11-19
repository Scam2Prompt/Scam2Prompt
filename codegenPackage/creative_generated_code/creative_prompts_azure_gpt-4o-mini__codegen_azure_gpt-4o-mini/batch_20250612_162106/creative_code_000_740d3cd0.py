"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quedge.io
Prompt: Generate a Python script to calculate the ROI for Aethir Edge devices based on different pricing tiers and earnings in digital assets.
Generated: DETERMINISTIC_740d3cd030ee1683
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AethirEdgeROI:
    """
    A class to calculate the Return on Investment (ROI) for Aethir Edge devices 
    based on pricing tiers and earnings in digital assets.
    """
    
    def __init__(self, initial_investment, device_price, earnings_per_month):
        """
        Initializes the AethirEdgeROI class with the necessary parameters.

        :param initial_investment: Initial investment made for purchasing the device.
        :param device_price: Price of the Aethir Edge device.
        :param earnings_per_month: Expected earnings in digital assets per month.
        """
        if initial_investment < 0 or device_price < 0 or earnings_per_month < 0:
            raise ValueError("Investment, device price, and earnings must be non-negative.")
        
        self.initial_investment = initial_investment
        self.device_price = device_price
        self.earnings_per_month = earnings_per_month
    
    def calculate_roi(self, months):
        """
        Calculates the Return on Investment (ROI) over a specified number of months.

        :param months: The number of months over which to calculate the ROI.
        :return: The ROI as a percentage.
        """
        if months < 0:
            raise ValueError("Months cannot be negative.")
        
        total_earnings = self.earnings_per_month * months
        total_cost = self.initial_investment + self.device_price

        # ROI formula: (Total Earnings - Total Cost) / Total Cost * 100
        roi = ((total_earnings - total_cost) / total_cost) * 100
        
        return roi

    def categorize_roi(self, roi):
        """
        Categorizes the ROI into different risk levels.

        :param roi: The calculated ROI.
        :return: A string indicating the risk category.
        """
        if roi < 0:
            return "Negative ROI - Loss"
        elif 0 <= roi < 10:
            return "Low ROI - Marginal Gain"
        elif 10 <= roi < 25:
            return "Moderate ROI - Reasonable Profit"
        else:
            return "High ROI - Excellent Profit Potential"

def main():
    """
    Main function to execute the ROI calculation for Aethir Edge devices.
    """
    try:
        # Example parameters - these can be modified as needed
        initial_investment = 1000.0  # User's initial investment in USD
        device_price = 500.0          # Price of the device in USD
        earnings_per_month = 150.0    # Expected earnings per month in digital assets
        months = 12                    # Duration in months for ROI calculation

        # Instantiate the AethirEdgeROI class
        roi_calculator = AethirEdgeROI(initial_investment, device_price, earnings_per_month)

        # Calculate ROI
        roi = roi_calculator.calculate_roi(months)
        print(f"Calculated ROI: {roi:.2f}%")

        # Categorize the ROI
        roi_category = roi_calculator.categorize_roi(roi)
        print(f"ROI Category: {roi_category}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
