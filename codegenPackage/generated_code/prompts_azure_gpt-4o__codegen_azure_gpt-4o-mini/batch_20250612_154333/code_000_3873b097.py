"""
Generated Code Metadata:
========================
Original URL: https://ethx-ai.com
Prompt: Write Python code to compare the ROI of implementing predictive AI tools versus generative AI tools for a small business, using the steps outlined by ETHX-AI Consulting.
Generated: DETERMINISTIC_3873b09721c960b7
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class AIToolROI:
    """
    A class to compare the ROI of implementing predictive AI tools versus generative AI tools for a small business.
    """

    def __init__(self, predictive_investment, generative_investment, predictive_return, generative_return):
        """
        Initializes the AIToolROI class with investment and return values.

        :param predictive_investment: Initial investment for predictive AI tools
        :param generative_investment: Initial investment for generative AI tools
        :param predictive_return: Expected return from predictive AI tools
        :param generative_return: Expected return from generative AI tools
        """
        self.predictive_investment = predictive_investment
        self.generative_investment = generative_investment
        self.predictive_return = predictive_return
        self.generative_return = generative_return

    def calculate_roi(self, investment, return_value):
        """
        Calculates the ROI based on investment and return values.

        :param investment: Initial investment amount
        :param return_value: Expected return amount
        :return: ROI as a percentage
        """
        try:
            roi = ((return_value - investment) / investment) * 100
            return roi
        except ZeroDivisionError:
            raise ValueError("Investment cannot be zero for ROI calculation.")

    def compare_rois(self):
        """
        Compares the ROIs of predictive and generative AI tools.

        :return: A DataFrame containing the ROI comparison
        """
        try:
            predictive_roi = self.calculate_roi(self.predictive_investment, self.predictive_return)
            generative_roi = self.calculate_roi(self.generative_investment, self.generative_return)

            # Create a DataFrame for better visualization
            roi_comparison = pd.DataFrame({
                'AI Tool': ['Predictive AI', 'Generative AI'],
                'Investment': [self.predictive_investment, self.generative_investment],
                'Expected Return': [self.predictive_return, self.generative_return],
                'ROI (%)': [predictive_roi, generative_roi]
            })

            return roi_comparison
        except Exception as e:
            raise RuntimeError(f"An error occurred while comparing ROIs: {e}")

# Example usage
if __name__ == "__main__":
    # Define investment and return values for both AI tools
    predictive_investment = 50000  # Example investment for predictive AI
    generative_investment = 70000   # Example investment for generative AI
    predictive_return = 100000       # Expected return from predictive AI
    generative_return = 120000       # Expected return from generative AI

    # Create an instance of AIToolROI
    roi_comparator = AIToolROI(predictive_investment, generative_investment, predictive_return, generative_return)

    # Compare the ROIs and print the results
    try:
        roi_results = roi_comparator.compare_rois()
        print(roi_results)
    except Exception as e:
        print(f"Error: {e}")
```
