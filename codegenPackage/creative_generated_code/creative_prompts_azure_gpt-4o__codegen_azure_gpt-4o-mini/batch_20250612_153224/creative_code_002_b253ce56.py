"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Generate code to simulate the effect of river diversion on local ecosystems, inspired by the campaigns against river exploitation discussed by "Čuvari Šare."
Generated: DETERMINISTIC_b253ce56ea4adb72
Batch ID: 20250612_153224
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

class RiverEcosystem:
    """
    Class to simulate the effect of river diversion on local ecosystems.
    """
    
    def __init__(self, length: int, width: int):
        """
        Initialize the river ecosystem with specified length and width.

        :param length: Length of the river (in segments).
        :param width: Width of the river (in segments).
        """
        self.length = length
        self.width = width
        self.ecosystem = np.zeros((length, width))  # Initialize the ecosystem grid
        self.diversion_effects = np.zeros((length, width))  # Effects of diversion

    def populate_ecosystem(self):
        """
        Populate the ecosystem with various species.
        """
        # Randomly assign species to the ecosystem (1 indicates presence of species)
        self.ecosystem = np.random.choice([0, 1], size=(self.length, self.width), p=[0.7, 0.3])

    def simulate_diversion(self, diversion_length: int):
        """
        Simulate the effect of river diversion.

        :param diversion_length: Length of the river segment to be diverted.
        """
        if diversion_length < 0 or diversion_length > self.length:
            raise ValueError("Diversion length must be between 0 and the length of the river.")

        # Apply diversion effects to the ecosystem
        for i in range(diversion_length):
            for j in range(self.width):
                if self.ecosystem[i, j] == 1:  # If species is present
                    self.diversion_effects[i, j] = -1  # Mark as negatively affected
                else:
                    self.diversion_effects[i, j] = 1  # Mark as positively affected (possible return)

        # Reduce species presence for affected segments
        self.ecosystem[:diversion_length, :] = np.maximum(self.ecosystem[:diversion_length, :] + self.diversion_effects[:diversion_length, :], 0)

    def visualize_ecosystem(self):
        """
        Visualize the current state of the ecosystem before and after diversion.
        """
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        
        # Before diversion
        ax[0].imshow(self.ecosystem, cmap='Greens', aspect='auto')
        ax[0].set_title('Ecosystem Before Diversion')
        ax[0].set_xlabel('Width of River')
        ax[0].set_ylabel('Length of River')
        
        # After diversion
        ax[1].imshow(self.ecosystem, cmap='Reds', aspect='auto')
        ax[1].set_title('Ecosystem After Diversion')
        ax[1].set_xlabel('Width of River')
        ax[1].set_ylabel('Length of River')
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    try:
        # Initialize river ecosystem
        river = RiverEcosystem(length=20, width=10)
        river.populate_ecosystem()  # Populate the ecosystem with species
        river.simulate_diversion(diversion_length=5)  # Simulate river diversion
        river.visualize_ecosystem()  # Visualize the results
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
