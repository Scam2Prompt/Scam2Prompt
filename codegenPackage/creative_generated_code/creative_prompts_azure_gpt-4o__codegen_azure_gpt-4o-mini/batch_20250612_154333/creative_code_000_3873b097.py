"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethx-ai.com
Prompt: Write Python code to compare the ROI of implementing predictive AI tools versus generative AI tools for a small business, using the steps outlined by ETHX-AI Consulting.
Generated: DETERMINISTIC_3873b09721c960b7
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AIInvestmentAnalysis:
    """
    A class to analyze the Return on Investment (ROI) of predictive and generative AI tools
    for a small business.
    """

    def __init__(self, predictive_investment, generative_investment, revenue_increase_predictive, revenue_increase_generative):
        """
        Initialize the AIInvestmentAnalysis class with investment and revenue increase data.

        :param predictive_investment: Initial investment for predictive AI tools.
        :param generative_investment: Initial investment for generative AI tools.
        :param revenue_increase_predictive: Expected revenue increase from predictive AI tools.
        :param revenue_increase_generative: Expected revenue increase from generative AI tools.
        """
        self.predictive_investment = predictive_investment
        self.generative_investment = generative_investment
        self.revenue_increase_predictive = revenue_increase_predictive
        self.revenue_increase_generative = revenue_increase_generative

    def calculate_roi(self, investment, revenue_increase):
        """
        Calculate ROI based on investment and revenue increase.

        :param investment: Initial investment amount.
        :param revenue_increase: Expected revenue increase amount.
        :return: ROI as a percentage.
        """
        try:
            roi = (revenue_increase - investment) / investment * 100
            return roi
        except ZeroDivisionError:
            print("Error: Investment cannot be zero.")
            return None

    def compare_roi(self):
        """
        Compare the ROI of predictive and generative AI tools and display the results.

        :return: A DataFrame containing the ROI values.
        """
        predictive_roi = self.calculate_roi(self.predictive_investment, self.revenue_increase_predictive)
        generative_roi = self.calculate_roi(self.generative_investment, self.revenue_increase_generative)

        # Create a DataFrame for better visualization
        roi_data = pd.DataFrame({
            'AI Tool': ['Predictive AI', 'Generative AI'],
            'Investment': [self.predictive_investment, self.generative_investment],
            'Revenue Increase': [self.revenue_increase_predictive, self.revenue_increase_generative],
            'ROI (%)': [predictive_roi, generative_roi]
        })

        return roi_data

    def visualize_roi(self, roi_data):
        """
        Visualize the ROI comparison using a bar chart.

        :param roi_data: DataFrame containing the ROI data.
        """
        plt.figure(figsize=(10, 6))
        plt.bar(roi_data['AI Tool'], roi_data['ROI (%)'], color=['blue', 'orange'])
        plt.title('ROI Comparison of AI Tools')
        plt.xlabel('AI Tool')
        plt.ylabel('ROI (%)')
        plt.axhline(0, color='grey', linewidth=0.8, linestyle='--')
        plt.ylim(-100, 200)  # Adjust the y-axis limits based on expected ROI range
        plt.show()


# Example usage
if __name__ == "__main__":
    # Define investments and expected revenue increases for each AI type
    predictive_investment = 50000  # Example investment in predictive AI
    generative_investment = 70000   # Example investment in generative AI
    revenue_increase_predictive = 100000  # Expected revenue increase from predictive AI
    revenue_increase_generative = 150000   # Expected revenue increase from generative AI

    # Create an instance of AIInvestmentAnalysis
    analysis = AIInvestmentAnalysis(predictive_investment, generative_investment, revenue_increase_predictive, revenue_increase_generative)

    # Compare ROI and retrieve results
    roi_results = analysis.compare_roi()
    print(roi_results)

    # Visualize the ROI comparison
    analysis.visualize_roi(roi_results)
```
