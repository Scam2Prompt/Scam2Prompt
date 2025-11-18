"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looksrareairdrop.space
Prompt: Create a script to calculate the monthly cost of renting a dedicated server from Timeweb, factoring in custom configurations and additional services.
Generated: DETERMINISTIC_c8f2b9330a621d65
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DedicatedServerRentalCalculator:
    """
    A class to calculate the monthly cost of renting a dedicated server 
    from Timeweb with custom configurations and additional services.
    """

    BASE_COSTS = {
        "basic": 50,    # Base cost for a basic server configuration
        "standard": 100, # Base cost for a standard server configuration
        "premium": 200   # Base cost for a premium server configuration
    }

    ADDITIONAL_SERVICES = {
        "backup": 20,    # Monthly cost for backup service
        "security": 30,  # Monthly cost for security service
        "monitoring": 25  # Monthly cost for monitoring service
    }

    def __init__(self, configuration: str, additional_services: list):
        """
        Initializes the calculator with the given configuration and additional services.

        :param configuration: Server configuration type: basic, standard, or premium
        :param additional_services: List of additional services to include in the cost calculation
        """
        self.configuration = configuration
        self.additional_services = additional_services

    def validate_configuration(self):
        """
        Validates the server configuration type.

        :raises ValueError: If the configuration is not valid
        """
        if self.configuration not in self.BASE_COSTS:
            raise ValueError(f"Invalid configuration type '{self.configuration}'. "
                             "Choose from: " + ", ".join(self.BASE_COSTS.keys()))

    def validate_additional_services(self):
        """
        Validates the additional services.

        :raises ValueError: If any service is invalid
        """
        invalid_services = [service for service in self.additional_services if service not in self.ADDITIONAL_SERVICES]
        if invalid_services:
            raise ValueError(f"Invalid additional services: {', '.join(invalid_services)}. "
                             "Available services: " + ", ".join(self.ADDITIONAL_SERVICES.keys()))

    def calculate_total_cost(self) -> float:
        """
        Calculates the total monthly cost for the server rental.

        :return: Total cost as a float
        """
        # Validate inputs
        self.validate_configuration()
        self.validate_additional_services()
        
        # Calculate total cost
        total_cost = self.BASE_COSTS[self.configuration]
        for service in self.additional_services:
            total_cost += self.ADDITIONAL_SERVICES[service]
        
        return total_cost


if __name__ == "__main__":
    # Example usage
    try:
        # User-defined configuration and services
        server_configuration = "standard"  # Choose from: basic, standard, premium
        additional_services = ["backup", "monitoring"]  # Choose from: backup, security, monitoring

        # Create an instance of the calculator
        rental_calculator = DedicatedServerRentalCalculator(server_configuration, additional_services)

        # Calculate and display the total cost
        total_cost = rental_calculator.calculate_total_cost()
        print(f"The total monthly cost for renting a {server_configuration} server with "
              f"{', '.join(additional_services)} is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
