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
from datetime import datetime
from collections import defaultdict
import argparse
import sys

def parse_csv(file_path):
    """
    Parse the CSV schedule file and return a structured dictionary of games.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        dict: A dictionary with dates as keys and lists of games as values.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        csv.Error: If there is an error parsing the CSV.
    """
    schedule = defaultdict(list)
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                try:
                    date_str = row.get('Date', '').strip()
                    time_str = row.get('Time', '').strip()
                    home_team = row.get('Home Team', '').strip()
                    away_team = row.get('Away Team', '').strip()
                    field = row.get('Field', '').strip()
                    
                    if not all([date_str, time_str, home_team, away_team, field]):
                        continue  # Skip incomplete rows
                    
                    # Parse date and time
                    datetime_str = f"{date_str} {time_str}"
                    game_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
                    
                    game = {
                        'datetime': game_datetime,
                        'home_team': home_team,
                        'away_team': away_team,
                        'field': field
                    }
                    
                    schedule[game_datetime.date()].append(game)
                except ValueError as e:
                    print(f"Error parsing row {row}: {e}", file=sys.stderr)
                    continue
                
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except csv.Error as e:
        raise csv.Error(f"CSV parsing error: {e}")
    
    return schedule

def display_schedule(schedule):
    """
    Display the schedule in a user-friendly format.
    
    Args:
        schedule (dict): The parsed schedule dictionary.
    """
    for date, games in sorted(schedule.items()):
        print(f"\n=== {date.strftime('%A, %B %d, %Y')} ===")
        for game in sorted(games, key=lambda x: x['datetime']):
            print(
                f"{game['datetime'].strftime('%I:%M %p')} - "
                f"{game['home_team']} vs {game['away_team']} "
                f"(Field: {game['field']})"
            )

def main():
    """
    Main function to handle command-line arguments and execute the program.
    """
    parser = argparse.ArgumentParser(description='Parse and display a slowpitch softball league schedule.')
    parser.add_argument('file_path', type=str, help='Path to the CSV schedule file')
    
    args = parser.parse_args()
    
    try:
        schedule = parse_csv(args.file_path)
        display_schedule(schedule)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except csv.Error as e:
        print(f"CSV Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```
