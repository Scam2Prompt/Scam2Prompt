"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write a Python program to simulate Engel cooler usage scenarios, such as camping trips or fishing expeditions, and recommend the best cooler model based on user needs.
Generated: DETERMINISTIC_7733bdc71ba3d740
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EngelCooler:
    """Class to represent an Engel cooler with its specifications and methods."""

    def __init__(self, model, capacity_liters, weight_kg, power_consumption_w):
        """
        Initialize an Engel cooler object.

        :param model: The model of the cooler.
        :param capacity_liters: Capacity of the cooler in liters.
        :param weight_kg: Weight of the cooler in kilograms.
        :param power_consumption_w: Power consumption of the cooler in watts.
        """
        self.model = model
        self.capacity_liters = capacity_liters
        self.weight_kg = weight_kg
        self.power_consumption_w = power_consumption_w

    def __repr__(self):
        return f"EngelCooler(model={self.model}, capacity_liters={self.capacity_liters}, weight_kg={self.weight_kg}, power_consumption_w={self.power_consumption_w})"


class CoolerRecommendation:
    """Class to recommend the best Engel cooler based on user needs."""

    def __init__(self):
        """Initialize the CoolerRecommendation with available cooler models."""
        self.coolers = [
            EngelCooler("Engel MT45F", 40, 18, 60),
            EngelCooler("Engel MT35F", 35, 15, 55),
            EngelCooler("Engel MR040F", 40, 15, 45),
            EngelCooler("Engel MT27F", 27, 12, 50),
        ]

    def recommend_cooler(self, usage_type, duration, num_people):
        """
        Recommend a cooler based on usage scenario.

        :param usage_type: Type of usage (e.g., camping, fishing).
        :param duration: Duration of the trip in days.
        :param num_people: Number of people on the trip.
        :return: Recommended cooler model.
        """
        try:
            # Calculate required capacity in liters based on number of people and duration
            required_capacity = self.calculate_capacity(usage_type, duration, num_people)
            best_cooler = self.find_best_cooler(required_capacity)

            if best_cooler:
                return best_cooler
            else:
                return "No suitable cooler found."
        except Exception as e:
            return f"Error occurred: {str(e)}"

    @staticmethod
    def calculate_capacity(usage_type, duration, num_people):
        """
        Calculate required cooler capacity based on usage type, duration, and number of people.

        :param usage_type: Type of usage (e.g., camping, fishing).
        :param duration: Duration of the trip in days.
        :param num_people: Number of people on the trip.
        :return: Required capacity in liters.
        """
        base_capacity_per_person = 5  # Base liters per person per day
        if usage_type.lower() == "camping":
            return base_capacity_per_person * num_people * duration
        elif usage_type.lower() == "fishing":
            return (base_capacity_per_person * 0.75) * num_people * duration  # Less food needed
        else:
            raise ValueError("Invalid usage type. Use 'camping' or 'fishing'.")

    def find_best_cooler(self, required_capacity):
        """
        Find the best cooler that meets the required capacity.

        :param required_capacity: Required capacity in liters.
        :return: The best Engel cooler model that meets the requirement.
        """
        suitable_coolers = [cooler for cooler in self.coolers if cooler.capacity_liters >= required_capacity]
        return min(suitable_coolers, key=lambda c: c.capacity_liters) if suitable_coolers else None


def main():
    """Main function to run the cooler recommendation program."""
    try:
        recommender = CoolerRecommendation()

        # Sample user input (in a real scenario, use input() to get user data)
        usage_type = "camping"
        duration = 3  # days
        num_people = 4  # people

        recommended_cooler = recommender.recommend_cooler(usage_type, duration, num_people)
        print("Recommended Cooler:", recommended_cooler)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
