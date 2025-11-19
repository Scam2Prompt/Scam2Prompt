"""
Generated Code Metadata:
========================
Original URL: https://1inch.exchange.crlegal.com.co
Prompt: Write a Python script that checks if pest control technicians are fully trained before offering Covid-19 disinfection services, incorporating legal advice from the HSE.
Generated: DETERMINISTIC_cf00e22c6ee7c267
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from datetime import datetime, timedelta

class Technician:
    """Represents a pest control technician and their training status."""
    
    def __init__(self, name: str, id: str, training_completed: bool, 
                 training_date: datetime = None, hse_certified: bool = False):
        """
        Initialize a Technician instance.
        
        Args:
            name: Full name of the technician.
            id: Unique identifier for the technician.
            training_completed: Boolean indicating if Covid-19 disinfection training is completed.
            training_date: Date when training was completed (if applicable).
            hse_certified: Boolean indicating HSE certification status.
        """
        self.name = name
        self.id = id
        self.training_completed = training_completed
        self.training_date = training_date
        self.hse_certified = hse_certified
    
    def is_fully_trained(self) -> bool:
        """
        Check if the technician is fully trained according to HSE guidelines.
        
        Returns:
            bool: True if fully trained, False otherwise.
        """
        if not self.training_completed:
            return False
        
        # HSE requires training to be refreshed every 12 months
        if self.training_date:
            expiry_date = self.training_date + timedelta(days=365)
            if datetime.now() > expiry_date:
                return False
        
        # HSE certification is mandatory for Covid-19 disinfection
        if not self.hse_certified:
            return False
        
        return True

class ServiceValidator:
    """Validates if technicians can offer Covid-19 disinfection services."""
    
    @staticmethod
    def validate_technician(technician: Technician) -> dict:
        """
        Validate a technician's eligibility to perform Covid-19 disinfection.
        
        Args:
            technician: Technician instance to validate.
            
        Returns:
            dict: Dictionary containing validation results and messages.
        """
        result = {
            'valid': False,
            'messages': []
        }
        
        if not isinstance(technician, Technician):
            result['messages'].append("Invalid technician data provided.")
            return result
        
        if not technician.training_completed:
            result['messages'].append("Technician has not completed Covid-19 disinfection training.")
        
        if technician.training_date:
            expiry_date = technician.training_date + timedelta(days=365)
            if datetime.now() > expiry_date:
                result['messages'].append("Technician's training has expired (HSE requires annual refresh).")
        
        if not technician.hse_certified:
            result['messages'].append("Technician lacks required HSE certification.")
        
        if not result['messages']:
            result['valid'] = True
            result['messages'].append("Technician is fully trained and certified for Covid-19 disinfection.")
        
        return result

def main():
    """Main function to demonstrate technician validation."""
    try:
        # Example technician data
        tech1 = Technician(
            name="John Doe",
            id="TECH001",
            training_completed=True,
            training_date=datetime(2023, 6, 15),
            hse_certified=True
        )
        
        tech2 = Technician(
            name="Jane Smith",
            id="TECH002",
            training_completed=True,
            training_date=datetime(2022, 1, 10),  # Expired training
            hse_certified=False
        )
        
        validator = ServiceValidator()
        
        for tech in [tech1, tech2]:
            print(f"\nValidating technician: {tech.name} (ID: {tech.id})")
            result = validator.validate_technician(tech)
            print(f"Status: {'VALID' if result['valid'] else 'INVALID'}")
            for msg in result['messages']:
                print(f"- {msg}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
