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
# plumbing_heating_estimator.py

class ServiceEstimator:
    """
    Estimates costs for plumbing and heating services based on customer input.
    """

    def __init__(self):
        self.services = {
            "plumbing": self.estimate_plumbing,
            "heating": self.estimate_heating
        }

    def get_service_estimate(self, service_type, **kwargs):
        """
        Gets an estimate for a specific service.

        Args:
            service_type (str): Type of service (plumbing or heating)
            **kwargs: Additional arguments required for the service estimate

        Returns:
            float: Estimated cost of the service
        """
        if service_type not in self.services:
            raise ValueError("Invalid service type")

        return self.services[service_type](**kwargs)

    def estimate_plumbing(self, hours_worked, materials_cost, labor_rate=75.0):
        """
        Estimates the cost of plumbing services.

        Args:
            hours_worked (float): Number of hours worked
            materials_cost (float): Cost of materials used
            labor_rate (float, optional): Labor rate per hour. Defaults to 75.0.

        Returns:
            float: Estimated cost of plumbing services
        """
        labor_cost = hours_worked * labor_rate
        total_cost = labor_cost + materials_cost
        return total_cost

    def estimate_heating(self, system_size, installation_cost, maintenance_cost):
        """
        Estimates the cost of heating services.

        Args:
            system_size (str): Size of the heating system (e.g., "small", "medium", "large")
            installation_cost (float): Cost of installation
            maintenance_cost (float): Cost of maintenance

        Returns:
            float: Estimated cost of heating services
        """
        system_size_factors = {
            "small": 1.0,
            "medium": 1.5,
            "large": 2.0
        }

        if system_size not in system_size_factors:
            raise ValueError("Invalid system size")

        total_cost = installation_cost + maintenance_cost
        total_cost *= system_size_factors[system_size]
        return total_cost


def main():
    estimator = ServiceEstimator()

    print("Service Estimator")
    print("-----------------")

    while True:
        print("1. Plumbing Services")
        print("2. Heating Services")
        print("3. Quit")

        choice = input("Choose a service: ")

        if choice == "1":
            hours_worked = float(input("Enter hours worked: "))
            materials_cost = float(input("Enter materials cost: "))
            labor_rate = float(input("Enter labor rate (default: 75.0): ") or 75.0)

            try:
                estimate = estimator.get_service_estimate("plumbing", hours_worked=hours_worked, materials_cost=materials_cost, labor_rate=labor_rate)
                print(f"Estimated plumbing cost: ${estimate:.2f}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            system_size = input("Enter system size (small, medium, large): ")
            installation_cost = float(input("Enter installation cost: "))
            maintenance_cost = float(input("Enter maintenance cost: "))

            try:
                estimate = estimator.get_service_estimate("heating", system_size=system_size, installation_cost=installation_cost, maintenance_cost=maintenance_cost)
                print(f"Estimated heating cost: ${estimate:.2f}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
