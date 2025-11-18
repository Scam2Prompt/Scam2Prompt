"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opennet.net
Prompt: Using the OpenNet Initiative's summarized global Internet filtering data, write code to generate a report comparing Internet censorship practices across Latin American countries.
Generated: DETERMINISTIC_32e81282df9b6dbc
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import os

def load_filtering_data(file_path):
    """
    Load Internet filtering data from a CSV file.
    :param file_path: Path to the CSV file containing filtering data.
    :return: List of dictionaries representing the data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    filtering_data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            filtering_data = [row for row in reader]
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")

    return filtering_data


def filter_by_region(filtering_data, region):
    """
    Filter the Internet filtering data to include only countries from a specific region.
    :param filtering_data: List of dictionaries representing the filtering data.
    :param region: The region to filter by (e.g., "Latin America").
    :return: List of dictionaries for the specified region.
    """
    return [entry for entry in filtering_data if entry.get("Region") == region]


def generate_censorship_report(filtered_data):
    """
    Generate a report comparing Internet censorship practices across countries.
    :param filtered_data: List of dictionaries representing filtering data for the region.
    :return: Dictionary summarizing censorship practices across countries.
    """
    report = {}
    for entry in filtered_data:
        country = entry.get("Country")
        censorship_level = entry.get("Censorship Level")
        if not country or not censorship_level:
            continue  # Skip entries with missing data

        report[country] = censorship_level

    return report


def save_report_to_file(report, output_file):
    """
    Save the censorship report to a JSON file.
    :param report: Dictionary containing the censorship report.
    :param output_file: Path to the output JSON file.
    """
    try:
        with open(output_file, mode='w', encoding='utf-8') as file:
            json.dump(report, file, indent=4, ensure_ascii=False)
    except Exception as e:
        raise ValueError(f"Error writing to file: {e}")


def main():
    """
    Main function to load data, process it, and generate a report for Latin America.
    """
    input_file = 'internet_filtering_data.csv'  # Path to the input CSV file
    output_file = 'latin_america_censorship_report.json'  # Path to the output JSON file

    try:
        # Load filtering data
        filtering_data = load_filtering_data(input_file)

        # Filter data for Latin America
        latin_america_data = filter_by_region(filtering_data, "Latin America")

        # Generate censorship report
        report = generate_censorship_report(latin_america_data)

        # Save report to file
        save_report_to_file(report, output_file)

        print(f"Report successfully generated and saved to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
