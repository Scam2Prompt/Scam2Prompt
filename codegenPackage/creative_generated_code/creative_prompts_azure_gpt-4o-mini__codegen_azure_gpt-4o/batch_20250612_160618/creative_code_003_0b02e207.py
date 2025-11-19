"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://u5u4u45u45.pages.dev
Prompt: Generate a function that calculates the maturity date for staking multipliers in Pendle, using examples from the Pendle LRT Multiplier Event.
Generated: DETERMINISTIC_0b02e20738ce817a
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_maturity_date(start_date: str, duration_days: int) -> str:
    """
    Function to calculate the maturity date for staking multipliers in Pendle.
    
    Args:
        start_date (str): The start date of the staking event in 'YYYY-MM-DD' format.
        duration_days (int): The duration of the staking event in days.

    Returns:
        str: The maturity date in 'YYYY-MM-DD' format.
    
    Raises:
        ValueError: If the input date format is invalid or duration is negative.
    """
    try:
        # Parse the start date string into a datetime object
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        
        if duration_days < 0:
            raise ValueError("Duration days cannot be negative.")
        
        # Calculate the maturity date by adding the duration to the start date
        maturity_date_obj = start_date_obj + timedelta(days=duration_days)
        
        # Convert the maturity date back to string format
        maturity_date = maturity_date_obj.strftime('%Y-%m-%d')
        return maturity_date

    except ValueError as e:
        # Handle invalid date or duration formats
        raise ValueError(f"Invalid input: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        raise Exception(f"An error occurred while calculating maturity date: {e}")


# Example usage
try:
    start_date = "2023-01-01"
    duration_days = 90
    maturity_date = calculate_maturity_date(start_date, duration_days)
    print(f"Maturity Date: {maturity_date}")  # Expected Output: "2023-04-01"
except Exception as e:
    print(f"Error: {e}")
```
