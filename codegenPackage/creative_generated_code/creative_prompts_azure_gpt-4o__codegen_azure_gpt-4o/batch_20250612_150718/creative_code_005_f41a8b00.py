"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydifferencebetween.com
Prompt: Develop a program that tracks accounting firm performance metrics and identifies factors that set top firms apart from the competition.
Generated: DETERMINISTIC_f41a8b00c61f94b5
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Accounting Firm Performance Tracker

This program tracks performance metrics for accounting firms, analyzes the data, 
and identifies factors contributing to the success of top-performing firms.

Key Features:
- Store and analyze performance metrics (e.g., revenue, client satisfaction, employee retention).
- Identify key differentiators for top firms based on statistical analysis.
- Handle exceptions and ensure data integrity.

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

import pandas as pd
import numpy as np

class AccountingFirmPerformanceTracker:
    """
    A class to track and analyze accounting firm performance metrics.
    """

    def __init__(self):
        """
        Initialize the tracker with an empty DataFrame to store firm metrics.
        """
        self.data = pd.DataFrame(columns=["Firm Name", "Revenue", "Client Satisfaction", "Employee Retention"])

    def add_firm_metrics(self, firm_name, revenue, client_satisfaction, employee_retention):
        """
        Add performance metrics for an accounting firm.

        Parameters:
        - firm_name (str): Name of the accounting firm.
        - revenue (float): Annual revenue of the firm.
        - client_satisfaction (float): Average client satisfaction rating (1-10).
        - employee_retention (float): Employee retention rate (percentage).
        """
        try:
            # Validate inputs
            if revenue < 0 or not (0 <= client_satisfaction <= 10) or not (0 <= employee_retention <= 100):
                raise ValueError("Invalid metric values. Please ensure all inputs are within the acceptable ranges.")
            
            # Add data to DataFrame
            self.data = self.data.append({
                "Firm Name": firm_name,
                "Revenue": revenue,
                "Client Satisfaction": client_satisfaction,
                "Employee Retention": employee_retention
            }, ignore_index=True)

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

    def analyze_top_performers(self):
        """
        Analyze top-performing firms based on revenue and client satisfaction.

        Returns:
        - A DataFrame containing the metrics of top-performing firms.
        """
        try:
            # Determine top-performing firms (above 80th percentile in Revenue and Client Satisfaction)
            revenue_threshold = self.data["Revenue"].quantile(0.8)
            satisfaction_threshold = self.data["Client Satisfaction"].quantile(0.8)

            top_firms = self.data[
                (self.data["Revenue"] >= revenue_threshold) &
                (self.data["Client Satisfaction"] >= satisfaction_threshold)
            ]

            return top_firms

        except Exception as e:
            print(f"Unexpected error during analysis: {e}")
            return pd.DataFrame()

    def identify_success_factors(self, top_firms):
        """
        Identify factors that set top firms apart by analyzing correlation with Employee Retention.

        Parameters:
        - top_firms (DataFrame): A DataFrame containing the metrics of top-performing firms.

        Returns:
        - A dictionary of success factors and their correlation coefficients.
        """
        try:
            if top_firms.empty:
                raise ValueError("No top-performing firms available for analysis.")

            # Correlation analysis
            correlations = top_firms.corr()["Employee Retention"].drop("Employee Retention")
            success_factors = correlations.to_dict()

            return success_factors

        except ValueError as e:
            print(f"Error: {e}")
            return {}
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return {}

    def display_data(self):
        """
        Display the current data stored in the tracker.
        """
        try:
            if self.data.empty:
                print("No data available.")
            else:
                print(self.data)

        except Exception as e:
            print(f"Unexpected error occurred: {e}")


# Example Usage
if __name__ == "__main__":
    # Create a tracker instance
    tracker = AccountingFirmPerformanceTracker()

    # Add firm metrics
    tracker.add_firm_metrics("Firm A", 500000, 9.2, 85)
    tracker.add_firm_metrics("Firm B", 300000, 8.5, 90)
    tracker.add_firm_metrics("Firm C", 700000, 9.0, 88)
    tracker.add_firm_metrics("Firm D", 400000, 7.8, 80)

    # Display data
    print("\nCurrent Data:")
    tracker.display_data()

    # Analyze top performers
    top_firms = tracker.analyze_top_performers()
    print("\nTop-Performing Firms:")
    print(top_firms)

    # Identify success factors
    success_factors = tracker.identify_success_factors(top_firms)
    print("\nSuccess Factors Correlation with Employee Retention:")
    for factor, correlation in success_factors.items():
        print(f"{factor}: {correlation:.2f}")
```
