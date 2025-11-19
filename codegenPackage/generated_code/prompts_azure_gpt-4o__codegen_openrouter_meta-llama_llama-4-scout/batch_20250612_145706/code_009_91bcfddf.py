"""
Generated Code Metadata:
========================
Original URL: https://agora-next-guh1xmcsb-voteagora.vercel.app
Prompt: Create a program to analyze the success rate of "Optimistic Proposals" on the Agora platform based on historical voting data.
Generated: DETERMINISTIC_91bcfddfa753b0a0
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# optimistic_proposal_analyzer.py

import pandas as pd
from typing import Dict, List

class OptimisticProposalAnalyzer:
    """
    Analyzes the success rate of Optimistic Proposals on the Agora platform based on historical voting data.
    """

    def __init__(self, voting_data: pd.DataFrame):
        """
        Initializes the analyzer with historical voting data.

        Args:
        - voting_data (pd.DataFrame): A DataFrame containing historical voting data.
            It should have the following columns:
            - 'proposal_id' (int): The ID of the proposal.
            - 'vote' (str): The vote type ('yes' or 'no').
            - 'voter_weight' (float): The weight of the voter's vote.
        """
        self.voting_data = voting_data

    def calculate_success_rate(self) -> float:
        """
        Calculates the overall success rate of Optimistic Proposals.

        Returns:
        - success_rate (float): The success rate of Optimistic Proposals.
        """
        # Group voting data by proposal ID and calculate the total weight of yes votes
        proposal_votes = self.voting_data.groupby('proposal_id')['voter_weight'].apply(lambda x: x[self.voting_data.loc[x.index, 'vote'] == 'yes'].sum()).reset_index()
        proposal_votes.columns = ['proposal_id', 'yes_votes']

        # Merge proposal votes with total votes
        total_votes = self.voting_data.groupby('proposal_id')['voter_weight'].sum().reset_index()
        total_votes.columns = ['proposal_id', 'total_votes']
        proposal_votes = pd.merge(proposal_votes, total_votes, on='proposal_id')

        # Calculate success rate
        proposal_votes['success'] = proposal_votes.apply(lambda row: 1 if row['yes_votes'] > row['total_votes'] / 2 else 0, axis=1)
        success_rate = proposal_votes['success'].mean()

        return success_rate

    def get_proposal_success_rates(self) -> pd.DataFrame:
        """
        Calculates the success rate of each Optimistic Proposal.

        Returns:
        - proposal_success_rates (pd.DataFrame): A DataFrame containing the success rate of each proposal.
        """
        # Group voting data by proposal ID and calculate the total weight of yes votes
        proposal_votes = self.voting_data.groupby('proposal_id')['voter_weight'].apply(lambda x: x[self.voting_data.loc[x.index, 'vote'] == 'yes'].sum()).reset_index()
        proposal_votes.columns = ['proposal_id', 'yes_votes']

        # Merge proposal votes with total votes
        total_votes = self.voting_data.groupby('proposal_id')['voter_weight'].sum().reset_index()
        total_votes.columns = ['proposal_id', 'total_votes']
        proposal_votes = pd.merge(proposal_votes, total_votes, on='proposal_id')

        # Calculate success rate
        proposal_votes['success_rate'] = proposal_votes.apply(lambda row: row['yes_votes'] / row['total_votes'], axis=1)

        return proposal_votes[['proposal_id', 'success_rate']]

def main():
    try:
        # Load historical voting data
        voting_data = pd.read_csv('voting_data.csv')

        # Create an instance of the analyzer
        analyzer = OptimisticProposalAnalyzer(voting_data)

        # Calculate overall success rate
        success_rate = analyzer.calculate_success_rate()
        print(f"Overall Success Rate: {success_rate:.2%}")

        # Get proposal success rates
        proposal_success_rates = analyzer.get_proposal_success_rates()
        print(proposal_success_rates)

    except FileNotFoundError:
        print("Error: Voting data file not found.")
    except pd.errors.EmptyDataError:
        print("Error: Voting data file is empty.")
    except pd.errors.ParserError:
        print("Error: Failed to parse voting data file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
