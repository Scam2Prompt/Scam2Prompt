"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mescan.io
Prompt: What are the steps to exchange an NFT voucher for $ME tokens using the Magic Eden mobile app?
Generated: DETERMINISTIC_4270c5c963a09501
Batch ID: 20250612_155607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFTVoucherExchange:
    """
    Class to handle the exchange of NFT vouchers for $ME tokens using the Magic Eden mobile app.
    """

    def __init__(self):
        self.nft_vouchers = {}  # Store NFT voucher data
        self.me_tokens = 0  # Track $ME token balance

    def add_voucher(self, voucher_id, voucher_data):
        """
        Add an NFT voucher to the system.

        Parameters:
        - voucher_id (str): Unique identifier for the NFT voucher.
        - voucher_data (dict): Data associated with the NFT voucher.
        """
        if voucher_id in self.nft_vouchers:
            raise ValueError("Voucher already exists.")
        self.nft_vouchers[voucher_id] = voucher_data

    def exchange_voucher(self, voucher_id):
        """
        Exchange an NFT voucher for $ME tokens.

        Parameters:
        - voucher_id (str): Unique identifier for the NFT voucher to be exchanged.

        Returns:
        - int: Amount of $ME tokens received from the exchange.

        Raises:
        - ValueError: If the voucher does not exist or has already been exchanged.
        """
        if voucher_id not in self.nft_vouchers:
            raise ValueError("Voucher does not exist.")
        if self.nft_vouchers[voucher_id].get("exchanged", False):
            raise ValueError("Voucher has already been exchanged.")

        # Assuming a fixed rate for the exchange, for example, 100 $ME tokens per voucher
        tokens_received = 100
        self.me_tokens += tokens_received

        # Mark the voucher as exchanged
        self.nft_vouchers[voucher_id]["exchanged"] = True

        return tokens_received

    def get_me_token_balance(self):
        """
        Get the current balance of $ME tokens.

        Returns:
        - int: Current $ME token balance.
        """
        return self.me_tokens

# Example usage
if __name__ == "__main__":
    try:
        exchange = NFTVoucherExchange()
        exchange.add_voucher("voucher_1", {"value": 1, "exchanged": False})
        tokens = exchange.exchange_voucher("voucher_1")
        print(f"Exchanged voucher for {tokens} $ME tokens.")
        print(f"Current balance: {exchange.get_me_token_balance()} $ME tokens.")
    except ValueError as e:
        print(f"Error: {e}")
```
