"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raydium.ink
Prompt: Generate a code snippet that implements a custom strategy for scaling operations based on business diagnostics.
Generated: DETERMINISTIC_61baca12d64cb2e6
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class ScalingStrategy:
    """
    A class to implement a custom strategy for scaling operations based on business diagnostics.
    """

    def __init__(self, max_scale=100, min_scale=10, threshold_up=0.75, threshold_down=0.25):
        """
        Initializes the scaling strategy with parameters.

        :param max_scale: Maximum scaling limit
        :param min_scale: Minimum scaling limit
        :param threshold_up: Threshold to scale up (e.g., utilization > 75%)
        :param threshold_down: Threshold to scale down (e.g., utilization < 25%)
        """
        self.max_scale = max_scale
        self.min_scale = min_scale
        self.threshold_up = threshold_up
        self.threshold_down = threshold_down
        self.current_scale = self.min_scale
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def compute_scale(self, utilization):
        """
        Computes the new scale based on utilization metrics.

        :param utilization: Business metric indicating the current utilization (0.0 to 1.0)
        :return: New scale value
        """
        try:
            # Validate utilization value
            if not (0.0 <= utilization <= 1.0):
                raise ValueError("Utilization must be between 0.0 and 1.0")

            if utilization > self.threshold_up:
                # Scale up: Increase by 20% of current scale while respecting max_scale
                new_scale = min(self.current_scale * 1.2, self.max_scale)
                self.logger.info(f"Scaling up: Utilization={utilization}, New Scale={new_scale}")
            elif utilization < self.threshold_down:
                # Scale down: Decrease by 20% of current scale while respecting min_scale
                new_scale = max(self.current_scale * 0.8, self.min_scale)
                self.logger.info(f"Scaling down: Utilization={utilization}, New Scale={new_scale}")
            else:
                # No scaling required, keep current scale
                new_scale = self.current_scale
                self.logger.info(f"No scaling: Utilization={utilization}, Current Scale={new_scale}")

            self.current_scale = new_scale
            return self.current_scale

        except Exception as e:
            self.logger.error(f"Error while computing scale: {e}")
            raise

if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Example usage of ScalingStrategy
    strategy = ScalingStrategy(max_scale=200, min_scale=50, threshold_up=0.8, threshold_down=0.3)

    # Simulate various utilization metrics
    utilization_metrics = [0.85, 0.65, 0.2, 0.9, 0.1]
    for utilization in utilization_metrics:
        try:
            new_scale = strategy.compute_scale(utilization)
            print(f"Utilization: {utilization}, New Scale: {new_scale}")
        except Exception as e:
            print(f"Error handling utilization {utilization}: {e}")
```
