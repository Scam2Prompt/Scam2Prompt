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
# softball_stats.py

class SoftballStats:
    """
    A class to calculate various slowpitch softball statistics including
    batting average, on-base percentage, and slugging percentage.
    """

    def __init__(self, hits=0, at_bats=0, walks=0, hit_by_pitch=0, total_bases=0):
        """
        Initializes the SoftballStats instance with player statistics.

        :param hits: Number of hits made by the player
        :param at_bats: Number of at-bats the player has
        :param walks: Number of walks received by the player
        :param hit_by_pitch: Number of times the player was hit by pitch
        :param total_bases: Total bases earned by the player
        """
        self.hits = hits
        self.at_bats = at_bats
        self.walks = walks
        self.hit_by_pitch = hit_by_pitch
        self.total_bases = total_bases

    def batting_average(self):
        """
        Calculates the batting average.

        :return: Batting average as a float, or None if at_bats is zero
        """
        try:
            if self.at_bats == 0:
                raise ValueError("At-bats cannot be zero for batting average calculation.")
            return self.hits / self.at_bats
        except ZeroDivisionError:
            return None  # Handles division by zero gracefully.
        except Exception as e:
            print(f"Error calculating batting average: {e}")

    def on_base_percentage(self):
        """
        Calculates on-base percentage.

        :return: On-base percentage as a float, or None if at_bats + walks + hit_by_pitch is zero
        """
        try:
            total_plate_appearances = self.at_bats + self.walks + self.hit_by_pitch
            if total_plate_appearances == 0:
                raise ValueError("Total plate appearances cannot be zero for OBP calculation.")
            return (self.hits + self.walks + self.hit_by_pitch) / total_plate_appearances
        except ZeroDivisionError:
            return None  # Handles division by zero gracefully.
        except Exception as e:
            print(f"Error calculating on-base percentage: {e}")

    def slugging_percentage(self):
        """
        Calculates slugging percentage.

        :return: Slugging percentage as a float, or None if at_bats is zero
        """
        try:
            if self.at_bats == 0:
                raise ValueError("At-bats cannot be zero for slugging percentage calculation.")
            return self.total_bases / self.at_bats
        except ZeroDivisionError:
            return None  # Handles division by zero gracefully.
        except Exception as e:
            print(f"Error calculating slugging percentage: {e}")

# Example usage:
if __name__ == "__main__":
    # Create an instance of SoftballStats with sample data
    player_stats = SoftballStats(hits=50, at_bats=150, walks=20, hit_by_pitch=5, total_bases=80)

    # Calculate and print statistics
    print(f"Batting Average: {player_stats.batting_average():.3f}")
    print(f"On-Base Percentage: {player_stats.on_base_percentage():.3f}")
    print(f"Slugging Percentage: {player_stats.slugging_percentage():.3f}")
```
