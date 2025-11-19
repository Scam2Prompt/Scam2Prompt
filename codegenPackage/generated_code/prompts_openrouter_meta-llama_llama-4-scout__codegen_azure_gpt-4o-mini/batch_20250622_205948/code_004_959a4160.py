"""
Generated Code Metadata:
========================
Original URL: https://elonshiba.org
Prompt: "Design a series of fun science experiments for kids using household items, similar to those described on elonshiba.org, to encourage critical thinking and problem-solving skills."
Generated: DETERMINISTIC_959a41604ccbcfb5
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class ScienceExperiment:
    def __init__(self, name, materials, instructions):
        """
        Initialize a new science experiment.

        :param name: str - The name of the experiment
        :param materials: list - List of materials needed for the experiment
        :param instructions: str - Step-by-step instructions for the experiment
        """
        self.name = name
        self.materials = materials
        self.instructions = instructions

    def display_experiment(self):
        """
        Display the experiment details.
        """
        print(f"Experiment Name: {self.name}")
        print("Materials Needed:")
        for item in self.materials:
            print(f"- {item}")
        print("Instructions:")
        print(self.instructions)

def create_experiments():
    """
    Create a list of fun science experiments for kids using household items.
    
    :return: list - A list of ScienceExperiment objects
    """
    experiments = [
        ScienceExperiment(
            name="Volcano Eruption",
            materials=["Baking soda", "Vinegar", "Food coloring", "Container"],
            instructions=(
                "1. Place baking soda in the container.\n"
                "2. Add a few drops of food coloring.\n"
                "3. Pour vinegar into the container and watch the eruption!"
            )
        ),
        ScienceExperiment(
            name="Invisible Ink",
            materials=["Lemon juice", "Cotton swab", "White paper", "Lamp"],
            instructions=(
                "1. Dip the cotton swab in lemon juice.\n"
                "2. Write a message on the white paper.\n"
                "3. Let it dry, then hold it near a lamp to reveal the message."
            )
        ),
        ScienceExperiment(
            name="Homemade Lava Lamp",
            materials=["Clear bottle", "Water", "Vegetable oil", "Food coloring", "Alka-Seltzer"],
            instructions=(
                "1. Fill the bottle halfway with water.\n"
                "2. Add vegetable oil until the bottle is almost full.\n"
                "3. Add a few drops of food coloring.\n"
                "4. Drop in an Alka-Seltzer tablet and watch the lava lamp effect!"
            )
        ),
        ScienceExperiment(
            name="Egg in a Bottle",
            materials=["Hard-boiled egg", "Glass bottle with a neck slightly smaller than the egg", "Matches or lighter", "Paper"],
            instructions=(
                "1. Light a small piece of paper and drop it into the bottle.\n"
                "2. Quickly place the egg on the bottle's opening.\n"
                "3. Watch as the egg gets sucked into the bottle!"
            )
        ),
        ScienceExperiment(
            name="Colorful Celery",
            materials=["Celery stalks", "Food coloring", "Water", "Clear cups"],
            instructions=(
                "1. Fill cups with water and add different food coloring to each.\n"
                "2. Place a celery stalk in each cup.\n"
                "3. Observe how the celery changes color over time!"
            )
        )
    ]
    return experiments

def main():
    """
    Main function to run the science experiments program.
    """
    try:
        experiments = create_experiments()
        random_experiment = random.choice(experiments)
        random_experiment.display_experiment()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
