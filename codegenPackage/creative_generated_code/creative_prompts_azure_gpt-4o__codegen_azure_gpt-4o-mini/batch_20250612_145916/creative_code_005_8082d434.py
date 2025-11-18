"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonminingpool.xyz
Prompt: Develop a function to generate deposit addresses for Toncoin, BTC, and USDT as described in TONMININGPOOL, and validate the minimum deposit limits for each currency.
Generated: DETERMINISTIC_8082d434bc345cee
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class DepositAddressGenerator:
    def __init__(self):
        # Set minimum deposit limits for each currency
        self.min_deposit_limits = {
            'Toncoin': 0.1,  # Example minimum deposit for Toncoin
            'BTC': 0.001,    # Example minimum deposit for Bitcoin
            'USDT': 10.0     # Example minimum deposit for USDT
        }

    def generate_address(self, currency):
        """
        Generate a unique deposit address for the specified currency.
        
        :param currency: str - The currency for which to generate the address
        :return: str - A unique deposit address
        :raises ValueError: If the currency is not supported
        """
        if currency not in self.min_deposit_limits:
            raise ValueError(f"Currency '{currency}' is not supported.")
        
        # Generate a unique deposit address using UUID
        address = f"{currency[:3].upper()}_{uuid.uuid4()}"
        return address

    def validate_deposit(self, currency, amount):
        """
        Validate the deposit amount against the minimum deposit limit.
        
        :param currency: str - The currency being deposited
        :param amount: float - The amount to validate
        :return: bool - True if valid, otherwise False
        :raises ValueError: If the currency is not supported
        """
        if currency not in self.min_deposit_limits:
            raise ValueError(f"Currency '{currency}' is not supported.")
        
        # Check if the deposit amount meets the minimum requirement
        return amount >= self.min_deposit_limits[currency]


# Example usage
if __name__ == "__main__":
    generator = DepositAddressGenerator()
    
    # Generate deposit addresses
    try:
        btc_address = generator.generate_address('BTC')
        toncoin_address = generator.generate_address('Toncoin')
        usdt_address = generator.generate_address('USDT')
        
        print(f"BTC Address: {btc_address}")
        print(f"Toncoin Address: {toncoin_address}")
        print(f"USDT Address: {usdt_address}")
        
    except ValueError as e:
        print(f"Error: {e}")

    # Validate deposits
    try:
        btc_valid = generator.validate_deposit('BTC', 0.002)
        print(f"BTC deposit valid: {btc_valid}")
        
        usdt_valid = generator.validate_deposit('USDT', 5.0)
        print(f"USDT deposit valid: {usdt_valid}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
