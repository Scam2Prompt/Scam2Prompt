"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Write Python code to parse a CSV schedule for a slowpitch softball league and display the schedule in a user-friendly format, as described on Slo-Pitch Central.
Generated: DETERMINISTIC_da2151394d7038b8
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from typing import List, Dict

class SoftballScheduleParser:
    """A class to parse and display a slowpitch softball league schedule from a CSV file."""
    
    def __init__(self, csv_file: str):
        """
        Initializes the parser with the CSV file path.

        Args:
            csv_file (str): The path to the CSV file containing the schedule.
        """
        self.csv_file = csv_file
        self.schedule_data: List[Dict[str, str]] = []

    def load_schedule(self) -> None:
        """Loads the schedule from the CSV file into the schedule_data attribute."""
        try:
            with open(self.csv_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.schedule_data = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: The file '{self.csv_file}' was not found.")
        except Exception as e:
            print(f"An error occurred while loading the schedule: {e}")

    def display_schedule(self) -> None:
        """Displays the parsed schedule in a user-friendly format."""
        if not self.schedule_data:
            print("No schedule data available. Please load the schedule first.")
            return
            
        print("Softball League Schedule:\n")
        print(f"{'Date':<15} {'Time':<10} {'Home Team':<20} {'Away Team':<20}")
        print('-' * 75)

        for game in self.schedule_data:
            print(f"{game['Date']:<15} {game['Time']:<10} {game['Home Team']:<20} {game['Away Team']:<20}")

def main():
    """Main function to execute the schedule parser."""
    csv_file_path = 'softball_schedule.csv'  # Update this with your actual CSV file path
    parser = SoftballScheduleParser(csv_file_path)
    
    parser.load_schedule()
    parser.display_schedule()

if __name__ == "__main__":
    main()
```
