"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-community.web.app
Prompt: How can I implement a minting function for a Mystery Box NFT that rewards users between $50 and $30,000?
Generated: DETERMINISTIC_21aa5f75d6734285
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MysteryBoxNFT:
    """
    A class to represent a Mystery Box NFT that rewards users with a value between $50 and $30,000.
    """

    def __init__(self):
        """
        Initializes the MysteryBoxNFT instance.
        """
        self.reward_range = (50, 30000)  # Minimum and maximum reward values

    def mint(self, user_id):
        """
        Mints a new Mystery Box NFT for the user and assigns a random reward value.

        Parameters:
        user_id (str): The unique identifier for the user minting the NFT.

        Returns:
        dict: A dictionary containing the user_id and the assigned reward value.
        """
        if not isinstance(user_id, str) or not user_id.strip():
            raise ValueError("Invalid user_id. It must be a non-empty string.")

        # Generate a random reward within the defined range
        reward_value = self.generate_reward()

        # Record the minted NFT (for demonstration, we simply return the data)
        nft_data = {
            'user_id': user_id,
            'reward_value': reward_value
        }

        return nft_data

    def generate_reward(self):
        """
        Generates a random reward value between the defined reward range.

        Returns:
        int: A randomly generated reward value.
        """
        return random.randint(self.reward_range[0], self.reward_range[1])

# Example Usage
if __name__ == "__main__":
    try:
        nft = MysteryBoxNFT()
        user_id = "user123"  # Example user ID
        minted_nft = nft.mint(user_id)
        print("Minted NFT:", minted_nft)
    except ValueError as e:
        print("Error during minting:", e)
```
