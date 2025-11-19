"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: "Generate a Python script to calculate estimates for plumbing and heating services based on customer input, similar to Flammedeauinc's 3-step process for service requests."
Generated: DETERMINISTIC_3d32091e87611c75
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class ServiceEstimator:
    def __init__(self):
        self.services = {
            'plumbing': {
                'leak_repair': 150,
                'pipe_installation': 300,
                'drain_cleaning': 100
            },
            'heating': {
                'furnace_repair': 200,
                'boiler_installation': 500,
                'thermostat_installation': 150
            }
        }

    def display_services(self):
        """Display available services and their costs."""
        print("Available Services:")
        for category, services in self.services.items():
            print(f"\n{category.capitalize()} Services:")
            for service, cost in services.items():
                print(f" - {service.replace('_', ' ').capitalize()}: ${cost}")

    def get_service_estimate(self, category, service):
        """Calculate the estimate for a given service."""
        try:
            return self.services[category][service]
        except KeyError:
            raise ValueError("Invalid service category or service name.")

    def main(self):
        """Main method to run the service estimator."""
        self.display_services()
        
        # Step 1: Get service category from user
        category = input("\nEnter the service category (plumbing/heating): ").strip().lower()
        
        # Step 2: Get specific service from user
        service = input(f"Enter the specific service from {category} services: ").strip().lower().replace(' ', '_')

        # Step 3: Calculate and display the estimate
        try:
            estimate = self.get_service_estimate(category, service)
            print(f"\nEstimated cost for {service.replace('_', ' ')} in {category} is: ${estimate}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    estimator = ServiceEstimator()
    estimator.main()
```
