"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Write a Python function that can automate the bookkeeping process for small businesses, incorporating best practices mentioned by Lund & Kieck.
Generated: DETERMINISTIC_51b9c606043963c2
Batch ID: 20250612_162203
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

def automate_bookkeeping(input_file, output_dir="bookkeeping_reports"):
    """
    Automates the bookkeeping process for small businesses.

    Args:
        input_file (str): Path to the CSV file containing financial transaction data.
                         Expected columns: ["Date", "Description", "Category", "Amount"]
        output_dir (str): Directory to save the generated bookkeeping report files.
                         Defaults to "bookkeeping_reports".

    Returns:
        str: Path to the generated summary report file.

    Raises:
        FileNotFoundError: If the input CSV file does not exist.
        ValueError: If the input CSV file format is invalid.
    """
    # Ensure the input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file '{input_file}' does not exist.")

    # Ensure the output directory exists, create if not
    os.makedirs(output_dir, exist_ok=True)

    # Initialize variables for bookkeeping
    transactions = []
    category_totals = {}

    try:
        # Read and validate the input CSV file
        with open(input_file, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            required_columns = {"Date", "Description", "Category", "Amount"}
            
            if not required_columns.issubset(reader.fieldnames):
                raise ValueError(f"Input file must contain the following columns: {', '.join(required_columns)}")
            
            # Process each transaction
            for row in reader:
                try:
                    # Parse and validate data
                    transaction_date = datetime.strptime(row["Date"], "%Y-%m-%d")
                    description = row["Description"].strip()
                    category = row["Category"].strip()
                    amount = float(row["Amount"])
                    
                    transactions.append({
                        "Date": transaction_date,
                        "Description": description,
                        "Category": category,
                        "Amount": amount
                    })
                    
                    # Accumulate totals by category
                    category_totals[category] = category_totals.get(category, 0) + amount
                
                except ValueError:
                    # Skip invalid rows with detailed warning
                    print(f"Skipping invalid transaction row: {row}")
        
        # Generate summary report
        summary_file = os.path.join(output_dir, f"summary_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
        with open(summary_file, "w", newline="") as summary_csv:
            writer = csv.writer(summary_csv)
            writer.writerow(["Category", "Total Amount"])
            
            for category, total in category_totals.items():
                writer.writerow([category, total])

        print(f"Summary report generated successfully: {summary_file}")
        return summary_file

    except Exception as e:
        # Log unexpected errors
        print(f"An error occurred during bookkeeping automation: {e}")
        raise

# Example Usage:
# automate_bookkeeping("transactions.csv")
```
