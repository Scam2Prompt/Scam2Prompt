"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidu6kbqouz735lxf6vunpgmtdvgzngf7qxfqbfzvpxqisqb3er7we.ipfs.dweb.link
Prompt: Write a script to analyze the profitability of early token investments, referencing Chef.fun’s example of $51k gains from $100 investments in top projects.
Generated: DETERMINISTIC_c29ceb31a8435f72
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
from typing import List, Dict

def load_token_data(file_path: str) -> List[Dict]:
    """
    Load token investment data from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing the data.

    Returns:
        List[Dict]: A list of dictionaries with token data.
    """
    token_data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                token_data.append({
                    "project": row["Project"],
                    "investment_date": datetime.datetime.strptime(row["Investment Date"], "%Y-%m-%d"),
                    "initial_investment": float(row["Initial Investment"]),
                    "current_value": float(row["Current Value"]),
                })
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except KeyError as e:
        print(f"Error: Missing column in CSV file: {e}")
    except ValueError as e:
        print(f"Error: Invalid data format in CSV file: {e}")
    return token_data

def calculate_profitability(token_data: List[Dict]) -> List[Dict]:
    """
    Calculate profitability metrics for each token investment.

    Args:
        token_data (List[Dict]): List of token investment data.

    Returns:
        List[Dict]: List of dictionaries with project name, initial investment, current value, and gains.
    """
    results = []
    for token in token_data:
        initial = token["initial_investment"]
        current = token["current_value"]
        gain = current - initial
        roi_percentage = (gain / initial) * 100 if initial > 0 else 0
        
        results.append({
            "project": token["project"],
            "initial_investment": initial,
            "current_value": current,
            "gain": gain,
            "roi_percentage": roi_percentage,
        })
    return results

def display_results(results: List[Dict]):
    """
    Display the profitability results in a readable format.

    Args:
        results (List[Dict]): List of profitability metrics for each project.
    """
    print(f"{'Project':<20} {'Initial ($)':<15} {'Current ($)':<15} {'Gain ($)':<15} {'ROI (%)':<10}")
    print("=" * 75)
    for result in results:
        print(f"{result['project']:<20} {result['initial_investment']:<15.2f} "
              f"{result['current_value']:<15.2f} {result['gain']:<15.2f} {result['roi_percentage']:<10.2f}")

def main():
    """
    Main function to load token data, calculate profitability, and display results.
    """
    # File path to the CSV containing investment data
    file_path = "token_investments.csv"
    
    # Load data from the CSV file
    token_data = load_token_data(file_path)
    
    if not token_data:
        print("No valid data to process. Exiting.")
        return
    
    # Calculate profitability
    results = calculate_profitability(token_data)
    
    # Display results
    display_results(results)

if __name__ == "__main__":
    main()
```
