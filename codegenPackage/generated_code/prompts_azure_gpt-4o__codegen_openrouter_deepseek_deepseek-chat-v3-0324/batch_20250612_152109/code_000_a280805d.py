"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: Write Python code to generate a step-by-step guide for creating a Halloween countdown calendar using paper crafts, as described on Craft Intra.
Generated: DETERMINISTIC_a280805d09b3af07
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class HalloweenCountdownCalendar:
    """
    A class to generate a step-by-step guide for creating a Halloween countdown calendar using paper crafts.
    """

    def __init__(self, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize the Halloween countdown calendar with start and end dates.
        
        Args:
            start_date (datetime.date): The start date of the countdown.
            end_date (datetime.date): The end date (Halloween).
        """
        self.start_date = start_date
        self.end_date = end_date
        self.days_count = (end_date - start_date).days + 1
        self.materials = self._get_default_materials()
        self.steps = self._generate_steps()

    def _get_default_materials(self) -> List[str]:
        """
        Get the default materials needed for the craft.
        
        Returns:
            List[str]: List of materials.
        """
        return [
            "Colored construction paper (orange, black, purple)",
            "Scissors",
            "Glue or double-sided tape",
            "Markers or colored pencils",
            "Ruler",
            "Pencil",
            "Small Halloween-themed stickers or drawings",
            "String or ribbon",
            "Hole punch"
        ]

    def _generate_steps(self) -> List[Dict[str, str]]:
        """
        Generate the step-by-step instructions for creating the calendar.
        
        Returns:
            List[Dict[str, str]]: List of steps with titles and descriptions.
        """
        steps = [
            {
                "title": "Prepare the Base",
                "description": "Cut a large piece of construction paper (approx. 12x18 inches) for the base."
            },
            {
                "title": "Create Calendar Grid",
                "description": f"Using a ruler and pencil, divide the base into {self.days_count} equal sections for each day of the countdown."
            },
            {
                "title": "Decorate the Sections",
                "description": "Decorate each section with Halloween-themed drawings or stickers. Number them from 1 to {self.days_count}."
            },
            {
                "title": "Make the Flaps",
                "description": "Cut small squares of paper slightly larger than each section. Glue the top edge to create flaps that can be lifted."
            },
            {
                "title": "Add Daily Surprises",
                "description": "Write fun Halloween activities or jokes under each flap for each day of the countdown."
            },
            {
                "title": "Final Touches",
                "description": "Punch a hole at the top and thread a ribbon for hanging. Add any final decorations."
            }
        ]
        return steps

    def get_materials(self) -> List[str]:
        """
        Get the list of materials needed.
        
        Returns:
            List[str]: List of materials.
        """
        return self.materials

    def get_steps(self) -> List[Dict[str, str]]:
        """
        Get the step-by-step instructions.
        
        Returns:
            List[Dict[str, str]]: List of steps with titles and descriptions.
        """
        return self.steps

    def print_guide(self) -> None:
        """
        Print the complete guide including materials and steps.
        """
        print("Halloween Countdown Calendar Guide\n")
        print("Materials Needed:")
        for i, material in enumerate(self.materials, 1):
            print(f"{i}. {material}")
        
        print("\nSteps:")
        for i, step in enumerate(self.steps, 1):
            print(f"\nStep {i}: {step['title']}")
            print(step['description'])

# Example usage
if __name__ == "__main__":
    try:
        # Set the start date (October 1st) and end date (October 31st) for the current year
        current_year = datetime.date.today().year
        start_date = datetime.date(current_year, 10, 1)
        end_date = datetime.date(current_year, 10, 31)
        
        calendar = HalloweenCountdownCalendar(start_date, end_date)
        calendar.print_guide()
    except Exception as e:
        print(f"An error occurred: {e}")
```
