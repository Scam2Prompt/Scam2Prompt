"""
Generated Code Metadata:
========================
Original URL: https://satoshidex-in.web.app
Prompt: Create a roadmap visualization tool in Python for tracking milestones like Bitcoin ETF launch, Bitcoin halving, and $SATX ecosystem growth as outlined in SatoshiDEX's roadmap.
Generated: DETERMINISTIC_69f823d3d2de6530
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from typing import List, Dict, Optional
import numpy as np

class RoadmapVisualizer:
    """
    A class to visualize project milestones on a timeline.
    """
    
    def __init__(self, title: str = "Project Roadmap"):
        """
        Initialize the RoadmapVisualizer with a title.
        
        Args:
            title (str): Title for the roadmap visualization.
        """
        self.title = title
        self.milestones: List[Dict] = []
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        
    def add_milestone(self, 
                     name: str, 
                     date: str, 
                     description: str = "", 
                     category: Optional[str] = None) -> None:
        """
        Add a milestone to the roadmap.
        
        Args:
            name (str): Name of the milestone
            date (str): Date in YYYY-MM-DD format
            description (str): Description of the milestone
            category (str, optional): Category for grouping milestones
        """
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
            self.milestones.append({
                "name": name,
                "date": parsed_date,
                "description": description,
                "category": category
            })
        except ValueError as e:
            raise ValueError(f"Invalid date format for milestone '{name}'. Use YYYY-MM-DD format.") from e
    
    def _prepare_data(self) -> None:
        """Prepare data for visualization by sorting milestones by date."""
        self.milestones.sort(key=lambda x: x["date"])
        
        # Extract data for plotting
        self.dates = [m["date"] for m in self.milestones]
        self.names = [m["name"] for m in self.milestones]
        self.descriptions = [m["description"] for m in self.milestones]
        self.categories = [m["category"] for m in self.milestones]
        
        # Get unique categories for color mapping
        unique_categories = list(set(filter(None, self.categories)))
        self.category_colors = plt.cm.tab20(np.linspace(0, 1, len(unique_categories)))
        self.category_map = {cat: color for cat, color in zip(unique_categories, self.category_colors)}
    
    def visualize(self, save_path: Optional[str] = None) -> None:
        """
        Generate and display the roadmap visualization.
        
        Args:
            save_path (str, optional): Path to save the visualization image. If None, shows plot.
        """
        if not self.milestones:
            raise ValueError("No milestones added to visualize.")
            
        self._prepare_data()
        
        # Configure plot
        self.ax.set_title(self.title, fontsize=16, pad=20)
        self.ax.set_xlabel("Timeline", fontsize=12)
        self.ax.set_ylabel("Milestones", fontsize=12)
        
        # Format x-axis as dates
        self.ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        self.fig.autofmt_xdate()
        
        # Plot each milestone
        y_pos = np.arange(len(self.milestones))
        for i, (date, name, desc, cat) in enumerate(zip(self.dates, self.names, self.descriptions, self.categories)):
            color = self.category_map.get(cat, 'gray') if cat else 'gray'
            self.ax.plot(date, y_pos[i], 'o', markersize=10, color=color)
            self.ax.text(date, y_pos[i] + 0.2, name, ha='center', va='bottom', fontsize=10)
            if desc:
                self.ax.text(date, y_pos[i] - 0.2, desc, ha='center', va='top', fontsize=8, alpha=0.7)
        
        # Add category legend if categories exist
        if self.category_map:
            handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10)
                      for color in self.category_map.values()]
            self.ax.legend(handles, self.category_map.keys(), title="Categories", loc='upper left', bbox_to_anchor=(1, 1))
        
        # Adjust layout
        self.ax.set_yticks(y_pos)
        self.ax.set_yticklabels([mdates.date2num(d) for d in self.dates])
        self.ax.set_yticklabels([])  # Hide y-axis labels as we're using text annotations
        self.ax.grid(True, axis='x', linestyle='--', alpha=0.6)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Roadmap saved to {save_path}")
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    # Create roadmap instance
    roadmap = RoadmapVisualizer(title="SatoshiDEX Roadmap")
    
    # Add milestones
    roadmap.add_milestone(
        name="Bitcoin ETF Launch",
        date="2024-01-10",
        description="Approval of first spot Bitcoin ETFs",
        category="Market Events"
    )
    
    roadmap.add_milestone(
        name="Bitcoin Halving",
        date="2024-04-20",
        description="4th Bitcoin halving event",
        category="Bitcoin"
    )
    
    roadmap.add_milestone(
        name="$SATX Phase 1",
        date="2024-03-01",
        description="Initial token launch and DEX integration",
        category="SATX Ecosystem"
    )
    
    roadmap.add_milestone(
        name="$SATX Phase 2",
        date="2024-06-01",
        description="Advanced trading features and partnerships",
        category="SATX Ecosystem"
    )
    
    roadmap.add_milestone(
        name="$SATX Phase 3",
        date="2024-09-01",
        description="Full ecosystem deployment and scaling",
        category="SATX Ecosystem"
    )
    
    # Generate visualization
    roadmap.visualize(save_path="satoshidex_roadmap.png")
```
