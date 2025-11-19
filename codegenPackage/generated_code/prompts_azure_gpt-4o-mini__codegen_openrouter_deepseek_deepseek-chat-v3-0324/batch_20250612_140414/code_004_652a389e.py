"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: Explain how ultrasonic cleaning can extend the lifespan of filters in the plastics industry and provide a case study example.
Generated: DETERMINISTIC_652a389ec81bce40
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how ultrasonic cleaning can extend the lifespan of filters
in the plastics industry through a simulated case study.

The code includes:
1. A Filter class representing industrial filters
2. Ultrasonic cleaning simulation
3. Performance metrics tracking
4. A case study example comparing cleaned vs. non-cleaned filters
"""

import random
from dataclasses import dataclass
from typing import List
import matplotlib.pyplot as plt
import numpy as np


@dataclass
class Filter:
    """Represents an industrial filter used in plastics processing."""
    id: int
    initial_efficiency: float = 0.95  # 95% efficiency when new
    current_efficiency: float = 0.95
    contamination_level: float = 0.0  # 0 = clean, 1 = fully clogged
    cleaning_cycles: int = 0
    total_operating_hours: float = 0.0
    
    def operate(self, hours: float):
        """Simulate filter operation, increasing contamination over time."""
        contamination_rate = 0.01  # per hour of operation
        self.contamination_level = min(
            1.0, 
            self.contamination_level + (hours * contamination_rate)
        )
        self.total_operating_hours += hours
        self._update_efficiency()
    
    def ultrasonic_clean(self):
        """Perform ultrasonic cleaning on the filter."""
        if self.contamination_level > 0:
            # Ultrasonic cleaning removes 70-90% of contamination
            cleaning_effectiveness = random.uniform(0.7, 0.9)
            self.contamination_level *= (1 - cleaning_effectiveness)
            self.cleaning_cycles += 1
            self._update_efficiency()
            return True
        return False
    
    def _update_efficiency(self):
        """Update filter efficiency based on contamination level."""
        efficiency_loss = self.contamination_level * 0.4  # Max 40% efficiency loss
        self.current_efficiency = max(
            0.6,  # Minimum operational efficiency
            self.initial_efficiency - efficiency_loss
        )
    
    def is_clogged(self) -> bool:
        """Check if filter is too clogged to function effectively."""
        return self.current_efficiency < 0.65 or self.contamination_level > 0.9


def run_case_study():
    """Run a comparative case study of cleaned vs. non-cleaned filters."""
    # Create two identical filters
    cleaned_filter = Filter(id=1)
    non_cleaned_filter = Filter(id=2)
    
    # Simulation parameters
    operating_hours_per_day = 24
    days_to_simulate = 365  # 1 year
    cleaning_interval_days = 7  # Weekly cleaning
    
    # Track metrics over time
    days = []
    cleaned_efficiencies = []
    non_cleaned_efficiencies = []
    
    for day in range(days_to_simulate):
        # Operate both filters
        cleaned_filter.operate(operating_hours_per_day)
        non_cleaned_filter.operate(operating_hours_per_day)
        
        # Perform ultrasonic cleaning on schedule
        if day % cleaning_interval_days == 0:
            cleaned_filter.ultrasonic_clean()
        
        # Record metrics
        days.append(day)
        cleaned_efficiencies.append(cleaned_filter.current_efficiency)
        non_cleaned_efficiencies.append(non_cleaned_filter.current_efficiency)
        
        # Check for filter failure
        if non_cleaned_filter.is_clogged():
            print(f"Non-cleaned filter failed on day {day}")
            break
    
    # Generate results visualization
    plt.figure(figsize=(10, 6))
    plt.plot(days, cleaned_efficiencies, label='With Ultrasonic Cleaning')
    plt.plot(days, non_cleaned_efficiencies, label='No Cleaning')
    plt.title('Filter Efficiency Over Time')
    plt.xlabel('Days of Operation')
    plt.ylabel('Filter Efficiency')
    plt.legend()
    plt.grid(True)
    plt.savefig('filter_efficiency_comparison.png')
    plt.close()
    
    # Print summary statistics
    print("\nCase Study Results:")
    print(f"Non-cleaned filter lifespan: {day} days")
    print(f"Cleaned filter efficiency after {days_to_simulate} days: {cleaned_filter.current_efficiency:.2f}")
    print(f"Cleaned filter contamination level: {cleaned_filter.contamination_level:.2f}")
    print(f"Number of cleaning cycles: {cleaned_filter.cleaning_cycles}")


if __name__ == "__main__":
    print("Plastics Industry Filter Lifespan Case Study")
    print("Simulating the impact of ultrasonic cleaning on filter lifespan...\n")
    run_case_study()
```
