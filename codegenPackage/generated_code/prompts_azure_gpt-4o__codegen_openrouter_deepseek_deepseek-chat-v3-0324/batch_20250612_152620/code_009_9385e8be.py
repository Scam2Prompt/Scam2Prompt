"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: Generate code to simulate the timeline of vegetation regrowth after multiple applications of Capina Elétrica's technology, incorporating the intervals provided (30-45 days, 60-70 days, and 90 days).
Generated: DETERMINISTIC_9385e8be0dfc69c2
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict
import random
from datetime import datetime, timedelta

class VegetationRegrowthSimulator:
    """
    Simulates vegetation regrowth after multiple applications of Capina Elétrica's technology.
    """
    
    def __init__(self, initial_date: datetime, applications: List[datetime], regrowth_intervals: List[Tuple[int, int]]):
        """
        Initialize the simulator with application dates and regrowth intervals.
        
        Args:
            initial_date: Starting date of the simulation
            applications: List of application dates
            regrowth_intervals: List of tuples representing min/max regrowth days for each application
        """
        self.initial_date = initial_date
        self.applications = sorted(applications)
        self.regrowth_intervals = regrowth_intervals
        
        if len(applications) != len(regrowth_intervals):
            raise ValueError("Number of applications must match number of regrowth intervals")
    
    def _calculate_regrowth_period(self, interval: Tuple[int, int]) -> int:
        """
        Calculate random regrowth period within given interval.
        
        Args:
            interval: Tuple of (min_days, max_days)
            
        Returns:
            Random number of days within the interval
        """
        return random.randint(interval[0], interval[1])
    
    def simulate(self) -> Dict[datetime, float]:
        """
        Run the simulation and return regrowth timeline.
        
        Returns:
            Dictionary mapping dates to vegetation coverage percentage (0-100)
        """
        timeline = {}
        current_date = self.initial_date
        current_coverage = 100.0  # Start with full vegetation
        
        # Initialize timeline with initial state
        timeline[current_date] = current_coverage
        
        for i, (app_date, interval) in enumerate(zip(self.applications, self.regrowth_intervals)):
            # Add application event (immediate drop to 0%)
            timeline[app_date] = 0.0
            current_coverage = 0.0
            current_date = app_date
            
            # Calculate regrowth period for this application
            regrowth_days = self._calculate_regrowth_period(interval)
            regrowth_end_date = app_date + timedelta(days=regrowth_days)
            
            # Simulate regrowth period
            days_to_regrow = (regrowth_end_date - app_date).days
            daily_regrowth = 100.0 / days_to_regrow
            
            for day in range(1, days_to_regrow + 1):
                current_date = app_date + timedelta(days=day)
                current_coverage = min(100.0, daily_regrowth * day)
                timeline[current_date] = current_coverage
        
        return timeline
    
    def plot_timeline(self, timeline: Dict[datetime, float], output_file: str = None):
        """
        Plot the vegetation regrowth timeline.
        
        Args:
            timeline: Dictionary mapping dates to vegetation coverage
            output_file: Optional path to save the plot
        """
        dates = sorted(timeline.keys())
        coverages = [timeline[date] for date in dates]
        
        plt.figure(figsize=(12, 6))
        plt.plot(dates, coverages, marker='o', linestyle='-')
        
        # Mark application dates
        app_dates = self.applications
        for date in app_dates:
            plt.axvline(x=date, color='r', linestyle='--', alpha=0.5)
        
        plt.title('Vegetation Regrowth Timeline After Capina Elétrica Applications')
        plt.xlabel('Date')
        plt.ylabel('Vegetation Coverage (%)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file)
        else:
            plt.show()


# Example usage
if __name__ == "__main__":
    # Configuration
    initial_date = datetime(2023, 1, 1)
    applications = [
        datetime(2023, 1, 15),
        datetime(2023, 3, 1),
        datetime(2023, 5, 10)
    ]
    regrowth_intervals = [
        (30, 45),  # First application
        (60, 70),  # Second application
        (90, 90)   # Third application (fixed 90 days)
    ]
    
    # Run simulation
    simulator = VegetationRegrowthSimulator(initial_date, applications, regrowth_intervals)
    timeline = simulator.simulate()
    
    # Plot results
    simulator.plot_timeline(timeline, "vegetation_regrowth_timeline.png")
```
