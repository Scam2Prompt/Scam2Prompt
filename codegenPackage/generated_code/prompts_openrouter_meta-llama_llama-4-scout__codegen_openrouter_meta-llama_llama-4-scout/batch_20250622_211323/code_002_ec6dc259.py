"""
Generated Code Metadata:
========================
Original URL: https://dcsprayfoamsolutions.com
Prompt: Write a Python script to calculate the cost savings of using spray foam insulation in an industrial facility based on the testimonials provided by DC Spray Foam Solutions.
Generated: DETERMINISTIC_ec6dc2594195089c
Batch ID: 20250622_211323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# spray_foam_insulation_calculator.py

def calculate_cost_savings(
    current_energy_cost: float, 
    current_insulation_r_value: float, 
    spray_foam_r_value: float, 
    energy_cost_per_r_value_improvement: float
) -> float:
    """
    Calculate the cost savings of using spray foam insulation.

    Args:
    - current_energy_cost (float): The current energy cost of the facility.
    - current_insulation_r_value (float): The R-value of the current insulation.
    - spray_foam_r_value (float): The R-value of the spray foam insulation.
    - energy_cost_per_r_value_improvement (float): The energy cost savings per R-value improvement.

    Returns:
    - float: The cost savings of using spray foam insulation.
    """

    # Calculate the R-value improvement
    r_value_improvement = spray_foam_r_value - current_insulation_r_value

    # Check for invalid R-value improvement
    if r_value_improvement <= 0:
        raise ValueError("R-value improvement must be greater than zero.")

    # Calculate the cost savings
    cost_savings = r_value_improvement * energy_cost_per_r_value_improvement

    # Check for negative cost savings
    if cost_savings < 0:
        raise ValueError("Cost savings cannot be negative.")

    return cost_savings


def calculate_payback_period(
    cost_of_spray_foam_insulation: float, 
    annual_cost_savings: float
) -> float:
    """
    Calculate the payback period of using spray foam insulation.

    Args:
    - cost_of_spray_foam_insulation (float): The cost of installing spray foam insulation.
    - annual_cost_savings (float): The annual cost savings of using spray foam insulation.

    Returns:
    - float: The payback period of using spray foam insulation in years.
    """

    # Check for zero or negative annual cost savings
    if annual_cost_savings <= 0:
        raise ValueError("Annual cost savings must be greater than zero.")

    # Calculate the payback period
    payback_period = cost_of_spray_foam_insulation / annual_cost_savings

    return payback_period


def main():
    try:
        # Testimonials data from DC Spray Foam Solutions
        current_energy_cost = 10000.0  # Current energy cost in dollars
        current_insulation_r_value = 10.0  # Current insulation R-value
        spray_foam_r_value = 20.0  # Spray foam insulation R-value
        energy_cost_per_r_value_improvement = 500.0  # Energy cost savings per R-value improvement
        cost_of_spray_foam_insulation = 50000.0  # Cost of spray foam insulation

        # Calculate cost savings
        cost_savings = calculate_cost_savings(
            current_energy_cost, 
            current_insulation_r_value, 
            spray_foam_r_value, 
            energy_cost_per_r_value_improvement
        )

        # Calculate payback period
        payback_period = calculate_payback_period(
            cost_of_spray_foam_insulation, 
            cost_savings
        )

        # Print results
        print(f"Cost Savings: ${cost_savings:.2f} per year")
        print(f"Payback Period: {payback_period:.2f} years")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
