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

class AIAssessment:
    """
    This class is used for comparing ROI between predictive AI tools and generative AI tools 
    for a small business following the steps outlined by ETHX-AI Consulting.
    """
    def __init__(self):
        self.results = {}

    def calculate_roi(self, revenue_increase, cost_reduction, implementation_cost):
        """
        Calculate ROI using the formula:
        ROI (%) = ((Revenue Increase + Cost Reduction - Implementation Cost) / Implementation Cost) * 100
        
        Params:
        - revenue_increase (float): Estimated revenue increase ($) from the AI tool
        - cost_reduction (float): Estimated cost savings ($) from the AI tool
        - implementation_cost (float): Cost of implementing the AI tool ($)
        
        Returns:
        - roi (float): ROI percentage
        """
        try:
            if implementation_cost <= 0:
                raise ValueError("Implementation cost must be greater than zero.")
            return ((revenue_increase + cost_reduction - implementation_cost) / implementation_cost) * 100
        except Exception as e:
            print(f"Error calculating ROI: {e}")
            return None

    def run_assessment(self):
        """
        Run the ROI comparison assessment for predictive AI tools vs generative AI tools.

        Steps outlined by ETHX-AI Consulting:
        1. Gather data: Input revenue increase, cost reduction, and implementation cost for each tool.
        2. Calculate ROI for both tools.
        3. Compare results and determine which AI tool is more beneficial for the business.
        """
        print("\nStarting ROI assessment for Predictive AI Tools...")
        predictive_revenue = float(input("Enter revenue increase ($) from Predictive AI tools: "))
        predictive_cost_reduction = float(input("Enter cost reduction ($) from Predictive AI tools: "))
        predictive_cost = float(input("Enter implementation cost ($) for Predictive AI tools: "))
        predictive_roi = self.calculate_roi(predictive_revenue, predictive_cost_reduction, predictive_cost)
        self.results['Predictive AI'] = predictive_roi
        
        print("\nStarting ROI assessment for Generative AI Tools...")
        generative_revenue = float(input("Enter revenue increase ($) from Generative AI tools: "))
        generative_cost_reduction = float(input("Enter cost reduction ($) from Generative AI tools: "))
        generative_cost = float(input("Enter implementation cost ($) for Generative AI tools: "))
        generative_roi = self.calculate_roi(generative_revenue, generative_cost_reduction, generative_cost)
        self.results['Generative AI'] = generative_roi

        self.compare_results()

    def compare_results(self):
        """
        Compare the ROI results between Predictive AI and Generative AI tools.
        """
        print("\nROI Comparison Results:")
        for tool, roi in self.results.items():
            if roi is not None:
                print(f"{tool} ROI: {roi:.2f}%")
            else:
                print(f"{tool} ROI: Calculation failed.")

        if None not in self.results.values():
            # Determine the more beneficial tool
            winner = max(self.results, key=self.results.get)
            print(f"\nThe AI tool with the higher ROI is: {winner}")
        else:
            print("\nUnable to determine the better AI tool due to calculation errors.")

# Entry point for the script
if __name__ == "__main__":
    print("Welcome to the AI ROI Assessment Tool!")
    assessment = AIAssessment()
    assessment.run_assessment()
```
