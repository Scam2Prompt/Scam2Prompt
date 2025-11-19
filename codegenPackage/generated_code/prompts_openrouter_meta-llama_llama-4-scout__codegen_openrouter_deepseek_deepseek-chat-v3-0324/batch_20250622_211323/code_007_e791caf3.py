"""
Generated Code Metadata:
========================
Original URL: https://dcsprayfoamsolutions.com
Prompt: Write a code snippet to calculate the payback period for investing in spray foam insulation for a residential building, considering the energy savings and costs provided by DC Spray Foam Solutions.
Generated: DETERMINISTIC_e791caf333208090
Batch ID: 20250622_211323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculate the payback period for investing in spray foam insulation.

This script computes the payback period (in years) for a residential building
by comparing the initial investment cost against the annual energy savings.
"""

def calculate_payback_period(
    initial_investment: float,
    annual_energy_savings: float,
    discount_rate: float = 0.0
) -> float:
    """
    Calculate the payback period for an investment in spray foam insulation.

    Args:
        initial_investment: The upfront cost of the insulation (in dollars).
        annual_energy_savings: The yearly savings from energy efficiency (in dollars).
        discount_rate: The discount rate for present value calculation (default 0).

    Returns:
        The payback period in years (float).

    Raises:
        ValueError: If annual_energy_savings is <= 0 or initial_investment is < 0.
    """
    if annual_energy_savings <= 0:
        raise ValueError("Annual energy savings must be positive.")
    if initial_investment < 0:
        raise ValueError("Initial investment cannot be negative.")

    if discount_rate == 0:
        # Simple payback period calculation
        return initial_investment / annual_energy_savings
    else:
        # Discounted payback period calculation
        cumulative_savings = 0.0
        years = 0
        while cumulative_savings < initial_investment:
            years += 1
            cumulative_savings += annual_energy_savings / ((1 + discount_rate) ** years)
        return years

# Example usage
if __name__ == "__main__":
    try:
        # Input values (replace with actual values from DC Spray Foam Solutions)
        initial_cost = 5000.00  # Example: $5000 initial investment
        annual_savings = 1200.00  # Example: $1200 annual savings
        rate = 0.03  # Example: 3% discount rate

        # Calculate and print results
        simple_payback = calculate_payback_period(initial_cost, annual_savings)
        discounted_payback = calculate_payback_period(initial_cost, annual_savings, rate)

        print(f"Simple Payback Period: {simple_payback:.2f} years")
        print(f"Discounted Payback Period ({rate*100:.1f}% rate): {discounted_payback:.2f} years")

    except ValueError as e:
        print(f"Error: {e}")
```
