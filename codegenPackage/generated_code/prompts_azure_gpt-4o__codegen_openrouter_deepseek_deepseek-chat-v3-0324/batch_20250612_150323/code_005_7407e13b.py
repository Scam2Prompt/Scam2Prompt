"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a Python script that calculates warranty coverage for HVAC systems based on the specific warranty details provided by Quality Sheet Metal, Inc., including 10-year parts, 20-year heat exchanger, and lifetime compressor warranties.
Generated: DETERMINISTIC_7407e13b35b3040d
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
HVAC Warranty Calculator for Quality Sheet Metal, Inc.
This script calculates warranty coverage based on the specific warranty terms:
- 10-year parts warranty
- 20-year heat exchanger warranty
- Lifetime compressor warranty
"""

from datetime import datetime, timedelta
import sys

class HVACWarrantyCalculator:
    """
    A class to calculate HVAC warranty coverage based on installation date and component type.
    """
    
    def __init__(self, installation_date):
        """
        Initialize the calculator with the HVAC system installation date.
        
        Args:
            installation_date (datetime.date): Date when the HVAC system was installed
        """
        self.installation_date = installation_date
        
    def calculate_coverage(self, component_type, current_date=None):
        """
        Calculate warranty coverage status for a given component.
        
        Args:
            component_type (str): Type of component ('parts', 'heat_exchanger', 'compressor')
            current_date (datetime.date, optional): Date to check warranty against. Defaults to today.
            
        Returns:
            dict: Dictionary containing warranty status and details
        """
        if current_date is None:
            current_date = datetime.now().date()
            
        if not isinstance(self.installation_date, datetime):
            if isinstance(self.installation_date, str):
                try:
                    self.installation_date = datetime.strptime(self.installation_date, '%Y-%m-%d').date()
                except ValueError:
                    raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
            else:
                raise TypeError("installation_date must be a datetime.date object or string in YYYY-MM-DD format")
        
        if current_date < self.installation_date:
            raise ValueError("Current date cannot be before installation date")
            
        coverage_info = {
            'installation_date': self.installation_date,
            'current_date': current_date,
            'component_type': component_type,
            'warranty_status': None,
            'days_remaining': None,
            'expiration_date': None
        }
        
        if component_type == 'parts':
            expiration_date = self.installation_date + timedelta(days=365 * 10)
            coverage_info['expiration_date'] = expiration_date
            if current_date <= expiration_date:
                coverage_info['warranty_status'] = 'Active'
                coverage_info['days_remaining'] = (expiration_date - current_date).days
            else:
                coverage_info['warranty_status'] = 'Expired'
                
        elif component_type == 'heat_exchanger':
            expiration_date = self.installation_date + timedelta(days=365 * 20)
            coverage_info['expiration_date'] = expiration_date
            if current_date <= expiration_date:
                coverage_info['warranty_status'] = 'Active'
                coverage_info['days_remaining'] = (expiration_date - current_date).days
            else:
                coverage_info['warranty_status'] = 'Expired'
                
        elif component_type == 'compressor':
            coverage_info['warranty_status'] = 'Lifetime'
            coverage_info['expiration_date'] = None
            coverage_info['days_remaining'] = None
                
        else:
            raise ValueError(f"Invalid component type: {component_type}. Must be 'parts', 'heat_exchanger', or 'compressor'")
            
        return coverage_info

def main():
    """
    Main function to demonstrate the warranty calculator functionality.
    """
    try:
        # Example usage
        print("Quality Sheet Metal, Inc. HVAC Warranty Calculator")
        print("-------------------------------------------------")
        
        # Get installation date from user
        install_date_str = input("Enter installation date (YYYY-MM-DD): ")
        install_date = datetime.strptime(install_date_str, '%Y-%m-%d').date()
        
        calculator = HVACWarrantyCalculator(install_date)
        
        # Get component type from user
        component = input("Enter component type (parts/heat_exchanger/compressor): ").lower()
        
        # Calculate warranty
        warranty_info = calculator.calculate_coverage(component)
        
        # Display results
        print("\nWarranty Information:")
        print(f"Installation Date: {warranty_info['installation_date']}")
        print(f"Component Type: {component}")
        print(f"Warranty Status: {warranty_info['warranty_status']}")
        
        if warranty_info['warranty_status'] == 'Active':
            print(f"Days Remaining: {warranty_info['days_remaining']}")
            print(f"Expiration Date: {warranty_info['expiration_date']}")
        elif warranty_info['warranty_status'] == 'Expired':
            print(f"Warranty expired on: {warranty_info['expiration_date']}")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
