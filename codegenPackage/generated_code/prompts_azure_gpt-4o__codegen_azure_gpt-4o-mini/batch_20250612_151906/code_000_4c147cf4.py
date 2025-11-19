"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Write Python code to calculate weekly mileage progression for a 100-mile running training plan, including peak weeks reaching 70-100 miles, as described on Boost Running.
Generated: DETERMINISTIC_4c147cf41878c65d
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RunningPlan:
    def __init__(self, total_miles=100, peak_weeks=(70, 100), base_mileage=20, weeks=12):
        """
        Initializes the running plan with the specified parameters.

        :param total_miles: Total miles to be run in the training plan (default is 100).
        :param peak_weeks: A tuple indicating the range of peak weekly mileage (default is (70, 100)).
        :param base_mileage: Base weekly mileage to start the training plan (default is 20).
        :param weeks: Total number of weeks for the training plan (default is 12).
        """
        self.total_miles = total_miles
        self.peak_weeks = peak_weeks
        self.base_mileage = base_mileage
        self.weeks = weeks
        self.mileage_progression = []

    def calculate_progression(self):
        """
        Calculates the weekly mileage progression for the training plan.
        The progression starts from base mileage and peaks within the specified range.
        """
        try:
            # Calculate the number of weeks to reach peak mileage
            peak_start_week = self.weeks // 2
            peak_end_week = peak_start_week + 3  # Peak for 3 weeks

            for week in range(1, self.weeks + 1):
                if week < peak_start_week:
                    # Gradually increase mileage to base mileage
                    mileage = self.base_mileage + (week - 1) * (self.peak_weeks[0] - self.base_mileage) / peak_start_week
                elif peak_start_week <= week < peak_end_week:
                    # Maintain peak mileage
                    mileage = self.peak_weeks[1]
                else:
                    # Gradually decrease mileage after peak
                    mileage = self.peak_weeks[1] - (week - peak_end_week) * (self.peak_weeks[1] - self.base_mileage) / (self.weeks - peak_end_week)

                self.mileage_progression.append(round(mileage, 2))

            # Ensure total mileage does not exceed the specified total miles
            if sum(self.mileage_progression) > self.total_miles:
                raise ValueError("Total mileage exceeds the specified limit.")

        except Exception as e:
            print(f"Error calculating mileage progression: {e}")

    def display_progression(self):
        """
        Displays the weekly mileage progression.
        """
        print("Weekly Mileage Progression:")
        for week, mileage in enumerate(self.mileage_progression, start=1):
            print(f"Week {week}: {mileage} miles")

if __name__ == "__main__":
    # Create a running plan instance
    training_plan = RunningPlan()
    
    # Calculate the mileage progression
    training_plan.calculate_progression()
    
    # Display the results
    training_plan.display_progression()
```
