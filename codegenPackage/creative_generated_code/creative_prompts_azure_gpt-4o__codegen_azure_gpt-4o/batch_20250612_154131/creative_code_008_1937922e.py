"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write a program to generate automated quotes for garage door repairs and installations, incorporating Trimatic's emphasis on tailored solutions for different types of doors.
Generated: DETERMINISTIC_1937922e0ee3c963
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class GarageDoorQuoteGenerator:
    """
    A class to generate automated quotes for garage door repairs and installations.
    Tailored solutions are provided based on the type of garage door and additional preferences.
    """
    
    def __init__(self):
        """
        Initializes the quote generator with pricing and service options for different types of doors.
        """
        self.pricing = {
            "standard_single": {"repair": 100, "installation": 500},
            "standard_double": {"repair": 150, "installation": 800},
            "custom_single": {"repair": 200, "installation": 1000},
            "custom_double": {"repair": 300, "installation": 1500},
        }
        self.additional_services = {
            "paint": 150,
            "insulation": 250,
            "smart_opener": 350,
        }

    def generate_quote(self, door_type: str, service_type: str, extras: list) -> dict:
        """
        Generates a quote based on door type, service type, and additional preferences.

        Args:
            door_type (str): Type of garage door (e.g., "standard_single", "standard_double", "custom_single", "custom_double").
            service_type (str): Type of service (e.g., "repair", "installation").
            extras (list): List of additional services (e.g., ["paint", "insulation"]).

        Returns:
            dict: A dictionary containing the detailed quote and total price.

        Raises:
            ValueError: If an invalid door type or service type is provided.
        """
        # Validate inputs
        if door_type not in self.pricing:
            raise ValueError(f"Invalid door type: {door_type}. Valid types are {list(self.pricing.keys())}.")
        if service_type not in self.pricing[door_type]:
            raise ValueError(f"Invalid service type: {service_type}. Valid types are ['repair', 'installation'].")
        
        # Base price calculation
        base_price = self.pricing[door_type][service_type]
        
        # Extras price calculation
        extras_price = 0
        extras_details = []
        for extra in extras:
            if extra in self.additional_services:
                extras_price += self.additional_services[extra]
                extras_details.append({"service": extra, "price": self.additional_services[extra]})
            else:
                raise ValueError(f"Invalid extra service: {extra}. Valid extras are {list(self.additional_services.keys())}.")
        
        # Final total price
        total_price = base_price + extras_price
        
        # Generate quote details
        quote = {
            "door_type": door_type,
            "service_type": service_type,
            "base_price": base_price,
            "extras": extras_details,
            "total_price": total_price,
        }
        
        return quote

    def save_quote_to_file(self, quote: dict, filename: str) -> None:
        """
        Saves the generated quote to a JSON file.

        Args:
            quote (dict): The quote dictionary to save.
            filename (str): Name of the file to save the quote to.

        Raises:
            IOError: If there is an issue saving the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(quote, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save quote to file '{filename}': {e}")


# Example usage of the GarageDoorQuoteGenerator class
if __name__ == "__main__":
    try:
        # Initialize the quote generator
        generator = GarageDoorQuoteGenerator()
        
        # Generate a tailored quote
        quote = generator.generate_quote(
            door_type="custom_double",
            service_type="installation",
            extras=["paint", "smart_opener"]
        )
        
        # Print the quote to the console
        print("Generated Quote:")
        print(json.dumps(quote, indent=4))
        
        # Save the quote to a file
        generator.save_quote_to_file(quote, "garage_door_quote.json")
        print("Quote saved to 'garage_door_quote.json'.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except IOError as ioe:
        print(f"Error: {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
