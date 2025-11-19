"""
Generated Code Metadata:
========================
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Create a code snippet to calculate the exchange rate between `wTAO` and `rsTAO` (1 wTAO = 1 rsTAO) and display the balances for both tokens.
Generated: DETERMINISTIC_d579dc7d7967d848
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_exchange_rate(wtao_balance, rsta_balance):
    """
    Calculate the exchange rate between wTAO and rsTAO (1:1).
    
    Args:
        wtao_balance (float): Balance of wTAO tokens
        rsta_balance (float): Balance of rsTAO tokens
    
    Returns:
        dict: Dictionary containing exchange rate and balances
    """
    try:
        # 1 wTAO = 1 rsTAO (fixed exchange rate)
        exchange_rate = 1.0
        
        return {
            'exchange_rate': exchange_rate,
            'wtao_balance': wtao_balance,
            'rsta_balance': rsta_balance,
            'equivalent_value': wtao_balance * exchange_rate  # Equivalent rsTAO value
        }
    except Exception as e:
        print(f"Error calculating exchange rate: {e}")
        return None

def display_balances(exchange_data):
    """
    Display the token balances and exchange rate information.
    
    Args:
        exchange_data (dict): Dictionary containing exchange information
    """
    if not exchange_data:
        print("No exchange data to display")
        return
    
    try:
        print("\nToken Balances and Exchange Rate:")
        print(f"- wTAO Balance: {exchange_data['wtao_balance']}")
        print(f"- rsTAO Balance: {exchange_data['rsta_balance']}")
        print(f"- Exchange Rate: 1 wTAO = {exchange_data['exchange_rate']} rsTAO")
        print(f"- Equivalent Value: {exchange_data['wtao_balance']} wTAO = {exchange_data['equivalent_value']} rsTAO")
    except KeyError as e:
        print(f"Error displaying balances: Missing key {e}")

# Example usage
if __name__ == "__main__":
    # Sample balances
    wtao = 100.0
    rsta = 150.0
    
    # Calculate exchange data
    exchange_data = calculate_exchange_rate(wtao, rsta)
    
    # Display results
    display_balances(exchange_data)
```
