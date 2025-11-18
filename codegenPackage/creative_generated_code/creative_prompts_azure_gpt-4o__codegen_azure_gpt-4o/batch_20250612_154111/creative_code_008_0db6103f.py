"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brokereo.com
Prompt: Write code to generate a report summarizing the actions taken by Neo Premium Investments Ltd. to refund balances and transfer unclaimed funds to CySEC.
Generated: DETERMINISTIC_0db6103fe0ee5b37
Batch ID: 20250612_154111
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
from datetime import datetime

def generate_report(refund_data_file, output_report_file):
    """
    Generates a report summarizing actions taken by Neo Premium Investments Ltd. to 
    refund balances and transfer unclaimed funds to CySEC.

    Args:
        refund_data_file (str): Path to the CSV file containing refund data.
        output_report_file (str): Path to the output report file.

    Returns:
        None
    """
    try:
        # Initialize summary counters
        total_refunded = 0.0
        total_transferred_to_cysec = 0.0
        total_refund_count = 0
        total_cysec_transfer_count = 0

        # Read refund data from CSV file
        if not os.path.exists(refund_data_file):
            raise FileNotFoundError(f"Refund data file '{refund_data_file}' not found.")

        with open(refund_data_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Parse and aggregate data
                if row["Action"] == "Refunded":
                    total_refunded += float(row["Amount"])
                    total_refund_count += 1
                elif row["Action"] == "Transferred to CySEC":
                    total_transferred_to_cysec += float(row["Amount"])
                    total_cysec_transfer_count += 1
                else:
                    # Skip rows with unknown actions
                    continue

        # Generate report content
        report_content = [
            f"Report on Actions Taken by Neo Premium Investments Ltd.",
            f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            f"Total Refunded Amount: €{total_refunded:,.2f}",
            f"Total Refund Transactions: {total_refund_count}",
            "",
            f"Total Transferred to CySEC: €{total_transferred_to_cysec:,.2f}",
            f"Total CySEC Transfer Transactions: {total_cysec_transfer_count}",
            "",
            "End of Report"
        ]

        # Write report to output file
        with open(output_report_file, mode='w', encoding='utf-8') as file:
            file.write("\n".join(report_content))

        print(f"Report successfully generated: {output_report_file}")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except KeyError as key_error:
        print(f"Error: Missing expected column in the input CSV file - {key_error}")
    except ValueError as value_error:
        print(f"Error: Invalid data format encountered - {value_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    input_csv_file = "refund_data.csv"  # Replace with the actual CSV file path
    output_file = "refund_report.txt"  # Replace with desired report file path
    generate_report(input_csv_file, output_file)
```
