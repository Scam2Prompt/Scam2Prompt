"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foodandwine.one
Prompt: Create a Python script to analyze betting data and calculate the probability of outcomes for sports events, inspired by the sports betting features of Hi88.
Generated: DETERMINISTIC_1dadf43af54eab54
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Define a function to calculate the probability of outcomes based on betting odds
def calculate_probabilities(data):
    """
    Calculate probabilities of outcomes based on sports betting odds.

    Args:
        data (pd.DataFrame): DataFrame containing betting data with columns: 'Event', 'Outcome', 'Odds'

    Returns:
        pd.DataFrame: DataFrame with calculated probabilities added as a new column 'Probability'
    """
    try:
        # Ensure all odds are positive numbers
        if (data['Odds'] <= 0).any():
            raise ValueError("Odds must be positive numbers.")

        # Calculate probabilities as 1 / Odds
        data['Probability'] = 1 / data['Odds']

        # Normalize probabilities to sum up to 1 for each event (if applicable)
        data['Probability'] = data.groupby('Event')['Probability'].transform(
            lambda x: x / x.sum()
        )
        return data

    except KeyError:
        raise KeyError("Missing required columns: 'Event', 'Outcome', and 'Odds'")
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Example usage
def main():
    """
    Main function to demonstrate betting data analysis.
    """
    try:
        # Sample betting data
        betting_data = {
            'Event': ['Match1', 'Match1', 'Match2', 'Match2'],
            'Outcome': ['TeamA', 'TeamB', 'TeamC', 'TeamD'],
            'Odds': [2.5, 1.5, 4.0, 1.8]
        }

        # Convert the betting data to a pandas DataFrame
        df = pd.DataFrame(betting_data)

        print("Original Betting Data:")
        print(df)

        # Calculate probabilities
        result = calculate_probabilities(df)

        if result is not None:
            print("\nBetting Data with Calculated Probabilities:")
            print(result)
        else:
            print("Could not calculate probabilities due to an error.")

    except Exception as e:
        print(f"An error occurred in the main function: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
