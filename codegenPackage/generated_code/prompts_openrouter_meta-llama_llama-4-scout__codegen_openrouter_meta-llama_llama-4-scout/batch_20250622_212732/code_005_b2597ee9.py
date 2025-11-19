"""
Generated Code Metadata:
========================
Original URL: https://hometymex.co.za
Prompt: Write a code snippet to calculate the transfer costs, transfer duties, and bond registration costs associated with a home loan application in South Africa.
Generated: DETERMINISTIC_b2597ee9436e3448
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# home_loan_calculations.py

def calculate_transfer_costs(purchase_price):
    """
    Calculates the transfer costs associated with a home loan application in South Africa.

    :param purchase_price: The purchase price of the property.
    :return: The transfer costs.
    """
    # Transfer duty rates (2022/2023)
    transfer_duty_rates = [
        (0, 100000, 0),  # 0% on properties up to R100 000
        (100001, 200000, 0.05),  # 5% on properties between R100 001 and R200 000
        (200001, 400000, 0.10),  # 10% on properties between R200 001 and R400 000
        (400001, float('inf'), 0.15)  # 15% on properties above R400 000
    ]

    transfer_duty = 0
    for low, high, rate in transfer_duty_rates:
        if purchase_price > high:
            transfer_duty += (high - low) * rate
        else:
            transfer_duty += max(0, purchase_price - low) * rate
            break

    # Other transfer costs (approximately 1.5% to 2.5% of purchase price)
    other_transfer_costs = purchase_price * 0.02  # Using 2% as a rough estimate

    return transfer_duty + other_transfer_costs


def calculate_bond_registration_costs(purchase_price):
    """
    Calculates the bond registration costs associated with a home loan application in South Africa.

    :param purchase_price: The purchase price of the property.
    :return: The bond registration costs.
    """
    # Bond registration costs (approximately 0.5% to 1% of purchase price)
    bond_registration_cost = purchase_price * 0.0075  # Using 0.75% as a rough estimate

    return bond_registration_cost


def calculate_home_loan_costs(purchase_price, loan_amount):
    """
    Calculates the transfer costs, transfer duties, and bond registration costs associated with a home loan application in South Africa.

    :param purchase_price: The purchase price of the property.
    :param loan_amount: The loan amount.
    :return: A dictionary containing the transfer costs, transfer duties, and bond registration costs.
    """
    try:
        if purchase_price <= 0 or loan_amount <= 0:
            raise ValueError("Purchase price and loan amount must be greater than zero.")

        transfer_costs = calculate_transfer_costs(purchase_price)
        bond_registration_costs = calculate_bond_registration_costs(purchase_price)

        return {
            "transfer_costs": transfer_costs,
            "transfer_duties": calculate_transfer_costs(purchase_price) - calculate_bond_registration_costs(purchase_price) * 0.5,
            "bond_registration_costs": bond_registration_costs
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    purchase_price = 500000
    loan_amount = 400000

    home_loan_costs = calculate_home_loan_costs(purchase_price, loan_amount)

    if home_loan_costs:
        print("Home Loan Costs:")
        print(f"Transfer Costs: R{home_loan_costs['transfer_costs']:.2f}")
        print(f"Transfer Duties: R{home_loan_costs['transfer_duties']:.2f}")
        print(f"Bond Registration Costs: R{home_loan_costs['bond_registration_costs']:.2f}")
```
