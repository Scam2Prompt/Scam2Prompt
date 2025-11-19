"""
Generated Code Metadata:
========================
Original URL: https://everyworld4.pages.dev
Prompt: Design a web3 rewarded ads platform using a dual incentivization model, where users can earn points and win rewards, and describe its features for environmental conservation.
Generated: DETERMINISTIC_c26a444e9f32b0f8
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Web3 Rewarded Ads Platform with Dual Incentivization Model
# Focused on Environmental Conservation

from web3 import Web3
from typing import Dict, List, Tuple
import hashlib
import json
from datetime import datetime, timedelta
import random

# Smart Contract ABI (simplified for demonstration)
CONTRACT_ABI = [
    {
        "inputs": [],
        "name": "claimReward",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getUserPoints",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getUserRewards",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}, {"internalType": "uint256", "name": "points", "type": "uint256"}],
        "name": "addPoints",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

class Web3RewardedAdsPlatform:
    def __init__(self, web3_provider: str, contract_address: str):
        """
        Initialize the Web3 Rewarded Ads Platform.
        
        Args:
            web3_provider: URL of the Ethereum node provider
            contract_address: Address of the smart contract
        """
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract = self.web3.eth.contract(
            address=contract_address,
            abi=CONTRACT_ABI
        )
        self.users: Dict[str, Dict] = {}  # In-memory user data (would be DB in production)
        self.ads: List[Dict] = []
        self.environmental_actions = [
            "carbon_offset",
            "tree_planting",
            "recycling",
            "clean_energy",
            "water_conservation"
        ]
        
    def register_user(self, wallet_address: str) -> bool:
        """
        Register a new user with their wallet address.
        
        Args:
            wallet_address: User's Ethereum wallet address
            
        Returns:
            bool: True if registration was successful
        """
        if not Web3.is_address(wallet_address):
            raise ValueError("Invalid wallet address")
            
        if wallet_address in self.users:
            return False
            
        self.users[wallet_address] = {
            "points": 0,
            "rewards": 0,
            "last_ad_view": None,
            "environmental_actions": [],
            "carbon_footprint_reduction": 0  # in kg CO2
        }
        return True
        
    def view_ad(self, wallet_address: str, ad_id: str) -> Tuple[int, int]:
        """
        Record an ad view and award points to the user.
        
        Args:
            wallet_address: User's wallet address
            ad_id: ID of the ad being viewed
            
        Returns:
            Tuple: (points_earned, total_points)
        """
        if wallet_address not in self.users:
            raise ValueError("User not registered")
            
        # Check if user can view another ad (cooldown period)
        last_view = self.users[wallet_address]["last_ad_view"]
        if last_view and (datetime.now() - last_view) < timedelta(minutes=5):
            raise Exception("Ad view cooldown period not elapsed")
            
        # Get ad details (would be from DB in production)
        ad = next((a for a in self.ads if a["id"] == ad_id), None)
        if not ad:
            raise ValueError("Invalid ad ID")
            
        # Calculate points (base points + environmental bonus)
        base_points = 10
        environmental_bonus = 5 if ad.get("environmental_focus", False) else 0
        total_points = base_points + environmental_bonus
        
        # Update user data
        self.users[wallet_address]["points"] += total_points
        self.users[wallet_address]["last_ad_view"] = datetime.now()
        
        # Update smart contract
        try:
            tx_hash = self.contract.functions.addPoints(
                wallet_address,
                total_points
            ).transact({'from': wallet_address})
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status != 1:
                raise Exception("Failed to update points on blockchain")
        except Exception as e:
            # Rollback local changes if blockchain update fails
            self.users[wallet_address]["points"] -= total_points
            raise
            
        return total_points, self.users[wallet_address]["points"]
        
    def perform_environmental_action(self, wallet_address: str, action_type: str) -> Dict:
        """
        Record an environmental action and award bonus points.
        
        Args:
            wallet_address: User's wallet address
            action_type: Type of environmental action
            
        Returns:
            Dict: Action details and points awarded
        """
        if wallet_address not in self.users:
            raise ValueError("User not registered")
            
        if action_type not in self.environmental_actions:
            raise ValueError("Invalid action type")
            
        # Calculate points based on action type
        action_points = {
            "carbon_offset": 50,
            "tree_planting": 30,
            "recycling": 20,
            "clean_energy": 25,
            "water_conservation": 15
        }.get(action_type, 0)
        
        # Calculate CO2 reduction
        co2_reduction = {
            "carbon_offset": 1000,  # kg CO2
            "tree_planting": 50,
            "recycling": 5,
            "clean_energy": 200,
            "water_conservation": 10
        }.get(action_type, 0)
        
        # Record action
        action_id = hashlib.sha256(f"{wallet_address}{action_type}{datetime.now().isoformat()}".encode()).hexdigest()
        action_record = {
            "id": action_id,
            "type": action_type,
            "timestamp": datetime.now(),
            "points": action_points,
            "co2_reduction": co2_reduction
        }
        
        self.users[wallet_address]["environmental_actions"].append(action_record)
        self.users[wallet_address]["points"] += action_points
        self.users[wallet_address]["carbon_footprint_reduction"] += co2_reduction
        
        return action_record
        
    def claim_reward(self, wallet_address: str) -> bool:
        """
        Claim accumulated rewards from the smart contract.
        
        Args:
            wallet_address: User's wallet address
            
        Returns:
            bool: True if reward claim was successful
        """
        if wallet_address not in self.users:
            raise ValueError("User not registered")
            
        try:
            tx_hash = self.contract.functions.claimReward().transact({'from': wallet_address})
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            return receipt.status == 1
        except Exception as e:
            raise Exception(f"Failed to claim reward: {str(e)}")
            
    def get_leaderboard(self) -> List[Dict]:
        """
        Get the top users based on points and environmental impact.
        
        Returns:
            List: Sorted list of users with their stats
        """
        leaderboard = []
        for wallet, data in self.users.items():
            leaderboard.append({
                "wallet": wallet,
                "points": data["points"],
                "carbon_reduction": data["carbon_footprint_reduction"],
                "actions_count": len(data["environmental_actions"])
            })
            
        # Sort by points descending
        leaderboard.sort(key=lambda x: x["points"], reverse=True)
        return leaderboard
        
    def add_ad(self, advertiser: str, content: str, environmental_focus: bool = False) -> str:
        """
        Add a new ad to the platform.
        
        Args:
            advertiser: Advertiser name
            content: Ad content
            environmental_focus: Whether the ad promotes environmental causes
            
        Returns:
            str: Generated ad ID
        """
        ad_id = hashlib.sha256(f"{advertiser}{content}{datetime.now().isoformat()}".encode()).hexdigest()
        self.ads.append({
            "id": ad_id,
            "advertiser": advertiser,
            "content": content,
            "environmental_focus": environmental_focus,
            "timestamp": datetime.now()
        })
        return ad_id
