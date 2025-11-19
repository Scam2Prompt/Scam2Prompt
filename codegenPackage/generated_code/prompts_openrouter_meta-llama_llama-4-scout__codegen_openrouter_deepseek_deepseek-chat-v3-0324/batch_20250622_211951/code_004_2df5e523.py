"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.com
Prompt: Design a data structure to store RedStone Finance user data, including wallet addresses, RSG rewards, and ranking information, and provide an example of how to populate it with sample data from this webpage.
Generated: DETERMINISTIC_2df5e5233b1aaf58
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class UserData:
    wallet_address: str
    rsg_rewards: float
    rank: Optional[int] = None

class RedStoneUserDataStore:
    """
    A data structure to store RedStone Finance user data including:
    - Wallet addresses
    - RSG rewards
    - Ranking information
    """
    
    def __init__(self):
        self.users: Dict[str, UserData] = {}  # Key: wallet_address, Value: UserData
    
    def add_user(self, wallet_address: str, rsg_rewards: float, rank: int = None) -> None:
        """
        Add a new user or update existing user data.
        
        Args:
            wallet_address: User's wallet address
            rsg_rewards: RSG rewards amount
            rank: User's rank (optional)
        """
        if not isinstance(wallet_address, str) or not wallet_address:
            raise ValueError("Wallet address must be a non-empty string")
        
        if not isinstance(rsg_rewards, (int, float)) or rsg_rewards < 0:
            raise ValueError("RSG rewards must be a positive number")
        
        if rank is not None and (not isinstance(rank, int) or rank <= 0):
            raise ValueError("Rank must be a positive integer or None")
        
        self.users[wallet_address] = UserData(
            wallet_address=wallet_address,
            rsg_rewards=rsg_rewards,
            rank=rank
        )
    
    def get_user(self, wallet_address: str) -> Optional[UserData]:
        """
        Retrieve user data by wallet address.
        
        Args:
            wallet_address: Wallet address to look up
            
        Returns:
            UserData if found, None otherwise
        """
        return self.users.get(wallet_address)
    
    def get_top_users(self, limit: int = 10) -> List[UserData]:
        """
        Get top users sorted by RSG rewards descending.
        
        Args:
            limit: Maximum number of users to return
            
        Returns:
            List of UserData objects
        """
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("Limit must be a positive integer")
        
        sorted_users = sorted(
            self.users.values(),
            key=lambda x: x.rsg_rewards,
            reverse=True
        )
        return sorted_users[:limit]
    
    def to_json(self) -> str:
        """
        Serialize the user data to JSON format.
        
        Returns:
            JSON string representation of the data
        """
        users_list = [
            {
                "wallet_address": user.wallet_address,
                "rsg_rewards": user.rsg_rewards,
                "rank": user.rank
            }
            for user in self.users.values()
        ]
        return json.dumps(users_list, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'RedStoneUserDataStore':
        """
        Create a RedStoneUserDataStore from JSON data.
        
        Args:
            json_str: JSON string containing user data
            
        Returns:
            New RedStoneUserDataStore instance
        """
        data_store = cls()
        try:
            users_data = json.loads(json_str)
            for user_data in users_data:
                data_store.add_user(
                    wallet_address=user_data["wallet_address"],
                    rsg_rewards=user_data["rsg_rewards"],
                    rank=user_data.get("rank")
                )
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            raise ValueError("Invalid JSON data format") from e
        return data_store

# Example usage with sample data
if __name__ == "__main__":
    # Sample data (would typically come from web scraping or API)
    sample_data = [
        {"wallet_address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e", "rsg_rewards": 1500.25, "rank": 1},
        {"wallet_address": "0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed", "rsg_rewards": 1200.50, "rank": 2},
        {"wallet_address": "0x6B175474E89094C44Da98b954EedeAC495271d0F", "rsg_rewards": 900.75, "rank": 3},
        {"wallet_address": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984", "rsg_rewards": 800.00},
        {"wallet_address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "rsg_rewards": 750.30, "rank": 5},
    ]
    
    # Create and populate the data store
    data_store = RedStoneUserDataStore()
    for user in sample_data:
        data_store.add_user(
            wallet_address=user["wallet_address"],
            rsg_rewards=user["rsg_rewards"],
            rank=user.get("rank")
        )
    
    # Example operations
    print("Top 3 users by RSG rewards:")
    for user in data_store.get_top_users(3):
        print(f"Rank: {user.rank}, Address: {user.wallet_address}, RSG: {user.rsg_rewards}")
    
    print("\nSerialized JSON data:")
    print(data_store.to_json())
```
