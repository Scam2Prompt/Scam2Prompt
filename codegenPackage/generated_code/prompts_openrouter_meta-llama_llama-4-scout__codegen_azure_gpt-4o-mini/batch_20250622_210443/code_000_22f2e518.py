"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: "Write a Python script to optimize business management and talent selection processes for a company looking to internationalize, considering factors such as cost competitiveness and expertise in multiple sectors."
Generated: DETERMINISTIC_22f2e51867b3cbe1
Batch ID: 20250622_210443
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

class TalentSelector:
    """
    A class to optimize talent selection for international business management.
    """

    def __init__(self, talent_data):
        """
        Initializes the TalentSelector with talent data.

        :param talent_data: DataFrame containing talent information.
        """
        self.talent_data = talent_data

    def filter_talent(self, cost_limit, expertise_required):
        """
        Filters talent based on cost competitiveness and required expertise.

        :param cost_limit: Maximum cost per talent.
        :param expertise_required: List of required expertise sectors.
        :return: Filtered DataFrame of talents.
        """
        try:
            # Filter by cost
            filtered_by_cost = self.talent_data[self.talent_data['Cost'] <= cost_limit]
            # Filter by expertise
            filtered_by_expertise = filtered_by_cost[
                filtered_by_cost['Expertise'].apply(lambda x: any(exp in x for exp in expertise_required))
            ]
            return filtered_by_expertise
        except Exception as e:
            print(f"Error filtering talent: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error

    def rank_talent(self, filtered_talent):
        """
        Ranks the filtered talent based on their experience and cost.

        :param filtered_talent: DataFrame of filtered talents.
        :return: Ranked DataFrame of talents.
        """
        try:
            # Calculate a score based on experience and cost
            filtered_talent['Score'] = (filtered_talent['Experience'] / filtered_talent['Cost'])
            ranked_talent = filtered_talent.sort_values(by='Score', ascending=False)
            return ranked_talent
        except Exception as e:
            print(f"Error ranking talent: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error

def main():
    # Sample data for talents
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Cost': [5000, 7000, 3000, 4000],
        'Experience': [5, 7, 3, 4],
        'Expertise': [['Finance', 'IT'], ['Marketing'], ['IT', 'HR'], ['Finance', 'Marketing']]
    }

    # Create a DataFrame
    talent_df = pd.DataFrame(data)

    # Initialize the TalentSelector
    selector = TalentSelector(talent_df)

    # Define cost limit and required expertise
    cost_limit = 6000
    expertise_required = ['IT', 'Finance']

    # Filter and rank talent
    filtered_talent = selector.filter_talent(cost_limit, expertise_required)
    ranked_talent = selector.rank_talent(filtered_talent)

    # Display the ranked talent
    print("Ranked Talent:")
    print(ranked_talent[['Name', 'Cost', 'Experience', 'Score']])

if __name__ == "__main__":
    main()
```
