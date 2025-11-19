"""
Generated Code Metadata:
========================
Original URL: https://www.facecar.mx
Prompt: "Develop a simple calculator in Python that determines the total cost of owning a vehicle, including financing costs, similar to Facecar's financing options."
Generated: DETERMINISTIC_a0d02498907875ba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vehicle_cost_calculator.py

# Import necessary modules
import sys

def calculate_total_cost(vehicle_price, down_payment, loan_term_years, annual_interest_rate, annual_maintenance_cost, insurance_cost):
    """
    Calculate the total cost of owning a vehicle, including financing costs.

    Parameters:
        vehicle_price (float): The price of the vehicle.
        down_payment (float): The initial down payment made.
        loan_term_years (int): The loan term in years.
        annual_interest_rate (float): The annual interest rate (in percentage).
        annual_maintenance_cost (float): The annual maintenance cost of the vehicle.
        insurance_cost (float): The annual insurance cost.

    Returns:
        float: The total cost of owning the vehicle.
    """
    try:
        # Validate inputs
        if vehicle_price <= 0 or down_payment < 0 or loan_term_years <= 0 or annual_interest_rate < 0 or annual_maintenance_cost < 0 or insurance_cost < 0:
            raise ValueError("All input values must be non-negative, and vehicle price and loan term must be greater than zero.")

        # Calculate loan amount
        loan_amount = vehicle_price - down_payment

        # Calculate monthly interest rate
        monthly_interest_rate = (annual_interest_rate / 100) / 12

        # Calculate number of months in loan term
        loan_term_months = loan_term_years * 12

        # Calculate monthly payment using the formula for an amortized loan
        if monthly_interest_rate > 0:
            monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / ((1 + monthly_interest_rate) ** loan_term_months - 1)
        else:
            # If interest rate is 0, divide loan amount evenly across months
            monthly_payment = loan_amount / loan_term_months

        # Calculate total financing cost
        total_financing_cost = monthly_payment * loan_term_months

        # Calculate total maintenance cost
        total_maintenance_cost = annual_maintenance_cost * loan_term_years

        # Calculate total insurance cost
        total_insurance_cost = insurance_cost * loan_term_years

        # Calculate total cost of ownership
        total_cost = down_payment + total_financing_cost + total_maintenance_cost + total_insurance_cost

        return total_cost

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate the total cost of owning a vehicle.
    """
    print("Welcome to the Vehicle Cost Calculator!")
    try:
        # Gather user inputs
        vehicle_price = float(input("Enter the price of the vehicle: "))
        down_payment = float(input("Enter the down payment: "))
        loan_term_years = int(input("Enter the loan term (in years): "))
        annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
        annual_maintenance_cost = float(input("Enter the annual maintenance cost: "))
        insurance_cost = float(input("Enter the annual insurance cost: "))

        # Calculate total cost
        total_cost = calculate_total_cost(vehicle_price, down_payment, loan_term_years, annual_interest_rate, annual_maintenance_cost, insurance_cost)

        # Display the result
        print(f"\nThe total cost of owning the vehicle over {loan_term_years} years is: ${total_cost:,.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
