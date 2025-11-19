"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibawo7r32uj46hju347auzbhmfq4h6f35azlyhnfqjz4d5whkaq5q.ipfs.dweb.link
Prompt: Explain how to vote on allocation criteria for the $KEP season 2 Claim and its impact on restaking rewards.
Generated: DETERMINISTIC_6f968c0579ff2a4c
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation with clean, well-documented, production-ready code:

```python
import json

class KEPVotingSystem:
    """
    A class to manage voting on allocation criteria for the $KEP season 2 Claim.
    This system impacts the distribution of restaking rewards based on votes.
    """
    
    def __init__(self):
        """
        Initializes the voting system with an empty set of criteria and votes.
        """
        self.criteria = {}  # Dictionary to hold allocation criteria
        self.votes = {}     # Dictionary to track votes per criterion

    def add_criterion(self, criterion_name):
        """
        Adds a new allocation criterion to the voting system.
        
        :param criterion_name: The name of the allocation criterion to add.
        :raises ValueError: If the criterion already exists.
        """
        if criterion_name in self.criteria:
            raise ValueError(f"Criterion '{criterion_name}' already exists.")
        self.criteria[criterion_name] = 0
        self.votes[criterion_name] = 0

    def vote(self, criterion_name):
        """
        Casts a vote for a specific allocation criterion.
        
        :param criterion_name: The name of the criterion to vote for.
        :raises ValueError: If the criterion is not found.
        """
        if criterion_name not in self.criteria:
            raise ValueError(f"Criterion '{criterion_name}' not found.")
        self.votes[criterion_name] += 1

    def calculate_rewards_impact(self):
        """
        Calculates the impact of votes on restaking rewards based on the allocation criteria.
        
        :return: A dictionary mapping criteria to their percentage weight in rewards distribution.
        """
        total_votes = sum(self.votes.values())
        if total_votes == 0:
            return {criterion: 0 for criterion in self.criteria}  # No votes, no impact

        # Calculate impact as a percentage of total votes
        return {
            criterion: (votes / total_votes) * 100
            for criterion, votes in self.votes.items()
        }

    def export_results(self, file_path="voting_results.json"):
        """
        Exports the voting results and calculated impact to a JSON file.
        
        :param file_path: The file path where results should be saved.
        """
        results = {
            "criteria": self.criteria,
            "votes": self.votes,
            "impact": self.calculate_rewards_impact()
        }
        try:
            with open(file_path, "w") as file:
                json.dump(results, file, indent=4)
        except IOError as e:
            print(f"Error writing to file: {e}")

    def import_results(self, file_path="voting_results.json"):
        """
        Imports voting results from a JSON file.
        
        :param file_path: The file path where results should be imported from.
        :raises ValueError: If the file doesn't contain valid data.
        """
        try:
            with open(file_path, "r") as file:
                results = json.load(file)
                self.criteria = results.get("criteria", {})
                self.votes = results.get("votes", {})
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Error reading or parsing file: {e}")

# Example usage
if __name__ == "__main__":
    system = KEPVotingSystem()

    # Adding criteria
    system.add_criterion("Environmental Sustainability")
    system.add_criterion("Community Growth")
    system.add_criterion("Innovation in Technology")

    # Casting votes
    system.vote("Environmental Sustainability")
    system.vote("Community Growth")
    system.vote("Community Growth")
    system.vote("Innovation in Technology")
    system.vote("Innovation in Technology")
    system.vote("Innovation in Technology")

    # Calculate the impact on rewards
    impact = system.calculate_rewards_impact()
    print("Impact on Restaking Rewards:")
    for criterion, percentage in impact.items():
        print(f"{criterion}: {percentage:.2f}%")

    # Export results
    system.export_results()

    # Import and verify results (optional)
    system.import_results()
```
