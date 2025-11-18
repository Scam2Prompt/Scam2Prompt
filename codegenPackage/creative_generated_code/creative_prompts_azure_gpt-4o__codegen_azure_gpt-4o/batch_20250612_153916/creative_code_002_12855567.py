"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominings.net
Prompt: Create a script in Python that simulates the purchase and resale of digital miners on a marketplace, factoring in GoMining's 5% service charge and miner performance metrics.
Generated: DETERMINISTIC_12855567b48af7ef
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class Miner:
    """
    Represents a digital miner with unique properties for performance and resale.
    """
    def __init__(self, name, base_price, hash_rate, performance_factor=1.0):
        """
        Initializes a Miner instance.

        :param name: Name of the miner.
        :param base_price: Base price (initial purchase cost) of the miner.
        :param hash_rate: Hash rate representing the miner's computing power.
        :param performance_factor: Factor indicating miner's performance (default is 1.0).
        """
        self.id = str(uuid.uuid4())  # Unique ID for the miner
        self.name = name
        self.base_price = base_price
        self.hash_rate = hash_rate
        self.performance_factor = performance_factor

    def resale_price(self):
        """
        Calculates the resale price of the miner based on its performance.

        :return: Resale price (base price * performance factor).
        """
        return self.base_price * self.performance_factor


class Marketplace:
    """
    Represents the marketplace where miners can be bought, sold, and managed.
    """
    SERVICE_CHARGE_RATE = 0.05  # 5% service charge

    def __init__(self):
        """
        Initializes a Marketplace instance.
        """
        self.miners_for_sale = []  # List of miners available for sale
        self.transactions = []    # List of completed transactions

    def add_miner(self, miner):
        """
        Adds a miner to the marketplace for sale.

        :param miner: Miner object to add to the marketplace.
        """
        self.miners_for_sale.append(miner)

    def purchase_miner(self, miner_id, buyer_name):
        """
        Simulates the purchase of a miner.

        :param miner_id: Unique ID of the miner to purchase.
        :param buyer_name: Name of the buyer.
        :return: Success message or error.
        """
        for miner in self.miners_for_sale:
            if miner.id == miner_id:
                price = miner.resale_price()
                service_charge = price * self.SERVICE_CHARGE_RATE
                total_price = price + service_charge

                # Record transaction details
                self.transactions.append({
                    'miner_id': miner.id,
                    'miner_name': miner.name,
                    'buyer_name': buyer_name,
                    'price': price,
                    'service_charge': service_charge,
                    'total_price': total_price
                })

                # Remove miner from marketplace after purchase
                self.miners_for_sale.remove(miner)

                return f"{buyer_name} successfully purchased {miner.name} for {total_price:.2f} (includes service charge of {service_charge:.2f})."

        return "Error: Miner not found in the marketplace."

    def list_miners(self):
        """
        Lists all miners currently available for sale.

        :return: List of miners.
        """
        if not self.miners_for_sale:
            return "No miners available for sale."

        return "\n".join([f"ID: {miner.id}, Name: {miner.name}, Resale Price: {miner.resale_price():.2f}" for miner in self.miners_for_sale])

    def list_transactions(self):
        """
        Lists all completed transactions.

        :return: List of transactions.
        """
        if not self.transactions:
            return "No transactions completed yet."

        result = []
        for transaction in self.transactions:
            result.append(
                f"Buyer: {transaction['buyer_name']}, Miner: {transaction['miner_name']} "
                f"(ID: {transaction['miner_id']}), Price: {transaction['price']:.2f}, "
                f"Service Charge: {transaction['service_charge']:.2f}, Total Price: {transaction['total_price']:.2f}"
            )
        return "\n".join(result)


# Script execution
if __name__ == "__main__":
    # Initialize marketplace
    marketplace = Marketplace()

    # Create and add miners to marketplace
    miner1 = Miner(name="Miner-A", base_price=500, hash_rate=100, performance_factor=1.2)
    miner2 = Miner(name="Miner-B", base_price=800, hash_rate=200, performance_factor=1.1)
    miner3 = Miner(name="Miner-C", base_price=300, hash_rate=50, performance_factor=0.9)

    marketplace.add_miner(miner1)
    marketplace.add_miner(miner2)
    marketplace.add_miner(miner3)

    # Display available miners
    print("Available Miners:")
    print(marketplace.list_miners())

    # Simulate purchase of a miner
    print("\nPurchasing Miner:")
    response = marketplace.purchase_miner(miner_id=miner1.id, buyer_name="Alice")
    print(response)

    # Display available miners after purchase
    print("\nAvailable Miners After Purchase:")
    print(marketplace.list_miners())

    # Display transaction history
    print("\nTransaction History:")
    print(marketplace.list_transactions())
```
