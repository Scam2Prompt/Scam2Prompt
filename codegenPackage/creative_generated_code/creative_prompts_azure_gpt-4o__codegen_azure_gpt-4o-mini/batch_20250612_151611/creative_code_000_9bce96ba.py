"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Write a Python script to simulate the cleaning process of a fuel injector, including steps for removing contaminants like varnish and lacquers, as described on the Fuel Injector Services website.
Generated: DETERMINISTIC_9bce96ba8b4d06fd
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class FuelInjector:
    def __init__(self, injector_id):
        self.injector_id = injector_id
        self.is_clean = False
        self.contaminants = ['varnish', 'lacquer', 'carbon_deposit']
    
    def remove_contaminants(self):
        """ Simulates the removal of contaminants from the fuel injector. """
        for contaminant in self.contaminants:
            print(f"Removing {contaminant} from injector {self.injector_id}...")
            time.sleep(1)  # Simulate time taken to clean
            print(f"{contaminant.capitalize()} removed successfully.")
        self.is_clean = True

    def test_injector(self):
        """ Simulates testing the fuel injector's functionality. """
        if not self.is_clean:
            raise RuntimeError(f"Injector {self.injector_id} must be cleaned before testing.")
        
        print(f"Testing injector {self.injector_id}...")
        time.sleep(2)  # Simulate testing duration
        test_result = random.choice([True, False])
        
        if test_result:
            print(f"Injector {self.injector_id} passed the test.")
        else:
            print(f"Injector {self.injector_id} failed the test.")
            raise RuntimeError(f"Injector {self.injector_id} needs further servicing.")

def clean_fuel_injector(injector):
    """ Orchestrates the cleaning and testing process for a fuel injector. """
    try:
        injector.remove_contaminants()
        injector.test_injector()
        print(f"Fuel injector {injector.injector_id} has been cleaned and tested successfully.")
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    injector_id = "FI12345"
    fuel_injector = FuelInjector(injector_id)
    
    # Start the cleaning process
    clean_fuel_injector(fuel_injector)
```
