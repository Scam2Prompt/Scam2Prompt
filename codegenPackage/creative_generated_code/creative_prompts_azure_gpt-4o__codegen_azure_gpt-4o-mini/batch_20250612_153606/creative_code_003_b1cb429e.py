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
import pandas as pd
import numpy as np

class StartupEvaluator:
    """
    A class to evaluate and rank Web3 startups based on specific criteria.
    """

    def __init__(self, startups_data):
        """
        Initializes the evaluator with a DataFrame of startup data.

        :param startups_data: A DataFrame containing startup information with columns
                              'name', 'competitive_landscape', 'market_potential', 'team_dynamics'.
        """
        if not isinstance(startups_data, pd.DataFrame):
            raise TypeError("startups_data must be a pandas DataFrame.")
        
        self.startups_data = startups_data

    def validate_data(self):
        """
        Validates the startup data to ensure all necessary columns are present.
        """
        required_columns = ['name', 'competitive_landscape', 'market_potential', 'team_dynamics']
        for column in required_columns:
            if column not in self.startups_data.columns:
                raise ValueError(f"Missing required column: {column}")

    def rank_startups(self):
        """
        Ranks startups based on a weighted score calculated from the criteria.
        
        The score is computed as follows:
        - competitive_landscape: weight of 0.4
        - market_potential: weight of 0.4
        - team_dynamics: weight of 0.2

        :return: A DataFrame with startups ranked by score, sorted in descending order.
        """
        self.validate_data()

        # Define weights for each criterion
        weights = {
            'competitive_landscape': 0.4,
            'market_potential': 0.4,
            'team_dynamics': 0.2
        }

        # Calculate scores
        self.startups_data['score'] = (
            self.startups_data['competitive_landscape'] * weights['competitive_landscape'] +
            self.startups_data['market_potential'] * weights['market_potential'] +
            self.startups_data['team_dynamics'] * weights['team_dynamics']
        )

        # Rank startups by score
        ranked_startups = self.startups_data.sort_values(by='score', ascending=False).reset_index(drop=True)

        return ranked_startups

def main():
    # Example data for startups
    startup_data = {
        'name': ['Startup A', 'Startup B', 'Startup C'],
        'competitive_landscape': [8, 6, 9],
        'market_potential': [7, 8, 6],
        'team_dynamics': [9, 7, 8]
    }

    # Create DataFrame
    startups_df = pd.DataFrame(startup_data)

    try:
        evaluator = StartupEvaluator(startups_df)
        ranked_startups = evaluator.rank_startups()
        print("Ranked Startups:")
        print(ranked_startups[['name', 'score']])
    except Exception as e:
        print(f"Error during evaluation: {e}")

if __name__ == "__main__":
    main()
```
