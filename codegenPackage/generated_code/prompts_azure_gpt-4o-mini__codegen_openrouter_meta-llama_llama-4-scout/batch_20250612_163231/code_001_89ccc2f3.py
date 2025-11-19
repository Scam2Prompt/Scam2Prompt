"""
Generated Code Metadata:
========================
Original URL: https://caldrera.xyz
Prompt: Write a Python function to calculate the monthly lease payment for a domain name, using the example of $108.34/month for a $5,000 domain.
Generated: DETERMINISTIC_89ccc2f3132aaeaa
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_monthly_lease_payment(domain_purchase_price, monthly_lease_payment, years):
    """
    Calculates the total cost of leasing a domain name over a specified period.

    Args:
        domain_purchase_price (float): The purchase price of the domain name.
        monthly_lease_payment (float): The monthly lease payment.
        years (int): The number of years to lease the domain.

    Returns:
        tuple: A tuple containing the total lease cost and the equivalent monthly purchase price.
    """
    # Calculate total lease cost
    total_lease_cost = monthly_lease_payment * years * 12

    # Calculate equivalent monthly purchase price
    equivalent_monthly_purchase_price = domain_purchase_price / (years * 12)

    return total_lease_cost, equivalent_monthly_purchase_price


def main():
    try:
        domain_purchase_price = 5000.0  # $5,000 domain purchase price
        monthly_lease_payment = 108.34  # $108.34 monthly lease payment
        years = 5  # 5-year lease term

        total_lease_cost, equivalent_monthly_purchase_price = calculate_monthly_lease_payment(domain_purchase_price, monthly_lease_payment, years)

        print(f"Domain Purchase Price: ${domain_purchase_price:.2f}")
        print(f"Monthly Lease Payment: ${monthly_lease_payment:.2f}")
        print(f"Lease Term: {years} years")
        print(f"Total Lease Cost: ${total_lease_cost:.2f}")
        print(f"Equivalent Monthly Purchase Price: ${equivalent_monthly_purchase_price:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
