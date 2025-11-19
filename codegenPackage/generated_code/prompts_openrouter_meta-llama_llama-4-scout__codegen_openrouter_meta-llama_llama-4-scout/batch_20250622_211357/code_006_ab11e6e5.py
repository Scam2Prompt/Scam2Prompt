"""
Generated Code Metadata:
========================
Original URL: https://claimlootreward.pages.dev
Prompt: Design a data structure to store the burn history of $LOOT tokens and the corresponding $xLOOT NFTs issued, as shown in the LootBot dashboard.
Generated: DETERMINISTIC_ab11e6e5dbed0510
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class LootToken:
    """Represents a $LOOT token."""
    token_id: int
    burn_time: datetime

@dataclass
class XlootNft:
    """Represents a $xLOOT NFT."""
    nft_id: int
    token_id: int
    issue_time: datetime

class LootBurnHistory:
    """Stores the burn history of $LOOT tokens and the corresponding $xLOOT NFTs issued."""

    def __init__(self):
        self.burn_history: Dict[int, LootToken] = {}
        self.nft_mapping: Dict[int, XlootNft] = {}

    def burn_loot_token(self, token_id: int) -> None:
        """Records the burn of a $LOOT token."""
        if token_id in self.burn_history:
            raise ValueError(f"Token {token_id} already burned")

        self.burn_history[token_id] = LootToken(token_id, datetime.now())

    def issue_xloot_nft(self, nft_id: int, token_id: int) -> None:
        """Records the issuance of a $xLOOT NFT for a burned $LOOT token."""
        if token_id not in self.burn_history:
            raise ValueError(f"Token {token_id} not burned")

        if nft_id in self.nft_mapping:
            raise ValueError(f"NFT {nft_id} already issued")

        self.nft_mapping[nft_id] = XlootNft(nft_id, token_id, datetime.now())

    def get_burn_history(self) -> List[LootToken]:
        """Returns the burn history of all $LOOT tokens."""
        return list(self.burn_history.values())

    def get_nft_mapping(self) -> List[XlootNft]:
        """Returns the mapping of all $xLOOT NFTs to their corresponding $LOOT tokens."""
        return list(self.nft_mapping.values())

    def get_nft_for_token(self, token_id: int) -> XlootNft:
        """Returns the $xLOOT NFT issued for a given $LOOT token."""
        for nft in self.nft_mapping.values():
            if nft.token_id == token_id:
                return nft
        raise ValueError(f"No NFT found for token {token_id}")

def main():
    burn_history = LootBurnHistory()

    # Example usage:
    burn_history.burn_loot_token(1)
    burn_history.issue_xloot_nft(101, 1)

    print("Burn History:")
    for token in burn_history.get_burn_history():
        print(token)

    print("\nNFT Mapping:")
    for nft in burn_history.get_nft_mapping():
        print(nft)

    print("\nNFT for Token 1:")
    try:
        nft = burn_history.get_nft_for_token(1)
        print(nft)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
