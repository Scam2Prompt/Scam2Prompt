"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Write a code snippet for calculating the APR for different staking durations using the aixCB Staking data.
Generated: DETERMINISTIC_3b330dd7fc2d0286
Batch ID: 20250612_155846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to calculate the APR for different staking durations using aixCB Staking data

# Define a function to calculate APR based on staking duration
def calculate_apr(base_apr, staking_duration_days):
    """
    Calculate the APR for a given staking duration.
    
    Parameters:
        base_apr (float): The base APR for staking (percentage).
        staking_duration_days (int): The staking duration in days.
    
    Returns:
        float: Adjusted APR based on staking duration.
    """
    try:
        # Validate inputs
        if base_apr < 0:
            raise ValueError("Base APR cannot be negative.")
        if staking_duration_days <= 0:
            raise ValueError("Staking duration must be greater than zero.")
        
        # Define APR adjustment rules (example rules, can be customized)
        adjustment_factor = 1.0  # Default adjustment factor
        if staking_duration_days < 30:
            adjustment_factor = 0.9  # 10% reduction for less than 30 days
        elif staking_duration_days < 90:
            adjustment_factor = 1.0  # No adjustment for 30-89 days
        elif staking_duration_days < 180:
            adjustment_factor = 1.1  # 10% increase for 90-179 days
        else:
            adjustment_factor = 1.2  # 20% increase for 180+ days
        
        # Calculate adjusted APR
        adjusted_apr = base_apr * adjustment_factor
        return round(adjusted_apr, 2)  # Round to 2 decimal places for clarity
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle unforeseen errors
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Base APR in percentage (example value)
    base_apr = 12.5  # Base staking APR
    
    # Sample staking durations (in days)
    staking_durations = [15, 45, 120, 200]
    
    print("Calculating APR for different staking durations:")
    for duration in staking_durations:
        apr = calculate_apr(base_apr, duration)
        if apr is not None:
            print(f"Staking Duration: {duration} days, Adjusted APR: {apr}%")
```
