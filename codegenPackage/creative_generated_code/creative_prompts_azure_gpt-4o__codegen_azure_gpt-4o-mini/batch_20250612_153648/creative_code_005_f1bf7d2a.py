"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Develop a program to calculate the abrasion resistance of golf grips based on input data from a DIN abrasion tester, as mentioned in Longhui Golf’s quality assurance section.
Generated: DETERMINISTIC_f1bf7d2a538c4711
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class GolfGripAbrasionTester:
    """
    A class to calculate the abrasion resistance of golf grips
    based on input data from a DIN abrasion tester.
    """

    def __init__(self, data_file):
        """
        Initializes the tester with the data from the given CSV file.
        
        :param data_file: Path to the CSV file containing the abrasion test results.
        """
        self.data_file = data_file
        self.data = None
        self.load_data()

    def load_data(self):
        """
        Loads the data from the CSV file into a Pandas DataFrame.
        Raises an error if the file cannot be read.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            if 'grip_id' not in self.data.columns or 'abrasion_loss' not in self.data.columns:
                raise ValueError("CSV must contain 'grip_id' and 'abrasion_loss' columns.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.data_file} not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the CSV file.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading data: {e}")

    def calculate_average_abrasion(self):
        """
        Calculates the average abrasion loss for the grips.
        
        :return: Average abrasion loss
        """
        if self.data is None or self.data.empty:
            raise ValueError("No data available for calculation.")
        
        average_loss = self.data['abrasion_loss'].mean()
        return average_loss

    def calculate_abrasion_variance(self):
        """
        Calculates the variance of abrasion loss for the grips.
        
        :return: Variance of abrasion loss
        """
        if self.data is None or self.data.empty:
            raise ValueError("No data available for calculation.")
        
        variance = self.data['abrasion_loss'].var()
        return variance

    def display_results(self):
        """
        Displays the average and variance of abrasion loss.
        """
        try:
            average_abrasion = self.calculate_average_abrasion()
            abrasion_variance = self.calculate_abrasion_variance()
            print(f"Average Abrasion Loss: {average_abrasion:.2f} mm")
            print(f"Abrasion Variance: {abrasion_variance:.2f} mm^2")
        except Exception as e:
            print(f"An error occurred while displaying results: {e}")

if __name__ == "__main__":
    # Replace 'abrasion_data.csv' with the actual path to your data file
    tester = GolfGripAbrasionTester('abrasion_data.csv')
    tester.display_results()
```
