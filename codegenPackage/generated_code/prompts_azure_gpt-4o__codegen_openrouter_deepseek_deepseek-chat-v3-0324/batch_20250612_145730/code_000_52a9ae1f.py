"""
Generated Code Metadata:
========================
Original URL: https://pansos4dmax.site
Prompt: Write a Python script to simulate a lottery result generator based on the format used by PANSOS4D, including results for locations like Wuhan, Sydney, and Singapore.
Generated: DETERMINISTIC_52a9ae1f12b0d42a
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
import pytz

class PANSOS4DLotteryGenerator:
    """
    Simulates a lottery result generator based on the PANSOS4D format.
    Generates results for specified locations with appropriate time zones.
    """
    
    def __init__(self):
        self.locations = {
            'Wuhan': {
                'timezone': 'Asia/Shanghai',
                'draw_times': ['13:00', '16:00', '19:00', '22:00']
            },
            'Sydney': {
                'timezone': 'Australia/Sydney',
                'draw_times': ['10:00', '13:00', '16:00', '19:00']
            },
            'Singapore': {
                'timezone': 'Asia/Singapore',
                'draw_times': ['09:00', '12:00', '15:00', '18:00']
            }
        }
    
    def generate_result(self):
        """
        Generates a random 4-digit lottery result (0000-9999).
        """
        return f"{random.randint(0, 9999):04d}"
    
    def get_next_draw_time(self, location):
        """
        Calculates the next upcoming draw time for a given location.
        """
        if location not in self.locations:
            raise ValueError(f"Invalid location: {location}")
        
        tz = pytz.timezone(self.locations[location]['timezone'])
        now = datetime.now(tz)
        today = now.date()
        
        for draw_time in self.locations[location]['draw_times']:
            hour, minute = map(int, draw_time.split(':'))
            draw_dt = tz.localize(datetime.combine(today, datetime.min.time().replace(hour=hour, minute=minute)))
            
            if draw_dt > now:
                return draw_dt
            
        # If all today's draws passed, return first draw of next day
        first_draw = self.locations[location]['draw_times'][0]
        hour, minute = map(int, first_draw.split(':'))
        return tz.localize(datetime.combine(today + timedelta(days=1), datetime.min.time().replace(hour=hour, minute=minute)))
    
    def generate_lottery_results(self, location, num_results=1):
        """
        Generates lottery results for a specified location.
        
        Args:
            location (str): One of the supported locations
            num_results (int): Number of results to generate
            
        Returns:
            list: List of dictionaries containing result details
        """
        if location not in self.locations:
            raise ValueError(f"Invalid location: {location}")
        
        if num_results < 1:
            raise ValueError("Number of results must be at least 1")
        
        results = []
        tz = pytz.timezone(self.locations[location]['timezone'])
        
        for _ in range(num_results):
            next_draw = self.get_next_draw_time(location)
            result = {
                'location': location,
                'result': self.generate_result(),
                'draw_time': next_draw.strftime('%Y-%m-%d %H:%M'),
                'timezone': self.locations[location]['timezone']
            }
            results.append(result)
        
        return results
    
    def display_results(self, results):
        """
        Displays the generated results in a formatted way.
        """
        print("\nPANSOS4D Lottery Results")
        print("=" * 30)
        for result in results:
            print(f"Location: {result['location']}")
            print(f"Draw Time: {result['draw_time']} ({result['timezone']})")
            print(f"Result: {result['result']}")
            print("-" * 30)

if __name__ == "__main__":
    try:
        generator = PANSOS4DLotteryGenerator()
        
        # Generate results for all locations
        all_results = []
        for location in generator.locations:
            all_results.extend(generator.generate_lottery_results(location))
        
        # Display the results
        generator.display_results(all_results)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
