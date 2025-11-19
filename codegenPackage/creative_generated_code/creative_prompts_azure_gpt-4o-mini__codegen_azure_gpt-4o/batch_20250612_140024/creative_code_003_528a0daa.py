"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://semillasplantae.com
Prompt: Develop a command-line tool in Python that helps users track their seed germination rates based on the seeds purchased from Semillas Plantae.
Generated: DETERMINISTIC_528a0daae9a6bda6
Batch ID: 20250612_140024
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
import sys

# Constants
DATA_FILE = "seed_germination.csv"

def initialize_data_file():
    """
    Initializes the seed germination data file if it doesn't exist.
    """
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Seed Type", "Purchased Seeds", "Germinated Seeds", "Germination Rate (%)"])

def calculate_germination_rate(purchased_seeds, germinated_seeds):
    """
    Calculate germination rate as a percentage.
    """
    if purchased_seeds == 0:
        return 0
    return round((germinated_seeds / purchased_seeds) * 100, 2)

def add_seed_entry(seed_type, purchased_seeds, germinated_seeds):
    """
    Adds a new seed entry to the data file.
    """
    try:
        germination_rate = calculate_germination_rate(purchased_seeds, germinated_seeds)
        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([seed_type, purchased_seeds, germinated_seeds, germination_rate])
        print(f"Successfully added entry for seed type: {seed_type}")
    except Exception as e:
        print(f"Error adding seed entry: {e}")

def view_all_entries():
    """
    Displays all entries in the seed germination data file.
    """
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print("\t".join(row))
    except FileNotFoundError:
        print("Data file not found. Please initialize the file first.")
    except Exception as e:
        print(f"Error reading data file: {e}")

def show_menu():
    """
    Displays the command-line menu for user interaction.
    """
    print("\nSeed Germination Tracker")
    print("1. Add a Seed Entry")
    print("2. View All Entries")
    print("3. Exit")

def main():
    """
    Main function that drives the command-line tool.
    """
    initialize_data_file()

    while True:
        show_menu()
        try:
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                seed_type = input("Enter seed type: ").strip()
                purchased_seeds = int(input("Enter number of purchased seeds: ").strip())
                germinated_seeds = int(input("Enter number of germinated seeds: ").strip())
                add_seed_entry(seed_type, purchased_seeds, germinated_seeds)
            elif choice == "2":
                view_all_entries()
            elif choice == "3":
                print("Exiting Seed Germination Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values where required.")
        except KeyboardInterrupt:
            print("\nAborted by user. Exiting Seed Germination Tracker.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
