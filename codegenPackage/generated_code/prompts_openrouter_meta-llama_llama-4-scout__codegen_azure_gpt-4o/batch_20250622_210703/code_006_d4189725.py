"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Compare and contrast different outsourcing models, such as team hiring and team assignment, for a software development project in Jordan.
Generated: DETERMINISTIC_d4189725a450642f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script compares and contrasts different outsourcing models for a software development project in Jordan.
The models considered are 'Team Hiring' and 'Team Assignment'. The comparison is based on factors such as cost,
flexibility, control, and expertise. The script uses a scoring system to evaluate each model and provides a summary
of the results.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import json

# Define the outsourcing models
class OutsourcingModel:
    def __init__(self, name, cost, flexibility, control, expertise):
        """
        Initialize an outsourcing model with its attributes.

        :param name: Name of the outsourcing model
        :param cost: Cost score (1-10, lower is better)
        :param flexibility: Flexibility score (1-10, higher is better)
        :param control: Control score (1-10, higher is better)
        :param expertise: Expertise score (1-10, higher is better)
        """
        self.name = name
        self.cost = cost
        self.flexibility = flexibility
        self.control = control
        self.expertise = expertise

    def calculate_total_score(self):
        """
        Calculate the total score for the model based on weighted factors.

        :return: Total score (higher is better)
        """
        # Define weights for each factor
        weights = {
            "cost": 0.3,  # Cost has 30% weight
            "flexibility": 0.25,  # Flexibility has 25% weight
            "control": 0.25,  # Control has 25% weight
            "expertise": 0.2  # Expertise has 20% weight
        }
        # Calculate weighted score
        total_score = (
            (10 - self.cost) * weights["cost"] +  # Lower cost is better
            self.flexibility * weights["flexibility"] +
            self.control * weights["control"] +
            self.expertise * weights["expertise"]
        )
        return total_score

    def to_dict(self):
        """
        Convert the model attributes to a dictionary for easy JSON serialization.

        :return: Dictionary representation of the model
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "flexibility": self.flexibility,
            "control": self.control,
            "expertise": self.expertise,
            "total_score": self.calculate_total_score()
        }


# Define the models with example data
team_hiring = OutsourcingModel(
    name="Team Hiring",
    cost=6,  # Moderate cost
    flexibility=8,  # High flexibility
    control=7,  # Moderate control
    expertise=9  # High expertise
)

team_assignment = OutsourcingModel(
    name="Team Assignment",
    cost=4,  # Lower cost
    flexibility=6,  # Moderate flexibility
    control=5,  # Lower control
    expertise=7  # Moderate expertise
)

# Compare the models
models = [team_hiring, team_assignment]
comparison_results = [model.to_dict() for model in models]

# Output the results
def save_results_to_file(results, filename="comparison_results.json"):
    """
    Save the comparison results to a JSON file.

    :param results: List of model comparison results
    :param filename: Name of the output file
    """
    try:
        with open(filename, "w") as file:
            json.dump(results, file, indent=4)
        print(f"Results successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving results to file: {e}")


# Display results in the console
print("Comparison Results:")
for result in comparison_results:
    print(json.dumps(result, indent=4))

# Save results to a file
save_results_to_file(comparison_results)
```
