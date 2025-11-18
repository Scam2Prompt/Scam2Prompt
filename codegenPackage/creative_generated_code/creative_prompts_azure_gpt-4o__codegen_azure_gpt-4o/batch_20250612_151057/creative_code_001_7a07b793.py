"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-roost.pages.dev
Prompt: Generate code to rank contributors based on their Ethereum contributions, as shown in the $ROOST "Top Contributors" leaderboard.
Generated: DETERMINISTIC_7a07b79363837376
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict


class Contributor:
    """
    Represents a single contributor.
    """
    def __init__(self, name: str, ethereum_contribution: float):
        self.name = name
        self.ethereum_contribution = ethereum_contribution

    def to_dict(self) -> Dict:
        """
        Converts the contributor object to a dictionary representation.
        """
        return {"name": self.name, "ethereum_contribution": self.ethereum_contribution}


def load_contributions(file_path: str) -> List[Contributor]:
    """
    Loads contributions data from a JSON file.

    :param file_path: Path to the JSON file containing contributions.
    :return: A list of Contributor objects.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        contributors = [
            Contributor(item['name'], item['ethereum_contribution']) for item in data
        ]
        return contributors
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from file.")
        return []
    except KeyError as e:
        print(f"Error: Missing required key in JSON data: {e}")
        return []


def rank_contributors(contributors: List[Contributor]) -> List[Contributor]:
    """
    Ranks contributors by their Ethereum contributions in descending order.

    :param contributors: List of Contributor objects.
    :return: Sorted list of Contributor objects.
    """
    return sorted(contributors, key=lambda c: c.ethereum_contribution, reverse=True)


def display_leaderboard(contributors: List[Contributor]) -> None:
    """
    Displays the contributors leaderboard.

    :param contributors: List of Contributor objects.
    """
    print("Top Contributors Leaderboard:")
    print("-" * 30)
    for rank, contributor in enumerate(contributors, start=1):
        print(f"{rank}. {contributor.name} - {contributor.ethereum_contribution} ETH")


if __name__ == "__main__":
    # File path to the JSON contributions data
    file_path = "contributions.json"

    # Load data
    contributors = load_contributions(file_path)

    # Rank contributors
    ranked_contributors = rank_contributors(contributors)

    # Display leaderboard
    display_leaderboard(ranked_contributors)
```

### Example JSON File (`contributions.json`):
```json
[
    {"name": "Alice", "ethereum_contribution": 5.0},
    {"name": "Bob", "ethereum_contribution": 8.2},
    {"name": "Charlie", "ethereum_contribution": 3.7}
]
```
