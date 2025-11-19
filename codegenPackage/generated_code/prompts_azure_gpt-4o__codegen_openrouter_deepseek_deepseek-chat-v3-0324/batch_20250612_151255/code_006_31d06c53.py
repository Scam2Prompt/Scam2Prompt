"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Provide an example of a marketing campaign strategy for launching a crypto token like WienerAI, emphasizing community rewards and staking incentives.
Generated: DETERMINISTIC_31d06c53ff110b0f
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crypto_campaign.py
# Example marketing campaign strategy for launching a crypto token like WienerAI
# Includes community rewards and staking incentives components

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random

class MarketingCampaign:
    """
    A class representing a marketing campaign for a crypto token launch.
    Handles community rewards and staking incentives strategies.
    """
    
    def __init__(self, token_name: str, total_supply: int):
        """
        Initialize the marketing campaign.
        
        Args:
            token_name (str): Name of the crypto token
            total_supply (int): Total token supply for distribution
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.community_rewards_pool = int(total_supply * 0.25)  # 25% for community rewards
        self.staking_pool = int(total_supply * 0.15)  # 15% for staking rewards
        self.campaign_start = datetime.now()
        self.campaign_end = self.campaign_start + timedelta(days=90)  # 90-day campaign
        self.participants = {}  # wallet_address: participant_data
        self.stakers = {}  # wallet_address: staking_data
        
    def add_participant(self, wallet_address: str, social_media_actions: Dict[str, int]) -> bool:
        """
        Add a participant to the community rewards program.
        
        Args:
            wallet_address (str): Participant's wallet address
            social_media_actions (Dict[str, int]): Dictionary of social media actions and counts
                                                  e.g. {"twitter_shares": 5, "telegram_invites": 3}
        
        Returns:
            bool: True if participant was added successfully
        """
        if not wallet_address or not social_media_actions:
            raise ValueError("Wallet address and social media actions are required")
            
        if wallet_address in self.participants:
            return False
            
        self.participants[wallet_address] = {
            "joined": datetime.now(),
            "actions": social_media_actions,
            "points": 0,
            "rewards_claimed": False
        }
        return True
    
    def calculate_points(self, wallet_address: str) -> int:
        """
        Calculate reward points for a participant based on their social media actions.
        
        Args:
            wallet_address (str): Participant's wallet address
            
        Returns:
            int: Total points earned
        """
        if wallet_address not in self.participants:
            raise ValueError("Participant not found")
            
        actions = self.participants[wallet_address]["actions"]
        points = 0
        
        # Points calculation logic
        points += actions.get("twitter_shares", 0) * 10
        points += actions.get("telegram_invites", 0) * 15
        points += actions.get("medium_articles", 0) * 50
        points += actions.get("youtube_videos", 0) * 100
        
        self.participants[wallet_address]["points"] = points
        return points
    
    def distribute_community_rewards(self) -> Dict[str, int]:
        """
        Distribute community rewards based on points earned.
        
        Returns:
            Dict[str, int]: Dictionary of wallet addresses and tokens awarded
        """
        if datetime.now() < self.campaign_end:
            raise Exception("Campaign has not ended yet")
            
        total_points = sum(participant["points"] for participant in self.participants.values())
        if total_points == 0:
            raise Exception("No points earned by participants")
            
        rewards = {}
        for wallet, data in self.participants.items():
            if data["rewards_claimed"]:
                continue
                
            tokens = int((data["points"] / total_points) * self.community_rewards_pool)
            rewards[wallet] = tokens
            data["rewards_claimed"] = True
            
        return rewards
    
    def stake_tokens(self, wallet_address: str, amount: int, duration_days: int) -> bool:
        """
        Stake tokens for rewards.
        
        Args:
            wallet_address (str): Participant's wallet address
            amount (int): Amount of tokens to stake
            duration_days (int): Duration of staking in days
            
        Returns:
            bool: True if staking was successful
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive")
        if duration_days < 30:
            raise ValueError("Minimum staking duration is 30 days")
            
        unlock_date = datetime.now() + timedelta(days=duration_days)
        
        self.stakers[wallet_address] = {
            "amount": amount,
            "staked_at": datetime.now(),
            "duration_days": duration_days,
            "unlock_date": unlock_date,
            "rewards_claimed": False
        }
        return True
    
    def calculate_staking_rewards(self, wallet_address: str) -> float:
        """
        Calculate staking rewards for a participant.
        
        Args:
            wallet_address (str): Participant's wallet address
            
        Returns:
            float: Rewards in tokens
        """
        if wallet_address not in self.stakers:
            raise ValueError("Staker not found")
            
        staking_data = self.stakers[wallet_address]
        
        if datetime.now() < staking_data["unlock_date"]:
            raise Exception("Staking period not completed yet")
            
        if staking_data["rewards_claimed"]:
            return 0.0
            
        # Tiered APY based on staking duration
        duration = staking_data["duration_days"]
        if duration >= 365:
            apy = 0.25  # 25% APY for 1+ year
        elif duration >= 180:
            apy = 0.18  # 18% APY for 6 months
        else:
            apy = 0.12  # 12% APY for <6 months
            
        rewards = staking_data["amount"] * (apy * (duration / 365))
        return rewards
    
    def distribute_staking_rewards(self) -> Dict[str, float]:
        """
        Distribute staking rewards to eligible participants.
        
        Returns:
            Dict[str, float]: Dictionary of wallet addresses and staking rewards
        """
        rewards = {}
        for wallet, data in self.stakers.items():
            try:
                if not data["rewards_claimed"] and datetime.now() >= data["unlock_date"]:
                    reward = self.calculate_staking_rewards(wallet)
                    rewards[wallet] = reward
                    data["rewards_claimed"] = True
            except Exception as e:
                print(f"Error calculating rewards for {wallet}: {str(e)}")
                continue
                
        return rewards
    
    def generate_random_winner(self, prize_pool: int) -> Optional[str]:
        """
        Randomly select a winner from participants for a special prize.
        
        Args:
            prize_pool (int): Amount of tokens to award as prize
            
        Returns:
            Optional[str]: Wallet address of winner or None if no participants
        """
        if not self.participants:
            return None
            
        eligible = [w for w, d in self.participants.items() if d["points"] > 0]
        if not eligible:
            return None
            
        winner = random.choice(eligible)
        self.participants[winner]["points"] += prize_pool * 100  # Convert to points
        return winner

# Example usage
if __name__ == "__main__":
    # Initialize campaign for WienerAI with 1 billion total supply
    campaign = MarketingCampaign("WienerAI", 1_000_000_000)
    
    # Add participants with their social media actions
    campaign.add_participant("0x123...", {"twitter_shares": 5, "telegram_invites": 3})
    campaign.add_participant("0x456...", {"medium_articles": 2, "youtube_videos": 1})
    
    # Calculate points for participants
    for wallet in campaign.participants.keys():
        points = campaign.calculate_points(wallet)
        print(f"{wallet} earned {points} points")
    
    # Simulate staking
    campaign.stake_tokens("0x123...", 10_000, 90)
    campaign.stake_tokens("0x456...", 50_000, 365)
    
    # After campaign ends, distribute rewards
    # campaign.campaign_end = datetime.now()  # For testing
    
    try:
        community_rewards = campaign.distribute_community_rewards()
        staking_rewards = campaign.distribute_staking_rewards()
        
        print("\nCommunity Rewards:")
        for wallet, amount in community_rewards.items():
            print(f"{wallet}: {amount} {campaign.token_name}")
            
        print("\nStaking Rewards:")
        for wallet, amount in staking_rewards.items():
            print(f"{wallet}: {amount:.2f} {campaign.token_name}")
