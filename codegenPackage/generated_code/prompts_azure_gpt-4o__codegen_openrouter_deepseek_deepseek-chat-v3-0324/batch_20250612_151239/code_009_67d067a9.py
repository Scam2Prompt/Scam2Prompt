"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Write a Python script to calculate the financial savings for domestic consumers installing PV systems under the loan scheme described by the Development Bank of Mauritius.
Generated: DETERMINISTIC_67d067a95759f7e9
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_savings(
    pv_capacity: float,
    loan_amount: float,
    loan_interest_rate: float,
    loan_term_years: int,
    electricity_rate: float,
    pv_system_efficiency: float,
    daily_sunlight_hours: float,
    system_lifespan_years: int,
    maintenance_cost_per_year: float,
    inflation_rate: float = 0.02
) -> dict:
    """
    Calculate financial savings for domestic consumers installing PV systems under a loan scheme.
    
    Args:
        pv_capacity: PV system capacity in kW
        loan_amount: Total loan amount in local currency
        loan_interest_rate: Annual interest rate (decimal)
        loan_term_years: Loan repayment period in years
        electricity_rate: Current electricity rate per kWh
        pv_system_efficiency: System efficiency (0 to 1)
        daily_sunlight_hours: Average daily sunlight hours
        system_lifespan_years: Expected lifespan of PV system
        maintenance_cost_per_year: Annual maintenance cost
        inflation_rate: Annual inflation rate (default 0.02)
        
    Returns:
        Dictionary containing all calculated financial metrics
    """
    
    # Validate inputs
    if any(arg <= 0 for arg in [pv_capacity, loan_amount, loan_term_years, electricity_rate, 
                               daily_sunlight_hours, system_lifespan_years]):
        raise ValueError("All numeric inputs must be positive")
    
    if not 0 <= pv_system_efficiency <= 1:
        raise ValueError("System efficiency must be between 0 and 1")
    
    if not 0 <= loan_interest_rate <= 1:
        raise ValueError("Interest rate must be between 0 and 1")
    
    # Calculate annual energy production (kWh)
    annual_energy_production = (
        pv_capacity * 
        daily_sunlight_hours * 
        365 * 
        pv_system_efficiency
    )
    
    # Calculate annual electricity savings (without inflation)
    annual_savings = annual_energy_production * electricity_rate
    
    # Calculate loan monthly payment (using annuity formula)
    monthly_interest_rate = loan_interest_rate / 12
    num_payments = loan_term_years * 12
    monthly_payment = (
        loan_amount * 
        monthly_interest_rate * 
        (1 + monthly_interest_rate) ** num_payments
    ) / (
        (1 + monthly_interest_rate) ** num_payments - 1
    )
    
    # Calculate total loan cost
    total_loan_cost = monthly_payment * num_payments
    
    # Calculate net present value of savings over system lifespan
    npv_savings = 0
    cumulative_savings = 0
    cumulative_costs = 0
    
    for year in range(1, system_lifespan_years + 1):
        # Inflation-adjusted savings
        inflated_savings = annual_savings * (1 + inflation_rate) ** (year - 1)
        
        # Costs (loan payments for first loan_term_years, then just maintenance)
        if year <= loan_term_years:
            annual_loan_cost = monthly_payment * 12
            annual_cost = annual_loan_cost + maintenance_cost_per_year
        else:
            annual_cost = maintenance_cost_per_year
        
        # Discounted cash flows
        discount_factor = (1 + inflation_rate) ** (year - 1)
        npv_savings += (inflated_savings - annual_cost) / discount_factor
        
        cumulative_savings += inflated_savings
        cumulative_costs += annual_cost
    
    # Calculate simple payback period (years to recover loan amount)
    net_annual_savings = annual_savings - (monthly_payment * 12) - maintenance_cost_per_year
    if net_annual_savings <= 0:
        payback_period = float('inf')
    else:
        payback_period = loan_amount / net_annual_savings
    
    # Calculate return on investment
    total_net_savings = cumulative_savings - cumulative_costs
    roi = (total_net_savings / cumulative_costs) * 100 if cumulative_costs > 0 else float('inf')
    
    return {
        'annual_energy_production_kwh': annual_energy_production,
        'annual_savings': annual_savings,
        'monthly_loan_payment': monthly_payment,
        'total_loan_cost': total_loan_cost,
        'total_maintenance_cost': maintenance_cost_per_year * system_lifespan_years,
        'total_savings': cumulative_savings,
        'total_costs': cumulative_costs,
        'net_savings': total_net_savings,
        'return_on_investment_percent': roi,
        'payback_period_years': payback_period,
        'npv_savings': npv_savings
    }

def main():
    try:
        # Example usage with typical values for Mauritius
        results = calculate_savings(
            pv_capacity=5.0,  # 5 kW system
            loan_amount=200000,  # MUR 200,000
            loan_interest_rate=0.05,  # 5% annual interest
            loan_term_years=10,
            electricity_rate=8.0,  # MUR 8 per kWh
            pv_system_efficiency=0.85,  # 85% efficiency
            daily_sunlight_hours=5.5,  # Mauritius average
            system_lifespan_years=25,
            maintenance_cost_per_year=5000  # MUR 5,000 per year
        )
        
        # Print results
        print("Financial Analysis for PV System Installation:")
        print(f"Annual Energy Production: {results['annual_energy_production_kwh']:.2f} kWh")
        print(f"Annual Savings: MUR {results['annual_savings']:.2f}")
        print(f"Monthly Loan Payment: MUR {results['monthly_loan_payment']:.2f}")
        print(f"Total Loan Cost: MUR {results['total_loan_cost']:.2f}")
        print(f"Total Maintenance Cost: MUR {results['total_maintenance_cost']:.2f}")
        print(f"Total Savings Over {results['payback_period_years']:.1f} Years: MUR {results['total_savings']:.2f}")
        print(f"Net Savings: MUR {results['net_savings']:.2f}")
        print(f"Return on Investment: {results['return_on_investment_percent']:.2f}%")
        print(f"Payback Period: {results['payback_period_years']:.1f} years")
        print(f"Net Present Value of Savings: MUR {results['npv_savings']:.2f}")
        
    except ValueError as e:
        print(f"Error in input parameters: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
