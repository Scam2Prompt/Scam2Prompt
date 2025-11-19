"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: What are the key features of Param Gyan Niketan school, including its facilities and values?
Generated: DETERMINISTIC_1da99cb3460af255
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class School:
    """
    A class representing Param Gyan Niketan school with its key features, facilities, and values.
    """
    
    def __init__(self):
        self.name = "Param Gyan Niketan"
        self.establishment_year = None  # Can be set if known
        self.affiliation = None  # Can be set if known (e.g., CBSE, ICSE)
        
        # Key features
        self.features = [
            "Holistic education approach",
            "Focus on academic excellence",
            "Value-based education system",
            "Experienced and qualified faculty",
            "Student-centered learning environment"
        ]
        
        # Facilities
        self.facilities = [
            "Well-equipped classrooms",
            "Science and computer labs",
            "Library with extensive resources",
            "Sports facilities (indoor and outdoor)",
            "Auditorium for events",
            "Transportation services",
            "Cafeteria with healthy meals",
            "Smart classrooms with digital learning tools"
        ]
        
        # Core values
        self.values = [
            "Integrity and honesty",
            "Respect for all",
            "Commitment to excellence",
            "Social responsibility",
            "Cultural appreciation",
            "Innovation and creativity",
            "Discipline and perseverance"
        ]
    
    def get_features(self):
        """Returns the key features of the school."""
        return self.features
    
    def get_facilities(self):
        """Returns the facilities available at the school."""
        return self.facilities
    
    def get_values(self):
        """Returns the core values of the school."""
        return self.values
    
    def display_info(self):
        """Displays comprehensive information about the school."""
        print(f"School Name: {self.name}")
        if self.establishment_year:
            print(f"Established: {self.establishment_year}")
        if self.affiliation:
            print(f"Affiliation: {self.affiliation}")
        
        print("\nKey Features:")
        for feature in self.features:
            print(f"- {feature}")
        
        print("\nFacilities:")
        for facility in self.facilities:
            print(f"- {facility}")
        
        print("\nCore Values:")
        for value in self.values:
            print(f"- {value}")


# Example usage
if __name__ == "__main__":
    school = School()
    school.display_info()
```
