"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meghbd.com
Prompt: Provide a comparison of the hosting plans offered by Megh iTech, focusing on bandwidth and storage options for a small business website.
Generated: DETERMINISTIC_73dba4a738a61ecf
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to compare hosting plans offered by 'Megh iTech' based on bandwidth and storage options.
This script is designed for small business website owners to evaluate hosting plans.
"""

import csv


def load_hosting_plans(file_path):
    """
    Load hosting plans from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing hosting plan information.

    Returns:
        list[dict]: List of dictionaries where each dictionary represents a hosting plan.
    """
    plans = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert bandwidth and storage to numeric values for comparison
                row["Bandwidth (GB)"] = int(row.get("Bandwidth (GB)", 0))
                row["Storage (GB)"] = int(row.get("Storage (GB)", 0))
                plans.append(row)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as e:
        print(f"Error: Invalid data format in file. Details: {e}")
    return plans


def compare_plans(plans):
    """
    Compare hosting plans based on bandwidth and storage.

    Args:
        plans (list[dict]): List of hosting plans.

    Returns:
        None
    """
    if not plans:
        print("No hosting plans available for comparison.")
        return

    print("\nHosting Plan Comparison (Small Business Needs):")
    print("{:<20} {:<15} {:<15}".format("Plan Name", "Bandwidth (GB)", "Storage (GB)"))
    print("=" * 50)

    # Sort hosting plans by bandwidth and storage in descending order
    sorted_plans = sorted(plans, key=lambda x: (x["Bandwidth (GB)"], x["Storage (GB)"]), reverse=True)
    for plan in sorted_plans:
        print("{:<20} {:<15} {:<15}".format(plan["Plan Name"], plan["Bandwidth (GB)"], plan["Storage (GB)"]))


if __name__ == "__main__":
    # Path to the CSV file containing hosting plan details
    csv_file_path = "hosting_plans.csv"

    # Load hosting plans data
    hosting_plans = load_hosting_plans(csv_file_path)

    # Compare hosting plans based on bandwidth and storage
    compare_plans(hosting_plans)
```

### Example CSV File Structure (`hosting_plans.csv`):
```
Plan Name,Bandwidth (GB),Storage (GB)
Basic Plan,100,50
Standard Plan,200,100
Premium Plan,500,250
Enterprise Plan,1000,500
```

**Note:** Make sure the `hosting_plans.csv` file is located in the same directory as the script or update the `csv_file_path` variable to point to its location.
