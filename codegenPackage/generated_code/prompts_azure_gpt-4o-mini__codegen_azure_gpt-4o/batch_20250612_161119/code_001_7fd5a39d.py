"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Python function that simulates the consórcio process for acquiring a Novo Tracker Turbo LTZ, including the calculation of total costs and potential savings.
Generated: DETERMINISTIC_7fd5a39df9cda36d
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def simulate_consorcio(vehicle_price, num_installments, admin_fee_percentage, monthly_interest_rate):
    """
    Simulates the consórcio process for acquiring a vehicle.

    Parameters:
        vehicle_price (float): The price of the vehicle (e.g., Novo Tracker Turbo LTZ).
        num_installments (int): The number of installments in the consórcio plan.
        admin_fee_percentage (float): The administrative fee percentage charged by the consórcio company.
        monthly_interest_rate (float): The monthly interest rate applied to the consórcio.

    Returns:
        dict: A dictionary containing the total cost, total savings, and installment details.
    """
    try:
        # Validate inputs
        if vehicle_price <= 0 or num_installments <= 0 or admin_fee_percentage < 0 or monthly_interest_rate < 0:
            raise ValueError("Invalid input values. Ensure all values are positive and non-zero where applicable.")

        # Calculate administrative fee
        admin_fee = vehicle_price * (admin_fee_percentage / 100)

        # Calculate total cost with interest
        total_cost_with_interest = 0
        installment_details = []
        for i in range(1, num_installments + 1):
            # Calculate the installment amount with interest
            installment_amount = (vehicle_price / num_installments) * (1 + monthly_interest_rate)
            total_cost_with_interest += installment_amount
            installment_details.append({
                "installment_number": i,
                "installment_amount": round(installment_amount, 2)
            })

        # Calculate total cost
        total_cost = total_cost_with_interest + admin_fee

        # Calculate potential savings (difference between upfront payment and consórcio total cost)
        potential_savings = total_cost - vehicle_price

        # Return results
        return {
            "vehicle_price": round(vehicle_price, 2),
            "num_installments": num_installments,
            "admin_fee": round(admin_fee, 2),
            "total_cost": round(total_cost, 2),
            "potential_savings": round(potential_savings, 2),
            "installment_details": installment_details
        }

    except Exception as e:
        # Handle unexpected errors
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    # Parameters for the consórcio simulation
    vehicle_price = 150000.00  # Price of Novo Tracker Turbo LTZ
    num_installments = 60      # Number of installments (e.g., 60 months)
    admin_fee_percentage = 10  # Administrative fee percentage (e.g., 10%)
    monthly_interest_rate = 0.01  # Monthly interest rate (e.g., 1%)

    # Simulate consórcio
    result = simulate_consorcio(vehicle_price, num_installments, admin_fee_percentage, monthly_interest_rate)

    # Print results
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("Consórcio Simulation Results:")
        print(f"Vehicle Price: R$ {result['vehicle_price']}")
        print(f"Number of Installments: {result['num_installments']}")
        print(f"Administrative Fee: R$ {result['admin_fee']}")
        print(f"Total Cost: R$ {result['total_cost']}")
        print(f"Potential Savings: R$ {result['potential_savings']}")
        print("Installment Details:")
        for installment in result["installment_details"]:
            print(f"  Installment {installment['installment_number']}: R$ {installment['installment_amount']}")
```
