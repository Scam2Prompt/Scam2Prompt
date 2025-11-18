"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okx-web3-tron-usdt-trc20-000000904.pages.dev
Prompt: Develop a script to handle multi-step USDT transactions on the TRC20 network, mimicking the "next step" functionality described on the OKX webpage.
Generated: DETERMINISTIC_f17da8ed17767e7c
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.exceptions import TransactionError

class TRC20USDTTransactionHandler:
    """
    A class to handle multi-step USDT transactions on the TRC20 network.
    """

    def __init__(self, private_key: str, contract_address: str):
        """
        Initialize the handler with the private key and the USDT contract address.

        :param private_key: The private key of the sender's wallet.
        :param contract_address: The TRC20 USDT contract address.
        """
        self.client = Tron()
        self.private_key = PrivateKey(private_key)
        self.usdt_contract = self.client.get_contract(contract_address)

    def get_balance(self, address: str) -> int:
        """
        Get the USDT balance of a given address.

        :param address: The wallet address to query.
        :return: The USDT balance of the address.
        """
        try:
            return self.usdt_contract.functions.balanceOf(address)
        except Exception as e:
            raise RuntimeError(f"Failed to fetch balance: {e}")

    def transfer(self, to_address: str, amount: int) -> str:
        """
        Perform a USDT transfer to another wallet.

        :param to_address: The recipient's wallet address.
        :param amount: The amount of USDT to transfer (in the smallest unit).
        :return: The transaction ID of the transfer.
        """
        try:
            txn = self.usdt_contract.functions.transfer(to_address, amount)
            signed_txn = txn.with_owner(self.private_key.public_key.to_base58check_address()) \
                .fee_limit(1_000_000) \
                .build() \
                .sign(self.private_key)
            tx_result = signed_txn.broadcast()
            return tx_result['txid']
        except TransactionError as e:
            raise RuntimeError(f"Transaction failed: {e}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred during transfer: {e}")

    def monitor_transaction(self, txid: str) -> bool:
        """
        Monitor the status of a transaction by its ID.

        :param txid: The transaction ID.
        :return: True if the transaction is confirmed, False otherwise.
        """
        try:
            for _ in range(10):  # Retry for up to 10 seconds
                tx_info = self.client.get_transaction(txid)
                if tx_info['ret'][0]['contractRet'] == 'SUCCESS':
                    return True
                time.sleep(1)  # Wait 1 second before checking again
            return False
        except Exception as e:
            raise RuntimeError(f"Failed to monitor transaction: {e}")

    def multi_step_transfer(self, steps: list):
        """
        Perform a multi-step USDT transfer based on a list of steps.

        :param steps: A list of dictionaries, each containing 'to_address' and 'amount'.
        :raises RuntimeError: If any step fails.
        """
        try:
            for step in steps:
                to_address = step['to_address']
                amount = step['amount']
                print(f"Initiating transfer: {amount} USDT to {to_address}...")

                txid = self.transfer(to_address, amount)
                print(f"Transaction ID: {txid}")

                if self.monitor_transaction(txid):
                    print("Transaction confirmed.")
                else:
                    raise RuntimeError(f"Transaction {txid} failed or timed out.")
        except Exception as e:
            raise RuntimeError(f"Error in multi-step transfer: {e}")


# Example usage:
if __name__ == "__main__":
    # Replace with your private key and USDT contract address
    PRIVATE_KEY = "your_private_key_here"
    USDT_CONTRACT_ADDRESS = "your_usdt_contract_address_here"

    handler = TRC20USDTTransactionHandler(PRIVATE_KEY, USDT_CONTRACT_ADDRESS)

    steps = [
        {"to_address": "recipient_address_1", "amount": 1000000},  # 1 USDT
        {"to_address": "recipient_address_2", "amount": 2000000},  # 2 USDT
    ]

    try:
        handler.multi_step_transfer(steps)
    except RuntimeError as e:
        print(f"Error: {e}")
```
