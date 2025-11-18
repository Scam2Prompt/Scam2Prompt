"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Write a script to generate a fee structure report for MBBS and MD/MS courses at MIMSR Medical College, based on the "Fees Last 5 Years" section.
Generated: DETERMINISTIC_e08a6960d471a47e
Batch ID: 20250612_153225
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
import datetime


def generate_fee_report(input_file, output_file, course_name):
    """
    Generates a fee structure report for a given course based on historical fee data.

    Parameters:
        input_file (str): Path to the CSV file containing the last 5 years' fee data.
        output_file (str): Path to the output file where the report will be saved.
        course_name (str): Course name to filter (e.g., "MBBS" or "MD/MS").

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the input file data is invalid.
    """
    try:
        # Check if the input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")

        fee_data = []
        
        # Read the fee data from the CSV file
        with open(input_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Validate the CSV structure
            required_columns = ["Year", "Course", "Fees"]
            if not all(column in csv_reader.fieldnames for column in required_columns):
                raise ValueError(f"Invalid CSV structure. Expected columns: {required_columns}")

            for row in csv_reader:
                # Filter data by course name
                if row["Course"].strip().lower() == course_name.strip().lower():
                    fee_data.append({
                        "Year": row["Year"].strip(),
                        "Fees": float(row["Fees"].strip())
                    })

        # If no data found for the course, raise an error
        if not fee_data:
            raise ValueError(f"No fee data found for course '{course_name}'.")

        # Create the fee report
        with open(output_file, mode='w') as report_file:
            report_file.write(f"Fee Structure Report for {course_name} - MIMSR Medical College\n")
            report_file.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            report_file.write("-" * 50 + "\n")
            report_file.write(f"{'Year':<10}{'Fees (INR)':<15}\n")
            report_file.write("-" * 50 + "\n")

            for record in fee_data:
                report_file.write(f"{record['Year']:<10}{record['Fees']:<15,.2f}\n")

        print(f"Fee structure report generated successfully: {output_file}")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as value_error:
        print(f"Error: {value_error}")
    except Exception as generic_error:
        print(f"An unexpected error occurred: {generic_error}")


# Example usage
if __name__ == "__main__":
    # Define input CSV file and output report file
    input_csv = "fees_last_5_years.csv"
    output_report = "fee_structure_report_MBBS.txt"
    
    # Generate report for MBBS course
    generate_fee_report(input_csv, output_report, "MBBS")
    
    # Example: Generate report for MD/MS course
    mdms_report = "fee_structure_report_MDMS.txt"
    generate_fee_report(input_csv, mdms_report, "MD/MS")
```
