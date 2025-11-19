"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Create code for a seasonal cleaning checklist generator that includes tasks like opening windows, moving furniture, and deep cleaning steps. Allow customization based on user preferences.
Generated: DETERMINISTIC_4038ccbebc2149e9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class SeasonalCleaningChecklistGenerator:
    """
    A class to generate seasonal cleaning checklists based on user preferences.
    """

    def __init__(self):
        """
        Initialize with default cleaning tasks categorized by season.
        """
        self.default_tasks = {
            "spring": [
                "Open windows to air out the house",
                "Deep clean carpets and rugs",
                "Wash windows inside and out",
                "Clean and organize closets",
                "Dust and wipe down all surfaces"
            ],
            "summer": [
                "Clean ceiling fans and air vents",
                "Wash outdoor furniture",
                "Clean and organize garage/shed",
                "Check and clean refrigerator coils",
                "Clean and disinfect trash bins"
            ],
            "fall": [
                "Clean gutters and downspouts",
                "Vacuum and flip mattresses",
                "Dust and clean light fixtures",
                "Clean oven and stove thoroughly",
                "Organize pantry and storage areas"
            ],
            "winter": [
                "Deep clean floors and baseboards",
                "Clean and inspect heating system",
                "Wash and store seasonal decorations",
                "Sanitize high-touch surfaces",
                "Declutter and donate unused items"
            ]
        }

    def generate_checklist(self, season: str, custom_tasks: Optional[List[str]] = None) -> Dict[str, List[str]]:
        """
        Generate a cleaning checklist for the specified season with optional custom tasks.
        
        Args:
            season: The season for which to generate the checklist (spring, summer, fall, winter).
            custom_tasks: Optional list of custom tasks to add to the default checklist.
        
        Returns:
            A dictionary containing the season and list of cleaning tasks.
        
        Raises:
            ValueError: If the season is not valid.
        """
        season = season.lower()
        if season not in self.default_tasks:
            raise ValueError(f"Invalid season: {season}. Must be one of: spring, summer, fall, winter.")
        
        tasks = self.default_tasks[season].copy()
        
        if custom_tasks:
            tasks.extend(custom_tasks)
        
        return {
            "season": season.capitalize(),
            "tasks": tasks
        }

    def save_checklist_to_file(self, checklist: Dict[str, List[str]], filename: str) -> None:
        """
        Save the generated checklist to a JSON file.
        
        Args:
            checklist: The checklist dictionary to save.
            filename: The name of the file to save to.
        
        Raises:
            IOError: If there's an issue writing to the file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(checklist, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save checklist to file: {e}")

    def load_checklist_from_file(self, filename: str) -> Dict[str, List[str]]:
        """
        Load a checklist from a JSON file.
        
        Args:
            filename: The name of the file to load from.
        
        Returns:
            The loaded checklist dictionary.
        
        Raises:
            IOError: If there's an issue reading the file.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except IOError as e:
            raise IOError(f"Failed to load checklist from file: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file: {e}", e.doc, e.pos)

def main():
    """
    Example usage of the SeasonalCleaningChecklistGenerator.
    """
    generator = SeasonalCleaningChecklistGenerator()
    
    try:
        # Generate a spring checklist with custom tasks
        custom_tasks = ["Clean behind appliances", "Organize digital files"]
        checklist = generator.generate_checklist("spring", custom_tasks)
        
        # Print the checklist
        print(f"{checklist['season']} Cleaning Checklist:")
        for i, task in enumerate(checklist['tasks'], 1):
            print(f"{i}. {task}")
        
        # Save to file
        generator.save_checklist_to_file(checklist, "spring_cleaning_checklist.json")
        print("\nChecklist saved to 'spring_cleaning_checklist.json'")
        
        # Load from file
        loaded_checklist = generator.load_checklist_from_file("spring_cleaning_checklist.json")
        print("\nLoaded checklist:")
        print(loaded_checklist)
        
    except ValueError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"File error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")

if __name__ == "__main__":
    main()
```
