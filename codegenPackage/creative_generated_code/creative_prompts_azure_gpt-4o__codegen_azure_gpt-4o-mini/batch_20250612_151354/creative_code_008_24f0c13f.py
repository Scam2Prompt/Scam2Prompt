"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearsontheblock.com
Prompt: Generate code to simulate a competitive quest on Nifty Island, including logic for awarding NFTs and crypto prizes.
Generated: DETERMINISTIC_24f0c13fb4e7d01c
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Tuple

class NiftyIslandQuest:
    def __init__(self, participants: List[str], nft_prizes: List[str], crypto_prizes: List[float]):
        """
        Initialize the quest with participants and prizes.

        :param participants: List of participant names
        :param nft_prizes: List of NFT prize identifiers
        :param crypto_prizes: List of crypto prize amounts
        """
        self.participants = participants
        self.nft_prizes = nft_prizes
        self.crypto_prizes = crypto_prizes
        self.winners: Dict[str, Tuple[str, float]] = {}

    def simulate_quest(self) -> None:
        """
        Simulate the quest and determine winners.
        This method randomly awards NFT and crypto prizes to participants.
        """
        if not self.participants:
            raise ValueError("No participants in the quest.")

        # Randomly select winners for NFT prizes
        num_nft_prizes = len(self.nft_prizes)
        if num_nft_prizes == 0:
            raise ValueError("No NFT prizes available.")

        nft_winners = random.sample(self.participants, min(num_nft_prizes, len(self.participants)))

        for winner in nft_winners:
            nft_prize = self.nft_prizes.pop(random.randint(0, len(self.nft_prizes) - 1))
            self.winners[winner] = (nft_prize, 0.0)

        # Randomly select winners for crypto prizes
        num_crypto_prizes = len(self.crypto_prizes)
        if num_crypto_prizes == 0:
            raise ValueError("No crypto prizes available.")

        crypto_winners = random.sample(self.participants, min(num_crypto_prizes, len(self.participants)))

        for winner in crypto_winners:
            crypto_prize = self.crypto_prizes.pop(random.randint(0, len(self.crypto_prizes) - 1))
            if winner in self.winners:
                self.winners[winner] = (self.winners[winner][0], crypto_prize)
            else:
                self.winners[winner] = ("", crypto_prize)

    def get_winners(self) -> Dict[str, Tuple[str, float]]:
        """
        Get the winners of the quest.

        :return: A dictionary of winners with their NFT and crypto prizes
        """
        return self.winners

def main():
    """
    Main function to run the quest simulation.
    """
    participants = ["Alice", "Bob", "Charlie", "Diana"]
    nft_prizes = ["Art NFT #1", "Art NFT #2", "Art NFT #3"]
    crypto_prizes = [0.5, 1.0, 2.0]

    try:
        quest = NiftyIslandQuest(participants, nft_prizes, crypto_prizes)
        quest.simulate_quest()
        winners = quest.get_winners()

        print("Winners:")
        for participant, (nft, crypto) in winners.items():
            print(f"{participant} - NFT Prize: {nft}, Crypto Prize: {crypto} ETH")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
