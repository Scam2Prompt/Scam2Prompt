"""
Generated Code Metadata:
========================
Original URL: https://greenbtcwebb.pages.dev
Prompt: Provide a Python example for calculating the energy consumption difference between Green Bitcoin ($GBTC) and traditional Bitcoin using the energy per transaction values provided (34 Wh vs. 1,173,000 Wh).
Generated: DETERMINISTIC_4d925395af8e3612
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_consumption_calculator.py

def calculate_energy_consumption_difference(
    green_bitcoin_energy_per_transaction: float, 
    traditional_bitcoin_energy_per_transaction: float, 
    transactions: int
) -> float:
    """
    Calculate the energy consumption difference between Green Bitcoin and traditional Bitcoin.

    Args:
    - green_bitcoin_energy_per_transaction (float): Energy consumption per Green Bitcoin transaction in Wh.
    - traditional_bitcoin_energy_per_transaction (float): Energy consumption per traditional Bitcoin transaction in Wh.
    - transactions (int): Number of transactions.

    Returns:
    - float: Energy consumption difference in Wh.
    """

    # Validate input values
    if green_bitcoin_energy_per_transaction <= 0:
        raise ValueError("Green Bitcoin energy per transaction must be greater than 0")
    if traditional_bitcoin_energy_per_transaction <= 0:
        raise ValueError("Traditional Bitcoin energy per transaction must be greater than 0")
    if transactions <= 0:
        raise ValueError("Number of transactions must be greater than 0")

    # Calculate energy consumption for both types of Bitcoin
    green_bitcoin_energy_consumption = green_bitcoin_energy_per_transaction * transactions
    traditional_bitcoin_energy_consumption = traditional_bitcoin_energy_per_transaction * transactions

    # Calculate energy consumption difference
    energy_consumption_difference = traditional_bitcoin_energy_consumption - green_bitcoin_energy_consumption

    return energy_consumption_difference


def main():
    # Energy per transaction values in Wh
    green_bitcoin_energy_per_transaction = 34  # Wh
    traditional_bitcoin_energy_per_transaction = 1_173_000  # Wh

    # Number of transactions
    transactions = 1_000_000  # 1 million transactions

    try:
        energy_consumption_difference = calculate_energy_consumption_difference(
            green_bitcoin_energy_per_transaction, 
            traditional_bitcoin_energy_per_transaction, 
            transactions
        )

        print(f"Energy consumption difference for {transactions} transactions: {energy_consumption_difference:,} Wh")
        print(f"Green Bitcoin saves {energy_consumption_difference / transactions:,.2f} Wh per transaction")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
