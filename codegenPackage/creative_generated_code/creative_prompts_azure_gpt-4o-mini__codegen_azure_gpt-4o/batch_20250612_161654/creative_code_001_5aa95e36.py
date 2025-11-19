"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theaflac.com
Prompt: Write a Python function that calculates the estimated premium for Aflac's Life Insurance based on user inputs such as age and coverage amount.
Generated: DETERMINISTIC_5aa95e362bd38768
Batch ID: 20250612_161654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_premium(age: int, coverage_amount: Union[int, float]) -> Union[float, None]:
    """
    Calculate the estimated premium for Aflac's Life Insurance.
    
    Parameters:
        age (int): The age of the individual (must be between 18 and 100).
        coverage_amount (Union[int, float]): Desired coverage amount in USD (must be positive).
    
    Returns:
        Union[float, None]: The calculated premium in USD or None if inputs are invalid.
    """
    try:
        # Validate inputs
        if not (18 <= age <= 100):
            raise ValueError("Age must be between 18 and 100.")
        if coverage_amount <= 0:
            raise ValueError("Coverage amount must be greater than 0.")
        
        # Base rate per $1000 of coverage
        base_rate = 0.05  # Example value, adjust based on business rules
        
        # Age surcharge multiplier
        if age < 30:
            age_multiplier = 1.2  # Younger individuals are charged slightly more
        elif 30 <= age <= 50:
            age_multiplier = 1.0  # Base multiplier for middle-aged individuals
        else:
            age_multiplier = 1.5  # Older individuals are charged higher
        
        # Calculate premium
        premium = (coverage_amount / 1000) * base_rate * age_multiplier
        
        return round(premium, 2)  # Return premium rounded to 2 decimal places
    
    except ValueError as e:
        print(f"Input Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage of the function
if __name__ == "__main__":
    user_age = 35
    user_coverage = 50000  # $50,000
    estimated_premium = calculate_premium(user_age, user_coverage)
    
    if estimated_premium is not None:
        print(f"Estimated Premium: ${estimated_premium}")
    else:
        print("Failed to calculate the premium. Please check your inputs.")
```
