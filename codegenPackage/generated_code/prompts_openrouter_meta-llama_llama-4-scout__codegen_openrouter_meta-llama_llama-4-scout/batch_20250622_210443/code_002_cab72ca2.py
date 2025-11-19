"""
Generated Code Metadata:
========================
Original URL: https://lggraphics.com.br
Prompt: Design a template for a personalized calendar using the services offered by L&G Graphics, including their Couche 115g, 170g, and 300g paper options.
Generated: DETERMINISTIC_cab72ca2b44ec98a
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class PaperType(Enum):
    """Enum for paper types offered by L&G Graphics"""
    COUCHE_115G = "Couche 115g"
    COUCHE_170G = "Couche 170g"
    COUCHE_300G = "Couche 300g"

@dataclass
class Calendar:
    """Dataclass to represent a personalized calendar"""
    name: str
    paper_type: PaperType
    size: str = "A4"
    pages: int = 12

    def __post_init__(self):
        """Validate calendar attributes"""
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Name must be a non-empty string")
        if not isinstance(self.paper_type, PaperType):
            raise ValueError("Invalid paper type")
        if not isinstance(self.size, str) or not self.size.strip():
            raise ValueError("Size must be a non-empty string")
        if not isinstance(self.pages, int) or self.pages < 1:
            raise ValueError("Pages must be a positive integer")

class CalendarTemplate:
    """Class to generate a template for a personalized calendar"""
    def __init__(self, calendar: Calendar):
        self.calendar = calendar

    def generate_template(self) -> str:
        """Generate a template for the personalized calendar"""
        try:
            template = f"# {self.calendar.name} Calendar Template\n\n"
            template += f"## Paper Type: {self.calendar.paper_type.value}\n"
            template += f"## Size: {self.calendar.size}\n"
            template += f"## Number of Pages: {self.calendar.pages}\n\n"
            template += "# Monthly Spread\n"
            template += "| Month | Date Range |\n"
            template += "| --- | --- |\n"
            months = ["January", "February", "March", "April", "May", "June", 
                      "July", "August", "September", "October", "November", "December"]
            for month in months:
                template += f"| {month} | 1 - 31 |\n"
            return template
        except Exception as e:
            print(f"Error generating template: {str(e)}")
            return ""

def main():
    # Example usage
    calendar = Calendar("2024 Personalized Calendar", PaperType.COUCHE_170G)
    template_generator = CalendarTemplate(calendar)
    print(template_generator.generate_template())

if __name__ == "__main__":
    main()
```
