"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terawit.net
Prompt: Write a code snippet that analyzes employee training effectiveness using Returns on Training Investment (ROTI) metrics.
Generated: DETERMINISTIC_5e4be988d939e3a2
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd

def calculate_roti(training_cost, performance_improvement, monetary_gain):
    """
    Calculate Returns on Training Investment (ROTI).
    
    Parameters:
        training_cost (float): Cost of the training program
        performance_improvement (float): Percentage improvement in employee performance
        monetary_gain (float): Monetary gain attributed to the training
        
    Returns:
        float: ROTI metric
    """
    try:
        # Ensure inputs are valid
        if training_cost <= 0:
            raise ValueError("Training cost must be a positive value.")
        if performance_improvement < 0:
            raise ValueError("Performance improvement cannot be negative.")
        if monetary_gain < 0:
            raise ValueError("Monetary gain cannot be negative.")
        
        # Calculate ROTI as (Monetary Gain - Training Cost) / Training Cost
        roti = (monetary_gain - training_cost) / training_cost
        return roti
    except Exception as e:
        # Handle errors and return appropriate message
        print(f"Error calculating ROTI: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Sample employee training data
    employee_training_data = [
        {"employee_id": 1, "training_cost": 1000, "performance_improvement": 20, "monetary_gain": 3000},
        {"employee_id": 2, "training_cost": 1500, "performance_improvement": 25, "monetary_gain": 4000},
        {"employee_id": 3, "training_cost": 1200, "performance_improvement": 15, "monetary_gain": 2500},
    ]
    
    # Convert data into a pandas DataFrame for easier analysis
    training_df = pd.DataFrame(employee_training_data)
    
    # Calculate ROTI for each employee and add it to the DataFrame
    training_df['roti'] = training_df.apply(
        lambda row: calculate_roti(row['training_cost'], row['performance_improvement'], row['monetary_gain']), axis=1
    )
    
    # Display the results
    print("Employee Training Effectiveness Analysis (ROTI Metrics):")
    print(training_df)
```
