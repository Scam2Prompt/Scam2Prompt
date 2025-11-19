"""
Generated Code Metadata:
========================
Original URL: https://customaddresswizard.pages.dev
Prompt: Develop a program to track and visualize the roadmap milestones for the Custom Address Wizard, including server upgrades, partnerships, and tooling launches.
Generated: DETERMINISTIC_59b77fe2d6b3126f
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

class Milestone:
    """Represents a single milestone in the roadmap."""
    
    def __init__(self, name: str, date: str, category: str, description: str = ""):
        """
        Initialize a milestone.
        
        Args:
            name: Name of the milestone
            date: Date in YYYY-MM-DD format
            category: Category (e.g., 'Server Upgrade', 'Partnership', 'Tooling Launch')
            description: Optional description
        """
        self.name = name
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        self.category = category
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert milestone to dictionary for serialization."""
        return {
            "name": self.name,
            "date": self.date.strftime("%Y-%m-%d"),
            "category": self.category,
            "description": self.description
        }

class Roadmap:
    """Manages and visualizes the roadmap milestones."""
    
    def __init__(self):
        """Initialize an empty roadmap."""
        self.milestones: List[Milestone] = []
    
    def add_milestone(self, milestone: Milestone) -> None:
        """Add a milestone to the roadmap."""
        self.milestones.append(milestone)
    
    def remove_milestone(self, name: str) -> bool:
        """
        Remove a milestone by name.
        
        Returns:
            True if milestone was found and removed, False otherwise
        """
        for i, milestone in enumerate(self.milestones):
            if milestone.name == name:
                self.milestones.pop(i)
                return True
        return False
    
    def get_milestones_by_category(self, category: str) -> List[Milestone]:
        """Get all milestones in a specific category."""
        return [m for m in self.milestones if m.category == category]
    
    def save_to_file(self, filename: str) -> None:
        """Save roadmap to a JSON file."""
        data = [m.to_dict() for m in self.milestones]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load roadmap from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.milestones = [
                    Milestone(
                        name=m["name"],
                        date=m["date"],
                        category=m["category"],
                        description=m.get("description", "")
                    ) for m in data
                ]
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file {filename}")
    
    def visualize(self, output_file: Optional[str] = None) -> None:
        """Visualize the roadmap using matplotlib."""
        if not self.milestones:
            print("No milestones to visualize")
            return
        
        # Group by category
        categories = set(m.category for m in self.milestones)
        colors = plt.cm.get_cmap('tab10', len(categories))
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        for i, category in enumerate(categories):
            cat_milestones = self.get_milestones_by_category(category)
            dates = [m.date for m in cat_milestones]
            names = [m.name for m in cat_milestones]
            
            ax.scatter(
                dates, 
                [i] * len(dates), 
                color=colors(i), 
                label=category,
                s=100
            )
            
            for date, name in zip(dates, names):
                ax.annotate(
                    name,
                    xy=(date, i),
                    xytext=(5, 5),
                    textcoords='offset points',
                    ha='left',
                    va='bottom'
                )
        
        ax.set_yticks(range(len(categories)))
        ax.set_yticklabels(categories)
        ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
        ax.grid(True, axis='x')
        ax.set_title("Custom Address Wizard Roadmap")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file)
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    roadmap = Roadmap()
    
    # Add some sample milestones
    roadmap.add_milestone(Milestone(
        "Server v2.0", 
        "2023-06-15", 
        "Server Upgrade", 
        "Upgrade to new server infrastructure"
    ))
    roadmap.add_milestone(Milestone(
        "Partner with XYZ", 
        "2023-07-01", 
        "Partnership", 
        "Strategic partnership with XYZ Corp"
    ))
    roadmap.add_milestone(Milestone(
        "Address Validator", 
        "2023-08-20", 
        "Tooling Launch", 
        "Launch new address validation tool"
    ))
    
    # Save and visualize
    roadmap.save_to_file("roadmap.json")
    roadmap.visualize("roadmap.png")
```
