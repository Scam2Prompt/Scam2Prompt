"""
Generated Code Metadata:
========================
Original URL: https://monadbridge.com
Prompt: Design a function to handle maximum transaction amounts for a cryptocurrency bridge service like Monad Bridge, considering multiple chain and token constraints.
Generated: DETERMINISTIC_858033a1f49481c1
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TransactionLimitExceededError(Exception):
    """Custom exception for handling transaction limit violations."""
    pass

class CryptoBridge:
    def __init__(self):
        # Dictionary to hold maximum transaction limits for each token on each chain
        self.transaction_limits = {
            'Ethereum': {
                'ETH': 10.0,  # Max 10 ETH
                'USDT': 5000.0  # Max 5000 USDT
            },
            'Binance Smart Chain': {
                'BNB': 5.0,  # Max 5 BNB
                'BUSD': 3000.0  # Max 3000 BUSD
            },
            # Add more chains and tokens as needed
        }

    def set_transaction_limit(self, chain: str, token: str, limit: float):
        """
        Set a new transaction limit for a specific token on a specific chain.

        :param chain: The blockchain name (e.g., 'Ethereum').
        :param token: The token symbol (e.g., 'ETH').
        :param limit: The new transaction limit.
        """
        if chain not in self.transaction_limits:
            self.transaction_limits[chain] = {}
        self.transaction_limits[chain][token] = limit

    def validate_transaction(self, chain: str, token: str, amount: float) -> bool:
        """
        Validate if the transaction amount is within the allowed limit.

        :param chain: The blockchain name (e.g., 'Ethereum').
        :param token: The token symbol (e.g., 'ETH').
        :param amount: The transaction amount to validate.
        :raises TransactionLimitExceededError: If the transaction exceeds the limit.
        :return: True if the transaction is valid, otherwise raises an error.
        """
        try:
            limit = self.transaction_limits[chain][token]
            if amount > limit:
                raise TransactionLimitExceededError(
                    f"Transaction amount of {amount} exceeds the limit of {limit} for {token} on {chain}."
                )
            return True
        except KeyError:
            raise ValueError(f"Transaction limit not set for {token} on {chain}.")

# Example usage
if __name__ == "__main__":
    bridge_service = CryptoBridge()
    
    # Set a new transaction limit
    bridge_service.set_transaction_limit('Ethereum', 'DAI', 2000.0)

    # Validate a transaction
    try:
        is_valid = bridge_service.validate_transaction('Ethereum', 'ETH', 5.0)
        print("Transaction is valid:", is_valid)
    except (TransactionLimitExceededError, ValueError) as e:
        print("Error:", e)
```
