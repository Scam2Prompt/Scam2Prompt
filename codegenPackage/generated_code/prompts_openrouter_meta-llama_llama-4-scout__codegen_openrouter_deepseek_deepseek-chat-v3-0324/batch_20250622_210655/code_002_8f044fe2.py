"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: Generate a code snippet to calculate the migration testing requirements for a food contact material, such as paperboard or glassware, under UK/EU testing regulations.
Generated: DETERMINISTIC_8f044fe29caec262
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# food_contact_material_migration.py

from typing import Dict, List, Optional, Union
import math

class MigrationTestingCalculator:
    """
    Calculates migration testing requirements for food contact materials (FCM)
    under UK/EU regulations (EU 10/2011, UK SI 2019 No. 1343).
    """
    
    # Typical food simulants based on EU 10/2011 Annex III
    FOOD_SIMULANTS = {
        'A': 'Ethanol 10% (v/v)',
        'B': 'Ethanol 3% (v/v)',
        'C': 'Acetic acid 3% (w/v)',
        'D1': 'Vegetable oil',
        'D2': 'Alternative fat simulant (e.g., ethanol 95%)',
        'E': 'Poly(2,6-diphenyl-p-phenylene oxide)'
    }
    
    # Typical migration limits in mg/kg
    MIGRATION_LIMITS = {
        'overall': 10,          # Overall migration limit (OML)
        'specific': {
            'plastic': 60,      # Example specific migration limit for plastics
            'paper': 0.1,       # Example specific migration limit for paper
            'glass': 0.01       # Example specific migration limit for glass
        }
    }
    
    def __init__(self, material_type: str, contact_surface_area: float, volume: float):
        """
        Initialize the calculator with material properties.
        
        Args:
            material_type: Type of material ('plastic', 'paper', 'glass', etc.)
            contact_surface_area: Contact surface area in dm²
            volume: Volume of food in contact in L
        """
        self.material_type = material_type.lower()
        self.contact_surface_area = contact_surface_area
        self.volume = volume
        
        if self.material_type not in self.MIGRATION_LIMITS['specific']:
            raise ValueError(f"Unsupported material type: {material_type}")
    
    def calculate_specific_migration_limit(self) -> float:
        """
        Calculate the specific migration limit (SML) for the material.
        
        Returns:
            Specific migration limit in mg/kg
        """
        return self.MIGRATION_LIMITS['specific'][self.material_type]
    
    def calculate_overall_migration_limit(self) -> float:
        """
        Calculate the overall migration limit (OML).
        
        Returns:
            Overall migration limit in mg/dm²
        """
        return self.MIGRATION_LIMITS['overall']
    
    def calculate_test_requirements(self, 
                                  test_type: str = 'specific',
                                  temperature: float = 40.0,
                                  duration: float = 10.0) -> Dict[str, Union[float, str, List[str]]]:
        """
        Calculate migration testing requirements.
        
        Args:
            test_type: Type of test ('specific' or 'overall')
            temperature: Test temperature in °C
            duration: Test duration in days
            
        Returns:
            Dictionary containing test requirements
        """
        if test_type not in ['specific', 'overall']:
            raise ValueError("Test type must be 'specific' or 'overall'")
        
        requirements = {
            'material_type': self.material_type,
            'contact_surface_area_dm2': self.contact_surface_area,
            'food_volume_l': self.volume,
            'test_type': test_type,
            'temperature_c': temperature,
            'duration_days': duration,
            'recommended_simulants': self._get_recommended_simulants(),
            'test_conditions': self._get_test_conditions(temperature, duration)
        }
        
        if test_type == 'specific':
            requirements['migration_limit'] = self.calculate_specific_migration_limit()
        else:
            requirements['migration_limit'] = self.calculate_overall_migration_limit()
        
        return requirements
    
    def _get_recommended_simulants(self) -> List[str]:
        """
        Get recommended food simulants based on material type.
        
        Returns:
            List of recommended simulants
        """
        if self.material_type == 'plastic':
            return [self.FOOD_SIMULANTS['A'], self.FOOD_SIMULANTS['D1']]
        elif self.material_type == 'paper':
            return [self.FOOD_SIMULANTS['B'], self.FOOD_SIMULANTS['C']]
        elif self.material_type == 'glass':
            return [self.FOOD_SIMULANTS['A']]
        else:
            return []
    
    def _get_test_conditions(self, temperature: float, duration: float) -> Dict[str, str]:
        """
        Get standard test conditions based on temperature and duration.
        
        Args:
            temperature: Test temperature in °C
            duration: Test duration in days
            
        Returns:
            Dictionary of test conditions
        """
        conditions = {
            'standard': f"{temperature}°C for {duration} days",
            'accelerated': f"{temperature + 10}°C for {duration / 2} days" if temperature < 100 else "Not recommended"
        }
        return conditions
    
    def validate_migration_results(self, 
                                 test_type: str,
                                 measured_value: float) -> Dict[str, Union[bool, str, float]]:
        """
        Validate migration test results against regulatory limits.
        
        Args:
            test_type: Type of test ('specific' or 'overall')
            measured_value: Measured migration value
            
        Returns:
            Dictionary with validation results
        """
        if test_type == 'specific':
            limit = self.calculate_specific_migration_limit()
        elif test_type == 'overall':
            limit = self.calculate_overall_migration_limit()
        else:
            raise ValueError("Test type must be 'specific' or 'overall'")
        
        return {
            'test_type': test_type,
            'measured_value': measured_value,
            'limit': limit,
            'is_compliant': measured_value <= limit,
            'compliance_status': 'Compliant' if measured_value <= limit else 'Non-compliant'
        }

# Example usage
if __name__ == "__main__":
    try:
        # Example for paperboard material
        paperboard_calculator = MigrationTestingCalculator(
            material_type='paper',
            contact_surface_area=6.0,
            volume=1.0
        )
        
        requirements = paperboard_calculator.calculate_test_requirements()
        print("Migration Testing Requirements:")
        for key, value in requirements.items():
            print(f"{key}: {value}")
        
        # Validate test results
        validation = paperboard_calculator.validate_migration_results(
            test_type='specific',
            measured_value=0.08
        )
        print("\nValidation Results:")
        for key, value in validation.items():
            print(f"{key}: {value}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
