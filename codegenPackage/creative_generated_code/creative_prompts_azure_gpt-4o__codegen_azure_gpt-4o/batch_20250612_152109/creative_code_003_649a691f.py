"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcandle404-en.web.app
Prompt: Generate code to implement a referral bonus system for the God Candle project, where users can earn rewards for referring others to purchase NFTs or claim tokens.
Generated: DETERMINISTIC_649a691f32e26068
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class ReferralBonusSystem:
    """
    Referral Bonus System for the God Candle project.
    Users earn rewards for referring others to purchase NFTs or claim tokens.
    """

    def __init__(self):
        """
        Initializes the referral bonus system with empty user and rewards data.
        """
        self.users = {}  # Dictionary to store user data: {user_id: {referrals: [], rewards: float}}
        self.referrals = {}  # Dictionary to track referral relationships: {referral_code: referrer_id}

    def create_user(self, name):
        """
        Creates a new user with a unique referral code.

        Args:
        - name (str): Name of the user.

        Returns:
        - dict: User information including the referral code.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        referral_code = str(uuid.uuid4())[:8]  # Generate a short unique referral code
        self.users[user_id] = {'name': name, 'referrals': [], 'rewards': 0.0}
        self.referrals[referral_code] = user_id
        return {'user_id': user_id, 'name': name, 'referral_code': referral_code}

    def process_referral(self, referral_code, nft_purchased=False, tokens_claimed=0):
        """
        Processes a referral when a referred user purchases NFTs or claims tokens.

        Args:
        - referral_code (str): Referral code of the referrer.
        - nft_purchased (bool): Whether the referred user purchased NFTs (default: False).
        - tokens_claimed (float): Number of tokens claimed by the referred user (default: 0).

        Returns:
        - str: Success message or error message.
        """
        referrer_id = self.referrals.get(referral_code)
        if not referrer_id:
            return "Invalid referral code."

        try:
            reward = 0.0
            if nft_purchased:
                reward += 10.0  # Flat reward for NFT purchase
            reward += tokens_claimed * 0.05  # Token-based reward (5% of claimed tokens)

            # Update referrer's data
            self.users[referrer_id]['referrals'].append({'nft_purchased': nft_purchased, 'tokens_claimed': tokens_claimed})
            self.users[referrer_id]['rewards'] += reward

            return f"Referral processed successfully. Reward added: {reward:.2f} units."
        except Exception as e:
            return f"Error processing referral: {str(e)}"

    def get_user_info(self, user_id):
        """
        Retrieves user information including their referrals and rewards.

        Args:
        - user_id (str): Unique ID of the user.

        Returns:
        - dict: User data including referrals and rewards, or an error message.
        """
        user_info = self.users.get(user_id)
        if not user_info:
            return {"error": "User not found."}
        return user_info

    def get_stats(self):
        """
        Retrieves statistics of the referral bonus system.

        Returns:
        - dict: Aggregated statistics including total users, total referrals, and total rewards distributed.
        """
        total_users = len(self.users)
        total_referrals = sum(len(user['referrals']) for user in self.users.values())
        total_rewards = sum(user['rewards'] for user in self.users.values())
        return {
            "total_users": total_users,
            "total_referrals": total_referrals,
            "total_rewards_distributed": total_rewards
        }


# Example usage (this would typically be replaced with actual application logic)
if __name__ == '__main__':
    system = ReferralBonusSystem()

    # Create users
    user1 = system.create_user("Alice")
    user2 = system.create_user("Bob")

    # Process referrals
    print(system.process_referral(user1['referral_code'], nft_purchased=True))
    print(system.process_referral(user1['referral_code'], tokens_claimed=100))

    # Get user info
    print(system.get_user_info(user1['user_id']))

    # Get system stats
    print(system.get_stats())
```
