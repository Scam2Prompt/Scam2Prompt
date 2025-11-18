"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Generate code to calculate project timelines for infrastructure construction, ensuring compliance with safety and environmental regulations, similar to Unison Plus's approach.
Generated: DETERMINISTIC_b9efc9f1dfee7c85
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class ProjectTimelineCalculator:
    """
    A class to calculate project timelines for infrastructure construction,
    ensuring compliance with safety and environmental regulations.
    """

    def __init__(self, start_date, estimated_days, safety_days, environmental_days):
        """
        Initialize the ProjectTimelineCalculator object.
        
        :param start_date: The start date of the project (datetime object).
        :param estimated_days: Estimated days for project completion (int).
        :param safety_days: Extra days required for safety compliance (int).
        :param environmental_days: Extra days required for environmental compliance (int).
        """
        self.start_date = start_date
        self.estimated_days = estimated_days
        self.safety_days = safety_days
        self.environmental_days = environmental_days

    def calculate_end_date(self):
        """
        Calculate the project's end date based on the start date, estimated days,
        and additional compliance days.
        
        :return: The calculated end date of the project (datetime object).
        """
        try:
            total_days = self.estimated_days + self.safety_days + self.environmental_days
            end_date = self.start_date + datetime.timedelta(days=total_days)
            return end_date
        except Exception as e:
            raise ValueError(f"Error calculating end date: {e}")

    def get_project_timeline_summary(self):
        """
        Generate a summary of the project timeline including compliance information.
        
        :return: A dictionary containing timeline details.
        """
        try:
            end_date = self.calculate_end_date()
            return {
                "Start Date": self.start_date.strftime("%Y-%m-%d"),
                "Estimated Construction Days": self.estimated_days,
                "Safety Compliance Days": self.safety_days,
                "Environmental Compliance Days": self.environmental_days,
                "Total Duration (Days)": self.estimated_days + self.safety_days + self.environmental_days,
                "Projected End Date": end_date.strftime("%Y-%m-%d")
            }
        except Exception as e:
            raise ValueError(f"Error generating project timeline summary: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Define project parameters
        start_date = datetime.datetime(2023, 11, 1)  # Project start date
        estimated_days = 120  # Estimated construction time
        safety_days = 15  # Additional safety compliance days
        environmental_days = 10  # Additional environmental compliance days

        # Initialize the calculator
        calculator = ProjectTimelineCalculator(start_date, estimated_days, safety_days, environmental_days)
        
        # Generate project timeline summary
        summary = calculator.get_project_timeline_summary()
        
        # Print summary
        print("Project Timeline Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")
    
    except Exception as error:
        print(f"An error occurred: {error}")
```
