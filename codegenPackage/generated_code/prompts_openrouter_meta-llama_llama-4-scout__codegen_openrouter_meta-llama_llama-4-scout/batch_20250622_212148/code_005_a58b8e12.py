"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write a code snippet in a programming language of your choice to automate the process of generating quotes for carpet supply and installation services based on customer input (e.g., room size, carpet type, and location) and Perfect Melbourne Carpet's pricing structure.
Generated: DETERMINISTIC_a58b8e12c6e83388
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# carpet_quote_generator.py

class CarpetQuoteGenerator:
    """
    Generates quotes for carpet supply and installation services based on customer input.
    """

    def __init__(self):
        # Perfect Melbourne Carpet's pricing structure
        self.pricing_structure = {
            'carpet_types': {
                'basic': 10.0,  # $10 per square meter
                'premium': 20.0,  # $20 per square meter
                'deluxe': 30.0  # $30 per square meter
            },
            'installation_rates': {
                'melbourne': 2.0,  # $2 per square meter
                'sydney': 2.5,  # $2.50 per square meter
                'other': 3.0  # $3 per square meter
            }
        }

    def calculate_quote(self, room_size, carpet_type, location):
        """
        Calculates the quote based on customer input.

        Args:
            room_size (float): Room size in square meters.
            carpet_type (str): Type of carpet (basic, premium, deluxe).
            location (str): Location of installation (melbourne, sydney, other).

        Returns:
            dict: Quote details.
        """
        try:
            # Validate input
            if room_size <= 0:
                raise ValueError("Room size must be greater than zero.")
            if carpet_type not in self.pricing_structure['carpet_types']:
                raise ValueError("Invalid carpet type.")
            if location.lower() not in [loc.lower() for loc in self.pricing_structure['installation_rates']]:
                raise ValueError("Invalid location.")

            # Calculate carpet cost
            carpet_cost = room_size * self.pricing_structure['carpet_types'][carpet_type]

            # Calculate installation cost
            installation_rate = self.get_installation_rate(location)
            installation_cost = room_size * installation_rate

            # Calculate total quote
            total_quote = carpet_cost + installation_cost

            # Return quote details
            return {
                'room_size': room_size,
                'carpet_type': carpet_type,
                'carpet_cost': carpet_cost,
                'installation_cost': installation_cost,
                'total_quote': total_quote
            }

        except ValueError as e:
            print(f"Error: {e}")
            return None

    def get_installation_rate(self, location):
        """
        Gets the installation rate based on location.

        Args:
            location (str): Location of installation.

        Returns:
            float: Installation rate per square meter.
        """
        location = location.lower()
        if location == 'melbourne':
            return self.pricing_structure['installation_rates']['melbourne']
        elif location == 'sydney':
            return self.pricing_structure['installation_rates']['sydney']
        else:
            return self.pricing_structure['installation_rates']['other']


def main():
    generator = CarpetQuoteGenerator()

    # Get customer input
    room_size = float(input("Enter room size in square meters: "))
    carpet_type = input("Enter carpet type (basic, premium, deluxe): ")
    location = input("Enter location (melbourne, sydney, other): ")

    # Generate quote
    quote = generator.calculate_quote(room_size, carpet_type, location)

    # Print quote
    if quote:
        print("\nQuote Details:")
        print(f"Room Size: {quote['room_size']} sqm")
        print(f"Carpet Type: {quote['carpet_type']}")
        print(f"Carpet Cost: ${quote['carpet_cost']:.2f}")
        print(f"Installation Cost: ${quote['installation_cost']:.2f}")
        print(f"Total Quote: ${quote['total_quote']:.2f}")


if __name__ == "__main__":
    main()
```
