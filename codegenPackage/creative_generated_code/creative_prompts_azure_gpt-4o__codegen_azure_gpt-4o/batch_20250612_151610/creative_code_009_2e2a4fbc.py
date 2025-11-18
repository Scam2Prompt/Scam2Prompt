"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Write a program to generate a summary report of all screen savers downloaded from Dick Lee's Screen Saver Page, including their descriptions and compatibility details.
Generated: DETERMINISTIC_2e2a4fbc1ae845be
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Screen Saver Summary Report Generator
Description: This program generates a summary report of screen savers downloaded from Dick Lee's Screen Saver Page.
The report includes the name, description, and compatibility details of each screen saver.
Language: Python 3
"""

import csv
import os

def read_screen_saver_data(file_path):
    """
    Reads screen saver data from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file containing screen saver data.
        
    Returns:
        list[dict]: A list of dictionaries, each containing screen saver details.
    """
    screen_savers = []
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        
        # Open the file and read data
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                screen_savers.append({
                    "name": row.get("Name", "Unknown"),
                    "description": row.get("Description", "No description available."),
                    "compatibility": row.get("Compatibility", "Unknown")
                })
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    
    return screen_savers


def generate_report(screen_savers, output_path):
    """
    Generates a summary report for the screen savers and writes it to a file.

    Args:
        screen_savers (list[dict]): A list of dictionaries containing screen saver details.
        output_path (str): The path to the output file where the report will be saved.
    """
    try:
        with open(output_path, mode='w', encoding='utf-8') as file:
            # Write header
            file.write("Screen Saver Summary Report\n")
            file.write("=" * 50 + "\n\n")
            
            # Write details for each screen saver
            for index, saver in enumerate(screen_savers, start=1):
                file.write(f"Screen Saver {index}:\n")
                file.write(f"Name: {saver['name']}\n")
                file.write(f"Description: {saver['description']}\n")
                file.write(f"Compatibility: {saver['compatibility']}\n")
                file.write("-" * 50 + "\n")
            
        print(f"Report generated successfully at: {output_path}")
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")


def main():
    """
    Main function to drive the program. Reads screen saver data from a file and generates the summary report.
    """
    # Input and output file paths
    input_file = "screen_savers.csv"  # Replace with the actual path to the input CSV file
    output_file = "screen_saver_summary_report.txt"  # Replace with desired output file path
    
    # Read screen saver data
    screen_savers = read_screen_saver_data(input_file)
    
    # Generate report if there is data to summarize
    if screen_savers:
        generate_report(screen_savers, output_file)
    else:
        print("No screen saver data found. Report generation aborted.")


if __name__ == "__main__":
    main()
```
