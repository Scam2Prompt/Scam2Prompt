"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Write a Python script to calculate the financial savings for domestic consumers installing PV systems under the loan scheme described by the Development Bank of Mauritius.
Generated: DETERMINISTIC_67d067a95759f7e9
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_savings(installed_capacity_kW, annual_consumption_kWh, loan_amount, interest_rate, loan_term_years, pv_system_cost_per_kW, annual_sunlight_hours, electricity_rate_per_kWh, degradation_rate=0.005):
    """
    Calculate financial savings for domestic consumers installing PV systems under a loan scheme.

    Parameters:
        installed_capacity_kW (float): The installed capacity of the PV system in kilowatts.
        annual_consumption_kWh (float): Annual electricity consumption in kilowatt-hours.
        loan_amount (float): Loan amount taken for the PV system installation.
        interest_rate (float): Annual interest rate of the loan (as a decimal, e.g., 0.05 for 5%).
        loan_term_years (int): Loan repayment term in years.
        pv_system_cost_per_kW (float): Cost of PV system installation per kilowatt.
        annual_sunlight_hours (float): Average number of sunlight hours per year.
        electricity_rate_per_kWh (float): Current electricity rate per kilowatt-hour.
        degradation_rate (float): Annual efficiency degradation rate of the PV system (default: 0.005).

    Returns:
        dict: Calculated savings, total costs, and benefits.
    """
    try:
        # Calculate the total PV system cost
        pv_system_cost = installed_capacity_kW * pv_system_cost_per_kW

        # Validate that the loan amount is not greater than the system cost
        if loan_amount > pv_system_cost:
            raise ValueError("Loan amount cannot exceed the total PV system cost.")

        # Calculate monthly loan repayment
        monthly_interest_rate = interest_rate / 12  # Convert annual interest rate to monthly
        num_payments = loan_term_years * 12
        monthly_repayment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

        # Calculate annual electricity generation by the PV system
        annual_generation_kWh = installed_capacity_kW * annual_sunlight_hours

        # Adjust generation by degradation rate over the loan term
        adjusted_annual_generation_kWh = 0
        for year in range(loan_term_years):
            adjusted_annual_generation_kWh += annual_generation_kWh * (1 - degradation_rate) ** year

        # Calculate annual savings from electricity generation (up to annual consumption)
        annual_savings = min(adjusted_annual_generation_kWh, annual_consumption_kWh) * electricity_rate_per_kWh

        # Calculate total savings over the loan term
        total_savings = annual_savings * loan_term_years

        # Calculate the net benefit (savings - loan repayments)
        total_loan_repayment = monthly_repayment * num_payments
        net_benefit = total_savings - total_loan_repayment

        # Return results
        return {
            "pv_system_cost": round(pv_system_cost, 2),
            "monthly_repayment": round(monthly_repayment, 2),
            "total_loan_repayment": round(total_loan_repayment, 2),
            "annual_savings": round(annual_savings, 2),
            "total_savings": round(total_savings, 2),
            "net_benefit": round(net_benefit, 2),
        }

    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    try:
        # Input parameters
        installed_capacity_kW = float(input("Enter installed capacity of PV system (in kW): "))
        annual_consumption_kWh = float(input("Enter annual electricity consumption (in kWh): "))
        loan_amount = float(input("Enter loan amount: "))
        interest_rate = float(input("Enter interest rate (as a decimal, e.g., 0.05 for 5%): "))
        loan_term_years = int(input("Enter loan term (in years): "))
        pv_system_cost_per_kW = float(input("Enter cost of PV system per kW: "))
        annual_sunlight_hours = float(input("Enter annual sunlight hours: "))
        electricity_rate_per_kWh = float(input("Enter electricity rate per kWh: "))

        results = calculate_savings(installed_capacity_kW, annual_consumption_kWh, loan_amount, interest_rate, loan_term_years, pv_system_cost_per_kW, annual_sunlight_hours, electricity_rate_per_kWh)

        if "error" in results:
            print(f"Error: {results['error']}")
        else:
            print("\n--- Financial Savings Calculation ---")
            print(f"PV System Cost: ${results['pv_system_cost']}")
            print(f"Monthly Loan Repayment: ${results['monthly_repayment']}")
            print(f"Total Loan Repayment: ${results['total_loan_repayment']}")
            print(f"Annual Savings: ${results['annual_savings']}")
            print(f"Total Savings Over Loan Term: ${results['total_savings']}")
            print(f"Net Benefit: ${results['net_benefit']}")
    except ValueError:
        print("Invalid input. Please ensure you enter numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
