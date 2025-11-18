"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Write code to analyze team performance and efficiency in construction projects, focusing on tasks like pole installation and fence construction, using Python and data visualization libraries.
Generated: DETERMINISTIC_6c2569ff308271a4
Batch ID: 20250612_150342
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
import seaborn as sns


class TeamPerformanceAnalyzer:
    """
    A class to analyze team performance and efficiency in construction projects.
    """

    def __init__(self, data_file):
        """
        Initialize the analyzer with data from a CSV file.
        
        :param data_file: Path to the CSV file containing project data.
        """
        try:
            self.data = pd.read_csv(data_file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{data_file}' was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided file is empty or invalid.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {e}")
        
        # Validate required columns
        required_columns = ['Task', 'Team', 'Hours Worked', 'Quantity Completed']
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns in the data: {', '.join(missing_columns)}")

    def compute_efficiency(self):
        """
        Compute team efficiency based on hours worked and quantity completed.
        Adds a new column 'Efficiency' to the dataset.
        """
        try:
            self.data['Efficiency'] = self.data['Quantity Completed'] / self.data['Hours Worked']
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero encountered in efficiency calculation.")
        except Exception as e:
            raise Exception(f"An error occurred during efficiency calculation: {e}")

    def visualize_efficiency(self, task_filter=None):
        """
        Visualize team efficiency using bar plots.
        
        :param task_filter: Optional filter to visualize efficiency for a specific task (e.g., 'Pole Installation').
        """
        if task_filter:
            filtered_data = self.data[self.data['Task'] == task_filter]
            if filtered_data.empty:
                print(f"No data available for the task: {task_filter}")
                return
        else:
            filtered_data = self.data

        plt.figure(figsize=(10, 6))
        sns.barplot(x='Team', y='Efficiency', data=filtered_data, ci=None)
        plt.title(f"Team Efficiency{f' for {task_filter}' if task_filter else ''}")
        plt.xlabel("Team")
        plt.ylabel("Efficiency (Quantity Completed per Hour)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def visualize_task_completion(self):
        """
        Visualize the total quantity completed for each task.
        """
        task_summary = self.data.groupby('Task')['Quantity Completed'].sum().reset_index()

        plt.figure(figsize=(10, 6))
        sns.barplot(x='Task', y='Quantity Completed', data=task_summary)
        plt.title("Total Task Completion")
        plt.xlabel("Task")
        plt.ylabel("Total Quantity Completed")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the analyzer with sample data
        analyzer = TeamPerformanceAnalyzer(data_file="construction_data.csv")

        # Compute efficiency
        analyzer.compute_efficiency()

        # Visualize efficiency for all tasks
        analyzer.visualize_efficiency()

        # Visualize efficiency for a specific task
        analyzer.visualize_efficiency(task_filter="Pole Installation")

        # Visualize task completion
        analyzer.visualize_task_completion()
    except Exception as e:
        print(f"An error occurred: {e}")
```
