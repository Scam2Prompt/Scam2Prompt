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
import os

def parse_softball_schedule(file_path):
    """
    Parses a CSV file containing a slowpitch softball league schedule 
    and displays the schedule in a user-friendly format.

    Args:
        file_path (str): Path to the CSV file containing the schedule.

    Returns:
        None
    """
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            if not csv_reader.fieldnames:
                print("Error: The CSV file appears to be empty or improperly formatted.")
                return

            print("\n--- Slowpitch Softball League Schedule ---")
            print(f"File: {file_path}")
            print("=" * 50)
            
            for row in csv_reader:
                # Ensure required fields are present in each row
                try:
                    date = row['Date']
                    time = row['Time']
                    teams = row['Teams']
                    location = row['Location']
                except KeyError as e:
                    print(f"Error: Missing expected column '{e.args[0]}' in the CSV file.")
                    return

                # Format and display each game in a readable way
                print(f"Date: {date}")
                print(f"Time: {time}")
                print(f"Teams: {teams}")
                print(f"Location: {location}")
                print("-" * 50)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Prompt the user for the CSV file path
    file_path = input("Enter the path to the softball schedule CSV file: ").strip()
    parse_softball_schedule(file_path)
```
