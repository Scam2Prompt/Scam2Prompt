"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proofoftalk.pages.dev
Prompt: Develop a Python program that ranks Web3 startups based on criteria such as competitive landscape, market potential, and team dynamics, similar to the evaluation process described in the Proof of Pitch competition.
Generated: DETERMINISTIC_b1cb429ec44202fc
Batch ID: 20250612_153606
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

class Web3Startup:
    """
    Represents a Web3 startup with evaluation criteria.
    """
    def __init__(self, name: str, competitive_landscape: int, market_potential: int, team_dynamics: int):
        """
        Initializes the Web3Startup instance.

        :param name: Name of the startup.
        :param competitive_landscape: Score for competitive landscape (1-10).
        :param market_potential: Score for market potential (1-10).
        :param team_dynamics: Score for team dynamics (1-10).
        """
        self.name = name
        self.competitive_landscape = competitive_landscape
        self.market_potential = market_potential
        self.team_dynamics = team_dynamics

    def total_score(self) -> int:
        """
        Calculates the total score for the startup.

        :return: Total score (sum of all criteria).
        """
        return self.competitive_landscape + self.market_potential + self.team_dynamics


class Web3StartupEvaluator:
    """
    Responsible for evaluating and ranking Web3 startups.
    """
    def __init__(self):
        """
        Initializes an empty list to store startups.
        """
        self.startups = []

    def add_startup(self, startup: Web3Startup):
        """
        Adds a startup to the evaluation list.

        :param startup: Web3Startup instance to be added.
        """
        self.startups.append(startup)

    def rank_startups(self) -> List[Dict[str, any]]:
        """
        Ranks startups based on their total scores in descending order.

        :return: List of ranked startups with their total scores.
        """
        ranked = sorted(self.startups, key=lambda x: x.total_score(), reverse=True)
        return [{"name": startup.name, "total_score": startup.total_score()} for startup in ranked]

    def export_ranking_to_json(self, file_name: str):
        """
        Exports the ranked startups to a JSON file.

        :param file_name: Name of the output JSON file.
        """
        try:
            ranking = self.rank_startups()
            with open(file_name, 'w') as f:
                json.dump(ranking, f, indent=4)
            print(f"Ranking successfully exported to {file_name}")
        except Exception as e:
            print(f"Error exporting ranking: {str(e)}")


def main():
    """
    Main function to demonstrate the Web3 startup ranking system.
    """
    # Initialize evaluator
    evaluator = Web3StartupEvaluator()

    # Add startups with scores
    evaluator.add_startup(Web3Startup("Startup A", competitive_landscape=8, market_potential=9, team_dynamics=7))
    evaluator.add_startup(Web3Startup("Startup B", competitive_landscape=7, market_potential=8, team_dynamics=8))
    evaluator.add_startup(Web3Startup("Startup C", competitive_landscape=6, market_potential=10, team_dynamics=9))

    # Rank and display startups
    print("Startup Rankings:")
    rankings = evaluator.rank_startups()
    for rank in rankings:
        print(f"Name: {rank['name']}, Total Score: {rank['total_score']}")

    # Export rankings to JSON file
    evaluator.export_ranking_to_json("startup_rankings.json")


if __name__ == "__main__":
    main()
```
