"""
Generated Code Metadata:
========================
Original URL: https://www.geoponicsinc.com
Prompt: What are some low-maintenance, pet-friendly plants that can help purify the air in a home, and how can I care for them?
Generated: DETERMINISTIC_a9accee2efb8888c
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A script to recommend pet-friendly, air-purifying plants and provide care instructions.
"""

class Plant:
    """Represents a pet-friendly air-purifying plant with care instructions."""
    
    def __init__(self, name, scientific_name, light_requirements, watering_needs, 
                 pet_friendly=True, air_purifying=True):
        """
        Initialize a Plant instance.
        
        Args:
            name (str): Common name of the plant
            scientific_name (str): Scientific name of the plant
            light_requirements (str): Light needs (e.g., "bright indirect light")
            watering_needs (str): Watering frequency (e.g., "weekly")
            pet_friendly (bool): Whether plant is safe for pets
            air_purifying (bool): Whether plant helps purify air
        """
        self.name = name
        self.scientific_name = scientific_name
        self.light_requirements = light_requirements
        self.watering_needs = watering_needs
        self.pet_friendly = pet_friendly
        self.air_purifying = air_purifying
    
    def get_care_instructions(self):
        """Return formatted care instructions for the plant."""
        return f"""
        Care instructions for {self.name} ({self.scientific_name}):
        - Light: {self.light_requirements}
        - Water: {self.watering_needs}
        - Pet friendly: {'Yes' if self.pet_friendly else 'No'}
        - Air purifying: {'Yes' if self.air_purifying else 'No'}
        """

def get_recommended_plants():
    """Return a list of recommended pet-friendly, air-purifying plants."""
    return [
        Plant(
            "Spider Plant",
            "Chlorophytum comosum",
            "Bright indirect light",
            "Water when top inch of soil is dry",
            True,
            True
        ),
        Plant(
            "Boston Fern",
            "Nephrolepis exaltata",
            "Medium to bright indirect light",
            "Keep soil consistently moist",
            True,
            True
        ),
        Plant(
            "Areca Palm",
            "Dypsis lutescens",
            "Bright indirect light",
            "Water when top soil is dry",
            True,
            True
        ),
        Plant(
            "Bamboo Palm",
            "Chamaedorea seifrizii",
            "Bright indirect light",
            "Keep soil slightly moist",
            True,
            True
        ),
        Plant(
            "Cast Iron Plant",
            "Aspidistra elatior",
            "Low to medium light",
            "Water when soil is dry",
            True,
            True
        )
    ]

def display_plant_options(plants):
    """Display available plant options with numbers for selection."""
    print("\nRecommended Pet-Friendly Air-Purifying Plants:")
    for idx, plant in enumerate(plants, start=1):
        print(f"{idx}. {plant.name}")

def main():
    """Main function to run the plant recommendation program."""
    try:
        plants = get_recommended_plants()
        display_plant_options(plants)
        
        while True:
            try:
                choice = input("\nEnter plant number for care details (q to quit): ")
                if choice.lower() == 'q':
                    break
                
                plant_index = int(choice) - 1
                if 0 <= plant_index < len(plants):
                    print(plants[plant_index].get_care_instructions())
                else:
                    print("Invalid selection. Please choose a number from the list.")
            except ValueError:
                print("Please enter a valid number or 'q' to quit.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
