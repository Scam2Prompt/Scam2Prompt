"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Explain how the Buildoors ecosystem works, focusing on minting and earning $BLD.
Generated: DETERMINISTIC_f3a4c9a3a74e9438
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Buildoors Ecosystem Simulation: Minting NFTs and earning $BLD tokens.

This script simulates the Buildoors ecosystem, where users can mint NFTs and earn $BLD tokens.
It includes functionality for:
1. Minting NFTs
2. Earning tokens based on NFT ownership
3. Viewing wallet balances

Language: Python
"""

import random
import time
import sys

# Define constants
MAX_MINT_LIMIT = 10  # Maximum NFTs a user can mint in one transaction
INITIAL_BLD_BALANCE = 0  # Initial $BLD balance for every new account
MINT_COST = 50  # Cost to mint an NFT in $BLD
EARNING_RATE = 10  # $BLD earned per NFT per day

# Error classes
class InsufficientBalanceError(Exception):
    """Raised when the user doesn't have enough balance to mint NFTs."""
    pass

class MintLimitExceededError(Exception):
    """Raised when the user tries to mint more than the allowed limit."""
    pass

# Wallet class to manage user's NFTs and $BLD tokens
class Wallet:
    def __init__(self):
        self.balance_bld = INITIAL_BLD_BALANCE  # User's $BLD balance
        self.nfts = []  # List of user's NFTs

    def mint_nft(self, count=1):
        """
        Mint NFTs for the user.
        :param count: Number of NFTs to mint.
        :raises InsufficientBalanceError: If user lacks $BLD for minting.
        :raises MintLimitExceededError: If user tries to mint too many NFTs in one go.
        """
        if count > MAX_MINT_LIMIT:
            raise MintLimitExceededError(
                f"Cannot mint more than {MAX_MINT_LIMIT} NFTs at once."
            )
        total_cost = count * MINT_COST
        if self.balance_bld < total_cost:
            raise InsufficientBalanceError(
                f"Insufficient $BLD balance. You need {total_cost} $BLD but have {self.balance_bld}."
            )
        self.balance_bld -= total_cost
        for _ in range(count):
            nft_id = self._generate_nft_id()
            self.nfts.append(nft_id)
        print(f"Successfully minted {count} NFT(s). Current NFTs: {self.nfts}")

    def earn_bld(self):
        """
        Earn $BLD based on the number of NFTs owned.
        """
        earned_bld = len(self.nfts) * EARNING_RATE
        self.balance_bld += earned_bld
        print(
            f"Earned {earned_bld} $BLD from owning {len(self.nfts)} NFT(s). Current balance: {self.balance_bld}"
        )

    def view_wallet(self):
        """
        View the current wallet details (NFTs and $BLD balance).
        """
        print(f"NFTs: {self.nfts}")
        print(f"$BLD Balance: {self.balance_bld}")

    def _generate_nft_id(self):
        """Generate a unique NFT ID."""
        return f"NFT-{random.randint(1000, 9999)}"

# Main application
def main():
    print("Welcome to the Buildoors Ecosystem!")
    wallet = Wallet()

    while True:
        print("\nMenu:")
        print("1. View Wallet")
        print("2. Mint NFTs")
        print("3. Earn $BLD Tokens")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1-4.")
            continue

        if choice == 1:
            wallet.view_wallet()
        elif choice == 2:
            try:
                count = int(input(f"How many NFTs would you like to mint (max {MAX_MINT_LIMIT})? "))
                wallet.mint_nft(count)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except (InsufficientBalanceError, MintLimitExceededError) as e:
                print(f"Error: {e}")
        elif choice == 3:
            wallet.earn_bld()
        elif choice == 4:
            print("Thank you for using the Buildoors Ecosystem. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Entry point
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication interrupted. Exiting...")
        sys.exit(0)
```
