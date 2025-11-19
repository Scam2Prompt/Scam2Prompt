"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Python function that simulates the consórcio process for acquiring a Novo Tracker Turbo LTZ, including the calculation of total costs and potential savings.
Generated: DETERMINISTIC_7fd5a39df9cda36d
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def simulate_consorcio(price, num_installments, admin_fee_percent, annual_interest_rate, months_to_interest_free):
    """
    Simulates the consórcio process for acquiring a vehicle.

    Parameters:
        price (float): The total price of the vehicle (Novo Tracker Turbo LTZ).
        num_installments (int): The number of installments in the consórcio.
        admin_fee_percent (float): Percentage-based administrative fee for the consórcio.
        annual_interest_rate (float): Annual interest rate applied to the consórcio payments.
        months_to_interest_free (int): Number of months with zero interest.

    Returns:
        dict: A dictionary containing total costs, total savings, and breakdown of payments.
    """

    # Validate input parameters
    if price <= 0 or num_installments <= 0 or admin_fee_percent < 0 or annual_interest_rate < 0 or months_to_interest_free < 0:
        raise ValueError("Invalid input parameters. All values must be positive.")

    # Calculate the administrative fee
    admin_fee = (admin_fee_percent / 100) * price

    # Calculate the monthly installment amount without interest
    base_monthly_installment = price / num_installments

    # Initialize variables for accumulators
    total_interest = 0
    total_payment = admin_fee  # Start with the administrative fee

    # Calculate monthly installments with interest applied after months_to_interest_free
    monthly_interest_rate = annual_interest_rate / 12 / 100
    payment_schedule = []

    for month in range(1, num_installments + 1):
        if month <= months_to_interest_free:
            # Interest-free months
            monthly_payment = base_monthly_installment
        else:
            # Interest applies after the interest-free period
            remaining_balance = price - (base_monthly_installment * (month - 1))
            monthly_payment = base_monthly_installment + (remaining_balance * monthly_interest_rate)
            total_interest += (remaining_balance * monthly_interest_rate)

        total_payment += monthly_payment
        payment_schedule.append({'Month': month, 'Payment': round(monthly_payment, 2)})

    # Calculate total cost and potential savings (if full upfront payment was made)
    total_cost = total_payment
    full_upfront_cost = price + admin_fee
    potential_savings = full_upfront_cost - total_cost

    # Return results as a dictionary
    return {
        'Total Cost': round(total_cost, 2),
        'Administrative Fee': round(admin_fee, 2),
        'Total Interest Paid': round(total_interest, 2),
        'Potential Savings': max(round(potential_savings, 2), 0),
        'Payment Schedule': payment_schedule
    }


# Example usage:
if __name__ == "__main__":
    try:
        # Novo Tracker Turbo LTZ price and consórcio details
        vehicle_price = 150000  # Price in currency units
        installments = 60  # Number of installments
        admin_fee_percentage = 10  # Administrative fee percentage
        annual_interest = 8  # Annual interest rate
        interest_free_months = 12  # Months with zero interest

        # Simulate consórcio
        result = simulate_consorcio(vehicle_price, installments, admin_fee_percentage, annual_interest, interest_free_months)

        # Print results
        print("Consórcio Simulation Results:")
        print(f"Total Cost: {result['Total Cost']}")
        print(f"Administrative Fee: {result['Administrative Fee']}")
        print(f"Total Interest Paid: {result['Total Interest Paid']}")
        print(f"Potential Savings: {result['Potential Savings']}")
        print("Payment Schedule:")
        for payment in result['Payment Schedule']:
            print(f"  Month {payment['Month']}: {payment['Payment']}")
    except Exception as e:
        print(f"Error: {e}")
```
