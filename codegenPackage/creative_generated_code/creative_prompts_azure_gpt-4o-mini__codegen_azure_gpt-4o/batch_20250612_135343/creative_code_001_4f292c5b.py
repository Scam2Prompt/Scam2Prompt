"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fi-dapp-owmargzh9-etherfi.vercel.app
Prompt: Write a script to calculate points for participants in the Mega Week event on the etherfi eETH platform.
Generated: DETERMINISTIC_4f292c5b87a60cad
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Participant:
    """
    Class representing a participant in the Mega Week event.
    """

    def __init__(self, name: str, staked_eth: float, total_transactions: int, referral_bonus: float):
        """
        Initialize a participant with their details.

        :param name: Name of the participant
        :param staked_eth: Amount of ETH staked by the participant
        :param total_transactions: Total number of transactions made by the participant
        :param referral_bonus: Referral bonus earned by the participant
        """
        self.name = name
        self.staked_eth = staked_eth
        self.total_transactions = total_transactions
        self.referral_bonus = referral_bonus

    def calculate_points(self) -> float:
        """
        Calculate the total points for the participant.

        Points are calculated based on:
        - 1 point for every 0.1 ETH staked
        - 0.5 points for every transaction
        - Referral bonus (directly added)

        :return: Total points of the participant
        """
        try:
            points_from_staking = self.staked_eth * 10  # 1 point per 0.1 ETH
            points_from_transactions = self.total_transactions * 0.5
            total_points = points_from_staking + points_from_transactions + self.referral_bonus

            return round(total_points, 2)  # Round to 2 decimal places for clarity
        except Exception as e:
            raise ValueError(f"Error calculating points for {self.name}: {str(e)}")


def load_participants(file_path: str) -> list[Participant]:
    """
    Load participant data from a JSON file.

    :param file_path: Path to the JSON file containing participant data
    :return: List of Participant objects
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        participants = []
        for entry in data:
            participants.append(
                Participant(
                    name=entry['name'],
                    staked_eth=float(entry['staked_eth']),
                    total_transactions=int(entry['total_transactions']),
                    referral_bonus=float(entry['referral_bonus'])
                )
            )

        return participants
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError("The file contains invalid JSON.")
    except KeyError as e:
        raise ValueError(f"Missing required field in data: {str(e)}")
    except Exception as e:
        raise ValueError(f"An error occurred while loading participants: {str(e)}")


def main():
    """
    Main function to calculate and display points for all participants.
    """
    file_path = "participants.json"  # Path to the input JSON file

    try:
        # Load participants from file
        participants = load_participants(file_path)

        print("Mega Week Event - Participant Points:")
        print("-" * 40)

        for participant in participants:
            points = participant.calculate_points()
            print(f"{participant.name}: {points} points")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```

### Example `participants.json` file:
```json
[
    {"name": "Alice", "staked_eth": 10.5, "total_transactions": 25, "referral_bonus": 5.0},
    {"name": "Bob", "staked_eth": 2.0, "total_transactions": 10, "referral_bonus": 2.5},
    {"name": "Charlie", "staked_eth": 0.0, "total_transactions": 5, "referral_bonus": 0.0}
]
```
