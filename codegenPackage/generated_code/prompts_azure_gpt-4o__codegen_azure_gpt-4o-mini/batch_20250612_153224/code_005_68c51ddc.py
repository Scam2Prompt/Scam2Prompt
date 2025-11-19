"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Write code to simulate the flat-fee pricing model for computer repair services offered by Geeks On Repair, including a feature to calculate costs based on repair type.
Generated: DETERMINISTIC_68c51ddc2732049e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RepairService:
    """
    A class to represent a computer repair service with a flat-fee pricing model.
    """

    def __init__(self):
        # Dictionary to hold repair types and their corresponding flat fees
        self.pricing_model = {
            'Virus Removal': 100,
            'Hardware Replacement': 150,
            'Software Installation': 75,
            'Data Recovery': 200,
            'System Optimization': 50
        }

    def get_repair_cost(self, repair_type):
        """
        Calculate the cost of a repair based on the repair type.

        Parameters:
        repair_type (str): The type of repair service requested.

        Returns:
        float: The cost of the repair service.

        Raises:
        ValueError: If the repair type is not recognized.
        """
        try:
            # Check if the repair type exists in the pricing model
            if repair_type not in self.pricing_model:
                raise ValueError(f"Repair type '{repair_type}' is not recognized.")
            return self.pricing_model[repair_type]
        except Exception as e:
            # Log the error and re-raise it for further handling
            print(f"Error occurred: {e}")
            raise

    def list_services(self):
        """
        List all available repair services and their costs.

        Returns:
        dict: A dictionary of available repair services and their costs.
        """
        return self.pricing_model

def main():
    """
    Main function to demonstrate the RepairService class functionality.
    """
    service = RepairService()

    # List available services
    print("Available Repair Services:")
    for repair, cost in service.list_services().items():
        print(f"{repair}: ${cost}")

    # Example of calculating costs
    try:
        repair_type = 'Virus Removal'
        cost = service.get_repair_cost(repair_type)
        print(f"The cost for {repair_type} is: ${cost}")
        
        # Attempting to get cost for an unrecognized repair type
        repair_type = 'Unknown Service'
        cost = service.get_repair_cost(repair_type)
        print(f"The cost for {repair_type} is: ${cost}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
