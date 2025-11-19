"""
Generated Code Metadata:
========================
Original URL: https://arkventure.net
Prompt: Develop a script to analyze the diversification level of the ARK Venture Fund, given its classification as a "non-diversified" investment company.
Generated: DETERMINISTIC_d4fb15b8c830d9d7
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

def calculate_diversification_level(holdings, threshold=5):
    """
    Calculate the diversification level of a fund.

    Parameters:
    holdings (pd.DataFrame): A DataFrame containing the holdings of the fund.
                             It should have a 'Name' column for the holding names
                             and a 'Percentage' column for their respective percentages.
    threshold (int): The maximum percentage any single holding can have to be considered diversified.

    Returns:
    diversification_level (str): The diversification level of the fund.
    """

    # Ensure the input is a DataFrame
    if not isinstance(holdings, pd.DataFrame):
        raise ValueError("Holdings must be a pandas DataFrame")

    # Check for required columns
    required_columns = ['Name', 'Percentage']
    if not all(column in holdings.columns for column in required_columns):
        raise ValueError("Holdings DataFrame must contain 'Name' and 'Percentage' columns")

    # Calculate the total percentage of the top holdings
    top_holdings = holdings.nlargest(1, 'Percentage')
    max_percentage = top_holdings['Percentage'].values[0]

    # Determine the diversification level
    if max_percentage > threshold:
        diversification_level = "Non-Diversified"
    else:
        diversification_level = "Diversified"

    return diversification_level


def analyze_ark_venture_fund(holdings_data):
    """
    Analyze the diversification level of the ARK Venture Fund.

    Parameters:
    holdings_data (dict or pd.DataFrame): A dictionary or DataFrame containing the holdings data of the ARK Venture Fund.
                                          It should have a 'Name' key/column for the holding names
                                          and a 'Percentage' key/column for their respective percentages.

    Returns:
    analysis_result (dict): A dictionary containing the analysis result.
    """

    # Convert holdings data to DataFrame if it's a dictionary
    if isinstance(holdings_data, dict):
        holdings = pd.DataFrame(holdings_data)
    else:
        holdings = holdings_data

    try:
        diversification_level = calculate_diversification_level(holdings)
        analysis_result = {
            "Diversification Level": diversification_level,
            "Holdings Data": holdings.to_dict(orient='records')
        }
        return analysis_result
    except Exception as e:
        analysis_result = {
            "Error": str(e)
        }
        return analysis_result


# Example usage
if __name__ == "__main__":
    holdings_data = [
        {"Name": "Holding1", "Percentage": 30},
        {"Name": "Holding2", "Percentage": 20},
        {"Name": "Holding3", "Percentage": 15},
        {"Name": "Holding4", "Percentage": 10},
        {"Name": "Holding5", "Percentage": 25}
    ]

    analysis_result = analyze_ark_venture_fund(holdings_data)
    print(analysis_result)
```
