"""
Generated Code Metadata:
========================
Original URL: https://cuicalli.edu.mx
Prompt: Compare the features of the different campuses of Universidad Tecnológico Cuicalli, including Naucalpan, Huixquilucan, Ecatepec, and Arboledas.
Generated: DETERMINISTIC_44c53c7024ff8ede
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Campus:
    """
    Represents a university campus with its features.
    """
    def __init__(self, name, location, programs, facilities, student_capacity):
        """
        Initialize a Campus object.
        
        Args:
            name (str): Name of the campus
            location (str): City where campus is located
            programs (list): List of academic programs offered
            facilities (list): List of campus facilities
            student_capacity (int): Maximum student capacity
        """
        self.name = name
        self.location = location
        self.programs = programs
        self.facilities = facilities
        self.student_capacity = student_capacity
    
    def __str__(self):
        """String representation of the campus."""
        return f"{self.name} Campus ({self.location})"
    
    def get_features(self):
        """Return a dictionary of campus features."""
        return {
            "name": self.name,
            "location": self.location,
            "programs": self.programs,
            "facilities": self.facilities,
            "student_capacity": self.student_capacity
        }

def compare_campuses(campuses):
    """
    Compare features of multiple campuses and return comparison data.
    
    Args:
        campuses (list): List of Campus objects to compare
        
    Returns:
        dict: Dictionary containing comparison data
    """
    comparison = {
        "locations": [],
        "programs": {},
        "facilities": {},
        "capacities": {}
    }
    
    for campus in campuses:
        features = campus.get_features()
        comparison["locations"].append(features["location"])
        
        # Track unique programs across campuses
        for program in features["programs"]:
            if program not in comparison["programs"]:
                comparison["programs"][program] = []
            comparison["programs"][program].append(campus.name)
        
        # Track unique facilities across campuses
        for facility in features["facilities"]:
            if facility not in comparison["facilities"]:
                comparison["facilities"][facility] = []
            comparison["facilities"][facility].append(campus.name)
        
        # Record student capacities
        comparison["capacities"][campus.name] = features["student_capacity"]
    
    return comparison

def main():
    """Main function to demonstrate campus comparison."""
    # Create campus objects
    naucalpan = Campus(
        "Naucalpan",
        "Naucalpan de Juárez",
        ["Computer Science", "Business Administration", "Engineering"],
        ["Library", "Sports Center", "Computer Labs"],
        5000
    )
    
    huixquilucan = Campus(
        "Huixquilucan",
        "Huixquilucan",
        ["Law", "Architecture", "Medicine"],
        ["Library", "Auditorium", "Medical Labs"],
        3500
    )
    
    ecatepec = Campus(
        "Ecatepec",
        "Ecatepec de Morelos",
        ["Education", "Psychology", "Communications"],
        ["Library", "Theater", "Psychology Labs"],
        4000
    )
    
    arboledas = Campus(
        "Arboledas",
        "Atizapán de Zaragoza",
        ["Graphic Design", "Marketing", "Industrial Design"],
        ["Library", "Design Studios", "Exhibition Hall"],
        3000
    )
    
    # Compare campuses
    campuses = [naucalpan, huixquilucan, ecatepec, arboledas]
    comparison = compare_campuses(campuses)
    
    # Print comparison results
    print("Campus Locations:", comparison["locations"])
    print("\nPrograms Offered:")
    for program, campuses in comparison["programs"].items():
        print(f"- {program}: Available at {', '.join(campuses)}")
    
    print("\nFacilities Available:")
    for facility, campuses in comparison["facilities"].items():
        print(f"- {facility}: Available at {', '.join(campuses)}")
    
    print("\nStudent Capacities:")
    for campus, capacity in comparison["capacities"].items():
        print(f"- {campus}: {capacity} students")

if __name__ == "__main__":
    main()
```
