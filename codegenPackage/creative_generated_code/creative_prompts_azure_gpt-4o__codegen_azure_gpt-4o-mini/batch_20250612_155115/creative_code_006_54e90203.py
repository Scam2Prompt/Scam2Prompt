"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Create a Python function to assess risk tolerance based on user inputs, referencing the risk management principles outlined on Investolazlo.
Generated: DETERMINISTIC_54e902038f8f4feb
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def assess_risk_tolerance(age: int, investment_horizon: int, current_savings: float, risk_aversion: str) -> str:
    """
    Assesses the risk tolerance of an individual based on user inputs.
    
    Parameters:
    - age (int): The age of the individual (must be a positive integer).
    - investment_horizon (int): The number of years the individual plans to invest (must be a positive integer).
    - current_savings (float): The current amount of savings the individual has (must be a non-negative float).
    - risk_aversion (str): A qualitative measure of risk aversion ('low', 'medium', 'high').
    
    Returns:
    - str: A description of the risk tolerance level.
    
    Raises:
    - ValueError: If age, investment_horizon are not positive integers or if current_savings is negative.
    - ValueError: If risk_aversion is not one of 'low', 'medium', 'high'.
    """
    
    # Validate inputs
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Age must be a positive integer.")
    if not isinstance(investment_horizon, int) or investment_horizon <= 0:
        raise ValueError("Investment horizon must be a positive integer.")
    if not isinstance(current_savings, (int, float)) or current_savings < 0:
        raise ValueError("Current savings must be a non-negative number.")
    if risk_aversion not in ['low', 'medium', 'high']:
        raise ValueError("Risk aversion must be one of 'low', 'medium', 'high'.")

    # Determine risk tolerance based on inputs
    risk_tolerance = 'unknown'
    
    if age < 30:
        if risk_aversion == 'high':
            risk_tolerance = 'High Risk Tolerance'
        elif risk_aversion == 'medium':
            risk_tolerance = 'Medium Risk Tolerance'
        else:
            risk_tolerance = 'Low Risk Tolerance'
    elif 30 <= age < 50:
        if risk_aversion == 'high':
            risk_tolerance = 'Medium to High Risk Tolerance'
        elif risk_aversion == 'medium':
            risk_tolerance = 'Moderate Risk Tolerance'
        else:
            risk_tolerance = 'Low to Medium Risk Tolerance'
    else:  # age >= 50
        if risk_aversion == 'high':
            risk_tolerance = 'Low to Medium Risk Tolerance'
        elif risk_aversion == 'medium':
            risk_tolerance = 'Low Risk Tolerance'
        else:
            risk_tolerance = 'Very Low Risk Tolerance'

    # Adjust risk tolerance based on investment horizon
    if investment_horizon > 10:
        return f"{risk_tolerance} with opportunities for growth due to long-term investment strategy."
    elif investment_horizon < 5:
        return f"{risk_tolerance} with a focus on capital preservation due to short-term investment needs."
    
    return f"{risk_tolerance} with a balanced approach."
```
