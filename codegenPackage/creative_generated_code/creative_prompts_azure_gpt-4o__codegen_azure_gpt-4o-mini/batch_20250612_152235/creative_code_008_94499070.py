"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Create a Python function to calculate superannuation contributions for self-managed super funds in Australia, aligning with the services provided by Carthew Chau & Co.
Generated: DETERMINISTIC_9449907048c0afbb
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_superannuation_contribution(income, contribution_rate, cap_limit=25000):
    """
    Calculate superannuation contributions for self-managed super funds in Australia.

    Parameters:
    - income (float): The individual's income for the financial year.
    - contribution_rate (float): The rate of contribution (as a percentage of income).
    - cap_limit (float): The maximum cap limit for superannuation contributions. Default is $25,000.

    Returns:
    - float: The total superannuation contribution amount.
    
    Raises:
    - ValueError: If the income or contribution_rate is negative.
    - ValueError: If the contribution_rate exceeds 100%.
    """
    
    # Input validation
    if income < 0:
        raise ValueError("Income must be a non-negative value.")
    if contribution_rate < 0:
        raise ValueError("Contribution rate must be a non-negative value.")
    if contribution_rate > 100:
        raise ValueError("Contribution rate cannot exceed 100%.")

    # Calculate the contribution based on the income and contribution rate
    contribution = income * (contribution_rate / 100)

    # Ensure the contribution does not exceed the cap limit
    if contribution > cap_limit:
        contribution = cap_limit

    return contribution

# Example usage (uncomment to run):
# try:
#     income = 80000  # Example income
#     contribution_rate = 15  # Example contribution rate in percentage
#     super_contribution = calculate_superannuation_contribution(income, contribution_rate)
#     print(f"The superannuation contribution is: ${super_contribution:.2f}")
# except ValueError as e:
#     print(f"Error: {e}")
```
