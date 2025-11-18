"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunsystems.hk
Prompt: Write a script to train staff on using Infor SunSystems effectively, including generating sample financial reports and scenarios for hands-on practice.
Generated: DETERMINISTIC_790a2b71c754d414
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to simulate training staff on using Infor SunSystems effectively.
The script generates sample financial reports and scenarios for hands-on practice.
Note: This is a simulated example and does not interface with Infor SunSystems directly.
"""

import csv
import random
import os

# Constants for generating sample data
ACCOUNTS = ["Sales", "Marketing", "R&D", "Operations", "HR"]
CURRENCY = ["USD", "EUR", "GBP", "JPY", "AUD"]
REPORT_FILE = "sample_financial_report.csv"

def generate_sample_data(num_entries=50):
    """
    Generate simulated financial data for training purposes.
    :param num_entries: Number of financial report entries to generate.
    :return: List of dictionaries containing the financial data.
    """
    sample_data = []
    for i in range(num_entries):
        entry = {
            "Account": random.choice(ACCOUNTS),
            "Date": f"{random.randint(2022, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
            "Transaction_Type": random.choice(["Debit", "Credit"]),
            "Amount": round(random.uniform(1000, 10000), 2),
            "Currency": random.choice(CURRENCY)
        }
        sample_data.append(entry)
    return sample_data


def write_to_csv(data, file_name=REPORT_FILE):
    """
    Write the generated financial data to a CSV file.
    :param data: List of dictionaries containing financial data.
    :param file_name: Name of the output CSV file.
    """
    try:
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Sample financial report saved to '{file_name}'.")
    except Exception as e:
        print(f"Error saving CSV file: {e}")


def display_scenarios():
    """
    Display sample scenarios for hands-on practice by staff.
    """
    scenarios = [
        "Scenario 1: Identify the highest spending account in the financial report.",
        "Scenario 2: Calculate the total debits and credits for each currency.",
        "Scenario 3: Generate a summary report for all transactions made in 2023.",
        "Scenario 4: Convert all amounts to USD using current exchange rates.",
        "Scenario 5: Audit transactions to ensure no duplicate entries exist."
    ]
    print("\nHands-on Practice Scenarios:")
    for scenario in scenarios:
        print(scenario)


def main():
    """
    Main function to simulate training on Infor SunSystems.
    """
    print("Generating sample financial data...")
    sample_data = generate_sample_data()
    
    print("Writing sample financial report to CSV...")
    write_to_csv(sample_data)
    
    print("Displaying practice scenarios for staff...")
    display_scenarios()


if __name__ == "__main__":
    # Ensure clean-up of previous report file (if exists)
    if os.path.exists(REPORT_FILE):
        os.remove(REPORT_FILE)

    # Run the main application
    main()
```
