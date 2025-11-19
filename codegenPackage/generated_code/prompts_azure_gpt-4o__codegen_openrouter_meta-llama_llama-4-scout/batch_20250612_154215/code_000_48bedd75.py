"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Write Python code to analyze esports tournament data, incorporating features like hosting, administration, and statistics, as described by Ace Pro Sports Technologies in Kenya.
Generated: DETERMINISTIC_48bedd75a1ad7fc9
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# esports_tournament_analysis.py

import pandas as pd
from datetime import datetime

class EsportsTournament:
    def __init__(self, data):
        """
        Initialize an EsportsTournament object.

        Args:
            data (dict): A dictionary containing tournament data.
        """
        self.data = pd.DataFrame(data)

    def validate_data(self):
        """
        Validate the tournament data.

        Raises:
            ValueError: If the data is invalid.
        """
        required_columns = ['tournament_name', 'start_date', 'end_date', 'host', 'administrator']
        if not all(column in self.data.columns for column in required_columns):
            raise ValueError("Invalid data: missing required columns")

    def calculate_duration(self):
        """
        Calculate the duration of the tournament.

        Returns:
            pandas.Series: A series containing the tournament duration in days.
        """
        self.data['start_date'] = pd.to_datetime(self.data['start_date'])
        self.data['end_date'] = pd.to_datetime(self.data['end_date'])
        return (self.data['end_date'] - self.data['start_date']).dt.days

    def get_hosting_details(self):
        """
        Get the hosting details of the tournament.

        Returns:
            pandas.DataFrame: A dataframe containing the hosting details.
        """
        return self.data[['tournament_name', 'host']]

    def get_administration_details(self):
        """
        Get the administration details of the tournament.

        Returns:
            pandas.DataFrame: A dataframe containing the administration details.
        """
        return self.data[['tournament_name', 'administrator']]

    def calculate_statistics(self):
        """
        Calculate statistics for the tournament.

        Returns:
            dict: A dictionary containing the tournament statistics.
        """
        statistics = {
            'number_of_tournaments': len(self.data),
            'average_duration': self.calculate_duration().mean()
        }
        return statistics


class EsportsTournamentAnalyzer:
    def __init__(self, tournaments):
        """
        Initialize an EsportsTournamentAnalyzer object.

        Args:
            tournaments (list): A list of EsportsTournament objects.
        """
        self.tournaments = tournaments

    def analyze_tournaments(self):
        """
        Analyze the tournaments and return the results.

        Returns:
            dict: A dictionary containing the analysis results.
        """
        results = []
        for tournament in self.tournaments:
            tournament.validate_data()
            results.append({
                'tournament_name': tournament.data['tournament_name'].iloc[0],
                'hosting_details': tournament.get_hosting_details().to_dict(orient='records'),
                'administration_details': tournament.get_administration_details().to_dict(orient='records'),
                'statistics': tournament.calculate_statistics()
            })
        return results


def main():
    # Example usage
    tournament_data1 = {
        'tournament_name': ['Tournament 1'],
        'start_date': ['2022-01-01'],
        'end_date': ['2022-01-31'],
        'host': ['Ace Pro Sports Technologies'],
        'administrator': ['John Doe']
    }

    tournament_data2 = {
        'tournament_name': ['Tournament 2'],
        'start_date': ['2022-02-01'],
        'end_date': ['2022-02-28'],
        'host': ['Ace Pro Sports Technologies'],
        'administrator': ['Jane Doe']
    }

    tournament1 = EsportsTournament(tournament_data1)
    tournament2 = EsportsTournament(tournament_data2)

    analyzer = EsportsTournamentAnalyzer([tournament1, tournament2])
    results = analyzer.analyze_tournaments()

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
```
