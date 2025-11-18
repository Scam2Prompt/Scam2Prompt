"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tarileague.pages.dev
Prompt: Create a tool to analyze Yat ownership data and display the total rewards earned based on hold time and rarity criteria.
Generated: DETERMINISTIC_dc0a60144bc215e2
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class YatOwnershipAnalyzer:
    """
    A tool to analyze Yat ownership data and calculate total rewards
    based on hold time and rarity criteria.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: Path to the CSV file containing Yat ownership data.
        """
        self.data_file = data_file
        self.yat_data = None
        self.load_data()

    def load_data(self):
        """
        Loads Yat ownership data from a CSV file into a pandas DataFrame.
        """
        try:
            self.yat_data = pd.read_csv(self.data_file)
            if 'hold_time' not in self.yat_data or 'rarity' not in self.yat_data:
                raise ValueError("Data must contain 'hold_time' and 'rarity' columns.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except ValueError as ve:
            print(f"Error: {ve}")
            raise

    def calculate_rewards(self):
        """
        Calculates total rewards based on hold time and rarity criteria.
        
        :return: Total rewards as a float.
        """
        if self.yat_data is None or self.yat_data.empty:
            raise RuntimeError("Yat data is not loaded or is empty.")
        
        try:
            # Define reward calculation based on conditions
            self.yat_data['rewards'] = self.yat_data.apply(self.compute_rewards, axis=1)
            total_rewards = self.yat_data['rewards'].sum()
            return total_rewards
        except Exception as e:
            print(f"Error during rewards calculation: {e}")
            raise

    def compute_rewards(self, row):
        """
        Computes rewards for a single row based on hold time and rarity.

        :param row: A single row from the DataFrame.
        :return: Calculated rewards based on conditions.
        """
        hold_time = row['hold_time']
        rarity = row['rarity']

        # Define reward logic
        base_reward = 0
        if hold_time >= 365:  # 1 year
            base_reward += 100
        elif hold_time >= 180:  # 6 months
            base_reward += 50
        elif hold_time >= 30:  # 1 month
            base_reward += 10

        if rarity == 'legendary':
            return base_reward * 2
        elif rarity == 'rare':
            return base_reward * 1.5
        else:
            return base_reward

if __name__ == "__main__":
    # Example usage of the YatOwnershipAnalyzer
    try:
        # Provide the path to your Yat ownership data CSV file
        analyzer = YatOwnershipAnalyzer('yat_ownership_data.csv')
        total_rewards = analyzer.calculate_rewards()
        print(f"Total rewards earned: ${total_rewards:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
