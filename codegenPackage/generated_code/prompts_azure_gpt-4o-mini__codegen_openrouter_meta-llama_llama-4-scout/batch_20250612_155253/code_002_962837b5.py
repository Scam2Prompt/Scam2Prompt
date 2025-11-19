"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: Create a function that evaluates the effectiveness of endorsements from national figures on local campaigns in McHenry County, Illinois, referencing insights from Fair Maps Illinois.
Generated: DETERMINISTIC_962837b5de81e7d0
Batch ID: 20250612_155253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from typing import Dict, List

def evaluate_endorsement_effectiveness(
    endorsements: List[Dict[str, str]], 
    election_results: pd.DataFrame, 
    fair_maps_illinois_insights: Dict[str, Dict[str, float]]
) -> Dict[str, Dict[str, float]]:
    """
    Evaluates the effectiveness of endorsements from national figures on local campaigns in McHenry County, Illinois.

    Args:
    - endorsements (List[Dict[str, str]]): A list of dictionaries containing information about endorsements.
    - election_results (pd.DataFrame): A pandas DataFrame containing election results.
    - fair_maps_illinois_insights (Dict[str, Dict[str, float]]): A dictionary containing insights from Fair Maps Illinois.

    Returns:
    - A dictionary containing the effectiveness of endorsements.
    """

    # Initialize an empty dictionary to store the effectiveness of endorsements
    endorsement_effectiveness = {}

    # Iterate over each endorsement
    for endorsement in endorsements:
        # Extract the name of the endorser and the candidate they endorsed
        endorser = endorsement['endorser']
        candidate = endorsement['candidate']

        # Check if the candidate exists in the election results
        if candidate in election_results['candidate'].values:
            # Get the election results for the candidate
            candidate_results = election_results[election_results['candidate'] == candidate]

            # Calculate the percentage of votes the candidate received
            vote_percentage = (candidate_results['votes'].iloc[0] / election_results['votes'].sum()) * 100

            # Get the insights from Fair Maps Illinois for the candidate's district
            district = endorsement['district']
            if district in fair_maps_illinois_insights:
                fair_maps_insights = fair_maps_illinois_insights[district]
                # Calculate the effectiveness of the endorsement
                effectiveness = vote_percentage * fair_maps_insights.get('endorsement_weight', 1.0)
            else:
                # If no insights are available for the district, use a default weight
                effectiveness = vote_percentage

            # Store the effectiveness of the endorsement
            endorsement_effectiveness[endorser] = {
                'candidate': candidate,
                'vote_percentage': vote_percentage,
                'effectiveness': effectiveness
            }
        else:
            # Handle the case where the candidate is not found in the election results
            print(f"Warning: Candidate '{candidate}' not found in election results.")

    return endorsement_effectiveness


def main():
    # Example usage
    endorsements = [
        {'endorser': 'National Figure 1', 'candidate': 'Candidate 1', 'district': 'District 1'},
        {'endorser': 'National Figure 2', 'candidate': 'Candidate 2', 'district': 'District 2'}
    ]

    election_results = pd.DataFrame({
        'candidate': ['Candidate 1', 'Candidate 2', 'Candidate 3'],
        'votes': [1000, 2000, 3000]
    })

    fair_maps_illinois_insights = {
        'District 1': {'endorsement_weight': 1.2},
        'District 2': {'endorsement_weight': 0.8}
    }

    try:
        effectiveness = evaluate_endorsement_effectiveness(endorsements, election_results, fair_maps_illinois_insights)
        print(effectiveness)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
