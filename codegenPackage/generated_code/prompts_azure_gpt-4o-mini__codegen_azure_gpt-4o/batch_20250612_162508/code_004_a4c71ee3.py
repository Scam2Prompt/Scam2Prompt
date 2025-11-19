"""
Generated Code Metadata:
========================
Original URL: https://chhatrapatitimes.com
Prompt: Summarize the findings of the transport department's recent inspection of school buses, including the number of buses checked and the revenue collected from fines.
Generated: DETERMINISTIC_a4c71ee3e09b88f0
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os

def summarize_inspection_results(file_path):
    """
    Summarizes the findings of the transport department's recent inspection of school buses.
    
    Args:
        file_path (str): Path to the CSV file containing inspection data.
        
    Returns:
        dict: A summary containing the number of buses checked and total revenue collected from fines.
    """
    # Initialize counters
    total_buses_checked = 0
    total_fine_revenue = 0.0

    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        # Open the CSV file and process its contents
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Validate the presence of required columns
            if 'BusID' not in reader.fieldnames or 'FineAmount' not in reader.fieldnames:
                raise ValueError("The CSV file must contain 'BusID' and 'FineAmount' columns.")
            
            for row in reader:
                # Increment the bus count
                total_buses_checked += 1
                
                # Accumulate the fine revenue
                try:
                    fine_amount = float(row['FineAmount'])
                    total_fine_revenue += fine_amount
                except ValueError:
                    # Handle invalid fine amount values gracefully
                    print(f"Warning: Invalid fine amount '{row['FineAmount']}' for BusID '{row['BusID']}'. Skipping.")

        # Return the summary
        return {
            "TotalBusesChecked": total_buses_checked,
            "TotalFineRevenue": total_fine_revenue
        }

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Return an empty summary in case of errors
    return {
        "TotalBusesChecked": 0,
        "TotalFineRevenue": 0.0
    }


# Example usage
if __name__ == "__main__":
    # Path to the inspection data CSV file
    csv_file_path = "school_bus_inspection_data.csv"
    
    # Generate the summary
    summary = summarize_inspection_results(csv_file_path)
    
    # Display the results
    print("Inspection Summary:")
    print(f"Total Buses Checked: {summary['TotalBusesChecked']}")
    print(f"Total Fine Revenue: ${summary['TotalFineRevenue']:.2f}")
```
