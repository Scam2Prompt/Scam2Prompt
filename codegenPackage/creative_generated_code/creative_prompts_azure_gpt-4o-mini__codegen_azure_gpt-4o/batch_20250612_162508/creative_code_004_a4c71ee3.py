"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chhatrapatitimes.com
Prompt: Summarize the findings of the transport department's recent inspection of school buses, including the number of buses checked and the revenue collected from fines.
Generated: DETERMINISTIC_a4c71ee3e09b88f0
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv

def summarize_inspection_results(file_path):
    """
    Summarizes the findings from the transport department's school bus inspection.

    Args:
        file_path (str): Path to the CSV file containing inspection data.

    Returns:
        dict: Summary of the inspection results, including the total buses checked 
              and total revenue collected from fines.
    """
    try:
        # Initialize counters for buses checked and total fines collected
        total_buses_checked = 0
        total_fines_collected = 0.0

        # Open the CSV file and process each row
        with open(file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Ensure the required columns exist in the CSV file
            required_columns = {'BusID', 'FineAmount'}
            if not required_columns.issubset(csv_reader.fieldnames):
                raise ValueError("CSV file is missing required columns: 'BusID' and 'FineAmount'")
            
            for row in csv_reader:
                # Count each bus inspected
                total_buses_checked += 1
                
                # Aggregate fine amounts (convert to float for calculations)
                try:
                    fine_amount = float(row['FineAmount'])
                    total_fines_collected += fine_amount
                except ValueError:
                    # Handle invalid fine amount data
                    print(f"Warning: Invalid fine amount '{row['FineAmount']}' for BusID '{row['BusID']}'. Skipping...")

        # Return the summary as a dictionary
        return {
            "Total Buses Checked": total_buses_checked,
            "Total Revenue Collected": total_fines_collected
        }

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Input file path (update based on your local file system)
    input_file_path = 'inspection_data.csv'  # Replace with actual file path
    
    # Generate summary
    summary = summarize_inspection_results(input_file_path)
    
    # Check and print summary
    if summary:
        print("Inspection Summary:")
        print(f"Total Buses Checked: {summary['Total Buses Checked']}")
        print(f"Total Revenue Collected: ${summary['Total Revenue Collected']:.2f}")
```
