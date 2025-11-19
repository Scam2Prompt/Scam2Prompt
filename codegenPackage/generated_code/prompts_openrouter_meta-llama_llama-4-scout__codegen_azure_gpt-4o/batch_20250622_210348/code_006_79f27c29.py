"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Write a script to analyze the impact of charity programs like those offered by Amir International Charity Organization, using metrics such as number of people served, donations received, and volunteer hours logged.
Generated: DETERMINISTIC_79f27c29ce7d6808
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import statistics

class CharityImpactAnalyzer:
    """
    A class to analyze the impact of charity programs using metrics such as:
    - Number of people served
    - Donations received
    - Volunteer hours logged
    """

    def __init__(self, data_file):
        """
        Initializes the CharityImpactAnalyzer with a CSV data file.

        :param data_file: Path to the CSV file containing charity program data.
        """
        self.data_file = data_file
        self.data = []

    def load_data(self):
        """
        Loads data from the CSV file into memory.

        The CSV file is expected to have the following columns:
        - Program Name
        - People Served
        - Donations Received
        - Volunteer Hours
        """
        try:
            with open(self.data_file, mode='r') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def calculate_metrics(self):
        """
        Calculates and prints key metrics for the charity programs.

        Metrics include:
        - Total people served
        - Total donations received
        - Total volunteer hours logged
        - Average people served per program
        - Average donations received per program
        - Average volunteer hours per program
        """
        try:
            people_served = [int(row['People Served']) for row in self.data]
            donations_received = [float(row['Donations Received']) for row in self.data]
            volunteer_hours = [float(row['Volunteer Hours']) for row in self.data]

            total_people_served = sum(people_served)
            total_donations_received = sum(donations_received)
            total_volunteer_hours = sum(volunteer_hours)

            avg_people_served = statistics.mean(people_served)
            avg_donations_received = statistics.mean(donations_received)
            avg_volunteer_hours = statistics.mean(volunteer_hours)

            print("Charity Impact Metrics:")
            print(f"Total People Served: {total_people_served}")
            print(f"Total Donations Received: ${total_donations_received:,.2f}")
            print(f"Total Volunteer Hours Logged: {total_volunteer_hours:.2f}")
            print(f"Average People Served per Program: {avg_people_served:.2f}")
            print(f"Average Donations Received per Program: ${avg_donations_received:,.2f}")
            print(f"Average Volunteer Hours per Program: {avg_volunteer_hours:.2f}")

        except ValueError as e:
            print(f"Error calculating metrics: {e}")
        except statistics.StatisticsError as e:
            print(f"Error calculating averages: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def run_analysis(self):
        """
        Runs the full analysis process: loading data and calculating metrics.
        """
        self.load_data()
        if self.data:
            self.calculate_metrics()


if __name__ == "__main__":
    # Path to the CSV file containing charity program data
    data_file_path = "charity_data.csv"

    # Create an instance of CharityImpactAnalyzer and run the analysis
    analyzer = CharityImpactAnalyzer(data_file_path)
    analyzer.run_analysis()
```

### Notes:
- Ensure the CSV file (`charity_data.csv`) exists and has the correct format before running the script.
- The script includes error handling for file operations and data processing.
- Replace `charity_data.csv` with the actual path to your data file.
