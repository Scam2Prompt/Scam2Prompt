"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Write Python code to parse a CSV schedule for a slowpitch softball league and display the schedule in a user-friendly format, as described on Slo-Pitch Central.
Generated: DETERMINISTIC_da2151394d7038b8
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from typing import List, Dict

class SoftballScheduleParser:
    """
    A class to parse a CSV schedule for a slowpitch softball league and display it in a user-friendly format.
    """

    def __init__(self, csv_file: str):
        """
        Initializes the parser with the path to the CSV file.

        :param csv_file: Path to the CSV file containing the schedule.
        """
        self.csv_file = csv_file
        self.schedule: List[Dict[str, str]] = []

    def load_schedule(self) -> None:
        """
        Loads the schedule from the CSV file and stores it in the schedule attribute.
        Raises an exception if the file cannot be read or parsed.
        """
        try:
            with open(self.csv_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.schedule = [row for row in reader]
        except FileNotFoundError:
            raise Exception(f"Error: The file '{self.csv_file}' was not found.")
        except Exception as e:
            raise Exception(f"Error reading the file: {e}")

    def display_schedule(self) -> None:
        """
        Displays the parsed schedule in a user-friendly format.
        """
        if not self.schedule:
            print("No schedule available. Please load the schedule first.")
            return

        print("Softball League Schedule:")
        print("-" * 30)
        for game in self.schedule:
            try:
                date = game.get('Date', 'N/A')
                time = game.get('Time', 'N/A')
                team_a = game.get('Team A', 'N/A')
                team_b = game.get('Team B', 'N/A')
                location = game.get('Location', 'N/A')

                print(f"Date: {date}, Time: {time}, {team_a} vs {team_b} at {location}")
            except Exception as e:
                print(f"Error displaying game information: {e}")

def main():
    """
    Main function to execute the schedule parser.
    """
    csv_file_path = 'softball_schedule.csv'  # Update with the actual path to your CSV file
    parser = SoftballScheduleParser(csv_file_path)

    try:
        parser.load_schedule()
        parser.display_schedule()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```
