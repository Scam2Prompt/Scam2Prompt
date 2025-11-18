"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Write a script to analyze student enrollment data for sales training programs, categorizing them by industry (e.g., real estate, automobile, financial products, insurance) as offered by Debridge Advisory.
Generated: DETERMINISTIC_5ccfe19355fab0c7
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from collections import defaultdict

def analyze_enrollment_data(input_file, output_file):
    """
    Analyzes student enrollment data for sales training programs and categorizes them by industry.
    
    Args:
        input_file (str): Path to the CSV file containing enrollment data.
        output_file (str): Path to the CSV file for saving categorized enrollment data.
    """

    # Dictionary to store categorized data by industry
    enrollment_by_industry = defaultdict(list)

    try:
        # Read the input CSV file
        with open(input_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            # Validate the presence of required columns
            if 'Student Name' not in csv_reader.fieldnames or 'Industry' not in csv_reader.fieldnames:
                raise ValueError("Input file must contain 'Student Name' and 'Industry' columns.")

            # Process each row and categorize by industry
            for row in csv_reader:
                industry = row['Industry'].strip()
                enrollment_by_industry[industry].append(row)

        # Write the categorized data to the output CSV file
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['Industry', 'Student Name', 'Program Name', 'Enrollment Date']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header row
            csv_writer.writeheader()

            # Write categorized data
            for industry, students in enrollment_by_industry.items():
                for student in students:
                    csv_writer.writerow({
                        'Industry': industry,
                        'Student Name': student.get('Student Name', '').strip(),
                        'Program Name': student.get('Program Name', '').strip(),
                        'Enrollment Date': student.get('Enrollment Date', '').strip()
                    })

        print(f"Enrollment data has been successfully categorized and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Paths to the input and output files
    input_csv = "student_enrollment_data.csv"
    output_csv = "categorized_enrollment_data.csv"

    # Analyze and categorize enrollment data
    analyze_enrollment_data(input_csv, output_csv)
```
