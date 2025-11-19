"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Compare the facilities offered by Param Gyan Niketan, such as computer labs, libraries, and transportation, with those of a typical CBSE school.
Generated: DETERMINISTIC_bb9677f307a78b3e
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SchoolFacility:
    """Base class representing a school facility."""
    
    def __init__(self, name, description, available):
        """
        Initialize a school facility.
        
        Args:
            name (str): Name of the facility
            description (str): Description of the facility
            available (bool): Whether the facility is available
        """
        self.name = name
        self.description = description
        self.available = available
    
    def __str__(self):
        """String representation of the facility."""
        return f"{self.name}: {self.description} ({'Available' if self.available else 'Not Available'})"

class School:
    """Class representing a school and its facilities."""
    
    def __init__(self, name, school_type):
        """
        Initialize a school with its facilities.
        
        Args:
            name (str): Name of the school
            school_type (str): Type of school (e.g., 'CBSE', 'State Board')
        """
        self.name = name
        self.school_type = school_type
        self.facilities = []
    
    def add_facility(self, facility):
        """
        Add a facility to the school.
        
        Args:
            facility (SchoolFacility): Facility object to add
        """
        self.facilities.append(facility)
    
    def get_facilities(self):
        """Return list of all facilities."""
        return self.facilities
    
    def compare_with(self, other_school):
        """
        Compare facilities with another school.
        
        Args:
            other_school (School): Another School object to compare with
            
        Returns:
            dict: Comparison results
        """
        comparison = {
            'school1': self.name,
            'school2': other_school.name,
            'comparisons': []
        }
        
        # Get all unique facility names from both schools
        all_facilities = set()
        for facility in self.facilities + other_school.facilities:
            all_facilities.add(facility.name)
        
        # Compare each facility
        for facility_name in all_facilities:
            school1_fac = next((f for f in self.facilities if f.name == facility_name), None)
            school2_fac = next((f for f in other_school.facilities if f.name == facility_name), None)
            
            comparison['comparisons'].append({
                'facility': facility_name,
                f'{self.name}_available': school1_fac.available if school1_fac else False,
                f'{self.name}_description': school1_fac.description if school1_fac else "Not available",
                f'{other_school.name}_available': school2_fac.available if school2_fac else False,
                f'{other_school.name}_description': school2_fac.description if school2_fac else "Not available"
            })
        
        return comparison

def create_param_gyan_niketan():
    """Create Param Gyan Niketan school with its facilities."""
    pgn = School("Param Gyan Niketan", "CBSE")
    
    pgn.add_facility(SchoolFacility(
        "Computer Lab",
        "Well-equipped computer lab with latest hardware and software",
        True
    ))
    
    pgn.add_facility(SchoolFacility(
        "Library",
        "Extensive collection of books with digital resources",
        True
    ))
    
    pgn.add_facility(SchoolFacility(
        "Transportation",
        "School buses covering major routes with GPS tracking",
        True
    ))
    
    pgn.add_facility(SchoolFacility(
        "Science Lab",
        "Modern equipment for physics, chemistry and biology",
        True
    ))
    
    return pgn

def create_typical_cbse_school():
    """Create a typical CBSE school with its facilities."""
    typical = School("Typical CBSE School", "CBSE")
    
    typical.add_facility(SchoolFacility(
        "Computer Lab",
        "Basic computer lab with standard equipment",
        True
    ))
    
    typical.add_facility(SchoolFacility(
        "Library",
        "Standard collection of books",
        True
    ))
    
    typical.add_facility(SchoolFacility(
        "Transportation",
        "Limited bus service available",
        False
    ))
    
    typical.add_facility(SchoolFacility(
        "Science Lab",
        "Basic lab equipment",
        True
    ))
    
    return typical

def compare_schools():
    """Main function to compare the two schools."""
    try:
        pgn = create_param_gyan_niketan()
        typical_cbse = create_typical_cbse_school()
        
        comparison = pgn.compare_with(typical_cbse)
        
        # Print comparison results
        print(f"Comparison between {comparison['school1']} and {comparison['school2']}:")
        print("-" * 50)
        
        for comp in comparison['comparisons']:
            print(f"\nFacility: {comp['facility']}")
            print(f"{comparison['school1']}:")
            print(f"  Available: {'Yes' if comp[f'{comparison['school1']}_available'] else 'No'}")
            print(f"  Description: {comp[f'{comparison['school1']}_description']}")
            print(f"{comparison['school2']}:")
            print(f"  Available: {'Yes' if comp[f'{comparison['school2']}_available'] else 'No'}")
            print(f"  Description: {comp[f'{comparison['school2']}_description']}")
        
        return comparison
    
    except Exception as e:
        print(f"An error occurred during comparison: {str(e)}")
        return None

if __name__ == "__main__":
    compare_schools()
```
