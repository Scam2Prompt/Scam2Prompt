"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Develop a 100-mile running training plan with a gradual mileage increase, peak weeks reaching 70-100 miles, and a sample weekly schedule, and provide advice on building endurance and mental tenacity.
Generated: DETERMINISTIC_30fa839a6c1b8660
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TrainingPlan:
    def __init__(self, total_miles=100, peak_miles=100, weeks=16):
        """
        Initialize the training plan with total miles, peak miles, and number of weeks.
        
        :param total_miles: Total miles to be run in the training plan (default is 100).
        :param peak_miles: Maximum miles to be run in peak weeks (default is 100).
        :param weeks: Total number of weeks for the training plan (default is 16).
        """
        self.total_miles = total_miles
        self.peak_miles = peak_miles
        self.weeks = weeks
        self.schedule = self.generate_schedule()

    def generate_schedule(self):
        """
        Generate a weekly training schedule with gradual mileage increase.
        
        :return: A list of weekly mileage targets.
        """
        schedule = []
        base_mileage = 10  # Starting mileage for the first week
        increment = (self.peak_miles - base_mileage) // (self.weeks - 1)

        for week in range(self.weeks):
            if week < self.weeks - 4:  # Build up to peak mileage
                weekly_miles = base_mileage + week * increment
            else:  # Maintain peak mileage for the last 4 weeks
                weekly_miles = self.peak_miles
            schedule.append(weekly_miles)

        return schedule

    def display_schedule(self):
        """
        Display the training schedule in a readable format.
        """
        print("Weekly Training Schedule (in miles):")
        for week, miles in enumerate(self.schedule, start=1):
            print(f"Week {week}: {miles} miles")

    @staticmethod
    def endurance_tips():
        """
        Provide tips for building endurance and mental tenacity.
        """
        tips = [
            "1. Gradually increase your long run distance each week.",
            "2. Incorporate cross-training activities like cycling or swimming.",
            "3. Focus on nutrition and hydration to fuel your runs.",
            "4. Practice mental strategies such as visualization and positive self-talk.",
            "5. Set small, achievable goals to build confidence.",
            "6. Include rest days to allow for recovery and prevent injury."
        ]
        print("\nTips for Building Endurance and Mental Tenacity:")
        for tip in tips:
            print(tip)

if __name__ == "__main__":
    try:
        # Create a training plan instance
        training_plan = TrainingPlan()
        
        # Display the generated training schedule
        training_plan.display_schedule()
        
        # Provide endurance tips
        training_plan.endurance_tips()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
