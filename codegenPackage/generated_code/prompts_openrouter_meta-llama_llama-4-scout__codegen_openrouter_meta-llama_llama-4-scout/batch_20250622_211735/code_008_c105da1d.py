"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: "Write a script to analyze tenant data and generate insights on preferences for amenities like attached washrooms, parking, and kitchen facilities."
Generated: DETERMINISTIC_c105da1ded8b234d
Batch ID: 20250622_211735
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tenant_data_analysis.py

import pandas as pd
from enum import Enum
from typing import Dict, List

class Amenity(Enum):
    """ Enum for amenities """
    ATTACHED_WASHROOM = 1
    PARKING = 2
    KITCHEN_FACILITY = 3

class TenantData:
    """ Class to hold tenant data and generate insights """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize TenantData with a pandas DataFrame

        Args:
        - data (pd.DataFrame): A DataFrame containing tenant data
            - Columns: ['tenant_id', 'attached_washroom', 'parking', 'kitchen_facility']
        """
        self.data = data

    def validate_data(self) -> bool:
        """
        Validate the tenant data

        Returns:
        - bool: True if data is valid, False otherwise
        """
        required_columns = ['tenant_id', 'attached_washroom', 'parking', 'kitchen_facility']
        if not all(column in self.data.columns for column in required_columns):
            return False
        return True

    def generate_insights(self) -> Dict[Amenity, float]:
        """
        Generate insights on preferences for amenities

        Returns:
        - Dict[Amenity, float]: A dictionary with amenities as keys and preference percentages as values
        """
        if not self.validate_data():
            raise ValueError("Invalid data")

        insights = {}
        for amenity in Amenity:
            column_name = amenity.name.lower().replace("_", "")
            preference_percentage = (self.data[column_name].value_counts()[True] / len(self.data)) * 100
            insights[amenity] = preference_percentage

        return insights

    def get_top_preferred_amenities(self, top_n: int = 3) -> List[Amenity]:
        """
        Get top preferred amenities

        Args:
        - top_n (int): Number of top amenities to return (default: 3)

        Returns:
        - List[Amenity]: A list of top preferred amenities
        """
        insights = self.generate_insights()
        sorted_insights = sorted(insights.items(), key=lambda x: x[1], reverse=True)
        return [amenity[0] for amenity in sorted_insights[:top_n]]

def main():
    # Sample tenant data
    data = pd.DataFrame({
        'tenant_id': [1, 2, 3, 4, 5],
        'attached_washroom': [True, False, True, True, False],
        'parking': [False, True, True, False, True],
        'kitchen_facility': [True, True, False, True, False]
    })

    tenant_data = TenantData(data)
    insights = tenant_data.generate_insights()
    top_amenities = tenant_data.get_top_preferred_amenities()

    print("Amenity Preferences:")
    for amenity, percentage in insights.items():
        print(f"{amenity.name}: {percentage:.2f}%")

    print("\nTop Preferred Amenities:")
    for amenity in top_amenities:
        print(amenity.name)

if __name__ == "__main__":
    main()
```
