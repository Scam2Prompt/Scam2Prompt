"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidxxnu2mmv3h3e3o4pjboi7c2ou6bluyjywr5cbxb53ltxd2gp244.ipfs.dweb.link
Prompt: Write code to calculate pledge percentages for a cryptocurrency investment firm, referencing DWF Labs' "$DWF Pledge Now" feature.
Generated: DETERMINISTIC_a1dba0c478d1126d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_pledge_percentages(total_pledged, individual_pledges):
    """
    Calculate pledge percentages for a cryptocurrency investment firm.

    Args:
        total_pledged (float): The total amount pledged by all investors.
        individual_pledges (list of float): A list of individual pledged amounts.

    Returns:
        list of float: A list of percentages representing individual contributions.
    """
    # Validate inputs
    if total_pledged <= 0:
        raise ValueError("Total pledged amount must be greater than zero.")
    if not individual_pledges or not all(isinstance(p, (int, float)) and p >= 0 for p in individual_pledges):
        raise ValueError("Individual pledged amounts must be a list of non-negative numbers.")

    # Calculate percentages
    percentages = [(pledge / total_pledged) * 100 for pledge in individual_pledges]
    return percentages


def main():
    """
    Main function to handle user input and display pledge percentages.
    """
    try:
        print("Welcome to the $DWF Pledge Percentage Calculator\n")

        # Input the total amount pledged
        total_pledged = float(input("Enter the total amount pledged (in USD or cryptocurrency units): "))

        # Input individual pledges as a comma-separated string
        pledges_input = input("Enter the individual pledges (comma-separated, e.g., 100,200,300): ")
        individual_pledges = [float(p.strip()) for p in pledges_input.split(',')]

        # Calculate percentages
        percentages = calculate_pledge_percentages(total_pledged, individual_pledges)

        # Display results
        print("\nPledge Percentages:")
        for i, percentage in enumerate(percentages, start=1):
            print(f"Investor {i}: {percentage:.2f}%")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
