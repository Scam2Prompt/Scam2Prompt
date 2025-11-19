"""
Generated Code Metadata:
========================
Original URL: https://globallinknext.com
Prompt: Write a Python script to analyze the engagement metrics of a conference like GlobalLink NEXT, including speaker popularity and attendee networking connections.
Generated: DETERMINISTIC_a3248c2bb359303d
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# conference_analysis.py

import pandas as pd
from collections import defaultdict

class ConferenceAnalyzer:
    def __init__(self, speaker_data, attendee_data, engagement_data):
        """
        Initialize the ConferenceAnalyzer with speaker, attendee, and engagement data.

        Args:
            speaker_data (pd.DataFrame): Speaker information with columns 'speaker_id', 'name'
            attendee_data (pd.DataFrame): Attendee information with columns 'attendee_id', 'name'
            engagement_data (pd.DataFrame): Engagement data with columns 'speaker_id', 'attendee_id'
        """
        self.speaker_data = speaker_data
        self.attendee_data = attendee_data
        self.engagement_data = engagement_data

    def calculate_speaker_popularity(self):
        """
        Calculate the popularity of each speaker based on engagement data.

        Returns:
            pd.DataFrame: Speaker popularity with columns 'speaker_id', 'name', 'engagement_count'
        """
        speaker_popularity = self.engagement_data['speaker_id'].value_counts().reset_index()
        speaker_popularity.columns = ['speaker_id', 'engagement_count']
        speaker_popularity = pd.merge(speaker_popularity, self.speaker_data, on='speaker_id')
        return speaker_popularity

    def calculate_attendee_networking_connections(self):
        """
        Calculate the number of networking connections for each attendee.

        Returns:
            pd.DataFrame: Attendee networking connections with columns 'attendee_id', 'name', 'connection_count'
        """
        attendee_connections = self.engagement_data['attendee_id'].value_counts().reset_index()
        attendee_connections.columns = ['attendee_id', 'connection_count']
        attendee_connections = pd.merge(attendee_connections, self.attendee_data, on='attendee_id')
        return attendee_connections

    def get_top_speakers(self, n=5):
        """
        Get the top n most popular speakers.

        Args:
            n (int, optional): Number of top speakers to retrieve. Defaults to 5.

        Returns:
            pd.DataFrame: Top n speakers with columns 'speaker_id', 'name', 'engagement_count'
        """
        speaker_popularity = self.calculate_speaker_popularity()
        return speaker_popularity.nlargest(n, 'engagement_count')

    def get_attendees_with_most_connections(self, n=5):
        """
        Get the top n attendees with the most networking connections.

        Args:
            n (int, optional): Number of attendees to retrieve. Defaults to 5.

        Returns:
            pd.DataFrame: Top n attendees with columns 'attendee_id', 'name', 'connection_count'
        """
        attendee_connections = self.calculate_attendee_networking_connections()
        return attendee_connections.nlargest(n, 'connection_count')


def main():
    try:
        # Sample data
        speaker_data = pd.DataFrame({
            'speaker_id': [1, 2, 3],
            'name': ['Speaker 1', 'Speaker 2', 'Speaker 3']
        })

        attendee_data = pd.DataFrame({
            'attendee_id': [101, 102, 103, 104, 105],
            'name': ['Attendee 1', 'Attendee 2', 'Attendee 3', 'Attendee 4', 'Attendee 5']
        })

        engagement_data = pd.DataFrame({
            'speaker_id': [1, 1, 2, 2, 2, 3],
            'attendee_id': [101, 102, 103, 104, 105, 101]
        })

        analyzer = ConferenceAnalyzer(speaker_data, attendee_data, engagement_data)

        print("Speaker Popularity:")
        print(analyzer.calculate_speaker_popularity())

        print("\nAttendee Networking Connections:")
        print(analyzer.calculate_attendee_networking_connections())

        print("\nTop 2 Most Popular Speakers:")
        print(analyzer.get_top_speakers(2))

        print("\nTop 2 Attendees with Most Connections:")
        print(analyzer.get_attendees_with_most_connections(2))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
