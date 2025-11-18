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
from typing import List, Tuple

def calculate_average_ath_roi(returns_data: List[Tuple[str, float]], num_projects: int) -> float:
    """
    Calculate the Average All-Time High (ATH) Return on Investment (ROI) for projects.

    :param returns_data: A list of tuples where each tuple contains a project name and its ATH ROI.
                         Example: [("Project A", 3.5), ("Project B", 2.0)]
    :param num_projects: The total number of projects for which the average ATH ROI is to be calculated.
    :return: The average ATH ROI for the given projects.

    :raises ValueError: If num_projects is less than or equal to 0 or if returns_data is empty.
    """

    # Validate inputs
    if num_projects <= 0:
        raise ValueError("Number of projects must be greater than 0.")
    
    if not returns_data:
        raise ValueError("Returns data cannot be empty.")

    total_roi = 0.0

    # Calculate the total ROI from the returns data
    for project, roi in returns_data:
        if roi < 0:
            raise ValueError(f"ROI must be non-negative for project '{project}'. Found: {roi}")
        total_roi += roi

    # Calculate the average ROI
    average_roi = total_roi / num_projects
    return average_roi

# Example usage
if __name__ == "__main__":
    # Sample data: List of projects with their ATH ROI
    sample_returns = [("Project A", 3.5), ("Project B", 2.0), ("Project C", 4.0)]
    project_count = len(sample_returns)

    try:
        average_roi = calculate_average_ath_roi(sample_returns, project_count)
        print(f"The Average ATH ROI for the projects is: {average_roi:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
