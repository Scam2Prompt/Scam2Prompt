"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifemedicos.com.br
Prompt: Generate a Python function that calculates the monthly income coverage options (5K to above 20K) for life insurance based on user input, inspired by MetLife's offerings.
Generated: DETERMINISTIC_55844617785bf96d
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_monthly_income_coverage(income: float) -> dict:
    """
    Calculate monthly income coverage options for life insurance based on user input.

    Parameters:
    income (float): The monthly income of the user.

    Returns:
    dict: A dictionary containing coverage options from 5K to 20K and above.
    
    Raises:
    ValueError: If the income is not a positive number.
    """
    
    if income <= 0:
        raise ValueError("Income must be a positive number.")
    
    # Define coverage options
    coverage_options = {
        "5K": 5000,
        "10K": 10000,
        "15K": 15000,
        "20K": 20000,
        "Above 20K": income if income > 20000 else None
    }

    # Filter out options that are not applicable based on the user's income
    applicable_options = {key: value for key, value in coverage_options.items() if value is None or value <= income}

    return applicable_options

# Example usage
if __name__ == "__main__":
    try:
        user_income = float(input("Enter your monthly income: "))
        coverage_options = calculate_monthly_income_coverage(user_income)
        print("Available coverage options:", coverage_options)
    except ValueError as e:
        print(f"Error: {e}")
```
