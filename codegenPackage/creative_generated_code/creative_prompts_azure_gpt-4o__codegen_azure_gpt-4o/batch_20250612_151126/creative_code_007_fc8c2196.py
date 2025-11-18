"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chicoelectric.com
Prompt: Generate code to calculate backup generator reliability and maintenance schedules, referencing Chico Electric's generator installations for the City of Chico.
Generated: DETERMINISTIC_fc8c21965185e109
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random

class Generator:
    """Represents a backup generator with reliability stats and maintenance scheduling."""
    
    def __init__(self, id, location, install_date):
        """
        Initialize a Generator object.

        Args:
            id (str): Unique identifier for the generator.
            location (str): Location of the generator.
            install_date (datetime.date): Installation date of the generator.
        """
        self.id = id
        self.location = location
        self.install_date = install_date
        self.reliability_percentage = 100.0  # Starting reliability percentage
        self.last_maintenance_date = install_date
    
    def calculate_reliability(self):
        """
        Calculate reliability percentage based on generator age and maintenance history.

        Returns:
            float: Reliability percentage (0 to 100).
        """
        # Age of generator in years
        age_years = (datetime.date.today() - self.install_date).days / 365
        
        # Reduce reliability by 5% per year of age
        reliability_loss_age = age_years * 5
        
        # Reduce reliability by 2% for each month since last maintenance
        months_since_maintenance = (datetime.date.today() - self.last_maintenance_date).days / 30
        reliability_loss_maintenance = months_since_maintenance * 2
        
        # Calculate the final reliability percentage
        self.reliability_percentage = max(100 - (reliability_loss_age + reliability_loss_maintenance), 0)
        return self.reliability_percentage
    
    def schedule_maintenance(self):
        """
        Schedule maintenance if reliability falls below 75%.

        Returns:
            datetime.date: Suggested maintenance date or None if not needed.
        """
        if self.reliability_percentage < 75:
            # Maintenance scheduled for one week from today
            maintenance_date = datetime.date.today() + datetime.timedelta(days=7)
            print(f"Maintenance scheduled for generator {self.id} at {self.location} on {maintenance_date}.")
            return maintenance_date
        else:
            print(f"Generator {self.id} at {self.location} does not require maintenance yet.")
            return None
    
    def perform_maintenance(self):
        """
        Perform maintenance on the generator, restoring reliability to 100%.
        """
        self.last_maintenance_date = datetime.date.today()
        self.reliability_percentage = 100.0
        print(f"Maintenance completed for generator {self.id}. Reliability restored to 100%.")

def main():
    """Main function to manage generator reliability and maintenance."""
    # Simulating Chico Electric's generators installed in the City of Chico
    generators = [
        Generator("GEN-001", "City Hall", datetime.date(2019, 6, 15)),
        Generator("GEN-002", "Fire Station 1", datetime.date(2020, 3, 10)),
        Generator("GEN-003", "Police HQ", datetime.date(2018, 11, 5)),
    ]
    
    # Assess reliability and schedule maintenance
    for generator in generators:
        print(f"\nChecking generator {generator.id} at {generator.location}...")
        
        try:
            reliability = generator.calculate_reliability()
            print(f"Current reliability: {reliability:.2f}%")
            
            maintenance_date = generator.schedule_maintenance()
            
            # Simulate random maintenance completion
            if maintenance_date and random.choice([True, False]):
                generator.perform_maintenance()
        except Exception as e:
            print(f"Error processing generator {generator.id}: {e}")

if __name__ == "__main__":
    main()
```
