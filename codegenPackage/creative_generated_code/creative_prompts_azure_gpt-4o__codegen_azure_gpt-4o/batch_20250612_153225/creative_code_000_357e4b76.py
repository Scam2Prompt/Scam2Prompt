"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltec-solutions.de
Prompt: Write Python code to calculate the potential cost savings from installing solar panels, incorporating financing options and government subsidies as described by Soltec Solutions.
Generated: DETERMINISTIC_357e4b76a30eaf81
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_solar_savings(
    monthly_energy_cost,
    energy_cost_increase_rate,
    system_cost,
    government_subsidy,
    loan_interest_rate,
    loan_term_years,
    solar_energy_offset
):
    """
    Calculate potential cost savings from installing solar panels.

    Parameters:
    - monthly_energy_cost (float): Current monthly energy cost in USD.
    - energy_cost_increase_rate (float): Annual percentage increase in energy costs (e.g., 0.03 for 3%).
    - system_cost (float): Total cost of the solar panel system in USD.
    - government_subsidy (float): Government subsidy in USD.
    - loan_interest_rate (float): Annual interest rate for financing in decimal form (e.g., 0.05 for 5%).
    - loan_term_years (int): Loan term in years.
    - solar_energy_offset (float): Percentage of energy costs offset by solar panels (e.g., 0.8 for 80%).

    Returns:
    - dict: A dictionary containing the total cost savings and details of the calculation.
    """
    try:
        # Apply government subsidy to system cost
        net_system_cost = system_cost - government_subsidy

        # Calculate monthly loan payment using the formula for amortized loans
        # M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
        r = loan_interest_rate / 12  # Monthly interest rate
        n = loan_term_years * 12  # Total number of payments
        monthly_payment = net_system_cost * (r * math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)

        # Calculate annual energy cost savings
        annual_energy_cost = monthly_energy_cost * 12
        annual_savings = annual_energy_cost * solar_energy_offset

        # Calculate energy cost savings over the loan term
        total_savings = 0
        for year in range(loan_term_years):
            # Account for annual energy cost increase
            annual_energy_cost *= (1 + energy_cost_increase_rate)
            total_savings += annual_energy_cost * solar_energy_offset

        # Total payments for financing
        total_financing_cost = monthly_payment * n

        # Net savings after financing
        net_savings = total_savings - total_financing_cost

        # Return detailed breakdown
        return {
            "System Cost (After Subsidy)": net_system_cost,
            "Monthly Loan Payment": monthly_payment,
            "Total Financing Cost": total_financing_cost,
            "Total Energy Cost Savings": total_savings,
            "Net Savings": net_savings
        }
    except Exception as e:
        return {"error": str(e)}


# Example usage:
if __name__ == "__main__":
    # Input values
    monthly_energy_cost = 150.0  # USD
    energy_cost_increase_rate = 0.03  # 3%
    system_cost = 20000.0  # USD
    government_subsidy = 5000.0  # USD
    loan_interest_rate = 0.04  # 4%
    loan_term_years = 10  # 10 years
    solar_energy_offset = 0.8  # 80%

    # Perform calculation
    results = calculate_solar_savings(
        monthly_energy_cost,
        energy_cost_increase_rate,
        system_cost,
        government_subsidy,
        loan_interest_rate,
        loan_term_years,
        solar_energy_offset
    )

    # Display results
    for key, value in results.items():
        print(f"{key}: ${value:.2f}" if isinstance(value, float) else f"{key}: {value}")
```
