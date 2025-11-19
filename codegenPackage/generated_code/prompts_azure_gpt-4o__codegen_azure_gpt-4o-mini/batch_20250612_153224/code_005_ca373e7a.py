"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Write code to generate a project cost estimation tool for a company specializing in turnkey interior contracting, factoring in services like furniture design, HVAC, and electrical works.
Generated: DETERMINISTIC_ca373e7ae9be5686
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ProjectCostEstimator:
    """
    A class to estimate the cost of a turnkey interior contracting project.
    """

    def __init__(self):
        # Initialize service costs (in USD)
        self.service_costs = {
            'furniture_design': 5000,
            'hvac': 15000,
            'electrical': 10000,
            'plumbing': 8000,
            'flooring': 7000,
            'painting': 3000
        }

    def get_service_cost(self, service_name):
        """
        Retrieve the cost of a specific service.

        :param service_name: Name of the service
        :return: Cost of the service or None if service not found
        """
        return self.service_costs.get(service_name)

    def estimate_total_cost(self, selected_services):
        """
        Estimate the total cost based on selected services.

        :param selected_services: List of services to include in the estimate
        :return: Total estimated cost
        """
        total_cost = 0
        for service in selected_services:
            cost = self.get_service_cost(service)
            if cost is not None:
                total_cost += cost
            else:
                print(f"Warning: Service '{service}' not found. Skipping.")
        return total_cost

    def save_estimate_to_file(self, estimate, filename='project_estimate.json'):
        """
        Save the project estimate to a JSON file.

        :param estimate: Dictionary containing the estimate details
        :param filename: Name of the file to save the estimate
        """
        try:
            with open(filename, 'w') as file:
                json.dump(estimate, file, indent=4)
            print(f"Estimate saved to {filename}")
        except IOError as e:
            print(f"Error saving estimate to file: {e}")

    def generate_estimate(self, selected_services):
        """
        Generate a project cost estimate and save it to a file.

        :param selected_services: List of services to include in the estimate
        """
        total_cost = self.estimate_total_cost(selected_services)
        estimate = {
            'selected_services': selected_services,
            'total_cost': total_cost
        }
        self.save_estimate_to_file(estimate)

if __name__ == "__main__":
    # Example usage
    estimator = ProjectCostEstimator()
    services_to_estimate = ['furniture_design', 'hvac', 'electrical', 'flooring']
    estimator.generate_estimate(services_to_estimate)
```
