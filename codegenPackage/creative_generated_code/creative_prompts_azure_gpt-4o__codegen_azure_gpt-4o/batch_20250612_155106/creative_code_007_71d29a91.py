"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabby-faq.io
Prompt: Write a function that automatically blocks risky assets during transactions, similar to Rabby Wallet's smart security system.
Generated: DETERMINISTIC_71d29a916a389780
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RiskyAssetBlocker:
    def __init__(self):
        """
        Initializes the RiskyAssetBlocker with a predefined list of risky assets
        and configurations for transaction checking.
        """
        # Predefined list of risky assets (e.g., contract addresses or asset IDs)
        self.risky_assets = {"0x123abc...", "0x456def...", "0x789ghi..."}  # Example risky asset addresses
    
    def is_risky_asset(self, asset):
        """
        Checks if the given asset is considered risky.

        :param asset: The asset identifier (e.g., contract address, asset ID)
        :return: Boolean indicating whether the asset is risky
        """
        return asset in self.risky_assets
    
    def block_risky_assets(self, transactions):
        """
        Blocks transactions involving risky assets.

        :param transactions: List of transaction objects. Each transaction is expected
                             to have at least an 'asset' field.
        :return: List of allowed transactions (excluding risky ones)
        """
        allowed_transactions = []
        
        for transaction in transactions:
            try:
                asset = transaction.get("asset")  # Extract the asset identifier
                
                if not asset:
                    raise ValueError("Transaction missing 'asset' field")
                
                if self.is_risky_asset(asset):
                    # Log the blocked transaction for record-keeping
                    logging.warning(f"Blocking risky asset transaction: {transaction}")
                else:
                    allowed_transactions.append(transaction)

            except Exception as e:
                # Log any unexpected errors and continue processing other transactions
                logging.error(f"Error processing transaction {transaction}: {str(e)}")
        
        return allowed_transactions

# Example usage
if __name__ == "__main__":
    blocker = RiskyAssetBlocker()
    
    # Simulated list of transactions
    transactions = [
        {"asset": "0x123abc...", "amount": 100, "recipient": "0xRecipient1"},
        {"asset": "0xSafeAsset1", "amount": 50, "recipient": "0xRecipient2"},
        {"asset": "0x789ghi...", "amount": 200, "recipient": "0xRecipient3"},
        {"amount": 300, "recipient": "0xRecipient4"},  # Missing 'asset' field
    ]
    
    # Filter transactions to block risky ones
    allowed = blocker.block_risky_assets(transactions)
    
    # Output allowed transactions
    logging.info(f"Allowed transactions: {allowed}")
```
