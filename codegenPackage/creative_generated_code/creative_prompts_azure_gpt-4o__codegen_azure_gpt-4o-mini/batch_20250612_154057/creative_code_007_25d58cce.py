"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mycoinbase.rscorp.com.br
Prompt: Write code to display a warning message if a user attempts to transfer funds without backing up their recovery phrase, based on the Coinbase Wallet setup process.
Generated: DETERMINISTIC_25d58cce930497f6
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Wallet:
    def __init__(self):
        """Initialize the wallet with a backup status."""
        self.has_backup = False

    def set_backup(self, status: bool):
        """Set the backup status of the wallet.
        
        Args:
            status (bool): Indicates if the recovery phrase is backed up or not.
        """
        self.has_backup = status

    def transfer_funds(self, amount: float):
        """Attempt to transfer funds. Warns if recovery phrase is not backed up.
        
        Args:
            amount (float): The amount of funds to transfer.
        
        Raises:
            ValueError: If the transfer amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")

        # Check if the recovery phrase is backed up
        if not self.has_backup:
            self.warn_user()

        # Proceed with the transfer (pseudo-code)
        # self.perform_transfer(amount)
        print(f"Transferring {amount} units of currency...")

    def warn_user(self):
        """Display a warning message to the user about the recovery phrase backup."""
        print("WARNING: You are about to transfer funds without backing up your recovery phrase. "
              "Please ensure you have a backup before proceeding.")

# Example usage
if __name__ == "__main__":
    wallet = Wallet()
    
    # Uncomment the following line to simulate backing up the recovery phrase
    # wallet.set_backup(True)

    try:
        wallet.transfer_funds(100)  # Attempt to transfer funds
    except ValueError as e:
        print(f"Error: {e}")
```
