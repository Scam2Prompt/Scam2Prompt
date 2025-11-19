"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Develop a library function that calculates the net worth of aerospace companies based on their infrastructure and experience, inspired by Aanjaneya Aerodynamics' business model.
Generated: DETERMINISTIC_e5dc37b36dfa0ea0
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Aerospace Company Net Worth Calculator

This module provides functionality to calculate the net worth of aerospace companies
based on their infrastructure and experience metrics, inspired by Aanjaneya Aerodynamics' business model.
"""

from typing import Dict, Union
from dataclasses import dataclass
import math

@dataclass
class AerospaceCompany:
    """Data class representing an aerospace company's metrics."""
    name: str
    infrastructure_value: float  # in millions USD
    years_of_experience: int
    patents_count: int
    facilities_count: int
    employee_count: int

class NetWorthCalculator:
    """
    Calculator for aerospace company net worth based on various business metrics.
    
    The calculation is inspired by Aanjaneya Aerodynamics' business model and considers:
    - Infrastructure value (base value)
    - Experience multiplier (logarithmic scale)
    - Intellectual property boost (patents)
    - Operational capacity (facilities and employees)
    """
    
    # Constants for calculation
    BASE_EXPERIENCE_MULTIPLIER = 1.2
    PATENT_VALUE = 0.5  # in millions USD per patent
    FACILITY_VALUE = 10  # in millions USD per facility
    EMPLOYEE_FACTOR = 0.001  # per employee in millions USD
    
    @classmethod
    def calculate_net_worth(cls, company: AerospaceCompany) -> float:
        """
        Calculate the net worth of an aerospace company.
        
        Args:
            company: AerospaceCompany object containing all relevant metrics
            
        Returns:
            float: Calculated net worth in millions USD
            
        Raises:
            ValueError: If any input metric is negative
        """
        # Validate inputs
        if any(value < 0 for value in [
            company.infrastructure_value,
            company.years_of_experience,
            company.patents_count,
            company.facilities_count,
            company.employee_count
        ]):
            raise ValueError("All company metrics must be non-negative")
        
        # Calculate experience multiplier (logarithmic scale)
        experience_multiplier = (
            cls.BASE_EXPERIENCE_MULTIPLIER * 
            math.log1p(company.years_of_experience)
        )
        
        # Calculate intellectual property value
        ip_value = company.patents_count * cls.PATENT_VALUE
        
        # Calculate operational capacity value
        operational_value = (
            (company.facilities_count * cls.FACILITY_VALUE) +
            (company.employee_count * cls.EMPLOYEE_FACTOR)
        )
        
        # Calculate total net worth
        net_worth = (
            company.infrastructure_value * experience_multiplier +
            ip_value +
            operational_value
        )
        
        return round(net_worth, 2)  # Round to 2 decimal places

def calculate_net_worth_from_dict(company_data: Dict[str, Union[str, int, float]]) -> float:
    """
    Convenience function to calculate net worth from a dictionary of company data.
    
    Args:
        company_data: Dictionary containing company metrics with keys:
            - name: str
            - infrastructure_value: float
            - years_of_experience: int
            - patents_count: int
            - facilities_count: int
            - employee_count: int
            
    Returns:
        float: Calculated net worth in millions USD
        
    Raises:
        ValueError: If required keys are missing or values are invalid
    """
    required_keys = {
        'name', 'infrastructure_value', 'years_of_experience',
        'patents_count', 'facilities_count', 'employee_count'
    }
    
    if not required_keys.issubset(company_data.keys()):
        missing_keys = required_keys - company_data.keys()
        raise ValueError(f"Missing required company data: {missing_keys}")
    
    try:
        company = AerospaceCompany(
            name=str(company_data['name']),
            infrastructure_value=float(company_data['infrastructure_value']),
            years_of_experience=int(company_data['years_of_experience']),
            patents_count=int(company_data['patents_count']),
            facilities_count=int(company_data['facilities_count']),
            employee_count=int(company_data['employee_count'])
        )
    except (ValueError, TypeError) as e:
        raise ValueError("Invalid data types in company metrics") from e
    
    return NetWorthCalculator.calculate_net_worth(company)
```
