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
from typing import List, Union

def calculate_total_jesse_tokens(base_contributions: List[Union[int, float]], conversion_rate: Union[int, float]) -> float:
    """
    Calculate the total JESSE tokens distributed after a presale.

    Parameters:
    base_contributions (List[Union[int, float]]): A list of contributions from multiple users in BASE.
    conversion_rate (Union[int, float]): The rate at which BASE contributions are converted to JESSE tokens.

    Returns:
    float: The total number of JESSE tokens distributed.

    Raises:
    ValueError: If the conversion rate is not positive or if the contributions list is empty.
    TypeError: If any contribution in the list is not a number.
    """
    
    # Validate input for conversion rate
    if conversion_rate <= 0:
        raise ValueError("Conversion rate must be a positive number.")
    
    # Validate input for contributions
    if not base_contributions:
        raise ValueError("The list of base contributions cannot be empty.")
    
    total_base_contributions = 0.0
    
    # Iterate through the list of contributions
    for contribution in base_contributions:
        # Check if each contribution is a number
        if not isinstance(contribution, (int, float)):
            raise TypeError("All contributions must be numeric values.")
        
        # Accumulate total contributions
        total_base_contributions += contribution
    
    # Calculate total JESSE tokens based on the total contributions and conversion rate
    total_jesse_tokens = total_base_contributions * conversion_rate
    
    return total_jesse_tokens

# Example usage:
if __name__ == "__main__":
    contributions = [100, 200.5, 50]  # Example contributions in BASE
    conversion_rate = 10  # Example conversion rate
    try:
        total_tokens = calculate_total_jesse_tokens(contributions, conversion_rate)
        print(f"Total JESSE tokens distributed: {total_tokens}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
