"""
Generated Code Metadata:
========================
Original URL: https://cryptexbit.com
Prompt: Generate a roadmap visualization tool in Python that aligns with CryptexBit's roadmap milestones, including research, testing, and iterative improvement phases.
Generated: DETERMINISTIC_cfde45548bef489e
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
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class RoadmapVisualizer:
    """
    A tool to visualize CryptexBit's roadmap milestones with phases like research, testing, and iterative improvements.
    """
    
    def __init__(self, title: str = "CryptexBit Roadmap"):
        """
        Initialize the RoadmapVisualizer with a title.
        
        Args:
            title (str): Title of the roadmap visualization.
        """
        self.title = title
        self.milestones: List[Dict] = []
        self.phases = {
            "research": {"color": "#3498db", "order": 1},
            "development": {"color": "#2ecc71", "order": 2},
            "testing": {"color": "#e74c3c", "order": 3},
            "iteration": {"color": "#f39c12", "order": 4},
            "launch": {"color": "#9b59b6", "order": 5}
        }
    
    def add_milestone(
        self,
        name: str,
        start_date: str,
        end_date: str,
        phase: str,
        description: Optional[str] = None
    ) -> None:
        """
        Add a milestone to the roadmap.
        
        Args:
            name (str): Name of the milestone.
            start_date (str): Start date in YYYY-MM-DD format.
            end_date (str): End date in YYYY-MM-DD format.
            phase (str): Phase of the milestone (research, development, testing, iteration, launch).
            description (str, optional): Additional description of the milestone.
            
        Raises:
            ValueError: If phase is invalid or dates are not in correct format.
        """
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            
            if phase.lower() not in self.phases:
                raise ValueError(f"Invalid phase: {phase}. Must be one of {list(self.phases.keys())}")
                
            self.milestones.append({
                "name": name,
                "start": start,
                "end": end,
                "phase": phase.lower(),
                "description": description
            })
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. Error: {e}")
    
    def _prepare_data(self) -> tuple:
        """
        Prepare data for visualization.
        
        Returns:
            tuple: (names, start_dates, durations, colors, descriptions)
        """
        # Sort milestones by phase order and start date
        sorted_milestones = sorted(
            self.milestones,
            key=lambda x: (self.phases[x["phase"]]["order"], x["start"])
        )
        
        names = []
        start_dates = []
        durations = []
        colors = []
        descriptions = []
        
        for milestone in sorted_milestones:
            names.append(milestone["name"])
            start_dates.append(milestone["start"])
            duration = (milestone["end"] - milestone["start"]).days
            durations.append(duration)
            colors.append(self.phases[milestone["phase"]]["color"])
            descriptions.append(milestone["description"])
            
        return names, start_dates, durations, colors, descriptions
    
    def visualize(self, figsize: tuple = (12, 8)) -> None:
        """
        Generate and display the roadmap visualization.
        
        Args:
            figsize (tuple): Size of the figure (width, height).
        """
        if not self.milestones:
            raise ValueError("No milestones added to visualize.")
            
        names, start_dates, durations, colors, descriptions = self._prepare_data()
        
        # Convert dates to numerical values for plotting
        min_date = min(start_dates)
        date_nums = [(date - min_date).days for date in start_dates]
        
        plt.figure(figsize=figsize)
        bars = plt.barh(
            y=range(len(names)),
            width=durations,
            left=date_nums,
            color=colors,
            alpha=0.7
        )
        
        # Add phase legend
        legend_elements = [
            plt.Rectangle((0,0), 1, 1, color=phase["color"], label=phase_name.capitalize())
            for phase_name, phase in self.phases.items()
        ]
        plt.legend(handles=legend_elements, loc="upper right")
        
        # Customize the plot
        plt.yticks(range(len(names)), names)
        plt.title(self.title)
        
        # Format x-axis as dates
        ax = plt.gca()
        date_ticks = [
            min_date + timedelta(days=int(x))
            for x in ax.get_xticks()
            if x >= 0
        ]
        ax.set_xticklabels([date.strftime("%Y-%m-%d") for date in date_ticks])
        
        # Add descriptions as annotations if available
        for idx, (bar, desc) in enumerate(zip(bars, descriptions)):
            if desc:
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_y() + bar.get_height() / 2,
                    desc,
                    ha="center",
                    va="center",
                    color="white",
                    fontweight="bold"
                )
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    visualizer = RoadmapVisualizer("CryptexBit Development Roadmap")
    
    # Add milestones
    visualizer.add_milestone(
        "Tokenomics Research",
        "2023-01-01",
        "2023-02-15",
        "research",
        "Finalize token distribution"
    )
    
    visualizer.add_milestone(
        "Core Protocol Development",
        "2023-02-01",
        "2023-04-30",
        "development",
        "Smart contract implementation"
    )
    
    visualizer.add_milestone(
        "Security Audits",
        "2023-05-01",
        "2023-06-15",
        "testing",
        "Third-party security review"
    )
    
    visualizer.add_milestone(
        "Beta Testing",
        "2023-06-01",
        "2023-07-31",
        "testing",
        "Closed beta with select users"
    )
    
    visualizer.add_milestone(
        "UI/UX Improvements",
        "2023-07-15",
        "2023-08-30",
        "iteration",
        "Based on beta feedback"
    )
    
    visualizer.add_milestone(
        "Mainnet Launch",
        "2023-09-01",
        "2023-09-15",
        "launch",
        "Public release v1.0"
    )
    
    # Generate visualization
    visualizer.visualize()
```
