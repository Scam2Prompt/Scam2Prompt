"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Write a program to assess the impact of new mental models in leadership, inspired by PConsultsa's focus on unlearning outdated concepts and fostering innovation.
Generated: DETERMINISTIC_7df349409f481448
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mental_model_assessor.py

class MentalModel:
    """Represents a mental model with its name, description, and impact score."""

    def __init__(self, name, description, impact_score):
        """
        Initializes a MentalModel instance.

        Args:
            name (str): The name of the mental model.
            description (str): A brief description of the mental model.
            impact_score (float): The impact score of the mental model (between 0 and 1).
        """
        self.name = name
        self.description = description
        self.impact_score = impact_score

        # Validate impact score
        if not (0 <= impact_score <= 1):
            raise ValueError("Impact score must be between 0 and 1")


class LeadershipAssessor:
    """Assesses the impact of new mental models in leadership."""

    def __init__(self):
        """Initializes a LeadershipAssessor instance."""
        self.mental_models = []

    def add_mental_model(self, mental_model):
        """
        Adds a mental model to the assessor.

        Args:
            mental_model (MentalModel): The mental model to add.
        """
        self.mental_models.append(mental_model)

    def assess_impact(self):
        """
        Calculates the overall impact score of all mental models.

        Returns:
            float: The overall impact score (between 0 and 1).
        """
        # Calculate overall impact score as the average of all mental model impact scores
        impact_scores = [model.impact_score for model in self.mental_models]
        overall_impact_score = sum(impact_scores) / len(impact_scores) if impact_scores else 0

        return overall_impact_score

    def get_mental_models(self):
        """
        Retrieves all mental models.

        Returns:
            list[MentalModel]: A list of all mental models.
        """
        return self.mental_models


def main():
    try:
        # Create mental models
        model1 = MentalModel("Growth Mindset", "Embracing challenges and learning from failures.", 0.8)
        model2 = MentalModel("Servant Leadership", "Prioritizing team members' needs and growth.", 0.9)
        model3 = MentalModel("Design Thinking", "Empathizing with users and iterating solutions.", 0.7)

        # Create leadership assessor
        assessor = LeadershipAssessor()

        # Add mental models to assessor
        assessor.add_mental_model(model1)
        assessor.add_mental_model(model2)
        assessor.add_mental_model(model3)

        # Assess impact
        overall_impact_score = assessor.assess_impact()

        # Print results
        print("Mental Models:")
        for model in assessor.get_mental_models():
            print(f"- {model.name}: {model.description} (Impact Score: {model.impact_score:.2f})")
        print(f"\nOverall Impact Score: {overall_impact_score:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
