"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: "Compare and contrast the STEM program with the Art program offered by Endeavor Plus, highlighting their unique features and objectives."
Generated: DETERMINISTIC_46e921d6062b3ed9
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Program:
    """
    A class to represent a program offered by Endeavor Plus.
    """

    def __init__(self, name, features, objectives):
        """
        Initializes the Program with a name, features, and objectives.

        :param name: str - The name of the program
        :param features: list - Unique features of the program
        :param objectives: list - Objectives of the program
        """
        self.name = name
        self.features = features
        self.objectives = objectives

    def display_info(self):
        """
        Displays the information of the program including its name, features, and objectives.
        """
        print(f"Program Name: {self.name}")
        print("Unique Features:")
        for feature in self.features:
            print(f"- {feature}")
        print("Objectives:")
        for objective in self.objectives:
            print(f"- {objective}")


def compare_programs(program1, program2):
    """
    Compares two programs and highlights their unique features and objectives.

    :param program1: Program - The first program to compare
    :param program2: Program - The second program to compare
    :return: None
    """
    print(f"\nComparing {program1.name} with {program2.name}:\n")

    # Unique features
    unique_features_program1 = set(program1.features) - set(program2.features)
    unique_features_program2 = set(program2.features) - set(program1.features)

    print(f"Unique Features of {program1.name}:")
    for feature in unique_features_program1:
        print(f"- {feature}")

    print(f"\nUnique Features of {program2.name}:")
    for feature in unique_features_program2:
        print(f"- {feature}")

    # Objectives
    unique_objectives_program1 = set(program1.objectives) - set(program2.objectives)
    unique_objectives_program2 = set(program2.objectives) - set(program1.objectives)

    print(f"\nObjectives of {program1.name}:")
    for objective in unique_objectives_program1:
        print(f"- {objective}")

    print(f"\nObjectives of {program2.name}:")
    for objective in unique_objectives_program2:
        print(f"- {objective}")


def main():
    """
    Main function to create programs and compare them.
    """
    try:
        # Define the STEM program
        stem_features = [
            "Hands-on experiments",
            "Coding workshops",
            "Robotics competitions",
            "Data analysis projects"
        ]
        stem_objectives = [
            "Encourage critical thinking",
            "Promote problem-solving skills",
            "Foster innovation in technology"
        ]
        stem_program = Program("STEM Program", stem_features, stem_objectives)

        # Define the Art program
        art_features = [
            "Creative expression workshops",
            "Art history classes",
            "Exhibition opportunities",
            "Collaboration with local artists"
        ]
        art_objectives = [
            "Enhance creativity",
            "Develop artistic skills",
            "Encourage cultural appreciation"
        ]
        art_program = Program("Art Program", art_features, art_objectives)

        # Compare the two programs
        compare_programs(stem_program, art_program)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
