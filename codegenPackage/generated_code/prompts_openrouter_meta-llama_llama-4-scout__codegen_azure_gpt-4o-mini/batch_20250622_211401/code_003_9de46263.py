"""
Generated Code Metadata:
========================
Original URL: https://optimisenow.net
Prompt: "Design a workflow optimization strategy for a company looking to outsource key business functions to specialized service providers using business process outsourcing (BPO)."
Generated: DETERMINISTIC_9de4626390bdd74d
Batch ID: 20250622_211401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class BPOServiceProvider:
    """Class representing a BPO service provider."""
    
    def __init__(self, name: str, services: List[str], rating: float):
        self.name = name
        self.services = services
        self.rating = rating

    def __repr__(self):
        return f"BPOServiceProvider(name={self.name}, services={self.services}, rating={self.rating})"


class WorkflowOptimizer:
    """Class to optimize workflows for outsourcing business functions."""
    
    def __init__(self, service_providers: List[BPOServiceProvider]):
        self.service_providers = service_providers

    def find_best_provider(self, required_services: List[str]) -> BPOServiceProvider:
        """Find the best service provider based on required services and rating."""
        best_provider = None
        highest_rating = 0.0
        
        for provider in self.service_providers:
            if all(service in provider.services for service in required_services):
                if provider.rating > highest_rating:
                    highest_rating = provider.rating
                    best_provider = provider
        
        if best_provider is None:
            raise ValueError("No suitable service provider found for the required services.")
        
        return best_provider

    def optimize_workflow(self, business_functions: Dict[str, List[str]]) -> Dict[str, Any]:
        """Optimize the workflow by outsourcing business functions to the best providers."""
        optimized_workflow = {}
        
        for function, services in business_functions.items():
            try:
                best_provider = self.find_best_provider(services)
                optimized_workflow[function] = {
                    "provider": best_provider.name,
                    "services": best_provider.services,
                    "rating": best_provider.rating
                }
            except ValueError as e:
                optimized_workflow[function] = {
                    "error": str(e)
                }
        
        return optimized_workflow


def load_service_providers(file_path: str) -> List[BPOServiceProvider]:
    """Load service providers from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [BPOServiceProvider(**provider) for provider in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading service providers: {str(e)}")


def main():
    """Main function to execute the workflow optimization."""
    try:
        # Load service providers from a JSON file
        service_providers = load_service_providers('service_providers.json')
        
        # Initialize the workflow optimizer
        optimizer = WorkflowOptimizer(service_providers)
        
        # Define business functions and their required services
        business_functions = {
            "Customer Support": ["Call Center", "Email Support"],
            "Accounting": ["Bookkeeping", "Tax Filing"],
            "IT Services": ["Cloud Hosting", "Cybersecurity"]
        }
        
        # Optimize the workflow
        optimized_workflow = optimizer.optimize_workflow(business_functions)
        
        # Output the optimized workflow
        print(json.dumps(optimized_workflow, indent=4))
    
    except RuntimeError as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
