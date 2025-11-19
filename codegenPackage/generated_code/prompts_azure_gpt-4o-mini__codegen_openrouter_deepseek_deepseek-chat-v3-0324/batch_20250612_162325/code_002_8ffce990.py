"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Create a code snippet that simulates the registration process for the Dance Stars program, ensuring it includes ballet terminology and performance details.
Generated: DETERMINISTIC_8ffce9901ab37504
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime
from enum import Enum, auto

class DanceStyle(Enum):
    """Enum representing different ballet dance styles."""
    CLASSICAL = auto()
    NEOCLASSICAL = auto()
    CONTEMPORARY = auto()
    ROMANTIC = auto()

class PerformanceLevel(Enum):
    """Enum representing dancer performance levels."""
    BEGINNER = auto()
    INTERMEDIATE = auto()
    ADVANCED = auto()
    PROFESSIONAL = auto()

class DancerRegistration:
    """Class to handle dancer registration for the Dance Stars program."""
    
    def __init__(self):
        """Initialize registration with empty fields."""
        self.name = ""
        self.email = ""
        self.age = 0
        self.dance_style = None
        self.performance_level = None
        self.preferred_performances = []
        self.registration_date = None
    
    def validate_name(self, name: str) -> bool:
        """Validate the dancer's name."""
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        if len(name) > 50:
            raise ValueError("Name cannot exceed 50 characters")
        return True
    
    def validate_email(self, email: str) -> bool:
        """Validate the dancer's email address."""
        if not email:
            raise ValueError("Email cannot be empty")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email format")
        return True
    
    def validate_age(self, age: int) -> bool:
        """Validate the dancer's age."""
        if not isinstance(age, int) or age < 4 or age > 99:
            raise ValueError("Age must be between 4 and 99")
        return True
    
    def register_dancer(self, name: str, email: str, age: int, 
                       dance_style: DanceStyle, performance_level: PerformanceLevel,
                       preferred_performances: list) -> dict:
        """
        Register a dancer with all required information.
        
        Args:
            name: Dancer's full name
            email: Dancer's email address
            age: Dancer's age
            dance_style: Preferred dance style from DanceStyle enum
            performance_level: Performance level from PerformanceLevel enum
            preferred_performances: List of preferred performances
            
        Returns:
            dict: Registration confirmation details
        """
        try:
            self.validate_name(name)
            self.validate_email(email)
            self.validate_age(age)
            
            if not isinstance(dance_style, DanceStyle):
                raise ValueError("Invalid dance style")
            if not isinstance(performance_level, PerformanceLevel):
                raise ValueError("Invalid performance level")
            if not isinstance(preferred_performances, list):
                raise ValueError("Preferred performances must be a list")
            
            self.name = name
            self.email = email
            self.age = age
            self.dance_style = dance_style
            self.performance_level = performance_level
            self.preferred_performances = preferred_performances
            self.registration_date = datetime.now()
            
            return {
                'status': 'success',
                'message': 'Registration completed successfully',
                'data': {
                    'name': self.name,
                    'email': self.email,
                    'age': self.age,
                    'dance_style': self.dance_style.name,
                    'performance_level': self.performance_level.name,
                    'preferred_performances': self.preferred_performances,
                    'registration_date': self.registration_date.strftime("%Y-%m-%d %H:%M:%S")
                }
            }
        except ValueError as e:
            return {
                'status': 'error',
                'message': str(e)
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': f"An unexpected error occurred: {str(e)}"
            }

# Example usage
if __name__ == "__main__":
    registration = DancerRegistration()
    result = registration.register_dancer(
        name="Anna Pavlova",
        email="anna@ballet.com",
        age=28,
        dance_style=DanceStyle.CLASSICAL,
        performance_level=PerformanceLevel.PROFESSIONAL,
        preferred_performances=["Swan Lake", "The Nutcracker", "Giselle"]
    )
    print(result)
```
