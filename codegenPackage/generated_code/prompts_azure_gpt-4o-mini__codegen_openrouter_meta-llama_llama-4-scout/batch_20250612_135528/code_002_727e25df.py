"""
Generated Code Metadata:
========================
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Explain how to design a leaderboard system for tracking user progress in an NFT evolution game based on the HV-MTL mechanics.
Generated: DETERMINISTIC_727e25df183a196f
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard_system.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class NFTStatus(Enum):
    """Enum representing NFT status"""
    EVOLVING = 1
    EVOLVED = 2
    MAX_LEVEL = 3

@dataclass
class NFT:
    """Class representing an NFT"""
    id: int
    user_id: int
    level: int
    status: NFTStatus
    last_evolution_time: datetime

class LeaderboardSystem:
    """Class representing the leaderboard system"""
    def __init__(self):
        self.nfts: Dict[int, NFT] = {}  # NFT ID to NFT object
        self.user_nfts: Dict[int, List[NFT]] = {}  # User ID to list of NFT objects

    def add_nft(self, nft: NFT):
        """Add an NFT to the system"""
        self.nfts[nft.id] = nft
        if nft.user_id not in self.user_nfts:
            self.user_nfts[nft.user_id] = []
        self.user_nfts[nft.user_id].append(nft)

    def update_nft(self, nft_id: int, level: int, status: NFTStatus):
        """Update an NFT's level and status"""
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        nft = self.nfts[nft_id]
        nft.level = level
        nft.status = status
        nft.last_evolution_time = datetime.now()

    def get_user_nfts(self, user_id: int) -> List[NFT]:
        """Get a user's NFTs"""
        return self.user_nfts.get(user_id, [])

    def get_leaderboard(self, top_n: int = 10) -> List[Dict]:
        """Get the leaderboard"""
        leaderboard = []
        for user_id, nfts in self.user_nfts.items():
            total_level = sum(nft.level for nft in nfts)
            leaderboard.append({"user_id": user_id, "total_level": total_level})
        leaderboard.sort(key=lambda x: x["total_level"], reverse=True)
        return leaderboard[:top_n]

    def get_user_rank(self, user_id: int) -> int:
        """Get a user's rank on the leaderboard"""
        leaderboard = self.get_leaderboard()
        for i, user in enumerate(leaderboard):
            if user["user_id"] == user_id:
                return i + 1
        return -1  # User not found on leaderboard

def main():
    leaderboard_system = LeaderboardSystem()

    # Create some NFTs
    nft1 = NFT(1, 1, 10, NFTStatus.EVOLVED, datetime.now())
    nft2 = NFT(2, 1, 20, NFTStatus.EVOLVING, datetime.now())
    nft3 = NFT(3, 2, 5, NFTStatus.EVOLVING, datetime.now())

    # Add NFTs to the system
    leaderboard_system.add_nft(nft1)
    leaderboard_system.add_nft(nft2)
    leaderboard_system.add_nft(nft3)

    # Update an NFT
    leaderboard_system.update_nft(1, 15, NFTStatus.EVOLVING)

    # Get a user's NFTs
    user_nfts = leaderboard_system.get_user_nfts(1)
    print("User 1's NFTs:")
    for nft in user_nfts:
        print(nft)

    # Get the leaderboard
    leaderboard = leaderboard_system.get_leaderboard()
    print("\nLeaderboard:")
    for user in leaderboard:
        print(user)

    # Get a user's rank
    user_rank = leaderboard_system.get_user_rank(1)
    print(f"\nUser 1's rank: {user_rank}")

if __name__ == "__main__":
    main()
```
