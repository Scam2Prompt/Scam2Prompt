"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmnt.org
Prompt: Provide a code example for setting up a marketplace that accepts GMNT Coin as a payment method, including transaction confirmation.
Generated: DETERMINISTIC_9bd2a93ad01ff154
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import uuid

class GMNTCoinWallet:
    def __init__(self, address, private_key):
        """
        Initialize a GMNTCoin wallet.
        :param address: The wallet address.
        :param private_key: The private key associated with the wallet.
        """
        self.address = address
        self.private_key = private_key

    def send_payment(self, recipient_address, amount):
        """
        Simulates sending GMNT Coin to a recipient.
        :param recipient_address: Address of the recipient.
        :param amount: Amount to send.
        :returns: A transaction ID if successful.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if not recipient_address:
            raise ValueError("Recipient address cannot be empty.")

        # Simulated transaction creation (in production, integrate with GMNT API)
        transaction_id = str(uuid.uuid4())
        print(f"Transaction created: {transaction_id}")
        print(f"Sending {amount} GMNT Coin to {recipient_address} from {self.address}...")
        
        # Simulate a delay for transaction processing
        time.sleep(2)
        
        # Simulated transaction success
        print("Transaction processed successfully.")
        return transaction_id

class Marketplace:
    def __init__(self, wallet):
        """
        Initialize the marketplace.
        :param wallet: GMNTCoinWallet instance for handling transactions.
        """
        self.wallet = wallet
        self.products = {}

    def add_product(self, product_id, product_name, price):
        """
        Add a product to the marketplace.
        :param product_id: Unique identifier for the product.
        :param product_name: Name of the product.
        :param price: Price of the product in GMNT Coin.
        """
        if product_id in self.products:
            raise ValueError("Product ID already exists.")
        self.products[product_id] = {
            "name": product_name,
            "price": price
        }
        print(f"Product added: {product_name} (ID: {product_id}, Price: {price} GMNT)")

    def purchase_product(self, product_id, buyer_address):
        """
        Handle the purchase of a product.
        :param product_id: ID of the product being purchased.
        :param buyer_address: GMNT Coin wallet address of the buyer.
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found.")

        product = self.products[product_id]
        price = product["price"]
        print(f"Processing purchase for product '{product['name']}' (Price: {price} GMNT)...")

        # Process payment via GMNTCoinWallet
        try:
            transaction_id = self.wallet.send_payment(buyer_address, price)
            print(f"Purchase successful! Transaction ID: {transaction_id}")
        except Exception as e:
            print(f"Error processing payment: {e}")

# Example usage
if __name__ == "__main__":
    # Simulated seller wallet details
    seller_wallet = GMNTCoinWallet(address="seller_wallet_address", private_key="seller_private_key")

    # Initialize the marketplace
    marketplace = Marketplace(wallet=seller_wallet)

    # Add products to the marketplace
    marketplace.add_product(product_id="001", product_name="Digital Art", price=10)
    marketplace.add_product(product_id="002", product_name="eBook", price=5)

    # Simulate a buyer purchasing a product
    buyer_wallet_address = "buyer_wallet_address"
    marketplace.purchase_product(product_id="001", buyer_address=buyer_wallet_address)
```
