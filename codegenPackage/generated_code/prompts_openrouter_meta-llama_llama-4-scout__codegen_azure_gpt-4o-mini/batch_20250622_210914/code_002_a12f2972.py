"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Generate a code example for calculating the hardness of stainless steel tubes based on factors like steel band annealing treatment and carbon content.
Generated: DETERMINISTIC_a12f2972178193a5
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StainlessSteelTube:
    """
    A class to represent a stainless steel tube and calculate its hardness
    based on annealing treatment and carbon content.
    """

    def __init__(self, carbon_content: float, annealing_treatment: str):
        """
        Initializes the StainlessSteelTube instance.

        :param carbon_content: The carbon content in percentage (0-100).
        :param annealing_treatment: The type of annealing treatment ('none', 'full', 'partial').
        """
        self.carbon_content = carbon_content
        self.annealing_treatment = annealing_treatment.lower()
        self.hardness = self.calculate_hardness()

    def calculate_hardness(self) -> float:
        """
        Calculates the hardness of the stainless steel tube based on carbon content
        and annealing treatment.

        :return: The calculated hardness value.
        """
        # Validate carbon content
        if not (0 <= self.carbon_content <= 100):
            raise ValueError("Carbon content must be between 0 and 100.")

        # Base hardness based on carbon content
        hardness = 100 + (self.carbon_content * 2)

        # Adjust hardness based on annealing treatment
        if self.annealing_treatment == 'none':
            hardness += 10  # No treatment increases hardness
        elif self.annealing_treatment == 'full':
            hardness -= 15  # Full annealing decreases hardness
        elif self.annealing_treatment == 'partial':
            hardness -= 5   # Partial annealing slightly decreases hardness
        else:
            raise ValueError("Invalid annealing treatment. Choose 'none', 'full', or 'partial'.")

        return hardness

    def __str__(self) -> str:
        """
        Returns a string representation of the StainlessSteelTube instance.

        :return: A string describing the tube's properties.
        """
        return (f"Stainless Steel Tube:\n"
                f"  Carbon Content: {self.carbon_content}%\n"
                f"  Annealing Treatment: {self.annealing_treatment.capitalize()}\n"
                f"  Hardness: {self.hardness}")

# Example usage
if __name__ == "__main__":
    try:
        tube = StainlessSteelTube(carbon_content=0.5, annealing_treatment='full')
        print(tube)
    except ValueError as e:
        print(f"Error: {e}")
```
