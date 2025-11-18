"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xmr.cz
Prompt: Create a Python script to interact with Monero's CLI wallet and send a transaction using the `Feather Wallet`.
Generated: DETERMINISTIC_5832ff8eb6e864dd
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import json
import sys
import os

class MoneroWallet:
    def __init__(self, wallet_path, wallet_password):
        """
        Initialize the Monero wallet instance.

        :param wallet_path: Path to the Monero wallet file.
        :param wallet_password: Password for the wallet.
        """
        self.wallet_path = wallet_path
        self.wallet_password = wallet_password
        self.wallet_cli = 'monero-wallet-cli'
        self.wallet_process = None

    def start_wallet(self):
        """Start the Monero wallet CLI."""
        try:
            self.wallet_process = subprocess.Popen(
                [self.wallet_cli, '--wallet-file', self.wallet_path, '--password', self.wallet_password],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            print("Wallet started successfully.")
        except Exception as e:
            print("Error starting wallet:", e)
            sys.exit(1)

    def send_transaction(self, address, amount, tx_fee=0):
        """
        Send a transaction from the wallet.

        :param address: The recipient's Monero address.
        :param amount: The amount of Monero to send.
        :param tx_fee: Transaction fee (optional).
        """
        try:
            command = f"transfer {address} {amount} {tx_fee}\n"
            self.wallet_process.stdin.write(command)
            self.wallet_process.stdin.flush()

            # Read the output from the wallet process
            output = self.wallet_process.stdout.readline()
            print("Transaction output:", output.strip())

        except Exception as e:
            print("Error sending transaction:", e)
            self.cleanup()
            sys.exit(1)

    def cleanup(self):
        """Clean up the wallet process."""
        if self.wallet_process:
            self.wallet_process.terminate()
            self.wallet_process.wait()
            print("Wallet process terminated.")

    def close_wallet(self):
        """Close the Monero wallet CLI."""
        self.cleanup()
        print("Wallet closed successfully.")

if __name__ == "__main__":
    # Example usage
    wallet_path = "your_wallet_path"  # Replace with your wallet path
    wallet_password = "your_wallet_password"  # Replace with your wallet password

    monero_wallet = MoneroWallet(wallet_path, wallet_password)
    monero_wallet.start_wallet()

    # Replace with actual address and amount
    recipient_address = "recipient_monero_address"  # Replace with recipient's address
    amount_to_send = 0.1  # Amount of Monero to send

    monero_wallet.send_transaction(recipient_address, amount_to_send)
    monero_wallet.close_wallet()
```

**Note:** This code assumes that the `monero-wallet-cli` command-line tool is installed and accessible in your environment. Adjust the `wallet_path`, `wallet_password`, and `recipient_address` in the example usage section accordingly.
