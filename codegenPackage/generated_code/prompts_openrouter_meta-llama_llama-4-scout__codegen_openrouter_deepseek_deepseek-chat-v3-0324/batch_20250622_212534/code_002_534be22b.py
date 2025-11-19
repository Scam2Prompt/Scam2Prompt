"""
Generated Code Metadata:
========================
Original URL: https://getsonicsolutions.com
Prompt: "Generate a case study on the application of ultrasonic cleaning for removing grease and scale from industrial equipment, using examples from Sonic Solutions Ltd."
Generated: DETERMINISTIC_534be22bd13e82ed
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study: Ultrasonic Cleaning Application for Industrial Equipment
Company: Sonic Solutions Ltd.
Objective: Demonstrate effectiveness of ultrasonic cleaning for grease and scale removal
"""

import json
from datetime import datetime
from typing import List, Dict, Optional

class CleaningCaseStudy:
    """
    Represents a case study of ultrasonic cleaning application.
    """
    
    def __init__(self, company: str, equipment_type: str, contaminant_type: str):
        """
        Initialize a cleaning case study.
        
        Args:
            company: Name of the company where cleaning was performed
            equipment_type: Type of industrial equipment cleaned
            contaminant_type: Type of contaminant removed (grease, scale, etc.)
        """
        self.company = company
        self.equipment_type = equipment_type
        self.contaminant_type = contaminant_type
        self.cleaning_date = datetime.now().strftime("%Y-%m-%d")
        self.results = {
            'before_cleaning': None,
            'after_cleaning': None,
            'efficiency': None
        }
        self.parameters = {
            'frequency': None,
            'temperature': None,
            'duration': None,
            'cleaning_solution': None
        }
        self.equipment_details = {
            'material': None,
            'age': None,
            'condition': None
        }
    
    def set_cleaning_parameters(self, frequency: float, temperature: float, 
                              duration: float, solution: str) -> None:
        """
        Set the ultrasonic cleaning parameters.
        
        Args:
            frequency: Ultrasonic frequency in kHz
            temperature: Solution temperature in °C
            duration: Cleaning duration in minutes
            solution: Cleaning solution used
        """
        self.parameters['frequency'] = frequency
        self.parameters['temperature'] = temperature
        self.parameters['duration'] = duration
        self.parameters['cleaning_solution'] = solution
    
    def set_equipment_details(self, material: str, age: int, condition: str) -> None:
        """
        Set details about the equipment being cleaned.
        
        Args:
            material: Equipment material composition
            age: Age of equipment in years
            condition: General condition before cleaning
        """
        self.equipment_details['material'] = material
        self.equipment_details['age'] = age
        self.equipment_details['condition'] = condition
    
    def record_results(self, before: Dict[str, float], after: Dict[str, float]) -> None:
        """
        Record cleaning results with before/after measurements.
        
        Args:
            before: Dictionary of measurements before cleaning
            after: Dictionary of measurements after cleaning
        """
        self.results['before_cleaning'] = before
        self.results['after_cleaning'] = after
        self._calculate_efficiency(before, after)
    
    def _calculate_efficiency(self, before: Dict[str, float], after: Dict[str, float]) -> None:
        """
        Calculate cleaning efficiency based on before/after measurements.
        
        Args:
            before: Pre-cleaning measurements
            after: Post-cleaning measurements
        """
        try:
            if 'contaminant_level' in before and 'contaminant_level' in after:
                reduction = before['contaminant_level'] - after['contaminant_level']
                self.results['efficiency'] = (reduction / before['contaminant_level']) * 100
        except (KeyError, TypeError, ZeroDivisionError) as e:
            print(f"Error calculating efficiency: {e}")
            self.results['efficiency'] = None
    
    def generate_report(self) -> Dict:
        """
        Generate a comprehensive report of the case study.
        
        Returns:
            Dictionary containing all case study data
        """
        return {
            'company': self.company,
            'study_date': self.cleaning_date,
            'equipment': {
                'type': self.equipment_type,
                'details': self.equipment_details
            },
            'contaminant': self.contaminant_type,
            'cleaning_parameters': self.parameters,
            'results': self.results
        }
    
    def save_to_json(self, filename: str) -> bool:
        """
        Save case study to JSON file.
        
        Args:
            filename: Name of file to save to
            
        Returns:
            True if save successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.generate_report(), f, indent=4)
            return True
        except (IOError, json.JSONEncodeError) as e:
            print(f"Error saving case study: {e}")
            return False

# Example usage for Sonic Solutions Ltd.
def create_sonic_solutions_case_study() -> CleaningCaseStudy:
    """
    Create a case study example for Sonic Solutions Ltd.
    
    Returns:
        Configured CleaningCaseStudy instance
    """
    case_study = CleaningCaseStudy(
        company="Sonic Solutions Ltd.",
        equipment_type="Heat Exchanger Plates",
        contaminant_type="Grease and Mineral Scale"
    )
    
    # Set equipment details
    case_study.set_equipment_details(
        material="Stainless Steel 316",
        age=5,
        condition="Heavy buildup, reduced efficiency"
    )
    
    # Set cleaning parameters
    case_study.set_cleaning_parameters(
        frequency=40.0,  # kHz
        temperature=60.0,  # °C
        duration=20.0,  # minutes
        solution="Alkaline detergent with chelating agents"
    )
    
    # Record results
    case_study.record_results(
        before={'contaminant_level': 85.2, 'thickness_mm': 2.1},
        after={'contaminant_level': 3.7, 'thickness_mm': 0.1}
    )
    
    return case_study

if __name__ == "__main__":
    # Generate and save case study
    sonic_case = create_sonic_solutions_case_study()
    report = sonic_case.generate_report()
    print("Case Study Summary:")
    print(json.dumps(report, indent=2))
    
    # Save to file
    if sonic_case.save_to_json("sonic_solutions_case_study.json"):
        print("Case study saved successfully.")
    else:
        print("Failed to save case study.")
```
