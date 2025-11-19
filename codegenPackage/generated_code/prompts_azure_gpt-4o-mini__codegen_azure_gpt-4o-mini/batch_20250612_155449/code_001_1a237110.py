"""
Generated Code Metadata:
========================
Original URL: https://suistrategies.com
Prompt: Write a function that calculates the percentage allocation of SUI in the investment strategy for each quarter from 2024 to 2026.
Generated: DETERMINISTIC_1a23711000127b24
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

def calculate_sui_allocation(investments: Dict[str, List[float]]) -> Dict[str, float]:
    """
    Calculate the percentage allocation of SUI in the investment strategy for each quarter from 2024 to 2026.

    Parameters:
    investments (Dict[str, List[float]]): A dictionary where keys are quarters in the format 'YYYY-Q' 
                                           (e.g., '2024-1') and values are lists of investment amounts 
                                           for each asset class, including SUI.

    Returns:
    Dict[str, float]: A dictionary with quarters as keys and the percentage allocation of SUI as values.
    
    Raises:
    ValueError: If the input data is not in the expected format or if SUI is not present in the investments.
    """
    
    # Initialize the result dictionary
    sui_allocation = {}

    # Iterate through each quarter in the specified range
    for quarter in investments:
        # Check if the quarter is within the specified range
        if quarter.startswith(('2024-', '2025-', '2026-')):
            try:
                # Extract the investments for the current quarter
                total_investment = sum(investments[quarter])
                sui_investment = investments[quarter][0]  # Assuming SUI is the first element

                # Check for total investment to avoid division by zero
                if total_investment == 0:
                    raise ValueError(f"Total investment for {quarter} is zero, cannot calculate allocation.")

                # Calculate the percentage allocation of SUI
                sui_percentage = (sui_investment / total_investment) * 100
                sui_allocation[quarter] = round(sui_percentage, 2)  # Round to 2 decimal places

            except IndexError:
                raise ValueError(f"SUI investment data is missing for {quarter}.")
            except Exception as e:
                raise ValueError(f"An error occurred while processing {quarter}: {str(e)}")

    return sui_allocation

# Example usage
if __name__ == "__main__":
    investments_data = {
        '2024-1': [5000, 3000, 2000],  # SUI is the first investment
        '2024-2': [6000, 4000, 1000],
        '2024-3': [7000, 2000, 3000],
        '2024-4': [8000, 5000, 2000],
        '2025-1': [9000, 3000, 1000],
        '2025-2': [10000, 4000, 2000],
        '2025-3': [11000, 5000, 3000],
        '2025-4': [12000, 6000, 4000],
        '2026-1': [13000, 7000, 5000],
        '2026-2': [14000, 8000, 6000],
        '2026-3': [15000, 9000, 7000],
        '2026-4': [16000, 10000, 8000],
    }

    try:
        allocation = calculate_sui_allocation(investments_data)
        print("SUI Allocation Percentage by Quarter:")
        for quarter, percentage in allocation.items():
            print(f"{quarter}: {percentage}%")
    except ValueError as e:
        print(f"Error: {e}")
```
