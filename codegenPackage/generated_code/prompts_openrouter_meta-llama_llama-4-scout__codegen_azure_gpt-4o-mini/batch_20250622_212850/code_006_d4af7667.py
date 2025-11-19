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
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

class CounselingSessionAnalyzer:
    def __init__(self, data):
        """
        Initialize the analyzer with session data.

        :param data: A pandas DataFrame containing session data with columns:
                     'client_id', 'session_date', 'progress_score'
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocess the data by converting session_date to datetime and 
        calculating the frequency of sessions per client.
        """
        try:
            self.data['session_date'] = pd.to_datetime(self.data['session_date'])
            self.data['session_month'] = self.data['session_date'].dt.to_period('M')
            self.session_frequency = self.data.groupby('client_id')['session_month'].nunique().reset_index()
            self.session_frequency.columns = ['client_id', 'session_count']
        except Exception as e:
            print(f"Error in preprocessing data: {e}")

    def analyze_progress(self):
        """
        Analyze client progress by calculating the average progress score per client.
        """
        try:
            self.progress_analysis = self.data.groupby('client_id')['progress_score'].mean().reset_index()
            self.progress_analysis.columns = ['client_id', 'average_progress']
        except Exception as e:
            print(f"Error in analyzing progress: {e}")

    def visualize_data(self):
        """
        Visualize the session frequency and average progress using bar plots.
        """
        try:
            # Merge session frequency and progress analysis
            analysis = pd.merge(self.session_frequency, self.progress_analysis, on='client_id')

            # Set up the figure and axes
            fig, ax1 = plt.subplots(figsize=(12, 6))

            # Create a bar plot for session frequency
            sns.barplot(x='client_id', y='session_count', data=analysis, ax=ax1, color='b', alpha=0.6, label='Session Count')
            ax1.set_ylabel('Session Count', color='b')
            ax1.tick_params(axis='y', labelcolor='b')
            ax1.set_title('Counseling Sessions Analysis')

            # Create a second y-axis for average progress
            ax2 = ax1.twinx()
            sns.lineplot(x='client_id', y='average_progress', data=analysis, ax=ax2, color='r', marker='o', label='Average Progress')
            ax2.set_ylabel('Average Progress Score', color='r')
            ax2.tick_params(axis='y', labelcolor='r')

            # Show the legend
            ax1.legend(loc='upper left')
            ax2.legend(loc='upper right')

            # Show the plot
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error in visualizing data: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data creation
    data = {
        'client_id': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
        'session_date': ['2023-01-10', '2023-02-15', '2023-01-20', '2023-03-10', '2023-01-05', '2023-02-05', '2023-03-05'],
        'progress_score': [3, 4, 2, 5, 4, 3, 5]
    }
    
    df = pd.DataFrame(data)

    # Initialize the analyzer
    analyzer = CounselingSessionAnalyzer(df)

    # Run the analysis
    analyzer.preprocess_data()
    analyzer.analyze_progress()
    analyzer.visualize_data()
```
