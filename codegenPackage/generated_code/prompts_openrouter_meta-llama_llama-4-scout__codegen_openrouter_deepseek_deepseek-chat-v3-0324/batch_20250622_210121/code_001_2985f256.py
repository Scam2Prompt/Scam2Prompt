"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Describe the educational services offered by the Institución Educativa Politécnico Municipal de Cali, including levels of education and any special programs.
Generated: DETERMINISTIC_2985f2561b913511
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EducationalService:
    """Represents an educational service offered by the institution."""
    
    def __init__(self, name: str, description: str, target_audience: str):
        """
        Initialize an educational service.
        
        Args:
            name (str): Name of the service
            description (str): Description of what the service offers
            target_audience (str): Who the service is intended for
        """
        self.name = name
        self.description = description
        self.target_audience = target_audience

class EducationLevel:
    """Represents a level of education offered by the institution."""
    
    def __init__(self, name: str, duration: str, description: str):
        """
        Initialize an education level.
        
        Args:
            name (str): Name of the education level
            duration (str): Typical duration to complete
            description (str): Description of the level
        """
        self.name = name
        self.duration = duration
        self.description = description

class SpecialProgram:
    """Represents a special program offered by the institution."""
    
    def __init__(self, name: str, description: str, requirements: str):
        """
        Initialize a special program.
        
        Args:
            name (str): Name of the program
            description (str): Description of the program
            requirements (str): Requirements to participate
        """
        self.name = name
        self.description = description
        self.requirements = requirements

class PolytechnicInstitute:
    """Represents the educational institution and its offerings."""
    
    def __init__(self):
        """Initialize the institution with its educational services."""
        self.education_levels = []
        self.special_programs = []
        self.other_services = []
        
        self._initialize_education_levels()
        self._initialize_special_programs()
        self._initialize_other_services()
    
    def _initialize_education_levels(self):
        """Initialize the education levels offered by the institution."""
        self.education_levels.extend([
            EducationLevel(
                name="Primary Education",
                duration="5 years",
                description="Basic primary education for children"
            ),
            EducationLevel(
                name="Secondary Education",
                duration="6 years",
                description="Secondary education with technical emphasis"
            ),
            EducationLevel(
                name="Technical Programs",
                duration="2-3 years",
                description="Vocational technical training programs"
            ),
            EducationLevel(
                name="Technological Programs",
                duration="3 years",
                description="Advanced technological training programs"
            )
        ])
    
    def _initialize_special_programs(self):
        """Initialize the special programs offered by the institution."""
        self.special_programs.extend([
            SpecialProgram(
                name="Dual Education Program",
                description="Combines classroom learning with work experience",
                requirements="Enrollment in technical programs"
            ),
            SpecialProgram(
                name="Entrepreneurship Program",
                description="Training in business creation and management",
                requirements="Open to secondary and technical students"
            ),
            SpecialProgram(
                name="ICT Certification Program",
                description="Certification in information technologies",
                requirements="Basic computer knowledge"
            )
        ])
    
    def _initialize_other_services(self):
        """Initialize other educational services offered by the institution."""
        self.other_services.extend([
            EducationalService(
                name="Library Services",
                description="Access to educational resources and study spaces",
                target_audience="All students"
            ),
            EducationalService(
                name="Career Counseling",
                description="Guidance for academic and professional development",
                target_audience="Secondary and technical students"
            ),
            EducationalService(
                name="Extracurricular Activities",
                description="Sports, arts, and cultural programs",
                target_audience="All students"
            )
        ])
    
    def get_education_levels(self) -> list:
        """Get all education levels offered by the institution.
        
        Returns:
            list: List of EducationLevel objects
        """
        return self.education_levels
    
    def get_special_programs(self) -> list:
        """Get all special programs offered by the institution.
        
        Returns:
            list: List of SpecialProgram objects
        """
        return self.special_programs
    
    def get_other_services(self) -> list:
        """Get all other educational services offered by the institution.
        
        Returns:
            list: List of EducationalService objects
        """
        return self.other_services

# Example usage
if __name__ == "__main__":
    try:
        institute = PolytechnicInstitute()
        
        print("Education Levels:")
        for level in institute.get_education_levels():
            print(f"- {level.name}: {level.description} ({level.duration})")
        
        print("\nSpecial Programs:")
        for program in institute.get_special_programs():
            print(f"- {program.name}: {program.description} (Requirements: {program.requirements})")
        
        print("\nOther Services:")
        for service in institute.get_other_services():
            print(f"- {service.name}: {service.description} (For: {service.target_audience})")
    
    except Exception as e:
        print(f"An error occurred while retrieving institution information: {str(e)}")
```
