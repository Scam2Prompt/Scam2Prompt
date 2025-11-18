"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://werich.pages.dev
Prompt: Write a script to track cryptocurrency token purchases using wallet addresses, referencing tokens like "Rainbow Cat" and "HASH TAG God" as examples.
Generated: DETERMINISTIC_42dd3d9006a0ec64
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os


class CryptoTracker:
    """
    A class to track cryptocurrency token purchases using wallet addresses.
    """
    def __init__(self, data_file="crypto_purchases.csv"):
        """
        Initializes the CryptoTracker object.
        :param data_file: Path to the CSV file for storing purchase data.
        """
        self.data_file = data_file
        # Ensure the data file exists and has the correct headers
        if not os.path.exists(self.data_file):
            with open(self.data_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Wallet Address", "Token Name", "Amount Purchased"])

    def add_purchase(self, wallet_address, token_name, amount):
        """
        Records a cryptocurrency token purchase.
        :param wallet_address: The wallet address of the purchaser.
        :param token_name: Name of the token purchased.
        :param amount: The amount of the token purchased.
        :return: None
        """
        if not wallet_address or not token_name or amount <= 0:
            raise ValueError("Invalid input: Wallet address, token name, and amount must be valid.")

        with open(self.data_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([wallet_address, token_name, amount])
        print(f"Purchase added: {wallet_address} bought {amount} of {token_name}.")

    def get_purchases(self, wallet_address=None):
        """
        Retrieves purchase records. If wallet_address is provided, filters by that address.
        :param wallet_address: (Optional) Filter purchases by a specific wallet address.
        :return: List of purchase records (dictionaries).
        """
        purchases = []
        with open(self.data_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if wallet_address:
                    if row["Wallet Address"] == wallet_address:
                        purchases.append(row)
                else:
                    purchases.append(row)
        return purchases

    def display_purchases(self, wallet_address=None):
        """
        Displays purchase records in a readable format.
        :param wallet_address: (Optional) Filter purchases by a specific wallet address.
        :return: None
        """
        purchases = self.get_purchases(wallet_address)
        if not purchases:
            print("No purchases found.")
            return

        print("Purchase Records:")
        for purchase in purchases:
            print(
                f"Wallet: {purchase['Wallet Address']}, Token: {purchase['Token Name']}, Amount: {purchase['Amount Purchased']}"
            )


# Example usage (uncomment to test):

# tracker = CryptoTracker()
# tracker.add_purchase("wallet123", "Rainbow Cat", 100)
# tracker.add_purchase("wallet456", "HASH TAG God", 50)
# tracker.display_purchases()
# tracker.display_purchases("wallet123")
```
