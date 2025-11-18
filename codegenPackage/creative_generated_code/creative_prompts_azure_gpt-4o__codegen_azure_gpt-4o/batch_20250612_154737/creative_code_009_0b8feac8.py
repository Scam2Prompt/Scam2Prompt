"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globaltradexplus.com
Prompt: Develop a program to analyze trading data and generate reports on user growth and average investment statistics, similar to the metrics provided by Globaltradexplus.
Generated: DETERMINISTIC_0b8feac82641dd01
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime
from statistics import mean

class TradingDataAnalyzer:
    """
    Class to analyze trading data and generate reports on user growth
    and average investment statistics.
    """

    def __init__(self, data_file):
        """
        Initialize the analyzer with a CSV data file.
        :param data_file: Path to the CSV file containing trading data.
        """
        self.data_file = data_file
        self.data = []
        self.users_by_month = {}
        self.average_investment_by_month = {}

    def load_data(self):
        """
        Load trading data from the CSV file.
        """
        try:
            with open(self.data_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Parse and validate necessary fields
                    try:
                        user_id = row['user_id']
                        investment = float(row['investment'])
                        signup_date = datetime.strptime(row['signup_date'], '%Y-%m-%d')
                        self.data.append({
                            'user_id': user_id,
                            'investment': investment,
                            'signup_date': signup_date
                        })
                    except (ValueError, KeyError) as e:
                        print(f"Error processing row: {row}. Skipping. ({e})")
        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found.")
        except Exception as e:
            print(f"Error: An unexpected error occurred while reading the file: {e}")

    def analyze_data(self):
        """
        Analyze the trading data to calculate user growth and average investment statistics.
        """
        for entry in self.data:
            signup_month = entry['signup_date'].strftime('%Y-%m')
            # Track user growth
            if signup_month not in self.users_by_month:
                self.users_by_month[signup_month] = set()
            self.users_by_month[signup_month].add(entry['user_id'])

            # Track investments
            if signup_month not in self.average_investment_by_month:
                self.average_investment_by_month[signup_month] = []
            self.average_investment_by_month[signup_month].append(entry['investment'])

        # Convert user sets to counts and calculate averages
        for month in self.users_by_month:
            self.users_by_month[month] = len(self.users_by_month[month])

        for month in self.average_investment_by_month:
            self.average_investment_by_month[month] = mean(self.average_investment_by_month[month])

    def generate_report(self):
        """
        Generate a textual report of user growth and average investment statistics.
        """
        print("Trading Data Report")
        print("====================")
        print("Month-by-Month Statistics:")
        print("--------------------------")
        for month in sorted(self.users_by_month.keys()):
            print(f"Month: {month}")
            print(f"  New Users: {self.users_by_month[month]}")
            print(f"  Average Investment: ${self.average_investment_by_month[month]:.2f}")
            print()

def main():
    """
    Main function to run the program.
    """
    # File path to the CSV data file
    data_file_path = 'trading_data.csv'

    # Initialize the analyzer
    analyzer = TradingDataAnalyzer(data_file_path)

    # Load data
    analyzer.load_data()

    # Analyze data
    analyzer.analyze_data()

    # Generate report
    analyzer.generate_report()

if __name__ == "__main__":
    main()
```
