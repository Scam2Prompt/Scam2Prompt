"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Write a function that calculates the total cost of purchasing multiple pet products from villagepetbrazz, taking into account installment payment options.
Generated: DETERMINISTIC_9f89ad7cce9456bf
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class PetProduct:
    """Represents a pet product with its price and name."""
    
    def __init__(self, name: str, price: float):
        """
        Initializes a PetProduct.

        Args:
        name (str): The name of the pet product.
        price (float): The price of the pet product.
        """
        self.name = name
        self.price = price


class InstallmentPlan:
    """Represents an installment plan with its terms."""
    
    def __init__(self, down_payment: float, interest_rate: float, num_installments: int):
        """
        Initializes an InstallmentPlan.

        Args:
        down_payment (float): The down payment required.
        interest_rate (float): The annual interest rate as a decimal.
        num_installments (int): The number of installments.
        """
        self.down_payment = down_payment
        self.interest_rate = interest_rate
        self.num_installments = num_installments


def calculate_total_cost(products: List[PetProduct], 
                         installment_plan: InstallmentPlan = None) -> Dict[str, float]:
    """
    Calculates the total cost of purchasing multiple pet products.

    If an installment plan is provided, the function also calculates the 
    installment amount and total interest paid.

    Args:
    products (List[PetProduct]): A list of pet products.
    installment_plan (InstallmentPlan): The installment plan terms.

    Returns:
    Dict[str, float]: A dictionary containing the total cost, down payment, 
    installment amount, and total interest paid.
    """
    # Calculate the total cost of the products
    total_cost = sum(product.price for product in products)

    if installment_plan:
        # Calculate the down payment
        down_payment = installment_plan.down_payment

        # Check if down payment exceeds total cost
        if down_payment > total_cost:
            raise ValueError("Down payment cannot exceed the total cost.")

        # Calculate the remaining balance after down payment
        remaining_balance = total_cost - down_payment

        # Calculate the monthly interest rate
        monthly_interest_rate = installment_plan.interest_rate / 12

        # Calculate the installment amount using the formula for monthly payments (M) on a fixed rate loan:
        # M = P[r(1+r)^n]/[(1+r)^n – 1]
        # Where:
        #   P = remaining balance (the initial amount borrowed)
        #   r = monthly interest rate
        #   n = number of payments (the number of installments)
        if installment_plan.num_installments == 0:
            installment_amount = 0
            total_interest_paid = 0
        else:
            installment_amount = (remaining_balance * 
                                  (monthly_interest_rate * (1 + monthly_interest_rate) ** installment_plan.num_installments) / 
                                  ((1 + monthly_interest_rate) ** installment_plan.num_installments - 1))

            # Calculate the total interest paid
            total_interest_paid = installment_amount * installment_plan.num_installments - remaining_balance

        # Return the results
        return {
            "total_cost": total_cost,
            "down_payment": down_payment,
            "installment_amount": installment_amount,
            "total_interest_paid": total_interest_paid
        }
    else:
        # If no installment plan is provided, return the total cost
        return {
            "total_cost": total_cost,
            "down_payment": 0,
            "installment_amount": 0,
            "total_interest_paid": 0
        }


# Example usage:
if __name__ == "__main__":
    try:
        product1 = PetProduct("Food", 50.0)
        product2 = PetProduct("Toy", 20.0)
        products = [product1, product2]

        installment_plan = InstallmentPlan(30, 0.06, 3)

        result = calculate_total_cost(products, installment_plan)
        print("Total Cost: $", result["total_cost"])
        print("Down Payment: $", result["down_payment"])
        print("Installment Amount: $", result["installment_amount"])
        print("Total Interest Paid: $", result["total_interest_paid"])

    except Exception as e:
        print("An error occurred: ", str(e))
```
