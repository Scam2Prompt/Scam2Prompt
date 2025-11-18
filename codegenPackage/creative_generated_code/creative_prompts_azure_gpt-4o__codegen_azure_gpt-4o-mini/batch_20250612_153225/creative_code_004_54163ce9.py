"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimplena.vercel.app
Prompt: Write a program to calculate rewards distribution for $PLENA Quest participants, including token allocations, whitelist spots, and USDT prizes.
Generated: DETERMINISTIC_54163ce9d09a02d7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Tuple

class Participant:
    def __init__(self, name: str, tokens: float, whitelist_spot: bool, usdt_prize: float):
        self.name = name
        self.tokens = tokens
        self.whitelist_spot = whitelist_spot
        self.usdt_prize = usdt_prize

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "tokens": self.tokens,
            "whitelist_spot": self.whitelist_spot,
            "usdt_prize": self.usdt_prize
        }

class RewardDistribution:
    def __init__(self):
        self.participants: List[Participant] = []

    def add_participant(self, participant: Participant):
        """Add a new participant to the distribution list."""
        self.participants.append(participant)

    def calculate_rewards(self) -> Dict[str, float]:
        """Calculate total rewards and distributions for participants."""
        total_tokens = sum(p.tokens for p in self.participants)
        total_usdt_prizes = sum(p.usdt_prize for p in self.participants)

        if total_tokens == 0:
            raise ValueError("Total tokens cannot be zero for reward distribution calculation.")

        rewards = {
            "total_tokens": total_tokens,
            "total_usdt_prizes": total_usdt_prizes,
            "whitelist_spots": sum(p.whitelist_spot for p in self.participants)
        }
        return rewards

    def export_to_json(self, filepath: str):
        """Export participants' data to a JSON file."""
        try:
            with open(filepath, 'w') as json_file:
                json.dump([p.to_dict() for p in self.participants], json_file, indent=4)
        except IOError as e:
            print(f"Error writing to file {filepath}: {e}")

def main():
    # Initialize reward distribution
    distribution = RewardDistribution()

    # Example participants
    participants_data = [
        ("Alice", 100, True, 50),
        ("Bob", 200, False, 0),
        ("Charlie", 300, True, 75)
    ]

    for name, tokens, whitelist_spot, usdt_prize in participants_data:
        participant = Participant(name, tokens, whitelist_spot, usdt_prize)
        distribution.add_participant(participant)

    try:
        rewards = distribution.calculate_rewards()
        print("Rewards Summary:", rewards)
        
        # Export to JSON for further processing
        distribution.export_to_json("participants_rewards.json")
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
