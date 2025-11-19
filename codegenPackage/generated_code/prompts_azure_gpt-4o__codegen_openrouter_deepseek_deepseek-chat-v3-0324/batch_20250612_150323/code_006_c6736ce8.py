"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Generate a script to track and visualize green energy generation, usage, and CO2 savings percentages (25%, 50%, 75%, 100%) as described on Stromkonto's platform.
Generated: DETERMINISTIC_c6736ce83b05bddb
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from typing import Dict, List, Optional, Tuple

class GreenEnergyTracker:
    """
    A class to track and visualize green energy generation, usage, and CO2 savings.
    """
    
    def __init__(self):
        self.energy_data = {
            'timestamps': [],
            'generation': [],  # in kWh
            'usage': [],       # in kWh
            'co2_savings': []  # as percentage (0-100)
        }
        self.milestones = [25, 50, 75, 100]
        self.last_update = None
        
    def add_data_point(self, generation: float, usage: float, co2_savings: float) -> None:
        """
        Add a new data point to the tracker.
        
        Args:
            generation: Energy generated in kWh
            usage: Energy used in kWh
            co2_savings: CO2 savings percentage (0-100)
        """
        if not (0 <= co2_savings <= 100):
            raise ValueError("CO2 savings must be between 0 and 100")
            
        timestamp = datetime.now()
        self.energy_data['timestamps'].append(timestamp)
        self.energy_data['generation'].append(generation)
        self.energy_data['usage'].append(usage)
        self.energy_data['co2_savings'].append(co2_savings)
        self.last_update = timestamp
        
    def get_milestone_progress(self) -> Dict[int, Tuple[float, datetime]]:
        """
        Calculate progress towards each CO2 savings milestone.
        
        Returns:
            Dictionary mapping milestones to (current_percentage, estimated_reach_date)
        """
        if len(self.energy_data['co2_savings']) < 2:
            return {}
            
        # Calculate linear regression for trend
        x = mdates.date2num(self.energy_data['timestamps'])
        y = np.array(self.energy_data['co2_savings'])
        coeffs = np.polyfit(x, y, 1)
        
        progress = {}
        current_co2 = self.energy_data['co2_savings'][-1]
        
        for milestone in self.milestones:
            if current_co2 >= milestone:
                progress[milestone] = (100, self.energy_data['timestamps'][-1])
                continue
                
            # Estimate when milestone will be reached
            days_to_milestone = (milestone - coeffs[1]) / coeffs[0] - x[-1]
            if days_to_milestone > 0:
                reach_date = self.energy_data['timestamps'][-1] + timedelta(days=days_to_milestone)
                progress[milestone] = (current_co2 / milestone * 100, reach_date)
            else:
                progress[milestone] = (current_co2 / milestone * 100, None)
                
        return progress
        
    def visualize_data(self, save_path: Optional[str] = None) -> None:
        """
        Generate visualization plots for the energy data.
        
        Args:
            save_path: Optional path to save the visualization
        """
        if not self.energy_data['timestamps']:
            raise ValueError("No data available for visualization")
            
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))
        fig.suptitle('Green Energy Tracking Dashboard')
        
        # Generation and Usage Plot
        ax1.plot(self.energy_data['timestamps'], self.energy_data['generation'], 
                label='Generation (kWh)', color='green')
        ax1.plot(self.energy_data['timestamps'], self.energy_data['usage'], 
                label='Usage (kWh)', color='blue')
        ax1.set_title('Energy Generation vs Usage')
        ax1.set_ylabel('kWh')
        ax1.legend()
        ax1.grid(True)
        
        # CO2 Savings Plot
        ax2.plot(self.energy_data['timestamps'], self.energy_data['co2_savings'], 
                color='orange')
        ax2.set_title('CO2 Savings Percentage')
        ax2.set_ylabel('%')
        ax2.set_ylim(0, 100)
        
        # Add milestone lines
        for milestone in self.milestones:
            ax2.axhline(y=milestone, color='gray', linestyle='--', alpha=0.5)
            ax2.text(self.energy_data['timestamps'][0], milestone + 2, 
                    f'{milestone}%', color='gray')
        ax2.grid(True)
        
        # Milestone Progress
        progress = self.get_milestone_progress()
        if progress:
            milestones = list(progress.keys())
            percentages = [progress[m][0] for m in milestones]
            ax3.bar([str(m) for m in milestones], percentages, color='teal')
            ax3.set_title('Milestone Progress')
            ax3.set_ylabel('% of milestone reached')
            ax3.set_ylim(0, 100)
            ax3.grid(True)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
            
    def save_data(self, file_path: str) -> None:
        """
        Save energy data to a JSON file.
        
        Args:
            file_path: Path to save the data
        """
        serializable_data = {
            'timestamps': [ts.isoformat() for ts in self.energy_data['timestamps']],
            'generation': self.energy_data['generation'],
            'usage': self.energy_data['usage'],
            'co2_savings': self.energy_data['co2_savings']
        }
        
        with open(file_path, 'w') as f:
            json.dump(serializable_data, f, indent=2)
            
    def load_data(self, file_path: str) -> None:
        """
        Load energy data from a JSON file.
        
        Args:
            file_path: Path to load the data from
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        self.energy_data = {
            'timestamps': [datetime.fromisoformat(ts) for ts in data['timestamps']],
            'generation': data['generation'],
            'usage': data['usage'],
            'co2_savings': data['co2_savings']
        }
        
        if self.energy_data['timestamps']:
            self.last_update = self.energy_data['timestamps'][-1]

# Example usage
if __name__ == "__main__":
    tracker = GreenEnergyTracker()
    
    # Simulate some data
    now = datetime.now()
    for i in range(30):
        timestamp = now - timedelta(days=29-i)
        generation = np.random.uniform(5, 15)
        usage = np.random.uniform(3, 10)
        co2_savings = min(100, 5 + i * 3 + np.random.uniform(-2, 2))
        
        # Create a temporary data point to add
        temp_data = {
            'timestamps': timestamp,
            'generation': generation,
            'usage': usage,
            'co2_savings': co2_savings
        }
        
        # Add data point (in real usage, you would call add_data_point directly)
        tracker.energy_data['timestamps'].append(temp_data['timestamps'])
        tracker.energy_data['generation'].append(temp_data['generation'])
        tracker.energy_data['usage'].append(temp_data['usage'])
        tracker.energy_data['co2_savings'].append(temp_data['co2_savings'])
    
    # Visualize and save
    tracker.visualize_data()
    tracker.save_data('energy_data.json')
    
    # Print milestone progress
    print("Milestone Progress:")
    for milestone, (progress, date) in tracker.get_milestone_progress().items():
        date_str = date.strftime('%Y-%m-%d') if date else "Not estimated"
        print(f"{milestone}%: {progress:.1f}% - Estimated: {date_str}")
```
