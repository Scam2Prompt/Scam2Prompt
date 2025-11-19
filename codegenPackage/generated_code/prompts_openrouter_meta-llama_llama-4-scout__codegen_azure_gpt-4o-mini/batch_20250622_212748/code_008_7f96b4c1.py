"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: "Generate a report on the benefits of online learning at CNU, focusing on flexibility and career-oriented programs."
Generated: DETERMINISTIC_7f96b4c145b17b20
Batch ID: 20250622_212748
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

class OnlineLearningReport:
    """
    A class to generate a report on the benefits of online learning at CNU.
    Focuses on flexibility and career-oriented programs.
    """

    def __init__(self, data_file):
        """
        Initializes the OnlineLearningReport with data from a CSV file.

        :param data_file: str, path to the CSV file containing online learning data
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads data from the specified CSV file.

        :return: DataFrame containing the online learning data
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def generate_flexibility_report(self):
        """
        Generates a report on the flexibility of online learning programs.
        """
        try:
            flexibility_data = self.data['Flexibility']
            average_flexibility = flexibility_data.mean()
            print(f"Average Flexibility Rating: {average_flexibility:.2f}")

            # Plotting flexibility data
            plt.figure(figsize=(10, 5))
            plt.hist(flexibility_data, bins=10, color='blue', alpha=0.7)
            plt.title('Flexibility Ratings of Online Learning Programs')
            plt.xlabel('Flexibility Rating')
            plt.ylabel('Frequency')
            plt.grid(axis='y')
            plt.show()
        except KeyError:
            print("Error: 'Flexibility' column not found in the data.")
            raise
        except Exception as e:
            print(f"An error occurred while generating flexibility report: {e}")
            raise

    def generate_career_oriented_report(self):
        """
        Generates a report on career-oriented programs offered through online learning.
        """
        try:
            career_data = self.data['Career_Oriented_Programs']
            total_programs = career_data.count()
            print(f"Total Career-Oriented Programs: {total_programs}")

            # Plotting career-oriented programs data
            plt.figure(figsize=(10, 5))
            career_data.value_counts().plot(kind='bar', color='green', alpha=0.7)
            plt.title('Career-Oriented Programs Offered')
            plt.xlabel('Programs')
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.grid(axis='y')
            plt.show()
        except KeyError:
            print("Error: 'Career_Oriented_Programs' column not found in the data.")
            raise
        except Exception as e:
            print(f"An error occurred while generating career-oriented report: {e}")
            raise

if __name__ == "__main__":
    # Path to the CSV file containing online learning data
    data_file_path = 'cnu_online_learning_data.csv'
    
    # Create an instance of OnlineLearningReport
    report = OnlineLearningReport(data_file_path)
    
    # Generate reports
    report.generate_flexibility_report()
    report.generate_career_oriented_report()
```
