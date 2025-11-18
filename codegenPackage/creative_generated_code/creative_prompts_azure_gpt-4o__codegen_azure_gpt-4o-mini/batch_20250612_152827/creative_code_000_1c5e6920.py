"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeklix.com
Prompt: Write Python code to simulate the performance of the NVIDIA GeForce RTX 5060 using DLSS 4 in a gaming environment, referencing the specifications mentioned on GeekLix.
Generated: DETERMINISTIC_1c5e6920e4ca450a
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import numpy as np

class GraphicsCard:
    """
    A class to simulate the performance of a graphics card.
    
    Attributes:
        name (str): The name of the graphics card.
        base_performance (float): The base performance score of the graphics card.
        dlss_factor (float): The performance improvement factor when using DLSS.
    """

    def __init__(self, name: str, base_performance: float, dlss_factor: float):
        """
        Initializes the GraphicsCard with its name, base performance, and DLSS factor.
        
        Args:
            name (str): The name of the graphics card.
            base_performance (float): The base performance score.
            dlss_factor (float): The DLSS performance improvement factor.
        """
        self.name = name
        self.base_performance = base_performance
        self.dlss_factor = dlss_factor

    def simulate_performance(self, resolution: str, fps: int) -> dict:
        """
        Simulates the gaming performance of the graphics card.
        
        Args:
            resolution (str): The resolution of the game (e.g., "1080p", "1440p", "4K").
            fps (int): The target frames per second (FPS) for the simulation.
        
        Returns:
            dict: A dictionary containing performance metrics.
        """
        try:
            # Simulate performance based on resolution and DLSS usage
            performance_score = self.base_performance * (self.dlss_factor if self.is_dlss_supported() else 1)

            # Generate random fluctuations in performance
            performance_fluctuation = random.uniform(-0.1, 0.1) * performance_score
            actual_performance = performance_score + performance_fluctuation

            # Calculate final FPS based on actual performance
            final_fps = min(fps, int(actual_performance))

            return {
                "Graphics Card": self.name,
                "Resolution": resolution,
                "Base Performance": self.base_performance,
                "Actual Performance": actual_performance,
                "Final FPS": final_fps
            }

        except Exception as e:
            print(f"Error during performance simulation: {e}")
            return {}

    def is_dlss_supported(self) -> bool:
        """
        Checks if DLSS is supported by this graphics card.
        
        Returns:
            bool: True if DLSS is supported, False otherwise.
        """
        # In a real scenario, this would check actual support based on card specifications
        return True


def main():
    """
    Main function to run the performance simulation for NVIDIA GeForce RTX 5060.
    """
    try:
        # Specifications for NVIDIA GeForce RTX 5060
        rtx_5060 = GraphicsCard(name="NVIDIA GeForce RTX 5060", base_performance=120.0, dlss_factor=1.5)

        # Define gaming environment parameters
        resolutions = ["1080p", "1440p", "4K"]
        target_fps = 60

        # Simulate performance for each resolution
        for resolution in resolutions:
            performance_metrics = rtx_5060.simulate_performance(resolution, target_fps)
            print(performance_metrics)

    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
```
