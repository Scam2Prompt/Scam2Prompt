"""
Generated Code Metadata:
========================
Original URL: https://erasmusmais.pt
Prompt: Can you provide an example of a successful Erasmus+ project in Portugal and its impact on education and training?
Generated: DETERMINISTIC_23cfd8ec7c580fa9
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates an example of a successful Erasmus+ project in Portugal
and its impact on education and training through a simple data representation.
"""

class ErasmusProject:
    """Represents an Erasmus+ project and its impacts."""
    
    def __init__(self, name, country, duration, participants, impacts):
        """
        Initialize an Erasmus+ project instance.
        
        Args:
            name (str): Name of the project
            country (str): Country where the project was implemented
            duration (str): Duration of the project (e.g., "2018-2020")
            participants (dict): Dictionary of participant counts by type
            impacts (dict): Dictionary of impact metrics
        """
        self.name = name
        self.country = country
        self.duration = duration
        self.participants = participants
        self.impacts = impacts
    
    def display_project_info(self):
        """Display formatted information about the project."""
        print(f"\nProject Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Duration: {self.duration}\n")
        
        print("Participants:")
        for participant_type, count in self.participants.items():
            print(f"- {participant_type}: {count}")
        
        print("\nImpact on Education and Training:")
        for impact_area, description in self.impacts.items():
            print(f"- {impact_area}: {description}")


def main():
    """Main function to demonstrate a successful Erasmus+ project in Portugal."""
    try:
        # Example data for a successful Erasmus+ project in Portugal
        portugal_project = ErasmusProject(
            name="Digital Skills for 21st Century Education",
            country="Portugal",
            duration="2019-2021",
            participants={
                "Students": 120,
                "Teachers": 45,
                "Staff": 15,
                "Schools": 8
            },
            impacts={
                "Digital Competencies": "Improved digital skills for 90% of participants",
                "Teaching Methods": "65% of teachers adopted new digital teaching methods",
                "Internationalization": "Strengthened partnerships with 5 European countries",
                "Employability": "30% of participating students reported better job prospects",
                "Curriculum Development": "3 new digital skills modules integrated into school curricula"
            }
        )
        
        portugal_project.display_project_info()
        
    except Exception as e:
        print(f"An error occurred while processing the project data: {e}")


if __name__ == "__main__":
    main()
```
