"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pandas-dsp.pages.dev
Prompt: Write a program to simulate gamified staking in PandaVerse, including leveling up NFT Pandas and tracking rewards dynamically.
Generated: DETERMINISTIC_9cb25c261255708e
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class PandaNFT:
    """
    Class representing an NFT Panda in the PandaVerse.
    Each Panda NFT has a unique ID, level, staked status, and accumulated rewards.
    """
    def __init__(self, panda_id):
        self.panda_id = panda_id
        self.level = 1
        self.staked = False
        self.rewards = 0.0

    def stake(self):
        """
        Stake the Panda NFT to start earning rewards.
        """
        if self.staked:
            raise ValueError(f"Panda {self.panda_id} is already staked.")
        self.staked = True
        print(f"Panda {self.panda_id} staked successfully.")

    def unstake(self):
        """
        Unstake the Panda NFT to stop earning rewards.
        """
        if not self.staked:
            raise ValueError(f"Panda {self.panda_id} is not currently staked.")
        self.staked = False
        print(f"Panda {self.panda_id} unstaked successfully.")

    def level_up(self):
        """
        Level up the Panda NFT. Leveling up increases reward rates.
        """
        self.level += 1
        print(f"Panda {self.panda_id} leveled up! Current level: {self.level}")

    def add_rewards(self, amount):
        """
        Add rewards to the Panda NFT.
        """
        self.rewards += amount

    def claim_rewards(self):
        """
        Claim all accumulated rewards.
        """
        if self.rewards > 0:
            claimed_rewards = self.rewards
            self.rewards = 0.0
            print(f"Panda {self.panda_id} claimed {claimed_rewards} rewards.")
            return claimed_rewards
        else:
            print(f"Panda {self.panda_id} has no rewards to claim.")
            return 0.0


class PandaVerse:
    """
    Class representing the PandaVerse ecosystem, managing NFT staking and rewards.
    """
    def __init__(self):
        self.pandas = {}

    def create_panda(self, panda_id):
        """
        Create a new Panda NFT in the PandaVerse.
        """
        if panda_id in self.pandas:
            raise ValueError(f"Panda {panda_id} already exists.")
        self.pandas[panda_id] = PandaNFT(panda_id)
        print(f"Panda {panda_id} has been created.")

    def stake_panda(self, panda_id):
        """
        Stake a Panda NFT to start earning rewards.
        """
        self.get_panda(panda_id).stake()

    def unstake_panda(self, panda_id):
        """
        Unstake a Panda NFT to stop earning rewards.
        """
        self.get_panda(panda_id).unstake()

    def level_up_panda(self, panda_id):
        """
        Level up a Panda NFT.
        """
        self.get_panda(panda_id).level_up()

    def claim_rewards(self, panda_id):
        """
        Claim rewards for a specific Panda NFT.
        """
        return self.get_panda(panda_id).claim_rewards()

    def simulate_rewards(self):
        """
        Simulate rewards for staked Pandas. Higher level Pandas earn more rewards.
        """
        for panda in self.pandas.values():
            if panda.staked:
                # Reward formula: base rate + (level multiplier)
                reward = random.uniform(1.0, 2.0) * panda.level
                panda.add_rewards(reward)
                print(f"Panda {panda.panda_id} earned {reward:.2f} rewards.")

    def get_panda(self, panda_id):
        """
        Retrieve a Panda NFT by its ID.
        """
        if panda_id not in self.pandas:
            raise ValueError(f"Panda {panda_id} does not exist.")
        return self.pandas[panda_id]


if __name__ == "__main__":
    # Initialize the PandaVerse
    panda_verse = PandaVerse()

    # Create Panda NFTs
    panda_verse.create_panda("Panda001")
    panda_verse.create_panda("Panda002")

    # Stake Panda NFTs
    panda_verse.stake_panda("Panda001")
    panda_verse.stake_panda("Panda002")

    # Simulate rewards for a few rounds
    for _ in range(5):
        time.sleep(1)  # Simulating time passing
        panda_verse.simulate_rewards()

    # Level up a Panda NFT
    panda_verse.level_up_panda("Panda001")

    # Claim rewards
    panda_verse.claim_rewards("Panda001")
    panda_verse.claim_rewards("Panda002")

    # Unstake Panda NFTs
    panda_verse.unstake_panda("Panda001")
    panda_verse.unstake_panda("Panda002")
```
