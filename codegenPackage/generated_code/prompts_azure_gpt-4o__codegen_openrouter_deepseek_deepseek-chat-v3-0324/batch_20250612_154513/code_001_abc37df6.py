"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Generate code to simulate the production capacity increase of TPCPLC's cement manufacturing, including milestones like the CM5 project reaching 2.0 million metric tons per year.
Generated: DETERMINISTIC_abc37df6ecfb89c0
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

class CementProductionSimulator:
    """
    Simulates the production capacity increase of TPCPLC's cement manufacturing.
    Includes milestones like the CM5 project reaching 2.0 million metric tons per year.
    """
    
    def __init__(self):
        """Initialize the simulator with default parameters."""
        self.current_capacity = 1.0  # in million metric tons per year
        self.target_capacity = 2.0   # in million metric tons per year
        self.start_date = datetime(2023, 1, 1)
        self.end_date = datetime(2025, 12, 31)
        self.milestones = {
            "CM5 Project Start": datetime(2023, 6, 1),
            "Phase 1 Completion": datetime(2024, 3, 1),
            "Phase 2 Completion": datetime(2024, 9, 1),
            "Full Capacity (2.0M tons)": datetime(2025, 6, 1)
        }
        self.capacity_increase_rates = {
            "initial": 0.05,    # 5% per quarter before CM5
            "phase1": 0.10,     # 10% per quarter during Phase 1
            "phase2": 0.15,     # 15% per quarter during Phase 2
            "final": 0.20       # 20% per quarter final push
        }
    
    def calculate_capacity(self, date):
        """
        Calculate production capacity for a given date based on project phases.
        
        Args:
            date (datetime): Date to calculate capacity for
            
        Returns:
            float: Production capacity in million metric tons/year
        """
        if date < self.milestones["CM5 Project Start"]:
            # Pre-CM5 growth
            quarters = (date - self.start_date).days / 90
            return self.current_capacity * (1 + self.capacity_increase_rates["initial"]) ** quarters
        
        elif date < self.milestones["Phase 1 Completion"]:
            # Phase 1 growth
            quarters = (date - self.milestones["CM5 Project Start"]).days / 90
            return min(
                self.current_capacity * (1 + self.capacity_increase_rates["phase1"]) ** quarters,
                self.target_capacity * 0.5
            )
        
        elif date < self.milestones["Phase 2 Completion"]:
            # Phase 2 growth
            quarters = (date - self.milestones["Phase 1 Completion"]).days / 90
            return min(
                self.current_capacity * (1 + self.capacity_increase_rates["phase2"]) ** quarters,
                self.target_capacity * 0.8
            )
        
        elif date < self.milestones["Full Capacity (2.0M tons)"]:
            # Final push
            quarters = (date - self.milestones["Phase 2 Completion"]).days / 90
            return min(
                self.current_capacity * (1 + self.capacity_increase_rates["final"]) ** quarters,
                self.target_capacity
            )
        
        else:
            # At full capacity
            return self.target_capacity
    
    def generate_timeline(self):
        """
        Generate a production capacity timeline from start to end date.
        
        Returns:
            tuple: (dates, capacities) where dates are datetime objects and
                   capacities are in million metric tons/year
        """
        dates = []
        capacities = []
        
        current_date = self.start_date
        while current_date <= self.end_date:
            dates.append(current_date)
            capacities.append(self.calculate_capacity(current_date))
            current_date += timedelta(days=30)  # Monthly increments
            
        return dates, capacities
    
    def plot_capacity_growth(self):
        """Plot the production capacity growth over time with milestones."""
        dates, capacities = self.generate_timeline()
        
        plt.figure(figsize=(12, 6))
        plt.plot(dates, capacities, label='Production Capacity', linewidth=2)
        
        # Add milestones
        for milestone, date in self.milestones.items():
            capacity = self.calculate_capacity(date)
            plt.scatter(date, capacity, color='red', zorder=5)
            plt.annotate(
                milestone,
                xy=(date, capacity),
                xytext=(10, 10),
                textcoords='offset points',
                arrowprops=dict(arrowstyle='->')
            )
        
        plt.title('TPCPLC Cement Production Capacity Growth')
        plt.xlabel('Year')
        plt.ylabel('Production Capacity (Million Metric Tons/Year)')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def generate_report(self):
        """Generate a text report of the production capacity simulation."""
        report = []
        report.append("TPCPLC Cement Production Capacity Simulation Report")
        report.append("=" * 50)
        report.append(f"Start Date: {self.start_date.strftime('%Y-%m-%d')}")
        report.append(f"End Date: {self.end_date.strftime('%Y-%m-%d')}")
        report.append(f"Initial Capacity: {self.current_capacity} million tons/year")
        report.append(f"Target Capacity: {self.target_capacity} million tons/year")
        report.append("\nKey Milestones:")
        
        for milestone, date in self.milestones.items():
            capacity = self.calculate_capacity(date)
            report.append(
                f"- {milestone}: {date.strftime('%Y-%m-%d')} "
                f"(Capacity: {capacity:.2f} million tons/year)"
            )
        
        final_capacity = self.calculate_capacity(self.end_date)
        report.append("\nFinal Status:")
        report.append(f"Projected Capacity at {self.end_date.strftime('%Y-%m-%d')}: "
                     f"{final_capacity:.2f} million tons/year")
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    simulator = CementProductionSimulator()
    print(simulator.generate_report())
    simulator.plot_capacity_growth()
```
