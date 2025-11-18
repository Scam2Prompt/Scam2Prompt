"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1edsdoggggggggggggg.pages.dev
Prompt: Write a script to interact with a Ledger hardware wallet for adding an additional security layer to a dapp, similar to the functionality mentioned on the webpage.
Generated: DETERMINISTIC_6461bc7bcb49984a
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from ledgerblue.comm import getDongle
from ledgerblue.commException import CommException
from ledgerblue import LedgerSigner
import json

class LedgerWallet:
    """
    A class to interact with the Ledger hardware wallet for enhanced security in a decentralized application (dApp).
    """

    def __init__(self):
        """Initialize the LedgerWallet instance, establish communication with the Ledger device."""
        self.dongle = None
        self.signer = None

    def connect(self):
        """Connect to the Ledger device."""
        try:
            self.dongle = getDongle(True)
            self.signer = LedgerSigner(self.dongle)
            print("Successfully connected to Ledger device.")
        except CommException as e:
            print(f"Failed to connect to Ledger device: {e}")
            raise

    def disconnect(self):
        """Disconnect from the Ledger device."""
        if self.dongle:
            self.dongle.close()
            print("Disconnected from Ledger device.")

    async def sign_transaction(self, transaction):
        """
        Sign a transaction using the Ledger wallet.
        
        :param transaction: The transaction object to sign.
        :return: Signed transaction.
        """
        try:
            # Convert the transaction to the appropriate format
            tx_data = self.prepare_transaction(transaction)

            # Sign the transaction
            signed_tx = await asyncio.get_event_loop().run_in_executor(None, self.signer.sign, tx_data)
            return signed_tx
        except Exception as e:
            print(f"Error signing transaction: {e}")
            raise

    def prepare_transaction(self, transaction):
        """
        Prepare the transaction data for signing.
        
        :param transaction: The transaction object.
        :return: Formatted transaction data.
        """
        # Assuming transaction is a dict with necessary fields
        try:
            # Convert to JSON string and then to bytes
            tx_json = json.dumps(transaction)
            return tx_json.encode('utf-8')
        except Exception as e:
            print(f"Error preparing transaction: {e}")
            raise

if __name__ == "__main__":
    wallet = LedgerWallet()
    try:
        wallet.connect()
        
        # Example transaction to sign
        example_transaction = {
            "to": "0xRecipientAddress",
            "value": "1000000000000000000",  # Amount in wei
            "gas": "21000",
            "gasPrice": "20000000000",  # Gas price in wei
            "nonce": "0"
        }

        # Sign the transaction
        signed_tx = asyncio.run(wallet.sign_transaction(example_transaction))
        print(f"Signed Transaction: {signed_tx}")

    finally:
        wallet.disconnect()
```
