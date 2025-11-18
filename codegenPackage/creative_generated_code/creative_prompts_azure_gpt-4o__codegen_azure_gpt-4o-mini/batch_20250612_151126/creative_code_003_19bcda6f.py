"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-core.com
Prompt: Write a script that checks the balance of a wallet using the Wallet-Core Devtool Console and handles errors like "Unable to display balance."
Generated: DETERMINISTIC_19bcda6f17e5381f
Batch ID: 20250612_151126
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

class WalletBalanceChecker:
    def __init__(self, wallet_address):
        """
        Initializes the WalletBalanceChecker with the given wallet address.

        :param wallet_address: str - The address of the wallet to check.
        """
        self.wallet_address = wallet_address
        self.devtool_command = "path/to/wallet-core-devtool"  # Update with the actual path to Wallet-Core Devtool

    def check_balance(self):
        """
        Checks the balance of the specified wallet address using the Wallet-Core Devtool Console.
        
        :return: float - The balance of the wallet.
        :raises RuntimeError: If the command fails or returns an error message.
        """
        try:
            # Construct the command to check balance
            command = [self.devtool_command, "get_balance", self.wallet_address]

            # Execute the command and capture the output
            result = subprocess.run(command, capture_output=True, text=True, check=True)

            # Parse the balance from the command output
            balance_info = json.loads(result.stdout)
            balance = balance_info.get('balance')

            if balance is None:
                raise RuntimeError("Unable to display balance.")

            return balance

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Command '{' '.join(command)}' failed with error: {e.stderr.strip()}")
        except json.JSONDecodeError:
            raise RuntimeError("Failed to decode JSON response from the wallet devtool.")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {str(e)}")

def main():
    # Example wallet address (update with a real address)
    wallet_address = "your_wallet_address_here"

    balance_checker = WalletBalanceChecker(wallet_address)

    try:
        balance = balance_checker.check_balance()
        print(f"The balance of the wallet '{wallet_address}' is: {balance}")
    except RuntimeError as e:
        print(f"Error checking balance: {e}")

if __name__ == "__main__":
    main()
```
