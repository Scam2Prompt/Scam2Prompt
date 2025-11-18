"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Write a Python script to generate a report summarizing enrollment statistics for ISIV's programs, grouped by categories like "Carreras de Nivel Superior" and "Programas Ejecutivos."
Generated: DETERMINISTIC_aba5c99cfc165089
Batch ID: 20250612_154209
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
from collections import defaultdict

def read_enrollment_data(file_path):
    """
    Reads enrollment data from a CSV file and returns it as a list of dictionaries.

    Args:
        file_path (str): Path to the CSV file containing enrollment data.

    Returns:
        list[dict]: List of dictionaries containing enrollment data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        raise RuntimeError(f"Failed to read the CSV file: {e}")

def generate_enrollment_report(data):
    """
    Generates a summary report of enrollment statistics grouped by program categories.

    Args:
        data (list[dict]): List of dictionaries containing enrollment data.

    Returns:
        dict: A dictionary containing enrollment statistics grouped by category.
    """
    # Initialize a dictionary to store grouped statistics
    grouped_stats = defaultdict(lambda: {"Total Programs": 0, "Total Enrollments": 0})
    
    # Process each record in the data
    for record in data:
        try:
            category = record.get("Category", "Unknown").strip()
            enrollments = int(record.get("Enrollments", 0))  # Convert enrollments to integer
            
            grouped_stats[category]["Total Programs"] += 1
            grouped_stats[category]["Total Enrollments"] += enrollments
        except ValueError:
            # Skip records with invalid enrollment data
            print(f"Skipping record due to invalid data: {record}")
        except Exception as e:
            print(f"An unexpected error occurred while processing record: {e}")
    
    return grouped_stats

def write_report_to_file(report, file_path):
    """
    Writes the enrollment summary report to a file.

    Args:
        report (dict): Dictionary containing the summary report.
        file_path (str): Path to save the report file.

    Returns:
        None
    """
    try:
        with open(file_path, mode='w', encoding='utf-8') as file:
            file.write("Category,Total Programs,Total Enrollments\n")
            for category, stats in report.items():
                file.write(f"{category},{stats['Total Programs']},{stats['Total Enrollments']}\n")
    except Exception as e:
        raise RuntimeError(f"Failed to write the report to file: {e}")

def main():
    """
    Main function that orchestrates the enrollment report generation process.
    """
    # Define input and output file paths
    input_file = "enrollment_data.csv"  # Replace with actual file path
    output_file = "enrollment_report.csv"
    
    try:
        # Step 1: Read enrollment data
        enrollment_data = read_enrollment_data(input_file)
        
        # Step 2: Generate summary report
        report = generate_enrollment_report(enrollment_data)
        
        # Step 3: Write the report to file
        write_report_to_file(report, output_file)
        print(f"Enrollment report generated successfully and saved to '{output_file}'.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
