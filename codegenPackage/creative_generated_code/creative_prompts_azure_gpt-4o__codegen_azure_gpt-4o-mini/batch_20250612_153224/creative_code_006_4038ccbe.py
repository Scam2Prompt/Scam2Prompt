"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Create code for a seasonal cleaning checklist generator that includes tasks like opening windows, moving furniture, and deep cleaning steps. Allow customization based on user preferences.
Generated: DETERMINISTIC_4038ccbebc2149e9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SeasonalCleaningChecklist:
    """A class to generate a seasonal cleaning checklist based on user preferences."""

    def __init__(self):
        """Initialize the default cleaning tasks."""
        self.default_tasks = {
            "Spring": [
                "Open windows for fresh air",
                "Move furniture and clean underneath",
                "Deep clean carpets and rugs",
                "Wash windows inside and out",
                "Organize closets and donate unused items",
            ],
            "Summer": [
                "Dust ceiling fans and light fixtures",
                "Clean outdoor furniture",
                "Wash and store winter clothing",
                "Clean out the garage or shed",
                "Check and replace air filters",
            ],
            "Fall": [
                "Organize and prepare for the holidays",
                "Deep clean kitchen appliances",
                "Dust and vacuum extensively",
                "Clean gutters and downspouts",
                "Inspect and prepare heating system",
            ],
            "Winter": [
                "Declutter and organize living spaces",
                "Clean and store outdoor tools",
                "Check smoke detectors and batteries",
                "Deep clean upholstery",
                "Plan for upcoming seasonal tasks",
            ]
        }
        self.user_tasks = {}

    def add_custom_task(self, season, task):
        """Add a custom task for a specific season."""
        if season not in self.default_tasks:
            raise ValueError(f"Invalid season: {season}. Choose from {list(self.default_tasks.keys())}.")
        if season not in self.user_tasks:
            self.user_tasks[season] = []
        self.user_tasks[season].append(task)

    def generate_checklist(self, season):
        """Generate the cleaning checklist for a specific season."""
        if season not in self.default_tasks:
            raise ValueError(f"Invalid season: {season}. Choose from {list(self.default_tasks.keys())}.")
        
        # Combine default tasks with user custom tasks
        checklist = self.default_tasks[season].copy()
        if season in self.user_tasks:
            checklist.extend(self.user_tasks[season])
        
        return checklist

    def save_checklist(self, season, filename):
        """Save the checklist to a JSON file."""
        checklist = self.generate_checklist(season)
        with open(filename, 'w') as file:
            json.dump(checklist, file, indent=4)
        print(f"Checklist for {season} saved to {filename}")

if __name__ == "__main__":
    # Example usage
    cleaning_checklist = SeasonalCleaningChecklist()

    # Adding custom tasks
    try:
        cleaning_checklist.add_custom_task("Spring", "Clean out the refrigerator")
        cleaning_checklist.add_custom_task("Winter", "Set up holiday decorations")
        
        # Generate and save checklist for Spring
        spring_checklist = cleaning_checklist.generate_checklist("Spring")
        print("Spring Cleaning Checklist:")
        print("\n".join(spring_checklist))
        
        cleaning_checklist.save_checklist("Spring", "spring_cleaning_checklist.json")
    
    except ValueError as e:
        print(f"Error: {e}")
```
