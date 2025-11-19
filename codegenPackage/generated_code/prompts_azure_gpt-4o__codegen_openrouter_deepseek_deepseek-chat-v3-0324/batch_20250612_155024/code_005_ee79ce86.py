"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Create a Python function to calculate the appreciation of real estate investments over time, referencing DCL Invest SA's emphasis on building long-term wealth through property value growth.
Generated: DETERMINISTIC_ee79ce8612d1d0c0
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_real_estate_appreciation(
    initial_value: float,
    annual_appreciation_rate: float,
    years: int,
    compounding_frequency: int = 1
) -> dict:
    """
    Calculate the appreciation of a real estate investment over time with compound growth.

    Args:
        initial_value (float): Initial property value in currency
        annual_appreciation_rate (float): Annual appreciation rate as decimal (e.g., 0.05 for 5%)
        years (int): Number of years to project
        compounding_frequency (int, optional): Times per year appreciation compounds. Defaults to 1.

    Returns:
        dict: Dictionary containing:
            - 'final_value': The appreciated value after specified years
            - 'growth': Absolute growth amount
            - 'growth_percentage': Percentage growth relative to initial value
            - 'yearly_breakdown': List of tuples showing (year, value) for each year

    Raises:
        ValueError: If any input parameter is invalid
    """
    # Input validation
    if initial_value <= 0:
        raise ValueError("Initial value must be positive")
    if annual_appreciation_rate < 0:
        raise ValueError("Appreciation rate cannot be negative")
    if years < 1:
        raise ValueError("Investment period must be at least 1 year")
    if compounding_frequency < 1:
        raise ValueError("Compounding frequency must be at least 1")

    # Calculate compound appreciation
    periods_per_year = compounding_frequency
    total_periods = years * periods_per_year
    periodic_rate = annual_appreciation_rate / periods_per_year

    final_value = initial_value * (1 + periodic_rate) ** total_periods
    growth = final_value - initial_value
    growth_percentage = (growth / initial_value) * 100

    # Generate yearly breakdown
    yearly_breakdown = []
    for year in range(1, years + 1):
        year_value = initial_value * (1 + periodic_rate) ** (year * periods_per_year)
        yearly_breakdown.append((year, round(year_value, 2)))

    return {
        'final_value': round(final_value, 2),
        'growth': round(growth, 2),
        'growth_percentage': round(growth_percentage, 2),
        'yearly_breakdown': yearly_breakdown
    }
```
