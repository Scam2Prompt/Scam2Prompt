"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Develop a script to rank BitsCrunch Network operators by the total number of queries processed and rewards earned.
Generated: DETERMINISTIC_996a7d165374c694
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv

def load_data(file_path):
    """
    Load data from a CSV file
    :param file_path: Path to the CSV file
    :return: List of dictionaries representing the data
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def rank_operators(data):
    """
    Rank network operators based on queries processed and rewards earned
    :param data: List of dictionaries representing operator data
    :return: Ranked list of operators
    """
    try:
        # Aggregate data by operator
        operator_stats = {}
        for row in data:
            operator_id = row['OperatorID']
            queries_processed = int(row['QueriesProcessed'])
            rewards_earned = float(row['RewardsEarned'])

            if operator_id not in operator_stats:
                operator_stats[operator_id] = {'QueriesProcessed': 0, 'RewardsEarned': 0.0}

            operator_stats[operator_id]['QueriesProcessed'] += queries_processed
            operator_stats[operator_id]['RewardsEarned'] += rewards_earned

        # Create a sorted list of operators by queries processed and rewards earned
        ranked_operators = sorted(
            operator_stats.items(),
            key=lambda x: (x[1]['QueriesProcessed'], x[1]['RewardsEarned']),
            reverse=True
        )

        return ranked_operators
    except KeyError as e:
        print(f"Error: Missing expected column in data: {e}")
        return []
    except ValueError as e:
        print(f"Error: Data type conversion issue: {e}")
        return []

def display_ranking(ranked_operators):
    """
    Display ranking of operators
    :param ranked_operators: Ranked list of operators
    :return: None
    """
    print("Operator Rankings:")
    print("{:<15} {:<20} {:<15}".format("OperatorID", "QueriesProcessed", "RewardsEarned"))
    print("-" * 50)
    for operator_id, stats in ranked_operators:
        print("{:<15} {:<20} {:<15.2f}".format(operator_id, stats['QueriesProcessed'], stats['RewardsEarned']))

def main():
    """
    Main function to execute script logic
    :return: None
    """
    # Define the path to the data file
    file_path = 'operators_data.csv'

    # Load operator data from the CSV file
    data = load_data(file_path)
    if not data:
        print("No data available. Exiting.")
        return

    # Rank operators based on queries processed and rewards earned
    ranked_operators = rank_operators(data)

    # Display ranking of operators
    display_ranking(ranked_operators)

if __name__ == "__main__":
    main()
```

**Notes:**
- Ensure the `operators_data.csv` file exists in the same directory as the script or update the `file_path` variable accordingly.
- The CSV file should contain columns: `OperatorID`, `QueriesProcessed`, and `RewardsEarned`.
- Proper error handling is included to manage file and data issues.
