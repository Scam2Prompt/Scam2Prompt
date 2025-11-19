"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maiv-whitelist.pages.dev
Prompt: Generate a Python script that assesses investment preferences based on varying returns and durations offered by MAIV.
Generated: DETERMINISTIC_61e3317265bafda2
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class InvestmentPreferenceAssessor:
    """
    A class to assess investment preferences based on varying returns
    and durations.
    """

    def __init__(self, investments):
        """
        Initializes the InvestmentPreferenceAssessor with a list of investments.

        :param investments: A list of dictionaries representing investment options.
        """
        self.investments = investments

    def assess_preferences(self):
        """
        Assesses investment preferences based on returns and durations.

        :return: A DataFrame containing assessed investments with preference score.
        """
        try:
            # Create a DataFrame from the investments
            df = pd.DataFrame(self.investments)
            
            # Check for required columns
            if not all(col in df.columns for col in ['name', 'return', 'duration']):
                raise ValueError("Investments must contain 'name', 'return', and 'duration' columns.")

            # Normalize return and duration for scoring
            df['normalized_return'] = (df['return'] - df['return'].min()) / (df['return'].max() - df['return'].min())
            df['normalized_duration'] = (df['duration'] - df['duration'].min()) / (df['duration'].max() - df['duration'].min())

            # Calculate preference score (higher is better)
            df['preference_score'] = df['normalized_return'] * (1 - df['normalized_duration'])

            return df[['name', 'preference_score']].sort_values(by='preference_score', ascending=False)

        except Exception as e:
            print(f"Error in assessing preferences: {e}")
            return None


if __name__ == "__main__":
    # Sample investment data
    investments = [
        {'name': 'Investment A', 'return': 5, 'duration': 12},
        {'name': 'Investment B', 'return': 7, 'duration': 24},
        {'name': 'Investment C', 'return': 6, 'duration': 18},
        {'name': 'Investment D', 'return': 8, 'duration': 36},
    ]

    # Instantiate the assessor
    assessor = InvestmentPreferenceAssessor(investments)

    # Assess preferences
    assessed_investments = assessor.assess_preferences()

    if assessed_investments is not None:
        print("Investment Preferences Assessment:")
        print(assessed_investments)
    else:
        print("No assessment could be made.")
```
