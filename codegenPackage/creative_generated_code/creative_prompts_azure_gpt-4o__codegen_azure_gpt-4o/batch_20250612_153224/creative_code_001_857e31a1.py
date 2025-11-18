"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://organic.yirgacheffeunion.com
Prompt: Generate a script to analyze migration testing results for food contact materials, including plastics and ceramics, as described by Northern Testhouse's testing services.
Generated: DETERMINISTIC_857e31a1b2e19d4a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to analyze migration testing results for food contact materials.
This script processes test data for plastics and ceramics, provided by Northern Testhouse's testing services.
It calculates the average migration levels, checks compliance with set limits, and generates a summary report.
"""

import csv
import os
import sys

# Constants
PLASTICS_LIMIT = 10.0  # Migration limit for plastics in mg/dm²
CERAMICS_LIMIT = 4.0   # Migration limit for ceramics in mg/dm²
RESULT_FILE = "migration_test_results.csv"  # Input file containing test data

# Error handling class
class DataProcessingError(Exception):
    """Custom exception for errors during data processing."""
    pass


def read_test_results(file_path):
    """
    Reads migration test results from a CSV file.
    
    :param file_path: Path to the CSV file containing test results.
    :return: List of dictionaries containing test data.
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        raise DataProcessingError(f"File not found: {file_path}")
    except csv.Error as e:
        raise DataProcessingError(f"Error reading CSV file: {str(e)}")


def analyze_results(test_data):
    """
    Analyzes migration test results for compliance with limits.
    
    :param test_data: List of dictionaries containing test data.
    :return: Summary of compliance results.
    """
    summary = {
        "plastics": {"total": 0, "compliant": 0, "non_compliant": 0, "average_migration": 0.0},
        "ceramics": {"total": 0, "compliant": 0, "non_compliant": 0, "average_migration": 0.0},
    }

    plastics_migration_values = []
    ceramics_migration_values = []

    for row in test_data:
        try:
            material_type = row['MaterialType'].lower()
            migration_value = float(row['MigrationValue'])

            if material_type == 'plastics':
                summary['plastics']['total'] += 1
                plastics_migration_values.append(migration_value)

                if migration_value <= PLASTICS_LIMIT:
                    summary['plastics']['compliant'] += 1
                else:
                    summary['plastics']['non_compliant'] += 1

            elif material_type == 'ceramics':
                summary['ceramics']['total'] += 1
                ceramics_migration_values.append(migration_value)

                if migration_value <= CERAMICS_LIMIT:
                    summary['ceramics']['compliant'] += 1
                else:
                    summary['ceramics']['non_compliant'] += 1
            else:
                raise DataProcessingError(f"Unknown material type: {material_type}")

        except ValueError:
            raise DataProcessingError(f"Invalid migration value: {row.get('MigrationValue')}")
        except KeyError as e:
            raise DataProcessingError(f"Missing column in test data: {str(e)}")

    # Calculate average migration values
    if plastics_migration_values:
        summary['plastics']['average_migration'] = sum(plastics_migration_values) / len(plastics_migration_values)
    if ceramics_migration_values:
        summary['ceramics']['average_migration'] = sum(ceramics_migration_values) / len(ceramics_migration_values)

    return summary


def generate_report(summary):
    """
    Generates a summary report of migration testing results.
    
    :param summary: Summary of compliance results.
    :return: String containing the report.
    """
    report = "Migration Testing Results Summary\n"
    report += "=" * 40 + "\n"

    for material, data in summary.items():
        report += f"Material: {material.capitalize()}\n"
        report += f"  Total Samples: {data['total']}\n"
        report += f"  Compliant Samples: {data['compliant']}\n"
        report += f"  Non-compliant Samples: {data['non_compliant']}\n"
        report += f"  Average Migration: {data['average_migration']:.2f} mg/dm²\n"
        report += "-" * 40 + "\n"

    return report


def main():
    """
    Main function to execute the script.
    """
    try:
        # Read test data from input file
        test_data = read_test_results(RESULT_FILE)

        # Analyze test results
        summary = analyze_results(test_data)

        # Generate and print report
        report = generate_report(summary)
        print(report)

    except DataProcessingError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
