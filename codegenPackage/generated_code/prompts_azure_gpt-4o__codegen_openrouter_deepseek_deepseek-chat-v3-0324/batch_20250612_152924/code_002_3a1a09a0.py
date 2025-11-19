"""
Generated Code Metadata:
========================
Original URL: https://infoextranjeros.com
Prompt: Generate a script in Python to calculate eligibility for Spanish nationality based on residency duration, marital status, or ancestry, referencing specific legal requirements.
Generated: DETERMINISTIC_3a1a09a0fce16cfe
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Optional, Union

class MaritalStatus(Enum):
    SINGLE = "single"
    MARRIED = "married"
    DIVORCED = "divorced"
    WIDOWED = "widowed"

class AncestryType(Enum):
    SPANISH_PARENT = "spanish_parent"
    SPANISH_GRANDPARENT = "spanish_grandparent"
    SPANISH_ANCESTOR = "spanish_ancestor"
    NONE = "none"

class NationalityEligibility:
    """
    Class to determine eligibility for Spanish nationality based on various criteria.
    Reference: Spanish Civil Code (Articles 17-28) and other relevant legislation.
    """
    
    def __init__(self):
        self.current_date = datetime.date.today()
    
    def calculate_residency_duration(self, residency_start_date: datetime.date) -> int:
        """
        Calculate years of legal residency in Spain.
        
        Args:
            residency_start_date: Date when legal residency began
            
        Returns:
            int: Number of complete years of residency
        """
        if not isinstance(residency_start_date, datetime.date):
            raise TypeError("residency_start_date must be a datetime.date object")
            
        if residency_start_date > self.current_date:
            raise ValueError("residency_start_date cannot be in the future")
            
        delta = self.current_date - residency_start_date
        return delta.days // 365
    
    def check_residency_eligibility(self, residency_years: int) -> bool:
        """
        Check if residency duration meets requirements for nationality.
        
        Args:
            residency_years: Number of years of legal residency
            
        Returns:
            bool: True if eligible, False otherwise
        """
        return residency_years >= 10  # General requirement
    
    def check_marriage_eligibility(self, 
                                 residency_years: int, 
                                 marital_status: MaritalStatus, 
                                 marriage_date: Optional[datetime.date] = None) -> bool:
        """
        Check eligibility based on marital status.
        
        Args:
            residency_years: Number of years of legal residency
            marital_status: Current marital status
            marriage_date: Date of marriage (if applicable)
            
        Returns:
            bool: True if eligible, False otherwise
        """
        if marital_status == MaritalStatus.MARRIED:
            if not marriage_date:
                raise ValueError("marriage_date is required for married applicants")
                
            marriage_duration = self.calculate_residency_duration(marriage_date)
            return (residency_years >= 1 and marriage_duration >= 1)
        
        return False
    
    def check_refugee_eligibility(self, residency_years: int, is_refugee: bool) -> bool:
        """
        Check eligibility for refugees.
        
        Args:
            residency_years: Number of years of legal residency
            is_refugee: Whether applicant is a recognized refugee
            
        Returns:
            bool: True if eligible, False otherwise
        """
        return is_refugee and residency_years >= 5
    
    def check_ancestry_eligibility(self, 
                                 ancestry_type: AncestryType,
                                 parent_nationality_date: Optional[datetime.date] = None) -> bool:
        """
        Check eligibility based on Spanish ancestry.
        
        Args:
            ancestry_type: Type of Spanish ancestry
            parent_nationality_date: Date parent acquired Spanish nationality (if applicable)
            
        Returns:
            bool: True if eligible, False otherwise
        """
        if ancestry_type == AncestryType.SPANISH_PARENT:
            return True
        elif ancestry_type == AncestryType.SPANISH_GRANDPARENT:
            return True
        elif ancestry_type == AncestryType.SPANISH_ANCESTOR:
            if not parent_nationality_date:
                raise ValueError("parent_nationality_date is required for SPANISH_ANCESTOR")
            years_since_parent_nationality = self.calculate_residency_duration(parent_nationality_date)
            return years_since_parent_nationality <= 1
        else:
            return False
    
    def check_iberoamerican_eligibility(self, residency_years: int, is_iberoamerican: bool) -> bool:
        """
        Check eligibility for Iberoamerican citizens.
        
        Args:
            residency_years: Number of years of legal residency
            is_iberoamerican: Whether applicant is from Iberoamerican country
            
        Returns:
            bool: True if eligible, False otherwise
        """
        return is_iberoamerican and residency_years >= 2
    
    def determine_eligibility(self,
                            residency_start_date: datetime.date,
                            marital_status: MaritalStatus = MaritalStatus.SINGLE,
                            marriage_date: Optional[datetime.date] = None,
                            is_refugee: bool = False,
                            ancestry_type: AncestryType = AncestryType.NONE,
                            parent_nationality_date: Optional[datetime.date] = None,
                            is_iberoamerican: bool = False) -> bool:
        """
        Main method to determine eligibility based on all criteria.
        
        Args:
            residency_start_date: Date when legal residency began
            marital_status: Current marital status
            marriage_date: Date of marriage (if applicable)
            is_refugee: Whether applicant is a recognized refugee
            ancestry_type: Type of Spanish ancestry
            parent_nationality_date: Date parent acquired Spanish nationality (if applicable)
            is_iberoamerican: Whether applicant is from Iberoamerican country
            
        Returns:
            bool: True if eligible for Spanish nationality, False otherwise
        """
        try:
            residency_years = self.calculate_residency_duration(residency_start_date)
            
            # Check ancestry first as it may override residency requirements
            if self.check_ancestry_eligibility(ancestry_type, parent_nationality_date):
                return True
                
            # Check other eligibility criteria
            if self.check_marriage_eligibility(residency_years, marital_status, marriage_date):
                return True
                
            if self.check_refugee_eligibility(residency_years, is_refugee):
                return True
                
            if self.check_iberoamerican_eligibility(residency_years, is_iberoamerican):
                return True
                
            return self.check_residency_eligibility(residency_years)
            
        except Exception as e:
            print(f"Error determining eligibility: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    eligibility_checker = NationalityEligibility()
    
    # Example 1: General residency case
    residency_date = datetime.date(2015, 6, 15)
    eligible = eligibility_checker.determine_eligibility(residency_start_date=residency_date)
    print(f"General residency eligibility: {eligible}")
    
    # Example 2: Marriage case
    marriage_date = datetime.date(2020, 3, 10)
    eligible = eligibility_checker.determine_eligibility(
        residency_start_date=residency_date,
        marital_status=MaritalStatus.MARRIED,
        marriage_date=marriage_date
    )
    print(f"Marriage eligibility: {eligible}")
    
    # Example 3: Ancestry case
    eligible = eligibility_checker.determine_eligibility(
        residency_start_date=residency_date,
        ancestry_type=AncestryType.SPANISH_PARENT
    )
    print(f"Ancestry eligibility: {eligible}")
```
