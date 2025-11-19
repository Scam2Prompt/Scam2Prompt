"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Generate code to calculate the optimal fishing line class for Emanuelson Reels models, such as "Trout 2 Wide" and "Salmon," using their specifications from the website.
Generated: DETERMINISTIC_7dc70ec32d8cbe8e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Emanuelson Reels Optimal Fishing Line Class Calculator

class EmanuelsonReel:
    def __init__(self, model, max_drag, line_capacity):
        """
        Initialize an Emanuelson Reel object.

        Args:
        - model (str): The model of the reel.
        - max_drag (float): The maximum drag pressure of the reel in pounds.
        - line_capacity (dict): A dictionary containing the line capacity of the reel in yards for different line classes.

        Example:
        - line_capacity = {"4 lb monofilament": 200, "6 lb monofilament": 150}
        """
        self.model = model
        self.max_drag = max_drag
        self.line_capacity = line_capacity

    def calculate_optimal_line_class(self, target_species, target_weight):
        """
        Calculate the optimal fishing line class for a given target species and weight.

        Args:
        - target_species (str): The target species.
        - target_weight (float): The target weight of the species in pounds.

        Returns:
        - optimal_line_class (str): The optimal fishing line class.

        Raises:
        - ValueError: If the target weight is less than or equal to 0.
        """
        if target_weight <= 0:
            raise ValueError("Target weight must be greater than 0")

        # Assume a general guideline for line class selection based on target species and weight
        if target_species.lower() == "trout":
            if target_weight < 5:
                optimal_line_class = "4-6 lb monofilament"
            elif target_weight < 10:
                optimal_line_class = "6-8 lb monofilament"
            else:
                optimal_line_class = "8-10 lb monofilament"
        elif target_species.lower() == "salmon":
            if target_weight < 10:
                optimal_line_class = "10-12 lb monofilament"
            elif target_weight < 20:
                optimal_line_class = "12-15 lb monofilament"
            else:
                optimal_line_class = "15-20 lb monofilament"
        else:
            raise ValueError("Unsupported target species")

        # Check if the optimal line class is within the reel's line capacity
        if optimal_line_class in self.line_capacity:
            return optimal_line_class
        else:
            raise ValueError("Reel does not support the optimal line class")


def main():
    # Define Emanuelson Reels models and their specifications
    reels = {
        "Trout 2 Wide": EmanuelsonReel(
            "Trout 2 Wide",
            max_drag=10,
            line_capacity={"4 lb monofilament": 200, "6 lb monofilament": 150, "8 lb monofilament": 100}
        ),
        "Salmon": EmanuelsonReel(
            "Salmon",
            max_drag=20,
            line_capacity={"10 lb monofilament": 150, "12 lb monofilament": 120, "15 lb monofilament": 100}
        )
    }

    # Calculate optimal line class for a given target species and weight
    target_species = "Trout"
    target_weight = 7

    for model, reel in reels.items():
        try:
            optimal_line_class = reel.calculate_optimal_line_class(target_species, target_weight)
            print(f"Optimal line class for {model} targeting {target_species} at {target_weight} pounds: {optimal_line_class}")
        except ValueError as e:
            print(f"Error for {model}: {str(e)}")


if __name__ == "__main__":
    main()
```
