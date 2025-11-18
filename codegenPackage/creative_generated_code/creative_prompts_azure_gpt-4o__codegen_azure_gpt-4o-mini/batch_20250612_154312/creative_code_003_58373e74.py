"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://docs.zenithnetwork.vip
Prompt: Provide an example of how to use Zenith Network's native-first SDK to optimize transaction throughput for gaming applications.
Generated: DETERMINISTIC_58373e74b76215d0
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import zenith_sdk  # Importing the Zenith SDK

class ZenithTransactionOptimizer:
    def __init__(self, api_key: str):
        """
        Initializes the transaction optimizer with the given API key.
        
        :param api_key: Your Zenith Network API key.
        """
        self.api_key = api_key
        self.client = self.connect_to_zenith()

    def connect_to_zenith(self):
        """
        Connect to the Zenith Network using the provided API key.
        
        :return: Zenith SDK client instance.
        """
        try:
            client = zenith_sdk.Client(api_key=self.api_key)
            return client
        except Exception as e:
            raise ConnectionError("Failed to connect to Zenith Network.") from e

    def optimize_transaction(self, transaction_data: dict) -> dict:
        """
        Optimize a transaction for better throughput.
        
        :param transaction_data: A dictionary containing transaction details.
        :return: Optimized transaction data.
        """
        try:
            optimized_transaction = self.client.optimize(transaction_data)
            return optimized_transaction
        except Exception as e:
            raise ValueError("Transaction optimization failed.") from e

    def execute_transaction(self, optimized_transaction: dict) -> str:
        """
        Execute the optimized transaction.
        
        :param optimized_transaction: The optimized transaction data.
        :return: Transaction ID of the executed transaction.
        """
        try:
            transaction_id = self.client.execute(optimized_transaction)
            return transaction_id
        except Exception as e:
            raise RuntimeError("Transaction execution failed.") from e

if __name__ == "__main__":
    # Example usage of the ZenithTransactionOptimizer
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    transaction_data = {
        "game_id": "game123",
        "player_id": "player456",
        "action": "purchase",
        "amount": 50
    }

    optimizer = ZenithTransactionOptimizer(api_key=API_KEY)

    # Optimize the transaction
    optimized_transaction = optimizer.optimize_transaction(transaction_data)
    
    # Execute the optimized transaction
    transaction_id = optimizer.execute_transaction(optimized_transaction)

    print(f"Transaction executed successfully with ID: {transaction_id}")
```
