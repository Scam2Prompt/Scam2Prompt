"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Optimize digital inventory for a sports business by identifying and actioning opportunities, including assessing performance and optimal potential of digital assets.
Generated: DETERMINISTIC_86ad6f9f95bd4423
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DigitalAsset:
    """
    Represents a digital asset in the inventory.
    Attributes:
        name (str): Name of the digital asset.
        performance (float): Current performance score of the asset (0-100).
        potential (float): Optimal potential score of the asset (0-100).
    """
    def __init__(self, name: str, performance: float, potential: float):
        self.name = name
        self.performance = performance
        self.potential = potential

    def improvement_needed(self) -> float:
        """
        Calculate the improvement needed to reach optimal potential.
        Returns:
            float: The difference between potential and performance.
        """
        return max(0, self.potential - self.performance)


class DigitalInventoryOptimizer:
    """
    Optimizes the digital inventory by identifying opportunities for improvement.
    Attributes:
        assets (List[DigitalAsset]): List of digital assets in the inventory.
    """
    def __init__(self, assets: List[DigitalAsset]):
        self.assets = assets

    def assess_performance(self) -> List[Dict[str, float]]:
        """
        Assess the performance of all digital assets and identify improvement opportunities.
        Returns:
            List[Dict[str, float]]: List of assets with their improvement needed.
        """
        improvement_list = []
        for asset in self.assets:
            improvement = asset.improvement_needed()
            improvement_list.append({
                'name': asset.name,
                'performance': asset.performance,
                'potential': asset.potential,
                'improvement_needed': improvement
            })
        return improvement_list

    def action_opportunities(self) -> None:
        """
        Take action on assets that need improvement.
        Logs the actions taken for each asset.
        """
        for asset in self.assets:
            improvement = asset.improvement_needed()
            if improvement > 0:
                logging.info(f"Asset '{asset.name}' needs improvement. "
                             f"Performance: {asset.performance}, Potential: {asset.potential}, "
                             f"Improvement Needed: {improvement}. Taking action...")
                # Placeholder for actual improvement logic
                self._improve_asset(asset)
            else:
                logging.info(f"Asset '{asset.name}' is performing optimally. No action needed.")

    def _improve_asset(self, asset: DigitalAsset) -> None:
        """
        Placeholder method to improve a digital asset.
        In a real-world scenario, this would contain logic to optimize the asset.
        """
        logging.info(f"Improving asset '{asset.name}'... (Simulated improvement process)")
        # Simulate improvement by setting performance equal to potential
        asset.performance = asset.potential


# Example usage
if __name__ == "__main__":
    # Create a list of digital assets
    assets = [
        DigitalAsset(name="Website", performance=75, potential=90),
        DigitalAsset(name="Mobile App", performance=60, potential=85),
        DigitalAsset(name="Social Media Campaign", performance=80, potential=80),
    ]

    # Initialize the optimizer
    optimizer = DigitalInventoryOptimizer(assets)

    # Assess performance
    performance_report = optimizer.assess_performance()
    for report in performance_report:
        logging.info(f"Asset: {report['name']}, Performance: {report['performance']}, "
                     f"Potential: {report['potential']}, Improvement Needed: {report['improvement_needed']}")

    # Action opportunities
    optimizer.action_opportunities()
```
