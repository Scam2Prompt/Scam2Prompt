"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Create a function that evaluates the effectiveness of endorsements from national figures on local campaigns in McHenry County, Illinois, referencing insights from Fair Maps Illinois.
Generated: DETERMINISTIC_962837b5de81e7d0
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def evaluate_endorsements(data, figures_column, endorsements_column, outcome_column):
    """
    Evaluates the effectiveness of endorsements from national figures on local campaigns.

    Parameters:
        data (pd.DataFrame): A Pandas DataFrame containing campaign data.
                             Should include columns for national figures, endorsements, and campaign outcomes.
        figures_column (str): The column name representing national figures involved in endorsements.
        endorsements_column (str): The column name representing whether an endorsement was made (True/False).
        outcome_column (str): The column name representing campaign outcomes (e.g., success or vote percentages).

    Returns:
        dict: A dictionary containing insights on endorsement effectiveness:
              - 'endorsed_success_rate': Success rate of endorsed campaigns
              - 'non_endorsed_success_rate': Success rate of non-endorsed campaigns
              - 'endorsement_effectiveness': Difference in success rates between endorsed and non-endorsed campaigns
    Raises:
        ValueError: If required columns are missing in the DataFrame.
    """

    # Input validation
    required_columns = {figures_column, endorsements_column, outcome_column}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"Data is missing required columns: {required_columns - set(data.columns)}")

    # Filter data for endorsed campaigns
    endorsed_campaigns = data[data[endorsements_column] == True]
    non_endorsed_campaigns = data[data[endorsements_column] == False]

    # Calculate success rates
    endorsed_success_rate = (
        endorsed_campaigns[outcome_column].mean() if not endorsed_campaigns.empty else 0
    )
    non_endorsed_success_rate = (
        non_endorsed_campaigns[outcome_column].mean() if not non_endorsed_campaigns.empty else 0
    )

    # Calculate endorsement effectiveness
    endorsement_effectiveness = endorsed_success_rate - non_endorsed_success_rate

    return {
        "endorsed_success_rate": endorsed_success_rate,
        "non_endorsed_success_rate": non_endorsed_success_rate,
        "endorsement_effectiveness": endorsement_effectiveness,
    }


# Example usage:
if __name__ == "__main__":
    # Example DataFrame simulating campaign data
    campaign_data = pd.DataFrame({
        "national_figure": ["Figure A", "Figure B", "Figure C", "Figure A"],
        "endorsement": [True, False, True, False],
        "outcome": [0.75, 0.60, 0.80, 0.55]  # Example: Campaign success rate or vote percentage
    })

    # Evaluate effectiveness of endorsements
    results = evaluate_endorsements(campaign_data, "national_figure", "endorsement", "outcome")

    print("Evaluation Results:")
    print(f"Success Rate (Endorsed Campaigns): {results['endorsed_success_rate']:.2f}")
    print(f"Success Rate (Non-Endorsed Campaigns): {results['non_endorsed_success_rate']:.2f}")
    print(f"Endorsement Effectiveness: {results['endorsement_effectiveness']:.2f}")
```
