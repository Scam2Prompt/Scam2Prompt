"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Write a function to calculate success metrics (e.g., cases solved, years of operation) for a legal firm like Ramdays, using their provided data structure.
Generated: DETERMINISTIC_9b0f805952d9ec39
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

def calculate_success_metrics(data: Dict[str, any]) -> Dict[str, any]:
    """
    Function to calculate success metrics for a legal firm based on provided data.

    Args:
        data (dict): A dictionary containing the firm's data. 
                     Expected fields:
                     - "cases": List of cases. Each case is a dictionary with "status" (str) and "resolved_date" (str, optional).
                     - "founding_date": The firm's founding date in "YYYY-MM-DD" format (str).

    Returns:
        dict: A dictionary containing calculated success metrics:
              - "cases_solved": Total number of cases solved.
              - "years_of_operation": Total years of operation since founding date.
    """
    try:
        # Validate input data
        if "cases" not in data or "founding_date" not in data:
            raise ValueError("Invalid input data: 'cases' and 'founding_date' are required fields.")

        # Extract cases and founding date
        cases = data["cases"]
        founding_date = data["founding_date"]

        # Calculate cases solved
        cases_solved = sum(1 for case in cases if case.get("status") == "solved")

        # Calculate years of operation
        founding_date_obj = datetime.datetime.strptime(founding_date, "%Y-%m-%d")
        current_date = datetime.datetime.now()
        years_of_operation = (current_date - founding_date_obj).days // 365

        # Return calculated metrics
        return {
            "cases_solved": cases_solved,
            "years_of_operation": years_of_operation
        }

    except ValueError as ve:
        # Handle value errors (e.g., invalid input data)
        print(f"Error: {ve}")
        return {"error": str(ve)}

    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred."}


# Example usage:
if __name__ == "__main__":
    # Sample data structure
    legal_firm_data = {
        "cases": [
            {"status": "solved", "resolved_date": "2022-05-10"},
            {"status": "pending"},
            {"status": "solved", "resolved_date": "2021-08-15"},
            {"status": "in-progress"},
        ],
        "founding_date": "2010-04-01"
    }

    # Calculate metrics
    metrics = calculate_success_metrics(legal_firm_data)
    print(metrics)
```
