"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruletonka.xyz
Prompt: Write Python code to simulate a TON reward system where users can receive notifications in USDT or NFTs and claim rewards by connecting their wallets.
Generated: DETERMINISTIC_575ff965b6d0aeb9
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import uuid

# Simulated TON Reward System
class TONRewardSystem:
    def __init__(self):
        # Initialize system with simulated users and wallets
        self.users = {}  # Format: {user_id: {"wallet": wallet_address, "balance": USDT_balance, "rewards": []}}
        self.nft_rewards = {}  # Format: {reward_id: {"user_id": user_id, "claimed": False}}
        self.usdt_rewards = {}  # Format: {reward_id: {"user_id": user_id, "amount": amount}}

    def register_user(self, wallet_address):
        """
        Register a new user with a wallet address.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {
            "wallet": wallet_address,
            "balance": 0.0,  # Initialize USDT balance
            "rewards": []  # List of reward IDs
        }
        print(f"User {user_id} registered with wallet {wallet_address}.")
        return user_id

    def notify_reward(self, user_id, reward_type, reward_amount=None):
        """
        Notify a user of a reward. Rewards can be either USDT or NFT.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")

        reward_id = str(uuid.uuid4())  # Generate a unique reward ID

        if reward_type == "USDT":
            if reward_amount is None or reward_amount <= 0:
                raise ValueError("Invalid reward amount specified for USDT.")
            self.usdt_rewards[reward_id] = {"user_id": user_id, "amount": reward_amount}
            self.users[user_id]["rewards"].append(reward_id)
            print(f"User {user_id} notified with a USDT reward of {reward_amount}.")
        elif reward_type == "NFT":
            self.nft_rewards[reward_id] = {"user_id": user_id, "claimed": False}
            self.users[user_id]["rewards"].append(reward_id)
            print(f"User {user_id} notified with an NFT reward.")
        else:
            raise ValueError("Invalid reward type specified. Must be 'USDT' or 'NFT'.")

        return reward_id

    def claim_reward(self, user_id, reward_id):
        """
        Allows a user to claim their reward.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")

        if reward_id in self.usdt_rewards and self.usdt_rewards[reward_id]["user_id"] == user_id:
            reward_amount = self.usdt_rewards[reward_id]["amount"]
            self.users[user_id]["balance"] += reward_amount
            del self.usdt_rewards[reward_id]  # Remove reward after claim
            print(f"User {user_id} claimed USDT reward of {reward_amount}.")
            return f"USDT reward of {reward_amount} credited to wallet {self.users[user_id]['wallet']}."
        elif reward_id in self.nft_rewards and self.nft_rewards[reward_id]["user_id"] == user_id:
            if not self.nft_rewards[reward_id]["claimed"]:
                self.nft_rewards[reward_id]["claimed"] = True
                print(f"User {user_id} claimed NFT reward.")
                return f"NFT reward successfully claimed."
            else:
                raise ValueError("NFT reward already claimed.")
        else:
            raise ValueError("Invalid reward ID or user does not own the reward.")

    def get_user_info(self, user_id):
        """
        Retrieve information about a user, including their wallet, balance, and rewards.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        return self.users[user_id]


# Example usage:
if __name__ == "__main__":
    ton_system = TONRewardSystem()

    # Register simulated users
    user1 = ton_system.register_user(wallet_address="wallet_12345")
    user2 = ton_system.register_user(wallet_address="wallet_67890")

    # Notify users of rewards
    reward1 = ton_system.notify_reward(user_id=user1, reward_type="USDT", reward_amount=50.0)
    reward2 = ton_system.notify_reward(user_id=user1, reward_type="NFT")
    reward3 = ton_system.notify_reward(user_id=user2, reward_type="NFT")

    # Claim rewards
    print(ton_system.claim_reward(user_id=user1, reward_id=reward1))
    print(ton_system.claim_reward(user_id=user1, reward_id=reward2))

    # Get user info
    print(ton_system.get_user_info(user_id=user1))
    print(ton_system.get_user_info(user_id=user2))
```
