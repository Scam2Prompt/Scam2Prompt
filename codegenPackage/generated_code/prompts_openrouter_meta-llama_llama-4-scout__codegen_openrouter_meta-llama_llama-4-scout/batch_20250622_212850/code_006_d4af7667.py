"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Write a code snippet to analyze and visualize the effectiveness of counseling sessions, using metrics such as session frequency and client progress.
Generated: DETERMINISTIC_d4af7667e72b83c7
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class CounselingSessionAnalyzer:
    def __init__(self, sessions_df, clients_df):
        """
        Initialize the CounselingSessionAnalyzer.

        Parameters:
        sessions_df (pd.DataFrame): A DataFrame containing counseling session data.
            It should have columns: 'client_id', 'session_date', 'progress'.
        clients_df (pd.DataFrame): A DataFrame containing client data.
            It should have columns: 'client_id', 'name'.
        """
        self.sessions_df = sessions_df
        self.clients_df = clients_df

    def _validate_input(self):
        required_columns_sessions = ['client_id', 'session_date', 'progress']
        required_columns_clients = ['client_id', 'name']

        if not all(col in self.sessions_df.columns for col in required_columns_sessions):
            raise ValueError("Sessions DataFrame is missing required columns")
        if not all(col in self.clients_df.columns for col in required_columns_clients):
            raise ValueError("Clients DataFrame is missing required columns")

        try:
            self.sessions_df['session_date'] = pd.to_datetime(self.sessions_df['session_date'])
        except ValueError:
            raise ValueError("Invalid date format in sessions DataFrame")

    def calculate_session_frequency(self):
        """
        Calculate the frequency of counseling sessions per client.

        Returns:
        pd.DataFrame: A DataFrame with client_id and session frequency.
        """
        session_frequency = self.sessions_df.groupby('client_id').size().reset_index(name='session_frequency')
        return session_frequency

    def calculate_client_progress(self):
        """
        Calculate the average progress of clients.

        Returns:
        pd.DataFrame: A DataFrame with client_id, name, and average progress.
        """
        client_progress = self.sessions_df.groupby('client_id')['progress'].mean().reset_index()
        client_progress = pd.merge(client_progress, self.clients_df, on='client_id')
        client_progress = client_progress.rename(columns={'progress': 'average_progress'})
        return client_progress

    def visualize_session_frequency(self, session_frequency_df):
        """
        Visualize the session frequency of clients.

        Parameters:
        session_frequency_df (pd.DataFrame): A DataFrame with client_id and session frequency.
        """
        plt.figure(figsize=(10,6))
        plt.bar(session_frequency_df['client_id'], session_frequency_df['session_frequency'])
        plt.xlabel('Client ID')
        plt.ylabel('Session Frequency')
        plt.title('Counseling Session Frequency')
        plt.show()

    def visualize_client_progress(self, client_progress_df):
        """
        Visualize the average progress of clients.

        Parameters:
        client_progress_df (pd.DataFrame): A DataFrame with client_id, name, and average progress.
        """
        plt.figure(figsize=(10,6))
        plt.bar(client_progress_df['name'], client_progress_df['average_progress'])
        plt.xlabel('Client Name')
        plt.ylabel('Average Progress')
        plt.title('Client Progress')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

def main():
    # Example usage
    sessions_data = {
        'client_id': [1, 1, 2, 2, 2, 3],
        'session_date': ['2022-01-01', '2022-01-15', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01'],
        'progress': [10, 20, 5, 15, 25, 30]
    }
    clients_data = {
        'client_id': [1, 2, 3],
        'name': ['John Doe', 'Jane Doe', 'Bob Smith']
    }

    sessions_df = pd.DataFrame(sessions_data)
    clients_df = pd.DataFrame(clients_data)

    analyzer = CounselingSessionAnalyzer(sessions_df, clients_df)
    analyzer._validate_input()

    session_frequency_df = analyzer.calculate_session_frequency()
    client_progress_df = analyzer.calculate_client_progress()

    analyzer.visualize_session_frequency(session_frequency_df)
    analyzer.visualize_client_progress(client_progress_df)

if __name__ == "__main__":
    main()
```
