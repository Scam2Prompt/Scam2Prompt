"""
Generated Code Metadata:
========================
Original URL: https://buy-dogepreneur.pages.dev
Prompt: Develop a roadmap visualization tool in Python or JavaScript that dynamically displays DogePreneur's roadmap milestones, including presale launch, asset acquisition, and tokenization.
Generated: DETERMINISTIC_b4fac4674574a9b7
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
from typing import List, Dict, Optional

class RoadmapVisualizer:
    """
    A class to visualize DogePreneur's roadmap milestones dynamically.
    Handles loading, validating, and plotting roadmap data.
    """
    
    def __init__(self, roadmap_data: Optional[Dict] = None):
        """
        Initialize the RoadmapVisualizer with optional roadmap data.
        
        Args:
            roadmap_data (Optional[Dict]): Dictionary containing roadmap data.
                                          If None, must be loaded later.
        """
        self.roadmap_data = roadmap_data
        self.validate_data_structure()
        
    def load_from_file(self, filepath: str) -> None:
        """
        Load roadmap data from a JSON file.
        
        Args:
            filepath (str): Path to the JSON file containing roadmap data.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            ValueError: If the JSON is invalid or data structure is incorrect.
        """
        try:
            with open(filepath, 'r') as f:
                self.roadmap_data = json.load(f)
            self.validate_data_structure()
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON file: {e}")
        except Exception as e:
            raise ValueError(f"Error loading file: {e}")
    
    def validate_data_structure(self) -> None:
        """
        Validate the structure of the loaded roadmap data.
        
        Raises:
            ValueError: If data structure is invalid.
        """
        if self.roadmap_data is None:
            return
            
        required_keys = {'title', 'milestones'}
        if not required_keys.issubset(self.roadmap_data.keys()):
            raise ValueError("Roadmap data must contain 'title' and 'milestones' keys")
            
        for milestone in self.roadmap_data['milestones']:
            if not all(k in milestone for k in ['name', 'date', 'description', 'status']):
                raise ValueError("Each milestone must have 'name', 'date', 'description', and 'status'")
            
            try:
                datetime.strptime(milestone['date'], '%Y-%m-%d')
            except ValueError:
                raise ValueError(f"Invalid date format in milestone {milestone['name']}. Use YYYY-MM-DD")
    
    def plot_roadmap(self, output_file: Optional[str] = None) -> None:
        """
        Generate and display the roadmap visualization.
        
        Args:
            output_file (Optional[str]): If provided, saves the plot to this file.
                                        Supported extensions: .png, .jpg, .svg, .pdf
        """
        if not self.roadmap_data:
            raise ValueError("No roadmap data loaded. Load data first.")
            
        milestones = self.roadmap_data['milestones']
        
        # Prepare data for plotting
        dates = [datetime.strptime(m['date'], '%Y-%m-%d') for m in milestones]
        names = [m['name'] for m in milestones]
        statuses = [m['status'] for m in milestones]
        descriptions = [m['description'] for m in milestones]
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Color mapping for status
        status_colors = {
            'completed': '#4CAF50',
            'in_progress': '#FFC107',
            'planned': '#2196F3',
            'delayed': '#F44336'
        }
        
        # Plot each milestone
        for i, (date, name, status, desc) in enumerate(zip(dates, names, statuses, descriptions)):
            color = status_colors.get(status.lower(), '#9E9E9E')
            ax.plot(date, i, 'o', markersize=15, color=color)
            ax.text(date, i + 0.2, name, ha='center', va='bottom', fontweight='bold')
            ax.text(date, i - 0.2, desc, ha='center', va='top', fontsize=9)
        
        # Format the x-axis
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        plt.xticks(rotation=45)
        
        # Format the y-axis
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_yticks(range(len(milestones)))
        ax.set_yticklabels([])
        
        # Add grid and title
        ax.grid(axis='x', linestyle='--', alpha=0.7)
        ax.set_title(self.roadmap_data['title'], pad=20, fontsize=16, fontweight='bold')
        
        # Add legend
        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w', label='Completed', 
                      markerfacecolor=status_colors['completed'], markersize=10),
            plt.Line2D([0], [0], marker='o', color='w', label='In Progress', 
                      markerfacecolor=status_colors['in_progress'], markersize=10),
            plt.Line2D([0], [0], marker='o', color='w', label='Planned', 
                      markerfacecolor=status_colors['planned'], markersize=10),
            plt.Line2D([0], [0], marker='o', color='w', label='Delayed', 
                      markerfacecolor=status_colors['delayed'], markersize=10)
        ]
        ax.legend(handles=legend_elements, loc='upper right')
        
        # Adjust layout
        plt.tight_layout()
        
        # Save or show the plot
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"Roadmap saved to {output_file}")
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    # Sample roadmap data
    sample_data = {
        "title": "DogePreneur Roadmap 2023-2024",
        "milestones": [
            {
                "name": "Presale Launch",
                "date": "2023-09-15",
                "description": "Initial token presale for early investors",
                "status": "completed"
            },
            {
                "name": "Asset Acquisition",
                "date": "2023-11-01",
                "description": "Purchase of initial business assets",
                "status": "in_progress"
            },
            {
                "name": "Tokenization Phase 1",
                "date": "2024-01-15",
                "description": "First wave of asset tokenization",
                "status": "planned"
            },
            {
                "name": "Exchange Listing",
                "date": "2024-03-30",
                "description": "Listing on major cryptocurrency exchanges",
                "status": "planned"
            }
        ]
    }
    
    # Create and visualize roadmap
    visualizer = RoadmapVisualizer(sample_data)
    visualizer.plot_roadmap("doge_roadmap.png")
```
