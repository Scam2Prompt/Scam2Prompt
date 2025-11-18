"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.raymasterbatch.com
Prompt: Develop a program to optimize pigment dispersion for automotive applications, using concepts from Ray Colors' nano masterbatch solutions.
Generated: DETERMINISTIC_b70d1fb239896919
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

class PigmentDispersionOptimizer:
    """
    A class to optimize pigment dispersion for automotive applications.
    The optimization is based on objectives such as color consistency and 
    stability of the pigment dispersion.
    """

    def __init__(self, base_colors, target_color, max_iterations=1000):
        """
        Initialize the optimizer with base colors and a target color.

        Parameters:
            base_colors (list): A list of base color values (in RGB).
            target_color (tuple): The desired target color in RGB.
            max_iterations (int): The maximum number of optimization iterations.
        """
        self.base_colors = np.array(base_colors)
        self.target_color = np.array(target_color)
        self.max_iterations = max_iterations

    def color_difference(self, pigments):
        """
        Calculate the color difference between the mixed color and target color.

        Parameters:
            pigments (np.array): The percentage of each base color.

        Returns:
            float: The Euclidean distance (color difference).
        """
        mixed_color = np.dot(pigments, self.base_colors)
        return np.linalg.norm(mixed_color - self.target_color)

    def optimize_dispersion(self):
        """
        Optimize the pigment dispersion to minimize the color difference.

        Returns:
            result (OptimizeResult): The optimization result containing the best pigment ratios.
        """
        # Initial guess: equal distribution of pigments
        initial_guess = np.ones(len(self.base_colors)) / len(self.base_colors)

        # Constraints: sum of pigment ratios must be equal to 1 and all must be >= 0
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = [(0, 1) for _ in self.base_colors]

        # Perform the optimization
        result = minimize(self.color_difference, initial_guess, 
                          method='SLSQP', bounds=bounds, constraints=constraints,
                          options={'maxiter': self.max_iterations})

        if not result.success:
            raise RuntimeError("Optimization failed: " + result.message)

        return result

    def plot_results(self, result):
        """
        Plot the optimization results for visual interpretation.

        Parameters:
            result (OptimizeResult): The optimization result containing the best pigment ratios.
        """
        pigments = result.x
        colors = [tuple((pigments[i] * self.base_colors[i]).astype(int)) for i in range(len(pigments))]

        plt.bar(range(len(colors)), pigments, color=colors)
        plt.xticks(range(len(colors)), [f'Color {i+1}' for i in range(len(colors))])
        plt.title('Optimized Pigment Ratios')
        plt.ylabel('Ratio')
        plt.xlabel('Base Colors')
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Define base colors as RGB values
        base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
        target_color = (100, 150, 200)  # Desired target color

        # Create an instance of the optimizer
        optimizer = PigmentDispersionOptimizer(base_colors, target_color)

        # Optimize the pigment dispersion
        optimization_result = optimizer.optimize_dispersion()

        # Display and plot the results
        print("Optimized Pigment Ratios:", optimization_result.x)
        optimizer.plot_results(optimization_result)

    except Exception as e:
        print(f"An error occurred: {e}")
```
