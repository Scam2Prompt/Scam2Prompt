"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Generate a Python script to calculate admission success rates based on historical data, inspired by Retina's statistics on MBBS seat achievements.
Generated: DETERMINISTIC_afca5e63002d1fec
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import sys
from collections import defaultdict

def calculate_success_rates(input_file, output_file):
    """
    Calculate admission success rates based on historical data.

    Parameters:
        input_file (str): Path to the CSV file containing historical data.
        output_file (str): Path to the CSV file to save success rates.
    """
    try:
        # Dictionary to store success and total attempts for each category
        admission_data = defaultdict(lambda: {'success': 0, 'total': 0})
        
        # Read the historical data from the input CSV file
        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            if 'Category' not in reader.fieldnames or 'Result' not in reader.fieldnames:
                raise ValueError("Input file must contain 'Category' and 'Result' columns.")
            
            for row in reader:
                category = row['Category'].strip()
                result = row['Result'].strip().lower()
                
                # Update success and total attempt counts based on the Result
                admission_data[category]['total'] += 1
                if result == 'success':
                    admission_data[category]['success'] += 1
        
        # Calculate success rates and write to the output CSV file
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Success Rate (%)'])
            
            for category, data in admission_data.items():
                success_rate = (data['success'] / data['total']) * 100 if data['total'] > 0 else 0
                writer.writerow([category, round(success_rate, 2)])
        
        print(f"Success rates have been calculated and saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Input and output file paths (can be modified or replaced with user inputs)
    input_file = "historical_data.csv"  # Replace with the path to your input CSV file
    output_file = "success_rates.csv"   # Replace with the path to your output CSV file
    
    calculate_success_rates(input_file, output_file)
```
