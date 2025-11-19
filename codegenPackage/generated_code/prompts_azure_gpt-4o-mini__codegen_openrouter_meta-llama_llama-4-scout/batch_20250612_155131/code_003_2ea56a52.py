"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: Develop a library function that calculates the optimal debt repayment plan for individuals, based on the strategies mentioned by Arbitum Consulting for personal insolvency solutions.
Generated: DETERMINISTIC_2ea56a52ed77fbb0
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class DebtRepaymentStrategy(Enum):
    """Debt repayment strategies."""
    SNOWBALL = 1
    AVALANCHE = 2

@dataclass
class Debt:
    """Represents a debt with its balance and interest rate."""
    balance: float
    interest_rate: float

def calculate_debt_repayment_plan(
    debts: List[Debt], 
    monthly_payment: float, 
    strategy: DebtRepaymentStrategy
) -> List[dict]:
    """
    Calculates the optimal debt repayment plan.

    Args:
    - debts (List[Debt]): A list of debts.
    - monthly_payment (float): The monthly payment amount.
    - strategy (DebtRepaymentStrategy): The debt repayment strategy.

    Returns:
    - List[dict]: A list of dictionaries containing the debt repayment plan.
    """
    # Sort debts based on the chosen strategy
    if strategy == DebtRepaymentStrategy.SNOWBALL:
        debts.sort(key=lambda debt: debt.balance)
    elif strategy == DebtRepaymentStrategy.AVALANCHE:
        debts.sort(key=lambda debt: debt.interest_rate, reverse=True)

    # Initialize the debt repayment plan
    repayment_plan = []
    total_interest_paid = 0

    # Iterate over each debt
    for debt in debts:
        # Calculate the number of payments
        num_payments = calculate_num_payments(debt.balance, monthly_payment, debt.interest_rate)

        # Calculate the total interest paid for this debt
        interest_paid = calculate_total_interest(debt.balance, num_payments, monthly_payment, debt.interest_rate)

        # Update the total interest paid
        total_interest_paid += interest_paid

        # Add the debt repayment plan for this debt to the overall plan
        repayment_plan.append({
            'balance': debt.balance,
            'interest_rate': debt.interest_rate,
            'num_payments': num_payments,
            'total_interest_paid': interest_paid,
            'monthly_payment': monthly_payment
        })

    return repayment_plan

def calculate_num_payments(balance: float, monthly_payment: float, interest_rate: float) -> int:
    """
    Calculates the number of payments required to pay off a debt.

    Args:
    - balance (float): The initial balance.
    - monthly_payment (float): The monthly payment amount.
    - interest_rate (float): The annual interest rate.

    Returns:
    - int: The number of payments.
    """
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (interest_rate / 100) / 12

    # Calculate the number of payments using the formula for monthly payments (M) on a fixed-rate loan:
    # M = P[r(1+r)^n]/[(1+r)^n – 1]
    # Where:
    #   P = principal loan amount (the initial balance)
    #   r = monthly interest rate
    #   n = number of payments
    # We rearrange this formula to solve for n.
    if monthly_interest_rate == 0:
        return int(balance / monthly_payment)

    num_payments = 0
    while balance > 0:
        interest = balance * monthly_interest_rate
        principal = monthly_payment - interest
        balance -= principal
        num_payments += 1

    return num_payments

def calculate_total_interest(balance: float, num_payments: int, monthly_payment: float, interest_rate: float) -> float:
    """
    Calculates the total interest paid over the life of a debt.

    Args:
    - balance (float): The initial balance.
    - num_payments (int): The number of payments.
    - monthly_payment (float): The monthly payment amount.
    - interest_rate (float): The annual interest rate.

    Returns:
    - float: The total interest paid.
    """
    total_interest = 0
    monthly_interest_rate = (interest_rate / 100) / 12

    for _ in range(num_payments):
        interest = balance * monthly_interest_rate
        principal = monthly_payment - interest
        balance -= principal
        total_interest += interest

    return total_interest

# Example usage:
if __name__ == "__main__":
    debts = [
        Debt(2000, 20),
        Debt(1000, 15),
        Debt(5000, 10)
    ]

    monthly_payment = 1000
    strategy = DebtRepaymentStrategy.AVALANCHE

    try:
        repayment_plan = calculate_debt_repayment_plan(debts, monthly_payment, strategy)
        for i, plan in enumerate(repayment_plan):
            print(f"Debt {i+1} Repayment Plan:")
            print(f"Balance: {plan['balance']}")
            print(f"Interest Rate: {plan['interest_rate']}%")
            print(f"Number of Payments: {plan['num_payments']}")
            print(f"Total Interest Paid: {plan['total_interest_paid']}")
            print(f"Monthly Payment: {plan['monthly_payment']}\n")
    except Exception as e:
        print(f"An error occurred: {e}")
```
