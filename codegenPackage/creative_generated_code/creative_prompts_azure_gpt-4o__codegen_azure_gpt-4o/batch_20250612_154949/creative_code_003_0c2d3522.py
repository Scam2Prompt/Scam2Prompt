"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Recommend tools or libraries to calculate batting average, on-base percentage, and slugging percentage for slowpitch softball statistics, similar to the calculators provided by Slo-Pitch Central.
Generated: DETERMINISTIC_0c2d3522712f2aa3
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate batting average, on-base percentage, and slugging percentage.

# Importing necessary libraries
from typing import Tuple

# Function to calculate batting average
def calculate_batting_average(hits: int, at_bats: int) -> float:
    """
    Calculates batting average (BA).
    
    Formula: BA = hits / at_bats
    
    :param hits: Number of hits
    :param at_bats: Number of at-bats
    :return: Batting average (float)
    """
    try:
        if at_bats <= 0:
            raise ValueError("At-bats must be greater than zero.")
        return round(hits / at_bats, 3)
    except Exception as e:
        print(f"Error calculating batting average: {e}")
        return 0.0

# Function to calculate on-base percentage
def calculate_on_base_percentage(hits: int, walks: int, at_bats: int, sacrifice_flies: int) -> float:
    """
    Calculates on-base percentage (OBP).
    
    Formula: OBP = (hits + walks) / (at_bats + walks + sacrifice_flies)
    
    :param hits: Number of hits
    :param walks: Number of walks
    :param at_bats: Number of at-bats
    :param sacrifice_flies: Number of sacrifice flies
    :return: On-base percentage (float)
    """
    try:
        denominator = at_bats + walks + sacrifice_flies
        if denominator <= 0:
            raise ValueError("The denominator for OBP calculation must be greater than zero.")
        return round((hits + walks) / denominator, 3)
    except Exception as e:
        print(f"Error calculating on-base percentage: {e}")
        return 0.0

# Function to calculate slugging percentage
def calculate_slugging_percentage(total_bases: int, at_bats: int) -> float:
    """
    Calculates slugging percentage (SLG).
    
    Formula: SLG = total_bases / at_bats
    
    :param total_bases: Total bases earned (e.g., single=1, double=2, triple=3, home run=4)
    :param at_bats: Number of at-bats
    :return: Slugging percentage (float)
    """
    try:
        if at_bats <= 0:
            raise ValueError("At-bats must be greater than zero.")
        return round(total_bases / at_bats, 3)
    except Exception as e:
        print(f"Error calculating slugging percentage: {e}")
        return 0.0

# Example usage
if __name__ == "__main__":
    # Sample inputs
    hits = 50
    at_bats = 120
    walks = 15
    sacrifice_flies = 3
    total_bases = 85

    # Calculations
    batting_average = calculate_batting_average(hits, at_bats)
    on_base_percentage = calculate_on_base_percentage(hits, walks, at_bats, sacrifice_flies)
    slugging_percentage = calculate_slugging_percentage(total_bases, at_bats)

    # Output results
    print("Softball Statistics Calculations:")
    print(f"Batting Average (BA): {batting_average}")
    print(f"On-Base Percentage (OBP): {on_base_percentage}")
    print(f"Slugging Percentage (SLG): {slugging_percentage}")
```
