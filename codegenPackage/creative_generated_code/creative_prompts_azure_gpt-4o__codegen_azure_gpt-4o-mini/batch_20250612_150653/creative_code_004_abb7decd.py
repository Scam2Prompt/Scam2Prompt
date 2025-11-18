"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Write a script to analyze the effectiveness of training programs for grassroots women leaders, incorporating metrics like advocacy communication skills and organizational sustainability.
Generated: DETERMINISTIC_abb7decdbb25fea3
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class TrainingProgramAnalyzer:
    """
    A class to analyze the effectiveness of training programs for grassroots women leaders.
    
    Attributes:
        data (pd.DataFrame): DataFrame containing training program metrics.
    """

    def __init__(self, csv_file):
        """
        Initializes the TrainingProgramAnalyzer with data from a CSV file.
        
        Args:
            csv_file (str): Path to the CSV file containing training metrics.
        """
        try:
            # Load data from CSV file
            self.data = pd.read_csv(csv_file)

            # Ensure the required columns are present
            required_columns = ['Program', 'Advocacy Skills Score', 'Organizational Sustainability Score']
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError(f"CSV must contain the following columns: {required_columns}")

        except FileNotFoundError:
            raise FileNotFoundError(f"The file {csv_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided CSV file is empty.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading the data: {e}")

    def analyze_effectiveness(self):
        """
        Analyzes and visualizes the effectiveness of the training programs.
        
        Returns:
            None: Displays a bar chart comparing advocacy skills and organizational sustainability scores.
        """
        # Calculate average scores for advocacy skills and organizational sustainability
        avg_scores = self.data[['Program', 'Advocacy Skills Score', 'Organizational Sustainability Score']].copy()
        avg_scores.set_index('Program', inplace=True)

        # Plot the results
        avg_scores.plot(kind='bar', figsize=(10, 6))
        plt.title('Effectiveness of Training Programs for Grassroots Women Leaders')
        plt.ylabel('Scores')
        plt.xlabel('Training Programs')
        plt.xticks(rotation=45)
        plt.legend(title='Metrics')
        plt.tight_layout()
        plt.grid(axis='y')
        plt.show()

    def summary_statistics(self):
        """
        Provides summary statistics for advocacy skills and organizational sustainability scores.
        
        Returns:
            pd.DataFrame: A DataFrame containing summary statistics.
        """
        summary = self.data[['Advocacy Skills Score', 'Organizational Sustainability Score']].describe()
        return summary

if __name__ == "__main__":
    # Example usage of the TrainingProgramAnalyzer
    try:
        analyzer = TrainingProgramAnalyzer("training_programs.csv")
        
        # Analyze the effectiveness of training programs
        analyzer.analyze_effectiveness()
        
        # Display summary statistics
        summary = analyzer.summary_statistics()
        print("Summary Statistics:\n", summary)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
