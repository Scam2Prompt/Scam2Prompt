"""
Generated Code Metadata:
========================
Original URL: https://safargenie.com
Prompt: Generate a detailed itinerary for a Chardham Yatra package that includes helicopter travel options and highlights key spiritual sites.
Generated: DETERMINISTIC_fedb5628d70ec7ca
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ChardhamYatraItinerary:
    """
    A class to generate a detailed itinerary for the Chardham Yatra package.
    Includes helicopter travel options and highlights key spiritual sites.
    """

    def __init__(self):
        # Initialize the itinerary with default values
        self.itinerary = []

    def add_day(self, day_number, title, description, travel_mode, highlights):
        """
        Add a day's itinerary to the package.

        :param day_number: Day number in the itinerary
        :param title: Title or summary of the day's activities
        :param description: Detailed description of the day's activities
        :param travel_mode: Mode of travel (e.g., Helicopter, Road)
        :param highlights: List of key spiritual sites or activities for the day
        """
        day_plan = {
            "day": day_number,
            "title": title,
            "description": description,
            "travel_mode": travel_mode,
            "highlights": highlights
        }
        self.itinerary.append(day_plan)

    def generate_itinerary(self):
        """
        Generate the complete itinerary as a JSON string.

        :return: JSON string of the itinerary
        """
        return json.dumps(self.itinerary, indent=4)

    def save_to_file(self, filename):
        """
        Save the itinerary to a file in JSON format.

        :param filename: Name of the file to save the itinerary
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.generate_itinerary())
            print(f"Itinerary successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving itinerary to file: {e}")


# Main function to create and display the Chardham Yatra itinerary
def main():
    # Create an instance of the itinerary generator
    yatra = ChardhamYatraItinerary()

    # Add details for each day of the Chardham Yatra
    yatra.add_day(
        day_number=1,
        title="Arrival in Dehradun",
        description="Arrive in Dehradun, the starting point of the Chardham Yatra. "
                    "Check into your hotel and attend a briefing session about the journey.",
        travel_mode="Road",
        highlights=["Welcome briefing", "Overnight stay in Dehradun"]
    )

    yatra.add_day(
        day_number=2,
        title="Yamunotri Darshan",
        description="Travel to Yamunotri by helicopter. Visit the Yamunotri Temple, "
                    "dedicated to Goddess Yamuna. Take a holy dip in the Yamuna River.",
        travel_mode="Helicopter",
        highlights=["Yamunotri Temple", "Holy dip in Yamuna River", "Prayers and rituals"]
    )

    yatra.add_day(
        day_number=3,
        title="Gangotri Darshan",
        description="Fly to Gangotri. Visit the Gangotri Temple, dedicated to Goddess Ganga. "
                    "Experience the serene beauty of the Bhagirathi River.",
        travel_mode="Helicopter",
        highlights=["Gangotri Temple", "Bhagirathi River", "Spiritual rituals"]
    )

    yatra.add_day(
        day_number=4,
        title="Kedarnath Darshan",
        description="Fly to Kedarnath. Visit the Kedarnath Temple, one of the twelve Jyotirlingas. "
                    "Experience the divine aura of the temple surrounded by majestic mountains.",
        travel_mode="Helicopter",
        highlights=["Kedarnath Temple", "Jyotirlinga darshan", "Scenic mountain views"]
    )

    yatra.add_day(
        day_number=5,
        title="Badrinath Darshan",
        description="Fly to Badrinath. Visit the Badrinath Temple, dedicated to Lord Vishnu. "
                    "Explore nearby attractions like Mana Village and Tapt Kund.",
        travel_mode="Helicopter",
        highlights=["Badrinath Temple", "Mana Village", "Tapt Kund"]
    )

    yatra.add_day(
        day_number=6,
        title="Return to Dehradun",
        description="Fly back to Dehradun. Conclude your Chardham Yatra with cherished memories.",
        travel_mode="Helicopter",
        highlights=["Farewell ceremony", "Return journey"]
    )

    # Generate and display the itinerary
    print("Generated Chardham Yatra Itinerary:")
    print(yatra.generate_itinerary())

    # Save the itinerary to a file
    yatra.save_to_file("chardham_yatra_itinerary.json")


# Entry point of the script
if __name__ == "__main__":
    main()
```
