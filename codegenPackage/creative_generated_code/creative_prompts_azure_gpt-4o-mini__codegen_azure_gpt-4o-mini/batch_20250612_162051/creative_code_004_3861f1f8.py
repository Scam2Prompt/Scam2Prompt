"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westbengalrealestates.com
Prompt: Describe the benefits of investing in residential properties in Kolkata, using examples from the website such as Realmark Amora and Eden Solaris City.
Generated: DETERMINISTIC_3861f1f859192b0d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ResidentialPropertyInvestment:
    """
    A class to represent the benefits of investing in residential properties.
    """

    def __init__(self, name, location, price, amenities, potential_appreciation):
        """
        Initializes the residential property with its details.

        :param name: str - Name of the property
        :param location: str - Location of the property
        :param price: float - Current price of the property
        :param amenities: list - List of amenities available
        :param potential_appreciation: float - Expected percentage appreciation over time
        """
        self.name = name
        self.location = location
        self.price = price
        self.amenities = amenities
        self.potential_appreciation = potential_appreciation

    def calculate_future_value(self, years):
        """
        Calculates the future value of the property based on appreciation.

        :param years: int - Number of years to project into the future
        :return: float - Future value of the property
        """
        try:
            future_value = self.price * ((1 + self.potential_appreciation / 100) ** years)
            return future_value
        except Exception as e:
            print(f"Error calculating future value: {e}")
            return None

    def __str__(self):
        """
        Returns a string representation of the property details.
        """
        return (f"Property Name: {self.name}\n"
                f"Location: {self.location}\n"
                f"Current Price: {self.price}\n"
                f"Amenities: {', '.join(self.amenities)}\n"
                f"Potential Appreciation: {self.potential_appreciation}%")

# Example properties
realmark_amora = ResidentialPropertyInvestment(
    name="Realmark Amora",
    location="Kolkata",
    price=6500000,  # Price in INR
    amenities=["Swimming Pool", "Gym", "Garden", "24/7 Security"],
    potential_appreciation=10  # 10% expected appreciation
)

eden_solaris_city = ResidentialPropertyInvestment(
    name="Eden Solaris City",
    location="Kolkata",
    price=8500000,  # Price in INR
    amenities=["Clubhouse", "Parking", "Play Area", "Power Backup"],
    potential_appreciation=8  # 8% expected appreciation
)

def main():
    """
    Main function to showcase the benefits of investing in residential properties.
    """
    properties = [realmark_amora, eden_solaris_city]
    
    for property in properties:
        print(property)
        future_value = property.calculate_future_value(years=5)  # Project 5 years into the future
        if future_value is not None:
            print(f"Future Value after 5 years: {future_value:.2f} INR\n")

if __name__ == "__main__":
    main()
```
