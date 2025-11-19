"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfi.pages.dev
Prompt: Write a Python script to analyze the tokenomics of a cryptocurrency project, focusing on non-transferable tokens and their impact on liquidity and governance.
Generated: DETERMINISTIC_2a0d3acabd479070
Batch ID: 20250612_155255
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
from typing import List, Dict

class TokenomicsAnalyzer:
    """
    A class to analyze the tokenomics of a cryptocurrency project,
    focusing on non-transferable tokens and their impact on liquidity 
    and governance.
    """

    def __init__(self, token_data: pd.DataFrame):
        """
        Initializes the TokenomicsAnalyzer with token data.

        :param token_data: DataFrame containing tokenomics data.
        """
        self.token_data = token_data

    def validate_data(self):
        """
        Validates the token data to ensure necessary columns are present.
        Raises ValueError if required columns are missing.
        """
        required_columns = ['token_id', 'is_transferable', 'liquidity', 'governance_score']
        missing_columns = [col for col in required_columns if col not in self.token_data.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in token data: {', '.join(missing_columns)}")

    def analyze_non_transferable_tokens(self) -> Dict[str, float]:
        """
        Analyzes non-transferable tokens and returns their total liquidity 
        and average governance score.

        :return: A dictionary with total liquidity and average governance score.
        """
        self.validate_data()

        # Filter non-transferable tokens
        non_transferable_tokens = self.token_data[self.token_data['is_transferable'] == False]

        # Calculate total liquidity and average governance score
        total_liquidity = non_transferable_tokens['liquidity'].sum()
        average_governance_score = non_transferable_tokens['governance_score'].mean()

        return {
            'total_liquidity': total_liquidity,
            'average_governance_score': average_governance_score
        }

    def get_summary(self) -> None:
        """
        Prints a summary of the analysis results for non-transferable tokens.
        """
        try:
            results = self.analyze_non_transferable_tokens()
            print("Non-Transferable Tokens Analysis:")
            print(f"Total Liquidity: {results['total_liquidity']}")
            print(f"Average Governance Score: {results['average_governance_score']:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Sample tokenomics data for testing
    sample_data = {
        'token_id': [1, 2, 3, 4, 5],
        'is_transferable': [False, True, False, True, False],
        'liquidity': [1000, 1500, 2000, 2500, 3000],
        'governance_score': [70, 80, 60, 90, 75]
    }

    # Create a DataFrame from the sample data
    token_data_df = pd.DataFrame(sample_data)

    # Initialize the TokenomicsAnalyzer
    analyzer = TokenomicsAnalyzer(token_data_df)

    # Get and print summary analysis
    analyzer.get_summary()
```
