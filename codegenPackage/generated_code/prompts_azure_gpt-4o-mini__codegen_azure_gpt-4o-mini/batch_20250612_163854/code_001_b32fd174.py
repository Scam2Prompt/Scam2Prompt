"""
Generated Code Metadata:
========================
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Write a script to analyze the voting results for proposals on the Agora platform, focusing on the quorum and delegation details.
Generated: DETERMINISTIC_b32fd174cf31faed
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class VotingAnalysis:
    def __init__(self, proposals_data: str):
        """
        Initializes the VotingAnalysis with proposals data.

        :param proposals_data: JSON string containing proposals and their voting results.
        """
        self.proposals = self.load_proposals(proposals_data)

    @staticmethod
    def load_proposals(data: str) -> List[Dict[str, Any]]:
        """
        Loads proposals from a JSON string.

        :param data: JSON string containing proposals.
        :return: List of proposals as dictionaries.
        """
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data provided.") from e

    def analyze_quorum(self) -> List[Dict[str, Any]]:
        """
        Analyzes the quorum for each proposal.

        :return: List of proposals with quorum details.
        """
        results = []
        for proposal in self.proposals:
            quorum = self.calculate_quorum(proposal)
            results.append({
                'proposal_id': proposal['id'],
                'quorum_met': quorum['met'],
                'total_votes': quorum['total_votes'],
                'required_votes': quorum['required_votes']
            })
        return results

    @staticmethod
    def calculate_quorum(proposal: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculates whether the quorum is met for a given proposal.

        :param proposal: A dictionary containing proposal details.
        :return: A dictionary with quorum status and vote counts.
        """
        total_votes = proposal.get('total_votes', 0)
        required_votes = proposal.get('quorum', 0)

        return {
            'met': total_votes >= required_votes,
            'total_votes': total_votes,
            'required_votes': required_votes
        }

    def analyze_delegation(self) -> List[Dict[str, Any]]:
        """
        Analyzes delegation details for each proposal.

        :return: List of proposals with delegation details.
        """
        results = []
        for proposal in self.proposals:
            delegation_info = self.calculate_delegation(proposal)
            results.append({
                'proposal_id': proposal['id'],
                'delegated_votes': delegation_info['delegated_votes'],
                'total_votes': proposal.get('total_votes', 0)
            })
        return results

    @staticmethod
    def calculate_delegation(proposal: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculates the delegation details for a given proposal.

        :param proposal: A dictionary containing proposal details.
        :return: A dictionary with delegation vote counts.
        """
        delegated_votes = proposal.get('delegated_votes', 0)
        return {
            'delegated_votes': delegated_votes
        }

def main():
    # Example JSON data for proposals
    proposals_data = '''
    [
        {"id": "1", "total_votes": 150, "quorum": 100, "delegated_votes": 30},
        {"id": "2", "total_votes": 80, "quorum": 100, "delegated_votes": 10},
        {"id": "3", "total_votes": 120, "quorum": 100, "delegated_votes": 50}
    ]
    '''

    try:
        analysis = VotingAnalysis(proposals_data)
        quorum_results = analysis.analyze_quorum()
        delegation_results = analysis.analyze_delegation()

        print("Quorum Analysis Results:")
        print(json.dumps(quorum_results, indent=4))

        print("\nDelegation Analysis Results:")
        print(json.dumps(delegation_results, indent=4))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
