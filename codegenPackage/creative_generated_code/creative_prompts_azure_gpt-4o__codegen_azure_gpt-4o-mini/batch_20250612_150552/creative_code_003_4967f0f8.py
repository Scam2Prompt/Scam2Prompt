"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bsquared-en.pages.dev
Prompt: Write a function to calculate transaction costs on the B² Network, demonstrating how it is 50x cheaper than the Bitcoin network.
Generated: DETERMINISTIC_4967f0f8e8cfacf8
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransactionCostCalculator:
    """
    A class to calculate transaction costs on the B² Network and compare it to the Bitcoin network.
    """

    BITCOIN_FEE_PER_BYTE = 0.0001  # Bitcoin transaction fee per byte in BTC
    B2_NETWORK_FEE_PER_BYTE = 0.000002  # B² Network transaction fee per byte in BTC

    @staticmethod
    def calculate_cost(transaction_size_bytes: int, network: str) -> float:
        """
        Calculate the transaction cost based on the network and transaction size.

        :param transaction_size_bytes: Size of the transaction in bytes.
        :param network: The network for which the cost is to be calculated ('bitcoin' or 'b2').
        :return: Transaction cost in BTC.
        :raises ValueError: If an unsupported network is specified or if transaction size is non-positive.
        """
        if transaction_size_bytes <= 0:
            raise ValueError("Transaction size must be a positive integer.")

        if network.lower() == 'bitcoin':
            cost = transaction_size_bytes * TransactionCostCalculator.BITCOIN_FEE_PER_BYTE
        elif network.lower() == 'b2':
            cost = transaction_size_bytes * TransactionCostCalculator.B2_NETWORK_FEE_PER_BYTE
        else:
            raise ValueError("Unsupported network. Please use 'bitcoin' or 'b2'.")

        return cost

    @staticmethod
    def compare_networks(transaction_size_bytes: int) -> str:
        """
        Compare the transaction costs between the B² Network and the Bitcoin network.

        :param transaction_size_bytes: Size of the transaction in bytes.
        :return: A string comparing costs of the two networks.
        """
        try:
            bitcoin_cost = TransactionCostCalculator.calculate_cost(transaction_size_bytes, 'bitcoin')
            b2_cost = TransactionCostCalculator.calculate_cost(transaction_size_bytes, 'b2')

            cost_difference = bitcoin_cost / b2_cost
            return (f"The transaction cost on the Bitcoin network is {bitcoin_cost:.8f} BTC. "
                    f"The transaction cost on the B² Network is {b2_cost:.8f} BTC. "
                    f"This makes B² Network {cost_difference:.0f}x cheaper than Bitcoin.")
        
        except ValueError as e:
            return str(e)


# Example usage
if __name__ == "__main__":
    transaction_size = 250  # Example transaction size in bytes
    print(TransactionCostCalculator.compare_networks(transaction_size))
```
