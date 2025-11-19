"""
Generated Code Metadata:
========================
Original URL: https://doglibretoken.web.app
Prompt: Create a simple roadmap or timeline for a Web3 project's development, including milestones like token launch, strategic partnerships, NFT releases, and metaverse game development, mirroring DogLibre's plans.
Generated: DETERMINISTIC_b7088541592b6b9a
Batch ID: 20250622_204931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Web3 Project Roadmap Generator
Creates a timeline for a Web3 project with key milestones.
"""

from datetime import datetime, timedelta
from typing import List, Dict
import json

class Web3Roadmap:
    """
    Generates and manages a Web3 project roadmap with milestones.
    """
    
    def __init__(self, project_name: str, start_date: str):
        """
        Initialize the roadmap with project name and start date.
        
        Args:
            project_name: Name of the Web3 project
            start_date: Project start date in YYYY-MM-DD format
        """
        self.project_name = project_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.milestones: List[Dict] = []
        
    def add_milestone(self, name: str, description: str, duration_days: int, dependencies: List[str] = None):
        """
        Add a milestone to the roadmap.
        
        Args:
            name: Milestone name
            description: Description of the milestone
            duration_days: Estimated duration in days
            dependencies: List of milestone names this depends on
        """
        if dependencies is None:
            dependencies = []
            
        self.milestones.append({
            "name": name,
            "description": description,
            "duration_days": duration_days,
            "dependencies": dependencies
        })
        
    def calculate_timeline(self) -> List[Dict]:
        """
        Calculate the timeline with start and end dates for each milestone.
        
        Returns:
            List of milestones with calculated dates
        """
        timeline = []
        processed_milestones = set()
        
        # Process milestones in dependency order
        while len(processed_milestones) < len(self.milestones):
            for milestone in self.milestones:
                if milestone["name"] in processed_milestones:
                    continue
                    
                # Check if all dependencies are processed
                all_deps_processed = all(
                    dep in processed_milestones for dep in milestone["dependencies"]
                )
                
                if not all_deps_processed and milestone["dependencies"]:
                    continue
                    
                # Calculate start date (max of dependency end dates or project start)
                start_date = self.start_date
                if milestone["dependencies"]:
                    dep_dates = [
                        m["end_date"] for m in timeline 
                        if m["name"] in milestone["dependencies"]
                    ]
                    if dep_dates:
                        start_date = max(dep_dates)
                
                end_date = start_date + timedelta(days=milestone["duration_days"])
                
                timeline.append({
                    "name": milestone["name"],
                    "description": milestone["description"],
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": end_date.strftime("%Y-%m-%d"),
                    "duration_days": milestone["duration_days"],
                    "dependencies": milestone["dependencies"]
                })
                processed_milestones.add(milestone["name"])
                
        return timeline
    
    def generate_roadmap(self, output_format: str = "json") -> str:
        """
        Generate the roadmap in specified format.
        
        Args:
            output_format: Output format ('json' or 'text')
            
        Returns:
            Formatted roadmap
            
        Raises:
            ValueError: If output format is invalid
        """
        timeline = self.calculate_timeline()
        
        if output_format == "json":
            return json.dumps({
                "project": self.project_name,
                "start_date": self.start_date.strftime("%Y-%m-%d"),
                "milestones": timeline
            }, indent=2)
        elif output_format == "text":
            text = f"Project: {self.project_name}\nStart Date: {self.start_date.strftime('%Y-%m-%d')}\n\n"
            text += "Milestones:\n"
            for milestone in timeline:
                text += (
                    f"- {milestone['name']}\n"
                    f"  Description: {milestone['description']}\n"
                    f"  Start: {milestone['start_date']}\n"
                    f"  End: {milestone['end_date']}\n"
                    f"  Duration: {milestone['duration_days']} days\n"
                )
                if milestone['dependencies']:
                    text += f"  Depends on: {', '.join(milestone['dependencies'])}\n"
                text += "\n"
            return text
        else:
            raise ValueError("Invalid output format. Choose 'json' or 'text'.")

# Example usage for a Web3 project similar to DogLibre
if __name__ == "__main__":
    try:
        roadmap = Web3Roadmap("DogLibre 2.0", "2023-01-01")
        
        # Add milestones
        roadmap.add_milestone(
            "Token Launch",
            "Initial token offering and distribution",
            30
        )
        
        roadmap.add_milestone(
            "Strategic Partnerships",
            "Form partnerships with key Web3 projects",
            60,
            ["Token Launch"]
        )
        
        roadmap.add_milestone(
            "NFT Collection V1",
            "Release first NFT collection",
            45,
            ["Token Launch"]
        )
        
        roadmap.add_milestone(
            "Metaverse Alpha",
            "First playable version of metaverse game",
            90,
            ["Strategic Partnerships"]
        )
        
        roadmap.add_milestone(
            "NFT Collection V2",
            "Second NFT collection with game integration",
            60,
            ["Metaverse Alpha"]
        )
        
        roadmap.add_milestone(
            "Metaverse Beta",
            "Public beta release with full features",
            120,
            ["NFT Collection V2"]
        )
        
        # Generate and print roadmap
        print(roadmap.generate_roadmap("text"))
        
    except Exception as e:
        print(f"Error generating roadmap: {str(e)}")
```
