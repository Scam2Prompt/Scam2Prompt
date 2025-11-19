"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Generate a code snippet to calculate the total cost of dumpster rental based on sizes and service areas mentioned on Purple Dumpster's website.
Generated: DETERMINISTIC_c5e49e4a98298f8d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DumpsterRental:
    def __init__(self):
        # Define the pricing structure based on dumpster sizes and service areas
        self.pricing = {
            'small': {'base_price': 200, 'service_area_fee': 50},
            'medium': {'base_price': 300, 'service_area_fee': 75},
            'large': {'base_price': 400, 'service_area_fee': 100},
        }

    def calculate_total_cost(self, size, service_area):
        """
        Calculate the total cost of dumpster rental based on size and service area.

        :param size: str, size of the dumpster ('small', 'medium', 'large')
        :param service_area: str, service area (e.g., 'local', 'extended')
        :return: float, total cost of the rental
        :raises ValueError: if the size is not valid
        """
        # Validate the dumpster size
        if size not in self.pricing:
            raise ValueError(f"Invalid dumpster size: {size}. Valid sizes are: {list(self.pricing.keys())}")

        # Base price and service area fee
        base_price = self.pricing[size]['base_price']
        service_area_fee = self.get_service_area_fee(service_area)

        # Calculate total cost
        total_cost = base_price + service_area_fee
        return total_cost

    def get_service_area_fee(self, service_area):
        """
        Get the service area fee based on the service area.

        :param service_area: str, service area (e.g., 'local', 'extended')
        :return: float, service area fee
        :raises ValueError: if the service area is not valid
        """
        # Define service area fees
        service_area_fees = {
            'local': 0,
            'extended': 50,
        }

        # Validate the service area
        if service_area not in service_area_fees:
            raise ValueError(f"Invalid service area: {service_area}. Valid areas are: {list(service_area_fees.keys())}")

        return service_area_fees[service_area]


# Example usage
if __name__ == "__main__":
    rental_service = DumpsterRental()
    
    try:
        size = 'medium'  # Example size
        service_area = 'extended'  # Example service area
        total_cost = rental_service.calculate_total_cost(size, service_area)
        print(f"The total cost for a {size} dumpster in the {service_area} area is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
