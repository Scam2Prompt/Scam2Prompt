"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Create a digital marketing campaign script using Python, incorporating strategies from PDMA's Digital Marketing Professional program, such as audience segmentation and A/B testing.
Generated: DETERMINISTIC_ef63ca24e142c71c
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import pandas as pd
from typing import List, Dict, Any

class DigitalMarketingCampaign:
    def __init__(self, audience_data: pd.DataFrame):
        """
        Initialize the DigitalMarketingCampaign with audience data.

        :param audience_data: DataFrame containing audience information.
        """
        if audience_data.empty:
            raise ValueError("Audience data cannot be empty.")
        self.audience_data = audience_data

    def segment_audience(self, criteria: Dict[str, Any]) -> pd.DataFrame:
        """
        Segment the audience based on given criteria.

        :param criteria: A dictionary where the key is the column name and the value is the value to filter by.
        :return: A DataFrame of the segmented audience.
        """
        # Ensure criteria is not empty
        if not criteria:
            raise ValueError("Criteria for segmentation cannot be empty.")

        segmented_audience = self.audience_data.copy()
        for key, value in criteria.items():
            if key in segmented_audience.columns:
                segmented_audience = segmented_audience[segmented_audience[key] == value]
            else:
                raise KeyError(f"Column '{key}' not found in audience data.")

        return segmented_audience

    def conduct_ab_testing(self, control_group: pd.DataFrame, test_group: pd.DataFrame) -> Dict[str, float]:
        """
        Conduct A/B testing between control and test groups.

        :param control_group: DataFrame for the control group.
        :param test_group: DataFrame for the test group.
        :return: A dictionary with statistics from the A/B test.
        """
        if control_group.empty or test_group.empty:
            raise ValueError("Control and test groups must not be empty.")

        # Simulated conversion rates (for demonstration purposes)
        control_conversion_rate = random.uniform(0.05, 0.15)
        test_conversion_rate = random.uniform(0.10, 0.20)

        results = {
            "Control Group Conversion Rate": control_conversion_rate,
            "Test Group Conversion Rate": test_conversion_rate,
            "Lift": test_conversion_rate - control_conversion_rate
        }

        return results

def main():
    # Example audience data
    data = {
        'Age': [25, 30, 35, 40, 25, 30, 35, 40],
        'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
        'Interest': ['Tech', 'Travel', 'Tech', 'Travel', 'Food', 'Food', 'Travel', 'Tech']
    }
    
    audience_data = pd.DataFrame(data)

    # Initialize campaign
    campaign = DigitalMarketingCampaign(audience_data)

    # Segment audience based on defined criteria
    criteria = {'Interest': 'Tech'}
    segmented_audience = campaign.segment_audience(criteria)
    print(f"Segmented Audience:\n{segmented_audience}\n")

    # Conduct A/B testing
    control_group = segmented_audience.sample(frac=0.5, random_state=42)
    test_group = segmented_audience.drop(control_group.index)

    ab_test_results = campaign.conduct_ab_testing(control_group, test_group)
    print(f"A/B Test Results:\n{ab_test_results}\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
