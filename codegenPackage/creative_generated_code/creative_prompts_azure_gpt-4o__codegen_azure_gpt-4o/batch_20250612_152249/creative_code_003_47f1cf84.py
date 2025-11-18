"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeih3gn5wsayvygu6qq4vwexe2dl4nf4ag25hrw2srld2z5zlirzzgi.ipfs.dweb.link
Prompt: Create a function to calculate capital efficiency in cross-chain transactions using the Mitosis liquidity protocol.
Generated: DETERMINISTIC_47f1cf84764cb81e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def calculate_capital_efficiency(transferred_amount, received_amount, transaction_costs):
    """
    Calculate capital efficiency in cross-chain transactions using the Mitosis liquidity protocol.
    
    Capital Efficiency Formula:
    Capital Efficiency (%) = ((Received Amount - Transaction Costs) / Transferred Amount) * 100

    Args:
        transferred_amount (float): The amount of funds transferred across chains.
        received_amount (float): The amount of funds received after the transaction.
        transaction_costs (float): The cumulative costs associated with the transaction.
    
    Returns:
        float: The capital efficiency percentage.
        
    Raises:
        ValueError: If any of the inputs are negative or if transferred_amount is zero.
    """
    # Validate inputs
    if transferred_amount <= 0:
        raise ValueError("Transferred amount must be greater than zero.")
    if received_amount < 0:
        raise ValueError("Received amount cannot be negative.")
    if transaction_costs < 0:
        raise ValueError("Transaction costs cannot be negative.")

    # Use decimal for precise financial calculations
    transferred_amount = decimal.Decimal(transferred_amount)
    received_amount = decimal.Decimal(received_amount)
    transaction_costs = decimal.Decimal(transaction_costs)

    # Calculate capital efficiency
    capital_efficiency = ((received_amount - transaction_costs) / transferred_amount) * 100

    # Ensure the result is rounded to two decimal places
    return round(float(capital_efficiency), 2)


# Example usage:
try:
    efficiency = calculate_capital_efficiency(transferred_amount=1000, received_amount=950, transaction_costs=20)
    print(f"Capital Efficiency: {efficiency}%")
except ValueError as e:
    print(f"Error: {e}")
```
