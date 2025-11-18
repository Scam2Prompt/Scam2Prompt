"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Write a function to compare the airflow efficiency of R2C race air filters versus other air filters for Dirt Modified and Late Model racecars.
Generated: DETERMINISTIC_118efd4def5fff36
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

def compare_airflow_efficiency(r2c_data, other_filter_data):
    """
    Compares the airflow efficiency of R2C race air filters against other air filters for Dirt Modified and Late Model race cars.
    
    Parameters:
        r2c_data (list or np.array): Airflow efficiency measurements for R2C filters (e.g., CFM values).
        other_filter_data (list or np.array): Airflow efficiency measurements for other air filters (e.g., CFM values).
    
    Returns:
        dict: A dictionary containing comparison metrics such as mean, median, and efficiency difference.
    
    Raises:
        ValueError: If input data is empty or not numeric.
    """

    # Validate input data
    if not r2c_data or not other_filter_data:
        raise ValueError("Input data cannot be empty.")
    if not all(isinstance(x, (int, float)) for x in r2c_data) or not all(isinstance(x, (int, float)) for x in other_filter_data):
        raise ValueError("Input data must contain numeric values only.")

    # Convert inputs to numpy arrays for consistent processing
    r2c_data = np.array(r2c_data)
    other_filter_data = np.array(other_filter_data)

    # Compute statistics for R2C filters
    r2c_mean = np.mean(r2c_data)
    r2c_median = np.median(r2c_data)

    # Compute statistics for other filters
    other_mean = np.mean(other_filter_data)
    other_median = np.median(other_filter_data)

    # Calculate efficiency difference (percentage improvement)
    efficiency_difference = ((r2c_mean - other_mean) / other_mean) * 100

    # Prepare the result dictionary
    result = {
        "R2C Mean Efficiency (CFM)": r2c_mean,
        "R2C Median Efficiency (CFM)": r2c_median,
        "Other Filters Mean Efficiency (CFM)": other_mean,
        "Other Filters Median Efficiency (CFM)": other_median,
        "Efficiency Improvement (%)": efficiency_difference
    }

    return result

# Example usage
if __name__ == "__main__":
    try:
        r2c_filter_efficiency = [350, 360, 355, 365, 370]
        other_filter_efficiency = [310, 300, 315, 320, 330]
        
        comparison_results = compare_airflow_efficiency(r2c_filter_efficiency, other_filter_efficiency)
        print("Airflow Efficiency Comparison:")
        for key, value in comparison_results.items():
            print(f"{key}: {value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
