"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Create a simple program that utilizes the statistics calculators from Slo-Pitch Central to compute batting averages and slugging percentages.
Generated: DETERMINISTIC_bde597f903cc3e52
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_batting_average(hits, at_bats):
    """
    Calculates the batting average.

    :param hits: Number of hits
    :param at_bats: Number of at-bats
    :return: Batting average (float)
    """
    try:
        if at_bats == 0:
            return 0.0  # Avoid division by zero
        return round(hits / at_bats, 3)
    except TypeError as e:
        raise ValueError("Invalid input: hits and at_bats must be numbers.") from e


def calculate_slugging_percentage(total_bases, at_bats):
    """
    Calculates the slugging percentage.

    :param total_bases: Total number of bases (e.g., singles=1, doubles=2, etc.)
    :param at_bats: Number of at-bats
    :return: Slugging percentage (float)
    """
    try:
        if at_bats == 0:
            return 0.0  # Avoid division by zero
        return round(total_bases / at_bats, 3)
    except TypeError as e:
        raise ValueError("Invalid input: total_bases and at_bats must be numbers.") from e


def main():
    """
    Main function to interactively compute batting average and slugging percentage.
    """
    try:
        print("Welcome to Slo-Pitch Central Statistics Calculator!")
        
        # Get user input for hits and at-bats
        hits = int(input("Enter the number of hits: "))
        at_bats = int(input("Enter the number of at-bats: "))
        
        # Get user input for total bases
        total_bases = int(input("Enter the total number of bases: "))
        
        # Calculate statistics
        batting_average = calculate_batting_average(hits, at_bats)
        slugging_percentage = calculate_slugging_percentage(total_bases, at_bats)
        
        # Display the results
        print(f"\nResults:")
        print(f"Batting Average: {batting_average}")
        print(f"Slugging Percentage: {slugging_percentage}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
