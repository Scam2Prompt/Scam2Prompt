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
# Import required libraries
import pandas as pd
import numpy as np

class AI_Tool:
    def __init__(self, name, implementation_cost, monthly_maintenance_cost, 
                 predicted_revenue_increase, predicted_cost_savings):
        """
        Initialize an AI tool object.

        Args:
        - name (str): Name of the AI tool.
        - implementation_cost (float): One-time implementation cost of the AI tool.
        - monthly_maintenance_cost (float): Monthly maintenance cost of the AI tool.
        - predicted_revenue_increase (float): Predicted monthly revenue increase.
        - predicted_cost_savings (float): Predicted monthly cost savings.
        """
        self.name = name
        self.implementation_cost = implementation_cost
        self.monthly_maintenance_cost = monthly_maintenance_cost
        self.predicted_revenue_increase = predicted_revenue_increase
        self.predicted_cost_savings = predicted_cost_savings

    def calculate_roi(self, months):
        """
        Calculate the ROI of the AI tool over a specified period.

        Args:
        - months (int): Number of months to calculate ROI for.

        Returns:
        - roi (float): ROI of the AI tool.
        """
        total_revenue_increase = self.predicted_revenue_increase * months
        total_cost_savings = self.predicted_cost_savings * months
        total_cost = self.implementation_cost + (self.monthly_maintenance_cost * months)
        net_benefit = total_revenue_increase + total_cost_savings - total_cost

        if total_cost == 0:
            return np.inf  # Return infinity if total cost is zero

        roi = (net_benefit / total_cost) * 100
        return roi


def compare_roi(predictive_ai_tool, generative_ai_tool, months):
    """
    Compare the ROI of predictive AI tools and generative AI tools.

    Args:
    - predictive_ai_tool (AI_Tool): Predictive AI tool object.
    - generative_ai_tool (AI_Tool): Generative AI tool object.
    - months (int): Number of months to calculate ROI for.

    Returns:
    - predictive_roi (float): ROI of the predictive AI tool.
    - generative_roi (float): ROI of the generative AI tool.
    """
    predictive_roi = predictive_ai_tool.calculate_roi(months)
    generative_roi = generative_ai_tool.calculate_roi(months)

    return predictive_roi, generative_roi


def main():
    try:
        # Define predictive AI tool parameters
        predictive_ai_tool = AI_Tool(
            "Predictive AI",
            implementation_cost=10000,
            monthly_maintenance_cost=2000,
            predicted_revenue_increase=5000,
            predicted_cost_savings=3000
        )

        # Define generative AI tool parameters
        generative_ai_tool = AI_Tool(
            "Generative AI",
            implementation_cost=8000,
            monthly_maintenance_cost=1500,
            predicted_revenue_increase=4000,
            predicted_cost_savings=2000
        )

        # Specify the number of months to calculate ROI for
        months = 12

        # Compare ROI of predictive and generative AI tools
        predictive_roi, generative_roi = compare_roi(predictive_ai_tool, generative_ai_tool, months)

        # Print the results
        print(f"Predictive AI Tool ROI over {months} months: {predictive_roi:.2f}%")
        print(f"Generative AI Tool ROI over {months} months: {generative_roi:.2f}%")

        # Determine which AI tool has a higher ROI
        if predictive_roi > generative_roi:
            print("The predictive AI tool has a higher ROI.")
        elif predictive_roi < generative_roi:
            print("The generative AI tool has a higher ROI.")
        else:
            print("Both AI tools have the same ROI.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
