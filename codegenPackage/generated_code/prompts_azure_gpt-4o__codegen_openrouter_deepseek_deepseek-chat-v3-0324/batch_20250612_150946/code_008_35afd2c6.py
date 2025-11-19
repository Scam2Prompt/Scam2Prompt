"""
Generated Code Metadata:
========================
Original URL: https://bitbama-14n.pages.dev
Prompt: Create a roadmap visualization tool for a cryptocurrency project, inspired by the roadmap section on Bitbama.
Generated: DETERMINISTIC_35afd2c6f017f858
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from typing import List, Dict, Optional

class RoadmapItem:
    """Represents a single item in the cryptocurrency project roadmap."""
    
    def __init__(self, title: str, description: str, date: str, status: str):
        """
        Initialize a roadmap item.
        
        Args:
            title: Title of the roadmap item
            description: Detailed description
            date: Target date in YYYY-MM-DD format
            status: Current status (planned, in-progress, completed)
        """
        self.title = title
        self.description = description
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.status = status.lower()
        
        if self.status not in ["planned", "in-progress", "completed"]:
            raise ValueError("Status must be one of: planned, in-progress, completed")

class RoadmapVisualizer:
    """Visualizes a cryptocurrency project roadmap."""
    
    def __init__(self, roadmap_items: List[RoadmapItem]):
        """
        Initialize the visualizer with roadmap items.
        
        Args:
            roadmap_items: List of RoadmapItem objects
        """
        self.roadmap_items = sorted(roadmap_items, key=lambda x: x.date)
        self.status_colors = {
            "planned": "#FFA500",  # Orange
            "in-progress": "#1E90FF",  # DodgerBlue
            "completed": "#32CD32"  # LimeGreen
        }
    
    @classmethod
    def from_json(cls, file_path: str):
        """
        Create RoadmapVisualizer from JSON file.
        
        Args:
            file_path: Path to JSON file containing roadmap data
            
        Returns:
            RoadmapVisualizer instance
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        items = []
        for item in data["roadmap"]:
            items.append(RoadmapItem(
                title=item["title"],
                description=item["description"],
                date=item["date"],
                status=item["status"]
            ))
        
        return cls(items)
    
    def visualize(self, output_file: Optional[str] = None):
        """
        Generate and display/save the roadmap visualization.
        
        Args:
            output_file: If provided, saves the visualization to this file
        """
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Set background color
        fig.patch.set_facecolor('#f5f5f5')
        ax.set_facecolor('#f5f5f5')
        
        # Plot each roadmap item
        for i, item in enumerate(self.roadmap_items):
            color = self.status_colors[item.status]
            ax.plot(
                [item.date, item.date],
                [i, i],
                marker='o',
                markersize=10,
                color=color,
                linewidth=3
            )
            
            # Add text annotation
            status_text = f"({item.status.replace('-', ' ')})"
            ax.text(
                item.date,
                i,
                f"{item.title}\n{status_text}",
                ha='left' if i % 2 == 0 else 'right',
                va='center',
                fontsize=10,
                bbox=dict(
                    facecolor='white',
                    alpha=0.8,
                    edgecolor=color,
                    boxstyle='round,pad=0.5'
                )
            )
        
        # Format the x-axis
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        plt.xticks(rotation=45)
        
        # Format the y-axis
        ax.set_yticks(range(len(self.roadmap_items)))
        ax.set_yticklabels([item.date.strftime('%Y-%m-%d') for item in self.roadmap_items])
        ax.invert_yaxis()
        
        # Remove spines and grid
        for spine in ['top', 'right', 'left']:
            ax.spines[spine].set_visible(False)
        
        ax.grid(axis='x', linestyle='--', alpha=0.7)
        
        # Add title and adjust layout
        plt.title("Cryptocurrency Project Roadmap", pad=20, fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"Roadmap saved to {output_file}")
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    # Example roadmap data (could also load from JSON)
    roadmap_data = {
        "roadmap": [
            {
                "title": "Token Launch",
                "description": "Initial token offering and listing",
                "date": "2023-03-15",
                "status": "completed"
            },
            {
                "title": "Exchange Listings",
                "description": "List on major exchanges",
                "date": "2023-06-30",
                "status": "in-progress"
            },
            {
                "title": "Mobile App Release",
                "description": "Launch iOS and Android apps",
                "date": "2023-09-15",
                "status": "planned"
            },
            {
                "title": "Mainnet Launch",
                "description": "Transition to our own blockchain",
                "date": "2023-12-31",
                "status": "planned"
            }
        ]
    }
    
    # Save example data to JSON file
    with open("roadmap_example.json", "w") as f:
        json.dump(roadmap_data, f, indent=2)
    
    # Create and visualize roadmap
    try:
        visualizer = RoadmapVisualizer.from_json("roadmap_example.json")
        visualizer.visualize(output_file="roadmap_visualization.png")
    except Exception as e:
        print(f"Error generating roadmap: {e}")
```
