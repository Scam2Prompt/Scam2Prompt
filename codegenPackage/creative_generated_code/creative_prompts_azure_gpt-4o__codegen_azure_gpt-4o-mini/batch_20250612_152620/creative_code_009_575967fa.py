"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-link.pages.dev
Prompt: Generate code to filter and exclude participants from restricted countries in IDOs hosted on TrustPad, based on the provided exclusion list.
Generated: DETERMINISTIC_575967faf02b50bf
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd

class ParticipantFilter:
    def __init__(self, exclusion_list):
        """
        Initializes the ParticipantFilter with an exclusion list.

        Parameters:
        exclusion_list (list): A list of restricted countries to exclude participants from.
        """
        self.exclusion_list = exclusion_list

    def filter_participants(self, participants_df):
        """
        Filters out participants from restricted countries.

        Parameters:
        participants_df (pd.DataFrame): DataFrame containing participant data with a column 'country'.

        Returns:
        pd.DataFrame: A DataFrame containing only participants from allowed countries.
        """
        # Check if the required column exists in the DataFrame
        if 'country' not in participants_df.columns:
            raise ValueError("Input DataFrame must contain a 'country' column.")

        # Filter out participants from excluded countries
        filtered_df = participants_df[~participants_df['country'].isin(self.exclusion_list)]

        return filtered_df

def main():
    # Example exclusion list of restricted countries
    exclusion_list = ['North Korea', 'Iran', 'Syria', 'Cuba']

    # Example participant data
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'country': ['USA', 'North Korea', 'Canada', 'Iran']
    }
    
    # Create a DataFrame from the participant data
    participants_df = pd.DataFrame(data)

    # Initialize the ParticipantFilter
    participant_filter = ParticipantFilter(exclusion_list)

    # Filter participants based on the exclusion list
    try:
        allowed_participants = participant_filter.filter_participants(participants_df)
        print("Allowed Participants:")
        print(allowed_participants)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
