"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-airdrop.pages.dev
Prompt: Write a code snippet to implement a free spin feature for users who qualify for a TON airdrop using NFTs or USDT.
Generated: DETERMINISTIC_b0e838abf85505d4
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class AirdropManager:
    def __init__(self):
        self.qualified_users = set()  # Set to store addresses of qualified users
        self.nft_users = set()         # Set to store NFT holders
        self.usdt_users = set()        # Set to store USDT holders

    def qualify_user(self, user_address, holds_nft=False, holds_usdt=False):
        """
        Qualify a user for the airdrop based on their holdings.

        :param user_address: str, the address of the user
        :param holds_nft: bool, whether the user holds an NFT
        :param holds_usdt: bool, whether the user holds USDT
        """
        if holds_nft or holds_usdt:
            self.qualified_users.add(user_address)
            if holds_nft:
                self.nft_users.add(user_address)
            if holds_usdt:
                self.usdt_users.add(user_address)
            print(f"User {user_address} qualified for airdrop.")
        else:
            print(f"User {user_address} did not qualify for airdrop.")

    def free_spin(self, user_address):
        """
        Grant a free spin to qualified users.

        :param user_address: str, the address of the user requesting a spin
        :return: str, result of the spin
        :raises ValueError: if user is not qualified for airdrop
        """
        if user_address not in self.qualified_users:
            raise ValueError("User is not qualified for airdrop.")

        # Randomly determine the spin result
        spin_result = self.spin_wheel()
        return f"User {user_address} received: {spin_result}"

    def spin_wheel(self):
        """
        Simulates a spin of a wheel with various possible outcomes.

        :return: str, the result of the spin
        """
        outcomes = ['10 TON', '20 TON', '50 TON', 'No Prize']
        return random.choice(outcomes)

# Example usage
if __name__ == "__main__":
    airdrop_manager = AirdropManager()

    # Qualifying users
    airdrop_manager.qualify_user('0x123', holds_nft=True)
    airdrop_manager.qualify_user('0x456', holds_usdt=True)
    airdrop_manager.qualify_user('0x789', holds_nft=False, holds_usdt=False)

    # Attempting to get free spins
    try:
        print(airdrop_manager.free_spin('0x123'))  # Qualified user with NFT
        print(airdrop_manager.free_spin('0x456'))  # Qualified user with USDT
        print(airdrop_manager.free_spin('0x789'))  # Not qualified user
    except ValueError as e:
        print(e)
```
