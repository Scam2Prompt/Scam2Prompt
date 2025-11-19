"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Generate a 16-week training plan for a half marathon, incorporating long runs, interval runs, and strength training as detailed on Boost Running.
Generated: DETERMINISTIC_7e46089b665f8894
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class HalfMarathonTrainingPlan:
    """
    A 16-week training plan for a half marathon, incorporating long runs, interval runs, and strength training.
    """
    
    def __init__(self, start_date):
        """
        Initialize the training plan with a start date.
        
        Args:
            start_date (str): Start date in 'YYYY-MM-DD' format.
        """
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        self.plan = self._generate_plan()
    
    def _generate_plan(self):
        """
        Generate the 16-week training plan.
        
        Returns:
            list: List of dictionaries representing each week's training plan.
        """
        plan = []
        for week in range(1, 17):
            week_start = self.start_date + timedelta(days=(week-1)*7)
            week_plan = {
                'week': week,
                'start_date': week_start.strftime('%Y-%m-%d'),
                'training': self._get_week_plan(week)
            }
            plan.append(week_plan)
        return plan
    
    def _get_week_plan(self, week_num):
        """
        Get the training plan for a specific week.
        
        Args:
            week_num (int): Week number (1-16).
            
        Returns:
            dict: Training plan for the week.
        """
        if week_num <= 4:
            # Base building phase
            return {
                'monday': 'Rest or cross-training',
                'tuesday': f'{3 + (week_num-1)*0.5} miles easy run',
                'wednesday': 'Strength training (30-45 mins)',
                'thursday': f'{3 + (week_num-1)*0.5} miles with 4x30s strides',
                'friday': 'Rest',
                'saturday': f'{4 + (week_num-1)} miles long run',
                'sunday': 'Rest or yoga'
            }
        elif week_num <= 8:
            # Building endurance
            return {
                'monday': 'Rest or cross-training',
                'tuesday': f'{4 + (week_num-5)*0.5} miles easy run',
                'wednesday': 'Strength training (30-45 mins)',
                'thursday': f'Interval: 1 mile warmup, {3 + (week_num-5)}x800m at 5K pace with 400m recovery, 1 mile cooldown',
                'friday': 'Rest',
                'saturday': f'{6 + (week_num-5)} miles long run',
                'sunday': 'Rest or yoga'
            }
        elif week_num <= 12:
            # Increasing intensity
            return {
                'monday': 'Rest or cross-training',
                'tuesday': f'{5 + (week_num-9)*0.5} miles easy run',
                'wednesday': 'Strength training (30-45 mins)',
                'thursday': f'Tempo: 1 mile warmup, {2 + (week_num-9)} miles at half marathon pace, 1 mile cooldown',
                'friday': 'Rest',
                'saturday': f'{8 + (week_num-9)} miles long run',
                'sunday': 'Rest or yoga'
            }
        else:
            # Tapering phase
            long_run = max(10 - (week_num-13)*2, 6)  # Reduce long run distance
            return {
                'monday': 'Rest or cross-training',
                'tuesday': f'{4 - (week_num-13)} miles easy run',
                'wednesday': 'Strength training (30 mins)',
                'thursday': f'Interval: 1 mile warmup, {4 - (week_num-13)}x400m at 5K pace with 400m recovery, 1 mile cooldown',
                'friday': 'Rest',
                'saturday': f'{long_run} miles long run',
                'sunday': 'Rest or yoga'
            }
    
    def to_json(self, filename=None):
        """
        Export the training plan to JSON format.
        
        Args:
            filename (str, optional): File to save the JSON to. If None, returns the JSON string.
            
        Returns:
            str: JSON string if filename is None, otherwise None.
        """
        json_data = json.dumps(self.plan, indent=2)
        if filename:
            with open(filename, 'w') as f:
                f.write(json_data)
        else:
            return json_data
    
    def print_plan(self):
        """Print the training plan in a human-readable format."""
        for week in self.plan:
            print(f"\nWeek {week['week']} ({week['start_date']}):")
            for day, workout in week['training'].items():
                print(f"  {day.capitalize()}: {workout}")

# Example usage
if __name__ == "__main__":
    try:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        plan = HalfMarathonTrainingPlan(start_date)
        plan.print_plan()
        
        # Optionally save to JSON
        save_json = input("Save to JSON file? (y/n): ").lower()
        if save_json == 'y':
            filename = input("Enter filename (e.g., training_plan.json): ")
            plan.to_json(filename)
            print(f"Plan saved to {filename}")
    except ValueError as e:
        print(f"Error: Invalid date format. Please use YYYY-MM-DD. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
