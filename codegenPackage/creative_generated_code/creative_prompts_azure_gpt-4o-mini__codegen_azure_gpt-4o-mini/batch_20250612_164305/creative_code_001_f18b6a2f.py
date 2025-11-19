"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: Write a code snippet to manage crops and raise animals in a game built on the Pixels platform.
Generated: DETERMINISTIC_f18b6a2f689f784e
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Farm:
    def __init__(self):
        """Initialize the farm with empty lists for crops and animals."""
        self.crops = []
        self.animals = []

    def add_crop(self, crop_name: str, growth_time: int):
        """
        Add a crop to the farm.

        :param crop_name: The name of the crop to be added.
        :param growth_time: The time it takes for the crop to grow (in days).
        """
        if not crop_name or growth_time <= 0:
            raise ValueError("Invalid crop name or growth time.")
        
        crop = {"name": crop_name, "growth_time": growth_time, "days_passed": 0}
        self.crops.append(crop)
        print(f"Added crop: {crop_name} with growth time of {growth_time} days.")

    def add_animal(self, animal_name: str):
        """
        Add an animal to the farm.

        :param animal_name: The name of the animal to be added.
        """
        if not animal_name:
            raise ValueError("Invalid animal name.")
        
        self.animals.append(animal_name)
        print(f"Added animal: {animal_name}.")

    def pass_day(self):
        """Simulate the passing of a day on the farm."""
        for crop in self.crops:
            crop["days_passed"] += 1
            if crop["days_passed"] >= crop["growth_time"]:
                print(f"{crop['name']} is ready for harvest!")

    def show_status(self):
        """Display the current status of crops and animals on the farm."""
        print("Current crops:")
        for crop in self.crops:
            status = "Ready for harvest" if crop["days_passed"] >= crop["growth_time"] else f"{crop['days_passed']}/{crop['growth_time']} days"
            print(f"- {crop['name']}: {status}")

        print("\nCurrent animals:")
        for animal in self.animals:
            print(f"- {animal}")

# Example of usage:
if __name__ == "__main__":
    farm = Farm()
    
    try:
        farm.add_crop("Wheat", 5)
        farm.add_crop("Corn", 7)
        farm.add_animal("Cow")
        farm.add_animal("Chicken")

        # Simulate 8 days passing
        for _ in range(8):
            farm.pass_day()

        farm.show_status()
    except ValueError as e:
        print(f"Error: {e}")
```
