"""
Generated Code Metadata:
========================
Original URL: https://infoextranjeros.com
Prompt: "What are the different options for obtaining a residence and work visa in Spain, and how can I determine which one is best for my situation?"
Generated: DETERMINISTIC_0f9c7dcfa6eac152
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum, auto

class VisaType(Enum):
    """Enumeration of different visa types for Spain."""
    WORK_VISA = auto()
    STUDENT_VISA = auto()
    INVESTOR_VISA = auto()
    ENTREPRENEUR_VISA = auto()
    FAMILY_REUNIFICATION = auto()
    NON_LUCARTIVE_VISA = auto()
    DIGITAL_NOMAD_VISA = auto()

class VisaOption:
    """Class representing a visa option with its requirements."""
    
    def __init__(self, visa_type: VisaType, requirements: dict, duration: str, allows_work: bool):
        """
        Initialize a visa option.
        
        Args:
            visa_type: Type of visa from VisaType enum
            requirements: Dictionary of requirements for this visa
            duration: String describing visa duration
            allows_work: Boolean indicating if work is permitted
        """
        self.visa_type = visa_type
        self.requirements = requirements
        self.duration = duration
        self.allows_work = allows_work
    
    def to_dict(self):
        """Convert visa option to dictionary for easy serialization."""
        return {
            'visa_type': self.visa_type.name,
            'requirements': self.requirements,
            'duration': self.duration,
            'allows_work': self.allows_work
        }

class VisaAdvisor:
    """Class to help determine the best visa option based on user situation."""
    
    def __init__(self):
        """Initialize visa advisor with available visa options."""
        self.visa_options = self._initialize_visa_options()
    
    def _initialize_visa_options(self) -> list[VisaOption]:
        """Create and return a list of available visa options for Spain."""
        return [
            VisaOption(
                VisaType.WORK_VISA,
                {
                    'job_offer': True,
                    'employer_sponsorship': True,
                    'professional_qualifications': 'Required',
                    'minimum_salary': 'As per Spanish labor laws'
                },
                '1-2 years, renewable',
                True
            ),
            VisaOption(
                VisaType.STUDENT_VISA,
                {
                    'university_admission': True,
                    'financial_means': 'Minimum €600/month',
                    'health_insurance': True
                },
                'Duration of studies',
                True
            ),
            VisaOption(
                VisaType.INVESTOR_VISA,
                {
                    'minimum_investment': '€500,000 in real estate or €1M in Spanish company',
                    'clean_criminal_record': True
                },
                'Initial 2 years, then renewable',
                True
            ),
            VisaOption(
                VisaType.ENTREPRENEUR_VISA,
                {
                    'business_plan': True,
                    'economic_viability': True,
                    'job_creation': 'Potential to create jobs'
                },
                'Initial 1 year, renewable',
                True
            ),
            VisaOption(
                VisaType.FAMILY_REUNIFICATION,
                {
                    'family_member_in_spain': True,
                    'residency_status': 'Legal resident or citizen',
                    'financial_means': 'Sufficient to support family'
                },
                'Depends on sponsor\'s visa',
                False
            ),
            VisaOption(
                VisaType.NON_LUCARTIVE_VISA,
                {
                    'financial_means': 'Minimum €27,000/year for individual',
                    'health_insurance': True,
                    'no_work': True
                },
                '1 year, renewable',
                False
            ),
            VisaOption(
                VisaType.DIGITAL_NOMAD_VISA,
                {
                    'remote_work': True,
                    'employer_outside_spain': True,
                    'minimum_income': '€2,000/month',
                    'health_insurance': True
                },
                '1 year, renewable up to 5',
                True
            )
        ]
    
    def get_matching_visas(self, user_profile: dict) -> list[dict]:
        """
        Return visa options that match the user's profile.
        
        Args:
            user_profile: Dictionary containing user's information
            
        Returns:
            List of matching visa options as dictionaries
        """
        matching_visas = []
        
        for option in self.visa_options:
            if self._matches_profile(option, user_profile):
                matching_visas.append(option.to_dict())
        
        return matching_visas
    
    def _matches_profile(self, visa_option: VisaOption, user_profile: dict) -> bool:
        """
        Check if a visa option matches the user's profile.
        
        Args:
            visa_option: VisaOption to check
            user_profile: User's information dictionary
            
        Returns:
            True if visa matches user profile, False otherwise
        """
        # Check basic work requirement
        if user_profile.get('wants_to_work', False) and not visa_option.allows_work:
            return False
        
        # Check specific requirements
        for req_key, req_value in visa_option.requirements.items():
            if req_key not in user_profile:
                return False
            
            user_value = user_profile[req_key]
            
            # Handle special cases
            if req_key == 'financial_means':
                if not self._check_financial_means(req_value, user_value):
                    return False
            elif req_key == 'minimum_investment':
                if not self._check_investment(req_value, user_value):
                    return False
            elif isinstance(req_value, bool) and user_value != req_value:
                return False
            elif isinstance(req_value, str) and not user_value:
                return False
        
        return True
    
    def _check_financial_means(self, requirement: str, user_value: float) -> bool:
        """Check if user meets financial requirements."""
        try:
            if '€' in requirement:
                min_amount = float(requirement.split('€')[1].split('/')[0].replace(',', ''))
                return user_value >= min_amount
            return True
        except (ValueError, IndexError):
            return False
    
    def _check_investment(self, requirement: str, user_value: float) -> bool:
        """Check if user meets investment requirements."""
        try:
            if '€' in requirement:
                min_amount = float(requirement.split('€')[1].split(' ')[0].replace(',', ''))
                return user_value >= min_amount
            return True
        except (ValueError, IndexError):
            return False
    
    def get_all_visa_options(self) -> list[dict]:
        """Return all visa options as dictionaries."""
        return [option.to_dict() for option in self.visa_options]

def main():
    """Main function to demonstrate visa advisor functionality."""
    advisor = VisaAdvisor()
    
    # Example user profile
    user_profile = {
        'wants_to_work': True,
        'job_offer': False,
        'employer_sponsorship': False,
        'remote_work': True,
        'employer_outside_spain': True,
        'minimum_income': 2500,
        'health_insurance': True
    }
    
    print("All available visa options:")
    print(json.dumps(advisor.get_all_visa_options(), indent=2))
    
    print("\nMatching visa options for your profile:")
    print(json.dumps(advisor.get_matching_visas(user_profile), indent=2))

if __name__ == "__main__":
    main()
```
