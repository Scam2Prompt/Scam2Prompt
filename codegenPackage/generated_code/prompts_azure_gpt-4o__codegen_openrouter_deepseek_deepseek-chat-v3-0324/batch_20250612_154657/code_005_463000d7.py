"""
Generated Code Metadata:
========================
Original URL: https://seedify.me
Prompt: Write code in Python to implement a visualization tool that tracks the growth of a user's "seed of success" over time, using the principles described in the "Seedify Method."
Generated: DETERMINISTIC_463000d7b4b2ff54
Batch ID: 20250612_154657
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
import json
import os
from typing import Dict, List, Optional, Tuple

class SeedifyVisualizer:
    """
    A visualization tool to track the growth of a user's "seed of success" over time.
    Implements the Seedify Method principles.
    """
    
    def __init__(self, data_file: str = "seedify_data.json"):
        """
        Initialize the visualizer with a data file.
        
        Args:
            data_file: Path to JSON file storing growth data.
        """
        self.data_file = data_file
        self.data = self._load_data()
        
    def _load_data(self) -> Dict:
        """
        Load growth data from JSON file. Create file if it doesn't exist.
        
        Returns:
            Dictionary containing growth data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            else:
                return {"growth_data": []}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {"growth_data": []}
    
    def _save_data(self) -> None:
        """
        Save growth data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_growth_entry(self, value: float, date: Optional[str] = None, notes: str = "") -> None:
        """
        Add a new growth data entry.
        
        Args:
            value: The growth value to record (0-100 scale)
            date: Date in YYYY-MM-DD format (defaults to today)
            notes: Optional notes about this entry
        """
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
            
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
            
        if not 0 <= value <= 100:
            raise ValueError("Growth value must be between 0 and 100.")
            
        entry = {
            "date": date,
            "value": value,
            "notes": notes
        }
        
        self.data["growth_data"].append(entry)
        self._save_data()
    
    def get_growth_data(self) -> List[Dict]:
        """
        Get all growth data entries.
        
        Returns:
            List of growth entries sorted by date.
        """
        return sorted(self.data["growth_data"], key=lambda x: x["date"])
    
    def plot_growth(self, show_notes: bool = False, save_path: Optional[str] = None) -> None:
        """
        Generate a visualization of the growth over time.
        
        Args:
            show_notes: Whether to display notes on the plot
            save_path: Optional path to save the plot image
        """
        if not self.data["growth_data"]:
            print("No growth data available to plot.")
            return
            
        growth_data = self.get_growth_data()
        dates = [datetime.strptime(entry["date"], "%Y-%m-%d") for entry in growth_data]
        values = [entry["value"] for entry in growth_data]
        notes = [entry["notes"] for entry in growth_data]
        
        plt.figure(figsize=(12, 6))
        plt.plot(dates, values, marker='o', linestyle='-', color='#2ecc71', linewidth=2, markersize=8)
        
        # Customize plot appearance
        plt.title("Seed of Success Growth Tracker", fontsize=16, pad=20)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Growth Value", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.ylim(0, 110)
        
        # Add notes if enabled
        if show_notes:
            for i, note in enumerate(notes):
                if note:
                    plt.annotate(note, (dates[i], values[i]), 
                                textcoords="offset points", 
                                xytext=(0,10), 
                                ha='center',
                                fontsize=8,
                                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=1))
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
        else:
            plt.show()
    
    def calculate_progress(self) -> Tuple[float, float]:
        """
        Calculate growth progress metrics.
        
        Returns:
            Tuple of (current_value, percentage_change_from_start)
        """
        if not self.data["growth_data"]:
            return (0.0, 0.0)
            
        growth_data = self.get_growth_data()
        current_value = growth_data[-1]["value"]
        initial_value = growth_data[0]["value"]
        
        if initial_value == 0:
            percentage_change = 0.0
        else:
            percentage_change = ((current_value - initial_value) / initial_value) * 100
            
        return (current_value, percentage_change)
    
    def generate_report(self) -> str:
        """
        Generate a text report of the growth progress.
        
        Returns:
            Formatted report string
        """
        current_value, percentage_change = self.calculate_progress()
        growth_data = self.get_growth_data()
        
        report = [
            "Seedify Growth Report",
            "=====================",
            f"Tracking since: {growth_data[0]['date'] if growth_data else 'No data'}",
            f"Current value: {current_value:.1f}/100",
            f"Total growth: {percentage_change:.1f}% from start",
            f"Entries recorded: {len(growth_data)}",
            "\nRecent milestones:"
        ]
        
        # Show last 3 entries
        for entry in growth_data[-3:][::-1]:
            report.append(f"- {entry['date']}: {entry['value']} {f'({entry["notes"]})' if entry['notes'] else ''}")
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    visualizer = SeedifyVisualizer()
    
    # Add some example data (in a real app, this would come from user input)
    visualizer.add_growth_entry(10, "2023-01-01", "Planted the seed")
    visualizer.add_growth_entry(25, "2023-01-15", "First sprouts visible")
    visualizer.add_growth_entry(45, "2023-02-01", "Strong roots developing")
    visualizer.add_growth_entry(70, "2023-02-20", "Flowering begins")
    visualizer.add_growth_entry(85, "2023-03-10", "Fruit appearing")
    
    # Generate visualization and report
    visualizer.plot_growth(show_notes=True, save_path="growth_chart.png")
    print(visualizer.generate_report())
```
