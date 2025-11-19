"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: "Write a Python script to analyze the effectiveness of digital marketing campaigns in Jordan, including metrics such as customer satisfaction rate, project completion rate, and sales increase percentage."
Generated: DETERMINISTIC_08e2907e1dd387f6
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

# Define a function to calculate customer satisfaction rate
def calculate_customer_satisfaction(data):
    """
    Calculate the customer satisfaction rate based on survey responses.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing customer satisfaction survey results.
        
    Returns:
        float: Customer satisfaction rate as a percentage.
    """
    try:
        satisfied_customers = data['satisfaction_score'].apply(lambda x: x >= 4).sum()
        total_customers = len(data)
        satisfaction_rate = (satisfied_customers / total_customers) * 100
        return round(satisfaction_rate, 2)
    except KeyError:
        raise ValueError("Data must contain a 'satisfaction_score' column.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating satisfaction rate: {e}")

# Define a function to calculate project completion rate
def calculate_project_completion(data):
    """
    Calculate the project completion rate based on campaign data.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing project completion information.
        
    Returns:
        float: Project completion rate as a percentage.
    """
    try:
        completed_projects = data['project_status'].apply(lambda x: x == 'Completed').sum()
        total_projects = len(data)
        completion_rate = (completed_projects / total_projects) * 100
        return round(completion_rate, 2)
    except KeyError:
        raise ValueError("Data must contain a 'project_status' column.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating project completion rate: {e}")

# Define a function to calculate sales increase percentage
def calculate_sales_increase(data):
    """
    Calculate the sales increase percentage based on campaign data.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing sales data before and after campaigns.
        
    Returns:
        float: Sales increase percentage.
    """
    try:
        if 'sales_before' not in data.columns or 'sales_after' not in data.columns:
            raise ValueError("Data must contain 'sales_before' and 'sales_after' columns.")
        
        total_sales_before = data['sales_before'].sum()
        total_sales_after = data['sales_after'].sum()
        
        if total_sales_before == 0:
            raise ValueError("Total sales before the campaign cannot be zero.")
        
        sales_increase = ((total_sales_after - total_sales_before) / total_sales_before) * 100
        return round(sales_increase, 2)
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating sales increase percentage: {e}")

# Main function to analyze digital marketing campaigns
def analyze_campaigns(data):
    """
    Analyze the effectiveness of digital marketing campaigns in Jordan.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing campaign data.
        
    Returns:
        dict: Dictionary containing calculated metrics.
    """
    try:
        metrics = {
            "Customer Satisfaction Rate (%)": calculate_customer_satisfaction(data),
            "Project Completion Rate (%)": calculate_project_completion(data),
            "Sales Increase Percentage (%)": calculate_sales_increase(data)
        }
        return metrics
    except Exception as e:
        raise RuntimeError(f"An error occurred during campaign analysis: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration purposes
    sample_data = pd.DataFrame({
        'satisfaction_score': [5, 4, 3, 5, 4, 2, 1, 5],
        'project_status': ['Completed', 'Completed', 'In Progress', 'Completed', 'Completed', 'In Progress', 'Completed', 'Completed'],
        'sales_before': [100, 200, 150, 300, 250, 400, 350, 500],
        'sales_after': [150, 250, 200, 350, 300, 450, 400, 550]
    })
    
    try:
        results = analyze_campaigns(sample_data)
        print("Campaign Analysis Results:")
        for metric, value in results.items():
            print(f"{metric}: {value}")
    except Exception as e:
        print(f"Error: {e}")
```
