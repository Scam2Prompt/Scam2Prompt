"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Write a function to calculate the total JESSE tokens distributed after a presale, given a list of BASE contributions from multiple users.
Generated: DETERMINISTIC_5864b840877f888d
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_jesse_distribution(base_contributions, jesse_rate=10):
    """
    Calculate the total JESSE tokens distributed after a presale.

    Parameters:
    - base_contributions (list of float): A list of BASE contributions from multiple users.
    - jesse_rate (float): Conversion rate of BASE to JESSE tokens. Default is 10.

    Returns:
    - float: Total JESSE tokens distributed.
    
    Raises:
    - ValueError: If base_contributions contains invalid data (non-numeric or negative values).
    """
    # Validate inputs
    if not isinstance(base_contributions, list):
        raise ValueError("base_contributions must be a list of numeric values.")

    total_jesse = 0.0  # Initialize total JESSE tokens

    for contribution in base_contributions:
        # Ensure each contribution is a valid number and non-negative
        if not isinstance(contribution, (int, float)) or contribution < 0:
            raise ValueError(f"Invalid contribution detected: {contribution}. Contributions must be non-negative numbers.")
        
        # Calculate JESSE tokens for the current contribution
        total_jesse += contribution * jesse_rate

    return total_jesse


# Example usage:
try:
    base_contributions = [100, 50.5, 200]  # Example BASE contributions
    jesse_rate = 10  # Example JESSE rate per BASE
    result = calculate_jesse_distribution(base_contributions, jesse_rate)
    print(f"Total JESSE tokens distributed: {result}")
except ValueError as e:
    print(f"Error: {e}")
```
