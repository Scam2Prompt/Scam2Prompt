"""
Generated Code Metadata:
========================
Original URL: https://spacem-world.vercel.app
Prompt: Develop a system to handle user eligibility for the SpaceM Hunt based on their country of residence, excluding citizens or residents of the USA, UK, and Canada.
Generated: DETERMINISTIC_117dc95dea464b2f
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Set, Optional
from enum import Enum, auto

class EligibilityError(Exception):
    """Base class for eligibility-related exceptions."""
    pass

class CountryNotAllowedError(EligibilityError):
    """Raised when a user's country is not allowed."""
    pass

class Country:
    """Represents a country with its name and ISO code."""
    
    def __init__(self, name: str, iso_code: str):
        self.name = name
        self.iso_code = iso_code

class User:
    """Represents a user with their country of residence."""
    
    def __init__(self, name: str, country: Country):
        self.name = name
        self.country = country

class EligibilityStatus(Enum):
    """Represents the eligibility status of a user."""
    ELIGIBLE = auto()
    NOT_ELIGIBLE = auto()

class EligibilityChecker:
    """Checks user eligibility based on their country of residence."""
    
    def __init__(self, excluded_countries: Set[str]):
        """
        Initialize the EligibilityChecker with a set of excluded country ISO codes.
        
        Args:
            excluded_countries: Set of ISO country codes to exclude.
        """
        self.excluded_countries = excluded_countries
    
    def is_eligible(self, user: User) -> EligibilityStatus:
        """
        Check if a user is eligible based on their country.
        
        Args:
            user: The user to check.
            
        Returns:
            EligibilityStatus: ELIGIBLE or NOT_ELIGIBLE.
        """
        if user.country.iso_code in self.excluded_countries:
            return EligibilityStatus.NOT_ELIGIBLE
        return EligibilityStatus.ELIGIBLE
    
    def check_eligibility(self, user: User) -> None:
        """
        Check user eligibility and raise an exception if not eligible.
        
        Args:
            user: The user to check.
            
        Raises:
            CountryNotAllowedError: If the user's country is excluded.
        """
        if not self.is_eligible(user) == EligibilityStatus.ELIGIBLE:
            raise CountryNotAllowedError(
                f"Users from {user.country.name} are not eligible for SpaceM Hunt."
            )

# Example usage
if __name__ == "__main__":
    # Define excluded countries (USA, UK, Canada)
    EXCLUDED_COUNTRIES = {"US", "GB", "CA"}
    
    # Initialize eligibility checker
    checker = EligibilityChecker(EXCLUDED_COUNTRIES)
    
    # Example users
    users = [
        User("Alice", Country("United States", "US")),
        User("Bob", Country("Germany", "DE")),
        User("Charlie", Country("United Kingdom", "GB")),
        User("Dana", Country("Canada", "CA")),
        User("Eve", Country("France", "FR")),
    ]
    
    # Check each user's eligibility
    for user in users:
        try:
            checker.check_eligibility(user)
            print(f"{user.name} is eligible for SpaceM Hunt.")
        except CountryNotAllowedError as e:
            print(f"{user.name} is not eligible: {str(e)}")
```
