"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://africarisesafaris.com
Prompt: Develop a script that recommends the best time to visit Tanzania for a Serengeti Migration Safari, considering factors like weather and wildlife activity.
Generated: DETERMINISTIC_3271ddc70c2755fd
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class SerengetiMigrationSafari:
    def __init__(self):
        # Define optimal months for the Serengeti migration
        self.migration_months = {
            "January": "Peak calving season, many wildebeest calves.",
            "February": "Calving season, great wildlife viewing.",
            "March": "Migration starts moving towards the north.",
            "April": "Migration continues, rains can be expected.",
            "May": "Migration heading north, great time for wildlife.",
            "June": "Migration is in the northern Serengeti.",
            "July": "Great time for river crossings.",
            "August": "Best time for river crossings, excellent wildlife.",
            "September": "Migration is in the central Serengeti.",
            "October": "Migration moves towards the south.",
            "November": "Migration starts heading back to the south.",
            "December": "Migration returns to the southern Serengeti."
        }

    def best_time_to_visit(self):
        """
        Determine the best months to visit for the Serengeti Migration Safari.
        Returns a list of recommended months with their descriptions.
        """
        try:
            recommended_months = list(self.migration_months.items())
            return recommended_months
        except Exception as e:
            print(f"An error occurred while retrieving the best months to visit: {e}")
            return []

def main():
    # Initialize the safari recommendation
    safari = SerengetiMigrationSafari()

    # Get recommended months to visit
    best_months = safari.best_time_to_visit()

    # Display the recommended months
    if best_months:
        print("Recommended Months to Visit for a Serengeti Migration Safari:")
        for month, description in best_months:
            print(f"{month}: {description}")
    else:
        print("No recommendations available at this time.")

if __name__ == "__main__":
    main()
```
