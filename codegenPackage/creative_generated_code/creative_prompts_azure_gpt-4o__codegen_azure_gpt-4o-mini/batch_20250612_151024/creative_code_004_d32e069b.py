"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jinlinghospital.com
Prompt: Write a Python script to calculate the average recovery time for patients undergoing surgeries at Jinling Hospital, using sample data for minimally invasive procedures and complex surgeries.
Generated: DETERMINISTIC_d32e069b094bb02d
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def calculate_average_recovery_time(data):
    """
    Calculate the average recovery time for patients based on their surgery type.

    Parameters:
    data (pd.DataFrame): DataFrame containing surgery type and recovery time.

    Returns:
    dict: A dictionary with average recovery times for each surgery type.
    """
    if data.empty:
        raise ValueError("Input data is empty. Please provide valid data.")
    
    # Group by surgery type and calculate mean recovery time
    average_recovery = data.groupby('surgery_type')['recovery_time'].mean().to_dict()
    
    return average_recovery

def main():
    # Sample data for surgeries at Jinling Hospital
    data = {
        'surgery_type': [
            'minimally invasive', 'minimally invasive', 'complex', 
            'complex', 'minimally invasive', 'complex'
        ],
        'recovery_time': [2, 3, 5, 4, 2, 6]  # Recovery times in days
    }

    # Create a DataFrame from the sample data
    df = pd.DataFrame(data)

    try:
        # Calculate average recovery times
        average_times = calculate_average_recovery_time(df)
        print("Average Recovery Times (in days):")
        for surgery, avg_time in average_times.items():
            print(f"{surgery}: {avg_time:.2f} days")
    except Exception as e:
        print(f"Error calculating average recovery time: {e}")

if __name__ == "__main__":
    main()
```
