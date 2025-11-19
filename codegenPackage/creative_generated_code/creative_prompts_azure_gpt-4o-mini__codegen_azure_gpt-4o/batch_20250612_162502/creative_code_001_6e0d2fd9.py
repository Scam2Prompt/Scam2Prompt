"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chevroletfinanciado.com.ar
Prompt: Write a function that calculates the total cost of a Chevrolet car purchase using the Plan de Ahorro, incorporating regional pricing variations.
Generated: DETERMINISTIC_6e0d2fd9e6810a86
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_chevrolet_plan_cost(base_price, region_factor, down_payment_percentage, num_installments, interest_rate):
    """
    Calculate the total cost of purchasing a Chevrolet car using the Plan de Ahorro.

    Args:
        base_price (float): The base price of the car (in USD or local currency).
        region_factor (float): The regional pricing multiplier (e.g., 1.1 for a 10% increase).
        down_payment_percentage (float): Percentage of the base price to be paid upfront (e.g., 0.2 for 20%).
        num_installments (int): Number of monthly installments for the remaining balance.
        interest_rate (float): Annual interest rate applied on the installments (e.g., 0.05 for 5%).

    Returns:
        float: The total cost of the car including down payment, installments, and interest.
    """
    try:
        # Validate input values
        if base_price <= 0 or region_factor <= 0 or down_payment_percentage < 0 or down_payment_percentage > 1 \
                or num_installments <= 0 or interest_rate < 0:
            raise ValueError("Invalid input parameters. Ensure all values are positive and percentages are between 0 and 1.")

        # Adjust base price based on regional factor
        adjusted_price = base_price * region_factor

        # Calculate the upfront down payment
        down_payment = adjusted_price * down_payment_percentage

        # Calculate the remaining balance after the down payment
        remaining_balance = adjusted_price - down_payment

        # Monthly interest rate derived from annual rate
        monthly_interest_rate = interest_rate / 12

        # Calculate monthly installment amount using the formula for an installment loan
        monthly_installment = (remaining_balance * monthly_interest_rate) / \
                              (1 - (1 + monthly_interest_rate) ** -num_installments)

        # Calculate total cost of installments
        total_installments_cost = monthly_installment * num_installments

        # Calculate the total cost of the car
        total_cost = down_payment + total_installments_cost

        return total_cost

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Example parameters
    base_price = 25000  # Base price of the car
    region_factor = 1.2  # Regional factor increases base price by 20%
    down_payment_percentage = 0.2  # 20% down payment
    num_installments = 36  # 36 monthly installments
    interest_rate = 0.05  # 5% annual interest rate

    total_cost = calculate_chevrolet_plan_cost(base_price, region_factor, down_payment_percentage, num_installments, interest_rate)
    
    if total_cost:
        print(f"The total cost of the Chevrolet car purchase is: ${total_cost:.2f}")
```
