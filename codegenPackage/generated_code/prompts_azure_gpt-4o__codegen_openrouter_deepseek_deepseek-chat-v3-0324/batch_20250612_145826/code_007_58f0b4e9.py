"""
Generated Code Metadata:
========================
Original URL: https://popofrogg.pages.dev
Prompt: Develop a roadmap visualization tool for a cryptocurrency project, showcasing milestones like contract audits, presale launches, staking platform releases, and gaming platform launches as described in Popo's roadmap.
Generated: DETERMINISTIC_58f0b4e968bb5be8
Batch ID: 20250612_145826
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

class RoadmapVisualizer:
    """
    A tool to visualize cryptocurrency project roadmaps with milestones.
    """

    def __init__(self, title: str, width: int = 12, height: int = 6):
        """
        Initialize the RoadmapVisualizer.
        
        Args:
            title: Title of the roadmap
            width: Width of the figure in inches
            height: Height of the figure in inches
        """
        self.title = title
        self.width = width
        self.height = height
        self.milestones: List[Dict] = []
        
    def add_milestone(self, name: str, date: str, description: str, 
                     milestone_type: str = "general", color: Optional[str] = None):
        """
        Add a milestone to the roadmap.
        
        Args:
            name: Name of the milestone
            date: Date in format 'YYYY-MM-DD'
            description: Description of the milestone
            milestone_type: Type of milestone (e.g., 'audit', 'launch', 'release')
            color: Optional color for the milestone marker
        """
        try:
            parsed_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format for milestone '{name}'. Use 'YYYY-MM-DD'.") from e
            
        if not color:
            color = self._get_default_color(milestone_type)
            
        self.milestones.append({
            'name': name,
            'date': parsed_date,
            'description': description,
            'type': milestone_type,
            'color': color
        })
        
    def _get_default_color(self, milestone_type: str) -> str:
        """
        Get default color based on milestone type.
        
        Args:
            milestone_type: Type of milestone
            
        Returns:
            str: Color code
        """
        colors = {
            'audit': '#FF6B6B',     # Red
            'presale': '#4ECDC4',   # Teal
            'staking': '#45B7D1',   # Blue
            'gaming': '#A37EBD',    # Purple
            'general': '#98D8C8'    # Green
        }
        return colors.get(milestone_type.lower(), '#98D8C8')
    
    def visualize(self, save_path: Optional[str] = None):
        """
        Generate and display the roadmap visualization.
        
        Args:
            save_path: Optional path to save the image (e.g., 'roadmap.png')
        """
        if not self.milestones:
            raise ValueError("No milestones added to visualize.")
            
        # Sort milestones by date
        sorted_milestones = sorted(self.milestones, key=lambda x: x['date'])
        dates = [m['date'] for m in sorted_milestones]
        names = [m['name'] for m in sorted_milestones]
        colors = [m['color'] for m in sorted_milestones]
        descriptions = [m['description'] for m in sorted_milestones]
        
        # Create figure
        fig, ax = plt.subplots(figsize=(self.width, self.height))
        
        # Plot milestones
        for i, (date, name, color, desc) in enumerate(zip(dates, names, colors, descriptions)):
            ax.plot(date, i, 'o', markersize=15, color=color)
            ax.text(date, i + 0.3, name, ha='center', va='bottom', fontweight='bold')
            ax.text(date, i - 0.3, desc, ha='center', va='top', fontsize=9)
        
        # Formatting
        ax.set_yticks([])
        ax.set_title(self.title, pad=20, fontsize=16, fontweight='bold')
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.grid(True, axis='x', linestyle='--', alpha=0.7)
        ax.margins(y=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save or show
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Roadmap saved to {save_path}")
        else:
            plt.show()
            
        plt.close()

# Example usage
if __name__ == "__main__":
    # Create roadmap
    roadmap = RoadmapVisualizer("Popo Cryptocurrency Project Roadmap")
    
    # Add milestones (example data)
    roadmap.add_milestone(
        "Smart Contract Audit", 
        "2023-06-15", 
        "Security audit completed by CertiK",
        "audit"
    )
    roadmap.add_milestone(
        "Presale Launch", 
        "2023-07-01", 
        "Public presale begins",
        "presale"
    )
    roadmap.add_milestone(
        "Staking Platform", 
        "2023-08-15", 
        "Staking platform v1 release",
        "staking"
    )
    roadmap.add_milestone(
        "Gaming Platform Alpha", 
        "2023-10-01", 
        "First playable alpha version",
        "gaming"
    )
    roadmap.add_milestone(
        "Mainnet Launch", 
        "2023-12-15", 
        "Full mainnet deployment",
        "general"
    )
    
    # Visualize
    roadmap.visualize(save_path="popo_roadmap.png")
```
