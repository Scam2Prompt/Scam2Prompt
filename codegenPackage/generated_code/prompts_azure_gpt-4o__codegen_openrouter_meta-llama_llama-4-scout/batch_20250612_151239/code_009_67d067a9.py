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
# pv_savings_calculator.py

import math

def calculate_monthly_loan_repayment(loan_amount, interest_rate, loan_tenor):
    """
    Calculate the monthly loan repayment.

    Args:
        loan_amount (float): The loan amount.
        interest_rate (float): The annual interest rate as a decimal.
        loan_tenor (int): The loan tenor in years.

    Returns:
        float: The monthly loan repayment.
    """
    monthly_interest_rate = interest_rate / 12
    number_of_payments = loan_tenor * 12
    monthly_repayment = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    return round(monthly_repayment, 2)


def calculate_electricity_bill_savings(current_bill, self_consumption, export_tariff, import_tariff):
    """
    Calculate the electricity bill savings.

    Args:
        current_bill (float): The current monthly electricity bill.
        self_consumption (float): The amount of electricity self-consumed.
        export_tariff (float): The export tariff per kWh.
        import_tariff (float): The import tariff per kWh.

    Returns:
        float: The electricity bill savings.
    """
    return round(current_bill - (current_bill - self_consumption * import_tariff - self_consumption * export_tariff), 2)


def calculate_net_savings(loan_repayment, electricity_bill_savings):
    """
    Calculate the net savings.

    Args:
        loan_repayment (float): The monthly loan repayment.
        electricity_bill_savings (float): The electricity bill savings.

    Returns:
        float: The net savings.
    """
    return round(electricity_bill_savings - loan_repayment, 2)


def main():
    try:
        # Input parameters
        loan_amount = float(input("Enter the loan amount: MUR "))
        interest_rate = float(input("Enter the annual interest rate (in %): ")) / 100
        loan_tenor = int(input("Enter the loan tenor (in years): "))
        current_bill = float(input("Enter the current monthly electricity bill: MUR "))
        pv_system_size = float(input("Enter the PV system size (in kWp): "))
        self_consumption_rate = float(input("Enter the self-consumption rate (in %): ")) / 100
        export_tariff = float(input("Enter the export tariff (in MUR/kWh): "))
        import_tariff = float(input("Enter the import tariff (in MUR/kWh): "))
        electricity_generation_per_kwp = 2000  # Assuming 2000 kWh/kWp/year

        # Calculate electricity self-consumed
        electricity_generation = pv_system_size * electricity_generation_per_kwp
        self_consumption = electricity_generation * self_consumption_rate / 12  # Monthly self-consumption

        # Calculate loan repayment
        monthly_loan_repayment = calculate_monthly_loan_repayment(loan_amount, interest_rate, loan_tenor)

        # Calculate electricity bill savings
        electricity_bill_savings = calculate_electricity_bill_savings(current_bill, self_consumption, export_tariff, import_tariff)

        # Calculate net savings
        net_savings = calculate_net_savings(monthly_loan_repayment, electricity_bill_savings)

        # Print results
        print("\nResults:")
        print(f"Monthly loan repayment: MUR {monthly_loan_repayment}")
        print(f"Electricity bill savings: MUR {electricity_bill_savings}")
        print(f"Net savings: MUR {net_savings}")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
