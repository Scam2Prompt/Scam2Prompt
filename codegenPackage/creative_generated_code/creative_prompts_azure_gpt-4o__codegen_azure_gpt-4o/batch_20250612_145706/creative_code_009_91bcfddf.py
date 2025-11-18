"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-guh1xmcsb-voteagora.vercel.app
Prompt: Create a program to analyze the success rate of "Optimistic Proposals" on the Agora platform based on historical voting data.
Generated: DETERMINISTIC_91bcfddfa753b0a0
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import csv
from typing import List, Dict


class AgoraProposalAnalyzer:
    """
    Class to analyze the success rate of 'Optimistic Proposals' on the Agora platform
    based on historical voting data.
    """

    def __init__(self, data_file: str):
        """
        Initialize the analyzer with the path to the data file.

        Args:
            data_file (str): Path to the JSON or CSV file containing proposal data.
        """
        self.data_file = data_file
        self.proposals = []

    def load_data(self) -> None:
        """
        Load historical voting data from the specified file.
        Supports both JSON and CSV formats.
        """
        try:
            if self.data_file.endswith('.json'):
                with open(self.data_file, 'r') as file:
                    self.proposals = json.load(file)
            elif self.data_file.endswith('.csv'):
                with open(self.data_file, 'r') as file:
                    reader = csv.DictReader(file)
                    self.proposals = [row for row in reader]
            else:
                raise ValueError("Unsupported file format. Use JSON or CSV.")

            # Standardize keys for consistency
            for proposal in self.proposals:
                proposal['type'] = proposal.get('type', '').lower()
                proposal['status'] = proposal.get('status', '').lower()
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Error loading data: {e}")

    def calculate_success_rate(self) -> float:
        """
        Calculate the success rate of 'Optimistic Proposals'.

        Returns:
            float: The success rate as a percentage (0 to 100).
        """
        if not self.proposals:
            raise RuntimeError("No proposals loaded. Call load_data() first.")

        optimistic_proposals = [
            proposal for proposal in self.proposals if proposal['type'] == 'optimistic'
        ]
        if not optimistic_proposals:
            return 0.0  # No optimistic proposals to analyze

        successful_proposals = [
            proposal for proposal in optimistic_proposals if proposal['status'] == 'successful'
        ]

        success_rate = (len(successful_proposals) / len(optimistic_proposals)) * 100
        return success_rate

    def analyze(self) -> Dict:
        """
        Perform the analysis and return a summary.

        Returns:
            dict: A dictionary containing the total number of optimistic proposals,
                  the number of successful proposals, and the success rate.
        """
        if not self.proposals:
            raise RuntimeError("No proposals loaded. Call load_data() first.")

        optimistic_proposals = [
            proposal for proposal in self.proposals if proposal['type'] == 'optimistic'
        ]
        successful_proposals = [
            proposal for proposal in optimistic_proposals if proposal['status'] == 'successful'
        ]

        return {
            "total_optimistic_proposals": len(optimistic_proposals),
            "successful_proposals": len(successful_proposals),
            "success_rate": self.calculate_success_rate(),
        }


if __name__ == "__main__":
    # Example usage
    data_file_path = "voting_data.json"  # Replace with your file path
    analyzer = AgoraProposalAnalyzer(data_file_path)

    try:
        # Load data and perform analysis
        analyzer.load_data()
        summary = analyzer.analyze()

        # Output the results
        print("Analysis Summary:")
        print(f"Total Optimistic Proposals: {summary['total_optimistic_proposals']}")
        print(f"Successful Proposals: {summary['successful_proposals']}")
        print(f"Success Rate: {summary['success_rate']:.2f}%")
    except RuntimeError as e:
        print(f"Error: {e}")
```
