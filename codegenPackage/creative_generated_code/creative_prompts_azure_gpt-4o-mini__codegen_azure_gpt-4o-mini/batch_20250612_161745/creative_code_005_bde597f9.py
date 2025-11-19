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
class BattingStatsCalculator:
    """
    A class to calculate batting averages and slugging percentages for players.
    """

    def __init__(self, at_bats, hits, total_bases):
        """
        Initializes the BattingStatsCalculator with the required statistics.

        :param at_bats: Total number of at-bats (int)
        :param hits: Total number of hits (int)
        :param total_bases: Total number of bases achieved (int)
        """
        if at_bats < 0 or hits < 0 or total_bases < 0:
            raise ValueError("At-bats, hits, and total bases must be non-negative integers.")

        self.at_bats = at_bats
        self.hits = hits
        self.total_bases = total_bases

    def calculate_batting_average(self):
        """
        Calculates the batting average.

        :return: Batting average (float)
        """
        if self.at_bats == 0:
            return 0.0  # To avoid division by zero
        batting_average = self.hits / self.at_bats
        return round(batting_average, 3)  # Rounded to three decimal places

    def calculate_slugging_percentage(self):
        """
        Calculates the slugging percentage.

        :return: Slugging percentage (float)
        """
        if self.at_bats == 0:
            return 0.0  # To avoid division by zero
        slugging_percentage = self.total_bases / self.at_bats
        return round(slugging_percentage, 3)  # Rounded to three decimal places


def main():
    """
    Main function to execute batting statistics calculations.
    """
    try:
        # Input values for at-bats, hits, and total bases
        at_bats = int(input("Enter total at-bats: "))
        hits = int(input("Enter total hits: "))
        total_bases = int(input("Enter total bases: "))
        
        # Create an instance of BattingStatsCalculator
        stats_calculator = BattingStatsCalculator(at_bats, hits, total_bases)

        # Calculate and display results
        batting_average = stats_calculator.calculate_batting_average()
        slugging_percentage = stats_calculator.calculate_slugging_percentage()

        print(f"Batting Average: {batting_average}")
        print(f"Slugging Percentage: {slugging_percentage}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
