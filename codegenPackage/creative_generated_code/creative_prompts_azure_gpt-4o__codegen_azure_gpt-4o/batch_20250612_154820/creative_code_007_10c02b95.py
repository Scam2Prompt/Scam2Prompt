"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-cvk.com
Prompt: Write code to filter and exclude participants from restricted countries (e.g., Bolivia, Iran, North Korea) in compliance with TrustPad's IDO rules.
Generated: DETERMINISTIC_10c02b95ec600652
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Participant Filtering Script
# This script filters and excludes participants from restricted countries
# in compliance with TrustPad's IDO rules.

# Import necessary modules
import csv

# List of restricted countries
RESTRICTED_COUNTRIES = {"Bolivia", "Iran", "North Korea"}

def load_participants(file_path):
    """
    Load participants from a CSV file.
    
    :param file_path: Path to the CSV file containing participant data.
    :return: List of participants (each participant is a dictionary).
    """
    participants = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            participants = [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error loading participants: {e}")
    return participants

def filter_participants(participants):
    """
    Filter out participants from restricted countries.
    
    :param participants: List of participant dictionaries.
    :return: List of eligible participants.
    """
    eligible_participants = []
    for participant in participants:
        try:
            country = participant.get("country", "").strip()
            if country not in RESTRICTED_COUNTRIES:
                eligible_participants.append(participant)
        except KeyError as e:
            print(f"Missing expected data in participant entry: {e}")
    return eligible_participants

def save_filtered_participants(file_path, eligible_participants):
    """
    Save eligible participants to a new CSV file.
    
    :param file_path: Path to the CSV file to save eligible participants.
    :param eligible_participants: List of eligible participant dictionaries.
    """
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as csv_file:
            if eligible_participants:
                writer = csv.DictWriter(csv_file, fieldnames=eligible_participants[0].keys())
                writer.writeheader()
                writer.writerows(eligible_participants)
            else:
                print("No eligible participants to save.")
    except Exception as e:
        print(f"Error saving filtered participants: {e}")

def main():
    """
    Main function to execute the participant filtering process.
    """
    input_file = "participants.csv"  # Input file containing participant data
    output_file = "eligible_participants.csv"  # Output file for filtered participants
    
    print("Loading participants...")
    participants = load_participants(input_file)
    
    print("Filtering participants...")
    eligible_participants = filter_participants(participants)
    
    print("Saving eligible participants...")
    save_filtered_participants(output_file, eligible_participants)
    
    print("Filtering process completed.")

if __name__ == "__main__":
    main()
```
