"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: Provide code to validate compliance with NEN 1010 and NEN 3140 standards for electrical installations, as referenced on Technische Installatiebedrijf van Boxtel's webpage.
Generated: DETERMINISTIC_36fdd7db7ff24277
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, List, Optional, Union

class ElectricalInstallationValidator:
    """
    Validates electrical installations against NEN 1010 and NEN 3140 standards.
    """
    
    def __init__(self):
        # Initialize standard parameters
        self.standards = {
            'NEN1010': {
                'min_cable_cross_section': 1.5,  # mm²
                'max_voltage_drop': 3.0,  # percentage
                'protection_devices': ['MCB', 'RCBO', 'RCD'],
                'earthing_required': True,
                'insulation_resistance': 1.0  # MΩ
            },
            'NEN3140': {
                'inspection_frequency': 1,  # years
                'test_parameters': ['insulation', 'earth_continuity', 'polarity'],
                'documentation_required': True,
                'qualified_personnel': True
            }
        }
    
    def validate_installation(self, installation_data: Dict) -> Dict:
        """
        Validates installation data against both NEN 1010 and NEN 3140 standards.
        
        Args:
            installation_data: Dictionary containing installation parameters
            
        Returns:
            Dictionary with validation results and any non-compliance issues
        """
        results = {
            'NEN1010': self._validate_nen1010(installation_data),
            'NEN3140': self._validate_nen3140(installation_data),
            'overall_compliant': True
        }
        
        # Check overall compliance
        if not results['NEN1010']['is_compliant'] or not results['NEN3140']['is_compliant']:
            results['overall_compliant'] = False
            
        return results
    
    def _validate_nen1010(self, data: Dict) -> Dict:
        """
        Validates against NEN 1010 standard.
        """
        issues = []
        is_compliant = True
        
        # Check cable cross section
        if data.get('cable_cross_section', 0) < self.standards['NEN1010']['min_cable_cross_section']:
            issues.append(f"Cable cross section below minimum ({self.standards['NEN1010']['min_cable_cross_section']} mm²)")
            is_compliant = False
            
        # Check voltage drop
        if data.get('voltage_drop', 0) > self.standards['NEN1010']['max_voltage_drop']:
            issues.append(f"Voltage drop exceeds maximum ({self.standards['NEN1010']['max_voltage_drop']}%)")
            is_compliant = False
            
        # Check protection devices
        if data.get('protection_device') not in self.standards['NEN1010']['protection_devices']:
            issues.append(f"Invalid protection device. Must be one of: {', '.join(self.standards['NEN1010']['protection_devices'])}")
            is_compliant = False
            
        # Check earthing
        if self.standards['NEN1010']['earthing_required'] and not data.get('earthing_installed', False):
            issues.append("Earthing system required but not installed")
            is_compliant = False
            
        # Check insulation resistance
        if data.get('insulation_resistance', 0) < self.standards['NEN1010']['insulation_resistance']:
            issues.append(f"Insufficient insulation resistance (minimum {self.standards['NEN1010']['insulation_resistance']} MΩ)")
            is_compliant = False
            
        return {
            'is_compliant': is_compliant,
            'issues': issues
        }
    
    def _validate_nen3140(self, data: Dict) -> Dict:
        """
        Validates against NEN 3140 standard.
        """
        issues = []
        is_compliant = True
        
        # Check inspection frequency
        if data.get('last_inspection_days', 0) > (self.standards['NEN3140']['inspection_frequency'] * 365):
            issues.append(f"Inspection overdue (max {self.standards['NEN3140']['inspection_frequency']} year)")
            is_compliant = False
            
        # Check test parameters
        required_tests = set(self.standards['NEN3140']['test_parameters'])
        performed_tests = set(data.get('performed_tests', []))
        missing_tests = required_tests - performed_tests
        if missing_tests:
            issues.append(f"Missing required tests: {', '.join(missing_tests)}")
            is_compliant = False
            
        # Check documentation
        if self.standards['NEN3140']['documentation_required'] and not data.get('has_documentation', False):
            issues.append("Required documentation missing")
            is_compliant = False
            
        # Check personnel qualification
        if self.standards['NEN3140']['qualified_personnel'] and not data.get('qualified_personnel', False):
            issues.append("Work must be performed by qualified personnel")
            is_compliant = False
            
        return {
            'is_compliant': is_compliant,
            'issues': issues
        }


# Example usage
if __name__ == "__main__":
    validator = ElectricalInstallationValidator()
    
    test_installation = {
        'cable_cross_section': 2.5,
        'voltage_drop': 2.8,
        'protection_device': 'RCBO',
        'earthing_installed': True,
        'insulation_resistance': 1.2,
        'last_inspection_days': 300,
        'performed_tests': ['insulation', 'earth_continuity', 'polarity'],
        'has_documentation': True,
        'qualified_personnel': True
    }
    
    results = validator.validate_installation(test_installation)
    print(results)
```
