"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Write a script to analyze the voting results for proposals on the Agora platform, focusing on the quorum and delegation details.
Generated: DETERMINISTIC_b32fd174cf31faed
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class AgoraVotingAnalyzer:
    """
    A class to analyze voting results on the Agora platform.
    """

    def __init__(self, proposals_data: pd.DataFrame):
        """
        Initializes the AgoraVotingAnalyzer with proposals data.

        Args:
            proposals_data (pd.DataFrame): DataFrame containing proposals voting results.
        """
        self.proposals_data = proposals_data

    def calculate_quorum(self, proposal_id: str) -> float:
        """
        Calculate the quorum for a given proposal.

        Args:
            proposal_id (str): The ID of the proposal to analyze.

        Returns:
            float: The percentage of votes that constitutes the quorum.
        """
        try:
            proposal = self.proposals_data[self.proposals_data['proposal_id'] == proposal_id]
            if proposal.empty:
                raise ValueError(f"No data found for proposal ID: {proposal_id}")

            total_votes = proposal['total_votes'].values[0]
            quorum_threshold = proposal['quorum_threshold'].values[0]

            if total_votes == 0:
                return 0.0
            
            quorum_percentage = (quorum_threshold / total_votes) * 100
            return quorum_percentage

        except Exception as e:
            print(f"Error calculating quorum: {e}")
            return None

    def analyze_delegation(self, proposal_id: str) -> dict:
        """
        Analyze delegation details for a given proposal.

        Args:
            proposal_id (str): The ID of the proposal to analyze.

        Returns:
            dict: A dictionary containing delegation details.
        """
        try:
            proposal = self.proposals_data[self.proposals_data['proposal_id'] == proposal_id]
            if proposal.empty:
                raise ValueError(f"No data found for proposal ID: {proposal_id}")

            total_delegated_votes = proposal['delegated_votes'].values[0]
            total_votes = proposal['total_votes'].values[0]
            
            if total_votes == 0:
                return {"delegated_percentage": 0.0}

            delegated_percentage = (total_delegated_votes / total_votes) * 100
            
            return {
                "total_delegated_votes": total_delegated_votes,
                "delegated_percentage": delegated_percentage
            }

        except Exception as e:
            print(f"Error analyzing delegation: {e}")
            return None

def main():
    """
    Main function to execute the analysis on voting results.
    """

    # Sample DataFrame creation for demonstration
    data = {
        'proposal_id': ['1', '2', '3'],
        'total_votes': [100, 200, 150],
        'quorum_threshold': [50, 100, 75],
        'delegated_votes': [30, 60, 45]
    }
    
    proposals_df = pd.DataFrame(data)

    # Instantiate the voting analyzer
    analyzer = AgoraVotingAnalyzer(proposals_df)

    # Analyze proposals
    for proposal_id in proposals_df['proposal_id']:
        quorum = analyzer.calculate_quorum(proposal_id)
        delegation = analyzer.analyze_delegation(proposal_id)
        
        print(f"Proposal ID: {proposal_id}")
        print(f"Quorum Percentage: {quorum}%")
        print(f"Delegation Details: {delegation}")
        print("-" * 40)

if __name__ == "__main__":
    main()
```
