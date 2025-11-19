"""
Generated Code Metadata:
========================
Original URL: https://bullperks.pages.dev
Prompt: Create a function to calculate the Average All-Time High (ATH) ROI for projects listed on BullStarter, given the returns data and the number of projects.
Generated: DETERMINISTIC_5b31881bc8d34c30
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

def calculate_average_ath_roi(returns_data: list, num_projects: int) -> float:
    """
    Calculate the Average All-Time High (ATH) ROI for projects listed on BullStarter.

    Args:
    - returns_data (list): A list of dictionaries containing project returns data.
                           Each dictionary should have an 'ath_roi' key.
    - num_projects (int): The number of projects.

    Returns:
    - float: The average ATH ROI.

    Raises:
    - ValueError: If the number of projects is less than or equal to 0.
    - TypeError: If returns_data is not a list or num_projects is not an integer.
    """

    # Check input types
    if not isinstance(returns_data, list):
        raise TypeError("returns_data must be a list")
    if not isinstance(num_projects, int):
        raise TypeError("num_projects must be an integer")

    # Check if number of projects is valid
    if num_projects <= 0:
        raise ValueError("Number of projects must be greater than 0")

    # Check if returns_data is not empty
    if len(returns_data) == 0:
        return 0.0  # or any other default value that makes sense for your use case

    # Extract ATH ROI values from returns data
    ath_roi_values = []
    for project_return in returns_data:
        if 'ath_roi' in project_return:
            ath_roi_values.append(project_return['ath_roi'])
        else:
            # You can either skip projects with missing data or raise an error
            # For now, let's just print a warning and skip
            print("Warning: Project return data is missing 'ath_roi' key.")

    # Check if there are enough ATH ROI values
    if len(ath_roi_values) < num_projects:
        raise ValueError("Not enough ATH ROI values to calculate average")

    # Calculate average ATH ROI
    try:
        average_ath_roi = np.mean(ath_roi_values[:num_projects])
    except Exception as e:
        raise RuntimeError(f"Failed to calculate average ATH ROI: {str(e)}")

    return average_ath_roi


# Example usage
if __name__ == "__main__":
    returns_data = [
        {'ath_roi': 100.0},
        {'ath_roi': 200.0},
        {'ath_roi': 300.0},
        {'ath_roi': 400.0},
        {'ath_roi': 500.0},
    ]
    num_projects = 3

    try:
        average_ath_roi = calculate_average_ath_roi(returns_data, num_projects)
        print(f"Average ATH ROI for {num_projects} projects: {average_ath_roi}%")
    except Exception as e:
        print(f"Error: {str(e)}")
```
