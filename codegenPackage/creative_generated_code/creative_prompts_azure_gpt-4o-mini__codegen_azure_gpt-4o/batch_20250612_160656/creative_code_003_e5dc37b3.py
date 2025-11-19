"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Develop a library function that calculates the net worth of aerospace companies based on their infrastructure and experience, inspired by Aanjaneya Aerodynamics' business model.
Generated: DETERMINISTIC_e5dc37b36dfa0ea0
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A library function to calculate the net worth of aerospace companies based on their infrastructure and experience.
The net worth calculation uses a weighted formula inspired by Aanjaneya Aerodynamics' business model.
"""

# Import necessary libraries
from typing import Dict

def calculate_net_worth(infrastructure: Dict[str, float], experience_years: int) -> float:
    """
    Calculate the net worth of an aerospace company based on its infrastructure and experience.

    Parameters:
        infrastructure (dict): A dictionary where the keys are categories of infrastructure
                               ('manufacturing', 'research', 'testing', etc.) and the values are their respective monetary values.
        experience_years (int): The number of years the company has been in operation.

    Returns:
        float: The calculated net worth of the company.

    Raises:
        ValueError: If experience_years is negative or infrastructure contains non-positive values.
    """
    # Validate input
    if experience_years < 0:
        raise ValueError("Experience years cannot be negative.")

    if not all(value > 0 for value in infrastructure.values()):
        raise ValueError("Infrastructure values must be positive.")

    # Constants for weight calculations
    EXPERIENCE_WEIGHT = 1.5  # Weighting factor for experience years
    INFRASTRUCTURE_WEIGHT = 2.0  # Weighting factor for infrastructure

    # Calculate the total infrastructure value
    total_infrastructure_value = sum(infrastructure.values())

    # Calculate weighted contributions
    experience_contribution = EXPERIENCE_WEIGHT * experience_years
    infrastructure_contribution = INFRASTRUCTURE_WEIGHT * total_infrastructure_value

    # Calculate net worth
    net_worth = experience_contribution + infrastructure_contribution

    return net_worth

# Example usage:
if __name__ == "__main__":
    # Example infrastructure data
    company_infrastructure = {
        'manufacturing': 5000000,  # Manufacturing facilities worth $5 million
        'research': 3000000,       # Research facilities worth $3 million
        'testing': 2000000         # Testing facilities worth $2 million
    }
    company_experience_years = 10  # 10 years of experience

    try:
        # Calculate the net worth
        net_worth = calculate_net_worth(company_infrastructure, company_experience_years)
        print(f"The company's net worth is: ${net_worth:.2f}")
    except ValueError as e:
        print(f"Error calculating net worth: {e}")
```
