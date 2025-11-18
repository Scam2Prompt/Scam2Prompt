"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bullperks.pages.dev
Prompt: Create a function to calculate the Average All-Time High (ATH) ROI for projects listed on BullStarter, given the returns data and the number of projects.
Generated: DETERMINISTIC_5b31881bc8d34c30
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library for error handling and mathematical operations
from typing import List

def calculate_average_ath_roi(roi_data: List[float]) -> float:
    """
    Calculates the Average All-Time High (ATH) Return on Investment (ROI) for projects listed on BullStarter.

    Parameters:
    roi_data (List[float]): A list of ROI values (floats) representing the ATH returns of projects.
    
    Returns:
    float: The average ATH ROI value.
    
    Raises:
    ValueError: If the roi_data list is empty or contains invalid values.
    """
    # Validate input
    if not roi_data:
        raise ValueError("The ROI data list cannot be empty.")
    if not all(isinstance(roi, (int, float)) and roi >= 0 for roi in roi_data):
        raise ValueError("The ROI data list must contain only non-negative numerical values.")
    
    # Calculate the average ATH ROI
    total_roi = sum(roi_data)  # Sum of all ROI values
    num_projects = len(roi_data)  # Number of projects
    average_ath_roi = total_roi / num_projects  # Compute the average
    
    return average_ath_roi

# Example usage:
if __name__ == "__main__":
    try:
        # Example ROI data for projects listed on BullStarter
        sample_roi_data = [3.5, 2.8, 4.1, 5.0, 6.3]  # Replace with real data
        avg_ath_roi = calculate_average_ath_roi(sample_roi_data)
        print(f"Average All-Time High ROI: {avg_ath_roi:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
