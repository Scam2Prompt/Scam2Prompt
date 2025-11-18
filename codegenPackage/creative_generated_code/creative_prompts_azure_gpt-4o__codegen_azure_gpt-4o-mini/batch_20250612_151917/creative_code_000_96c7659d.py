"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfi.pages.dev
Prompt: Write a Python script to analyze the tokenomics of a cryptocurrency project with non-transferable tokens, similar to WorldLibertyFi, focusing on governance participation and liquidity constraints.
Generated: DETERMINISTIC_96c7659d9f2dfd26
Batch ID: 20250612_151917
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

class TokenomicsAnalyzer:
    """
    A class to analyze the tokenomics of a cryptocurrency project with non-transferable tokens.
    
    Attributes:
        data (pd.DataFrame): A DataFrame containing token metrics.
    """

    def __init__(self, data):
        """
        Initializes the TokenomicsAnalyzer with the provided data.
        
        Parameters:
            data (pd.DataFrame): A DataFrame containing tokenomics data.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the input data to ensure it has the necessary columns.
        
        Raises:
            ValueError: If the required columns are not present in the DataFrame.
        """
        required_columns = ['token_holders', 'votes_casted', 'liquidity']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def participation_rate(self):
        """
        Calculates the governance participation rate.
        
        Returns:
            float: The participation rate as a percentage.
        """
        total_holders = self.data['token_holders'].sum()
        total_votes = self.data['votes_casted'].sum()
        participation = (total_votes / total_holders) * 100 if total_holders > 0 else 0
        return participation

    def liquidity_ratio(self):
        """
        Calculates the liquidity ratio.
        
        Returns:
            float: The average liquidity per token holder.
        """
        total_liquidity = self.data['liquidity'].sum()
        total_holders = self.data['token_holders'].sum()
        liquidity_ratio = total_liquidity / total_holders if total_holders > 0 else 0
        return liquidity_ratio

    def analyze(self):
        """
        Performs the analysis of tokenomics and returns the results.
        
        Returns:
            dict: A dictionary containing participation rate and liquidity ratio.
        """
        self.validate_data()
        
        participation = self.participation_rate()
        liquidity = self.liquidity_ratio()
        
        return {
            'participation_rate': participation,
            'liquidity_ratio': liquidity
        }

# Sample usage
if __name__ == "__main__":
    # Example tokenomics data
    sample_data = {
        'token_holders': [100, 200, 150],
        'votes_casted': [75, 100, 50],
        'liquidity': [1000, 2000, 1500]
    }
    
    # Create DataFrame
    tokenomics_df = pd.DataFrame(sample_data)
    
    # Initialize analyzer
    analyzer = TokenomicsAnalyzer(tokenomics_df)
    
    try:
        # Perform analysis
        results = analyzer.analyze()
        print("Tokenomics Analysis Results:")
        print(f"Participation Rate: {results['participation_rate']}%")
        print(f"Liquidity Ratio: {results['liquidity_ratio']}")
    except ValueError as e:
        print(f"Error in analysis: {e}")
```
