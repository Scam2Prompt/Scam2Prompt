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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ProposalAnalyzer:
    """
    A class to analyze the success rate of 'Optimistic Proposals' on the Agora platform.
    """

    def __init__(self, file_path):
        """
        Initializes the ProposalAnalyzer with the given CSV file path.

        :param file_path: Path to the CSV file containing historical voting data.
        """
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the voting data from a CSV file.

        :return: A DataFrame containing the voting data.
        """
        try:
            data = pd.read_csv(self.file_path)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def filter_optimistic_proposals(self):
        """
        Filters the DataFrame for optimistic proposals.

        :return: A DataFrame containing only optimistic proposals.
        """
        optimistic_proposals = self.data[self.data['type'] == 'Optimistic']
        print(f"Filtered {len(optimistic_proposals)} optimistic proposals.")
        return optimistic_proposals

    def calculate_success_rate(self, proposals):
        """
        Calculates the success rate of the given proposals.

        :param proposals: A DataFrame of proposals.
        :return: The success rate as a percentage.
        """
        total_proposals = len(proposals)
        successful_proposals = proposals[proposals['status'] == 'approved']
        success_rate = (len(successful_proposals) / total_proposals) * 100 if total_proposals > 0 else 0
        print(f"Calculated success rate: {success_rate:.2f}%")
        return success_rate

    def visualize_success_rate(self, success_rate):
        """
        Visualizes the success rate using a bar chart.

        :param success_rate: The success rate to visualize.
        """
        plt.bar(['Optimistic Proposals'], [success_rate], color='green')
        plt.ylabel('Success Rate (%)')
        plt.title('Success Rate of Optimistic Proposals on Agora')
        plt.ylim(0, 100)
        plt.grid(axis='y', linestyle='--')
        plt.show()

    def run_analysis(self):
        """
        Runs the analysis for optimistic proposals.
        """
        proposals = self.filter_optimistic_proposals()
        success_rate = self.calculate_success_rate(proposals)
        self.visualize_success_rate(success_rate)

if __name__ == "__main__":
    # Provide the path to the historical voting data CSV file
    file_path = 'historical_voting_data.csv'
    
    # Create an instance of ProposalAnalyzer and run the analysis
    analyzer = ProposalAnalyzer(file_path)
    analyzer.run_analysis()
```

Make sure to replace `'historical_voting_data.csv'` with the actual path to your CSV file containing the historical voting data. The CSV file should have columns `type` and `status` for this code to work correctly.
