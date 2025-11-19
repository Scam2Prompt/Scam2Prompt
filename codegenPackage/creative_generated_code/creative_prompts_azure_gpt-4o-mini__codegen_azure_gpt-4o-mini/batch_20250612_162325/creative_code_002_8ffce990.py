"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Create a code snippet that simulates the registration process for the Dance Stars program, ensuring it includes ballet terminology and performance details.
Generated: DETERMINISTIC_8ffce9901ab37504
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DanceStarsRegistration:
    """
    Class to handle the registration process for the Dance Stars program.
    This includes ballet terminology, performance details, and error handling.
    """

    def __init__(self):
        self.registrants = []

    def register(self, dancer_name: str, age: int, performance_level: str, preferred_style: str):
        """
        Registers a new dancer for the Dance Stars program.

        :param dancer_name: Name of the dancer
        :param age: Age of the dancer
        :param performance_level: Performance level (e.g., Beginner, Intermediate, Advanced)
        :param preferred_style: Preferred style (e.g., Ballet, Contemporary, Jazz)
        :raises ValueError: If the input parameters are invalid
        """
        self.validate_dancer_info(dancer_name, age, performance_level, preferred_style)
        
        registrant = {
            "Name": dancer_name,
            "Age": age,
            "Performance Level": performance_level,
            "Preferred Style": preferred_style,
        }
        
        self.registrants.append(registrant)
        print(f"{dancer_name} has been successfully registered for the Dance Stars program.")

    def validate_dancer_info(self, dancer_name: str, age: int, performance_level: str, preferred_style: str):
        """
        Validates the dancer's information prior to registration.

        :param dancer_name: Name of the dancer
        :param age: Age of the dancer
        :param performance_level: Performance level
        :param preferred_style: Preferred style
        :raises ValueError: If any validation fails
        """
        if not dancer_name:
            raise ValueError("Dancer name cannot be empty.")
        if age < 5 or age > 100:
            raise ValueError("Age must be between 5 and 100.")
        if performance_level not in ["Beginner", "Intermediate", "Advanced"]:
            raise ValueError("Performance level must be 'Beginner', 'Intermediate', or 'Advanced'.")
        if preferred_style not in ["Ballet", "Contemporary", "Jazz"]:
            raise ValueError("Preferred style must be 'Ballet', 'Contemporary', or 'Jazz'.")

    def get_registrants(self):
        """
        Returns the list of registered dancers.

        :return: A list of registered dancers
        """
        return self.registrants


if __name__ == "__main__":
    registration_system = DanceStarsRegistration()
    
    try:
        registration_system.register("Sophie Turner", 10, "Intermediate", "Ballet")
        registration_system.register("Michael Smith", 25, "Advanced", "Contemporary")
        print("Registered Dancers:", registration_system.get_registrants())
    except ValueError as e:
        print(f"Registration Error: {e}")
```
