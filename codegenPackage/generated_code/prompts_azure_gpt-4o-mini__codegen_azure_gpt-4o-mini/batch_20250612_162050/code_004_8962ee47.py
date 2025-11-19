"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Write a program that models the effects of automation on creative processes, based on the ideas presented in "KI, Gewalt und Krieg."
Generated: DETERMINISTIC_8962ee4773ec40ef
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import matplotlib.pyplot as plt

class CreativeProcess:
    """
    A class to model the creative process and the impact of automation on it.
    """

    def __init__(self, creativity_level: float, automation_level: float):
        """
        Initializes the CreativeProcess with a given creativity and automation level.

        :param creativity_level: Initial level of creativity (0 to 1)
        :param automation_level: Level of automation affecting creativity (0 to 1)
        """
        self.creativity_level = self._validate_level(creativity_level)
        self.automation_level = self._validate_level(automation_level)

    @staticmethod
    def _validate_level(level: float) -> float:
        """
        Validates that the level is between 0 and 1.

        :param level: The level to validate
        :return: The validated level
        :raises ValueError: If the level is not between 0 and 1
        """
        if not (0 <= level <= 1):
            raise ValueError("Level must be between 0 and 1.")
        return level

    def simulate_creativity(self, iterations: int) -> list:
        """
        Simulates the creative process over a number of iterations, factoring in automation.

        :param iterations: Number of iterations to simulate
        :return: A list of creativity levels over time
        """
        creativity_over_time = []
        for _ in range(iterations):
            # Simulate the effect of automation on creativity
            creativity_change = random.uniform(-0.1, 0.1) * (1 - self.automation_level)
            self.creativity_level += creativity_change
            self.creativity_level = self._validate_level(self.creativity_level)
            creativity_over_time.append(self.creativity_level)
        return creativity_over_time

    def plot_creativity(self, creativity_data: list):
        """
        Plots the creativity levels over time.

        :param creativity_data: List of creativity levels to plot
        """
        plt.figure(figsize=(10, 5))
        plt.plot(creativity_data, label='Creativity Level', color='blue')
        plt.title('Effects of Automation on Creative Processes')
        plt.xlabel('Iterations')
        plt.ylabel('Creativity Level')
        plt.ylim(0, 1)
        plt.axhline(y=0.5, color='r', linestyle='--', label='Average Creativity Level')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the simulation of the creative process.
    """
    try:
        # Initialize the creative process with a creativity level and automation level
        creativity_process = CreativeProcess(creativity_level=0.7, automation_level=0.3)
        
        # Simulate creativity over 100 iterations
        creativity_data = creativity_process.simulate_creativity(iterations=100)
        
        # Plot the results
        creativity_process.plot_creativity(creativity_data)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
