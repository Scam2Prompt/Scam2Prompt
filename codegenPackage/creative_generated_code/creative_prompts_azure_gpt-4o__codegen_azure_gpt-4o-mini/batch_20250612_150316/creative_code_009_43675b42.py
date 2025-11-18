"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzooprotocal.net
Prompt: Suggest a library for managing service provider trustworthiness and reliability, including features for vetting cleaners and tracking their performance, as emphasized in Queen Bee Renzo ProtocolCleaning's customer testimonials.
Generated: DETERMINISTIC_43675b4274f665d3
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import json
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServiceProvider:
    """Class to represent a service provider, such as a cleaner."""
    
    def __init__(self, name: str, reliability_score: float):
        """
        Initialize a new service provider.
        
        :param name: Name of the service provider.
        :param reliability_score: Score indicating the provider's reliability (0-10 scale).
        """
        self.name = name
        self.reliability_score = reliability_score
        self.performance_history = []

    def add_performance_entry(self, rating: float):
        """
        Add a performance entry for the service provider.
        
        :param rating: Performance rating (0-10 scale).
        """
        if not (0 <= rating <= 10):
            logging.error("Rating must be between 0 and 10.")
            raise ValueError("Rating must be between 0 and 10.")
        
        self.performance_history.append(rating)

    def calculate_average_rating(self) -> float:
        """
        Calculate the average performance rating of the service provider.
        
        :return: Average rating or 0 if no entries exist.
        """
        return sum(self.performance_history) / len(self.performance_history) if self.performance_history else 0


class ServiceProviderManager:
    """Class to manage multiple service providers."""
    
    def __init__(self):
        """Initialize the service provider manager."""
        self.providers: Dict[str, ServiceProvider] = {}

    def add_provider(self, provider: ServiceProvider):
        """
        Add a service provider to the management system.
        
        :param provider: An instance of ServiceProvider.
        """
        if provider.name in self.providers:
            logging.warning(f"Provider {provider.name} already exists. Updating existing entry.")
        
        self.providers[provider.name] = provider

    def vet_provider(self, name: str) -> bool:
        """
        Vet a service provider based on reliability score and performance.
        
        :param name: Name of the service provider to vet.
        :return: True if the provider is trustworthy, False otherwise.
        """
        provider = self.providers.get(name)
        if not provider:
            logging.error(f"No provider found with name: {name}")
            return False
            
        average_rating = provider.calculate_average_rating()
        is_trustworthy = provider.reliability_score >= 7 and average_rating >= 7
        
        logging.info(f"Provider {name} is {'trustworthy' if is_trustworthy else 'not trustworthy'}.")
        return is_trustworthy

    def export_report(self, filepath: str):
        """
        Export the service provider performance report to a JSON file.
        
        :param filepath: Path to the file where the report will be saved.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump({name: {
                    "reliability_score": provider.reliability_score,
                    "average_rating": provider.calculate_average_rating(),
                    "performance_history": provider.performance_history
                } for name, provider in self.providers.items()}, file)
            logging.info(f"Report successfully exported to {filepath}.")
        except IOError as e:
            logging.error(f"Failed to write report to {filepath}: {e}")

# Example of using the classes:
if __name__ == "__main__":
    manager = ServiceProviderManager()
    
    # Create service providers
    provider1 = ServiceProvider("CleanCo", 8.5)
    provider1.add_performance_entry(9)
    provider1.add_performance_entry(8)
    
    provider2 = ServiceProvider("SparkleClean", 6.0)
    provider2.add_performance_entry(5)
    provider2.add_performance_entry(7)
    
    # Adding providers to the manager
    manager.add_provider(provider1)
    manager.add_provider(provider2)
    
    # Vetting providers
    manager.vet_provider("CleanCo")
    manager.vet_provider("SparkleClean")
    
    # Exporting report
    manager.export_report("service_providers_report.json")
```
