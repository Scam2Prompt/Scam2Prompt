"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: Generate code to simulate the impact of third-party candidates on election outcomes in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_ba0cfa0e2aea32e3
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ElectionSimulator:
    """
    A class to simulate the impact of third-party candidates on election outcomes.
    """

    def __init__(self, total_voters, main_candidate_share, third_party_share):
        """
        Initializes the ElectionSimulator with the number of voters and candidate shares.

        :param total_voters: Total number of voters in the election.
        :param main_candidate_share: Percentage of votes for the main candidate (0-1).
        :param third_party_share: Percentage of votes for the third-party candidate (0-1).
        """
        self.total_voters = total_voters
        self.main_candidate_share = main_candidate_share
        self.third_party_share = third_party_share
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates the input parameters to ensure they are within acceptable ranges.
        """
        if not (0 <= self.main_candidate_share <= 1):
            raise ValueError("Main candidate share must be between 0 and 1.")
        if not (0 <= self.third_party_share <= 1):
            raise ValueError("Third party share must be between 0 and 1.")
        if self.main_candidate_share + self.third_party_share > 1:
            raise ValueError("The sum of main candidate share and third-party share must not exceed 1.")

    def simulate_election(self, num_simulations=10000):
        """
        Simulates the election outcome over a specified number of simulations.

        :param num_simulations: Number of simulations to run.
        :return: A DataFrame containing the results of the simulations.
        """
        results = {
            'Main Candidate Wins': 0,
            'Third Party Wins': 0,
            'Main Candidate Loses': 0
        }

        for _ in range(num_simulations):
            # Simulate votes
            votes = np.random.rand(self.total_voters)
            main_candidate_votes = np.sum(votes < self.main_candidate_share)
            third_party_votes = np.sum((votes >= self.main_candidate_share) & (votes < self.main_candidate_share + self.third_party_share))
            other_votes = self.total_voters - main_candidate_votes - third_party_votes

            # Determine outcome
            if main_candidate_votes > third_party_votes:
                results['Main Candidate Wins'] += 1
            elif third_party_votes > main_candidate_votes:
                results['Third Party Wins'] += 1
            else:
                results['Main Candidate Loses'] += 1

        return pd.DataFrame.from_dict(results, orient='index', columns=['Count'])

    def plot_results(self, results):
        """
        Plots the results of the election simulations.

        :param results: A DataFrame containing the results of the simulations.
        """
        results.plot(kind='bar', legend=False)
        plt.title('Election Simulation Results')
        plt.xlabel('Outcome')
        plt.ylabel('Number of Simulations')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # Example usage
    try:
        total_voters = 10000
        main_candidate_share = 0.55  # 55% of the votes
        third_party_share = 0.10      # 10% of the votes

        simulator = ElectionSimulator(total_voters, main_candidate_share, third_party_share)
        results = simulator.simulate_election()
        print(results)
        simulator.plot_results(results)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
