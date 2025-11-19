"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Generate a Python script that automates the process of calculating taxes based on the courses offered in the "Impuesto a la renta" category at AulaContable.
Generated: DETERMINISTIC_03baf2ada5910c0f
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass

@dataclass
class Course:
    """Represents a course with its price and tax category."""
    name: str
    price: float
    tax_category: str

class TaxCalculator:
    """Handles tax calculations for courses based on tax categories."""
    
    def __init__(self, tax_rates: Dict[str, float]):
        """
        Initialize the TaxCalculator with tax rates for different categories.
        
        Args:
            tax_rates: Dictionary mapping tax categories to their respective rates.
        """
        self.tax_rates = tax_rates
    
    def calculate_tax(self, course: Course) -> float:
        """
        Calculate the tax for a given course based on its tax category.
        
        Args:
            course: Course object for which tax will be calculated.
        
        Returns:
            float: Calculated tax amount.
            
        Raises:
            ValueError: If the course's tax category is not recognized.
        """
        if course.tax_category not in self.tax_rates:
            raise ValueError(f"Unknown tax category: {course.tax_category}")
        return course.price * self.tax_rates[course.tax_category]
    
    def calculate_total(self, courses: List[Course]) -> Dict[str, Union[float, Dict[str, float]]]:
        """
        Calculate total tax and breakdown per category for a list of courses.
        
        Args:
            courses: List of Course objects to process.
            
        Returns:
            Dictionary containing:
                - 'total_tax': Sum of all taxes
                - 'breakdown': Dictionary of taxes per category
        """
        breakdown = {category: 0.0 for category in self.tax_rates}
        total_tax = 0.0
        
        for course in courses:
            try:
                tax = self.calculate_tax(course)
                breakdown[course.tax_category] += tax
                total_tax += tax
            except ValueError as e:
                print(f"Warning: {e}. Skipping course '{course.name}'.")
        
        return {
            'total_tax': total_tax,
            'breakdown': breakdown
        }

class AulaContableAPI:
    """Mock class to simulate fetching courses from AulaContable."""
    
    @staticmethod
    def fetch_courses() -> List[Dict[str, Union[str, float]]]:
        """
        Mock method to fetch courses from AulaContable.
        
        Returns:
            List of dictionaries with course information.
        """
        # In a real implementation, this would make an API call
        return [
            {"name": "Fundamentos Contables", "price": 100.0, "tax_category": "standard"},
            {"name": "Impuesto a la Renta", "price": 150.0, "tax_category": "renta"},
            {"name": "IVA Avanzado", "price": 120.0, "tax_category": "iva"},
            {"name": "Contabilidad Internacional", "price": 200.0, "tax_category": "standard"}
        ]

def load_config(file_path: str = "config.json") -> Dict[str, float]:
    """
    Load tax rates configuration from a JSON file.
    
    Args:
        file_path: Path to the configuration file.
        
    Returns:
        Dictionary of tax rates.
        
    Raises:
        FileNotFoundError: If config file doesn't exist.
        json.JSONDecodeError: If config file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Config file not found at {file_path}")
        raise
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in config file at {file_path}")
        raise

def main():
    """Main execution function."""
    try:
        # Load tax configuration
        tax_rates = load_config()
        
        # Initialize calculator
        calculator = TaxCalculator(tax_rates)
        
        # Fetch courses
        course_data = AulaContableAPI.fetch_courses()
        courses = [Course(**data) for data in course_data]
        
        # Calculate taxes
        results = calculator.calculate_total(courses)
        
        # Print results
        print("\nTax Calculation Results:")
        print(f"Total Tax: ${results['total_tax']:.2f}")
        print("\nBreakdown by Category:")
        for category, amount in results['breakdown'].items():
            print(f"{category.capitalize()}: ${amount:.2f}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
```
