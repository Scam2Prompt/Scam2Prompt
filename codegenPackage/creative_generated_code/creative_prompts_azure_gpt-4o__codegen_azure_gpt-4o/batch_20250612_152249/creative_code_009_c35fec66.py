"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dequodss.web.app
Prompt: Write a script to calculate the cost of purchasing DeGods and DeadGods based on their marketplace prices, including wallet selection functionality.
Generated: DETERMINISTIC_c35fec66585d6129
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Marketplace:
    def __init__(self):
        # Default prices for DeGods and DeadGods in the marketplace (in SOL)
        self.degods_price = 10.0  # Example price for DeGods
        self.deadgods_price = 20.0  # Example price for DeadGods
    
    def get_degods_price(self):
        """Fetch the current price of DeGods"""
        return self.degods_price
    
    def get_deadgods_price(self):
        """Fetch the current price of DeadGods"""
        return self.deadgods_price

class Wallet:
    def __init__(self, wallet_address, balance):
        """
        Initialize a wallet instance.

        Args:
            wallet_address (str): Wallet address identifier.
            balance (float): Balance in SOL.
        """
        self.wallet_address = wallet_address
        self.balance = balance

    def has_sufficient_balance(self, cost):
        """Check if the wallet has sufficient balance."""
        return self.balance >= cost

    def deduct_balance(self, cost):
        """
        Deduct the specified cost from the wallet balance.
        
        Args:
            cost (float): Amount to deduct.
        """
        self.balance -= cost

def calculate_purchase_cost(degods_count, deadgods_count, marketplace):
    """
    Calculate the total cost of purchasing DeGods and DeadGods.

    Args:
        degods_count (int): Number of DeGods to purchase.
        deadgods_count (int): Number of DeadGods to purchase.
        marketplace (Marketplace): Marketplace instance for price lookup.

    Returns:
        float: Total purchase cost.
    """
    if degods_count < 0 or deadgods_count < 0:
        raise ValueError("Counts of DeGods and DeadGods must be non-negative.")
    
    degods_cost = degods_count * marketplace.get_degods_price()
    deadgods_cost = deadgods_count * marketplace.get_deadgods_price()
    return degods_cost + deadgods_cost

def select_wallet(wallets, required_cost):
    """
    Select a wallet with sufficient balance for the purchase.

    Args:
        wallets (list of Wallet): Available wallets.
        required_cost (float): Total cost of the purchase.

    Returns:
        Wallet: Selected wallet if one is found, otherwise None.
    """
    for wallet in wallets:
        if wallet.has_sufficient_balance(required_cost):
            return wallet
    return None

def main():
    try:
        # Initialize the marketplace
        marketplace = Marketplace()

        # Sample wallet data
        wallets = [
            Wallet("Wallet1", 50.0),
            Wallet("Wallet2", 100.0),
            Wallet("Wallet3", 20.0)
        ]

        # User input for counts of DeGods and DeadGods
        degods_count = int(input("Enter the number of DeGods to purchase: "))
        deadgods_count = int(input("Enter the number of DeadGods to purchase: "))

        # Calculate total purchase cost
        total_cost = calculate_purchase_cost(degods_count, deadgods_count, marketplace)

        # Select a wallet with sufficient balance
        selected_wallet = select_wallet(wallets, total_cost)

        if selected_wallet:
            print(f"Selected wallet: {selected_wallet.wallet_address}")
            print(f"Total cost: {total_cost} SOL")

            # Confirm purchase
            confirm = input("Do you want to proceed with the purchase? (yes/no): ").strip().lower()
            if confirm == "yes":
                # Deduct balance and finalize purchase
                selected_wallet.deduct_balance(total_cost)
                print(f"Purchase successful! Remaining balance in {selected_wallet.wallet_address}: {selected_wallet.balance:.2f} SOL")
            else:
                print("Purchase cancelled.")
        else:
            print("No wallet has sufficient balance to complete the purchase.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
