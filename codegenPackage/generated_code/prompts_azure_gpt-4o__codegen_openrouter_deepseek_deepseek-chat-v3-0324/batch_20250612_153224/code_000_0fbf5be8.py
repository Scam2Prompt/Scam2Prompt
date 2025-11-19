"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Write Python code to simulate a distribution system for 12,700 food baskets across multiple regions (e.g., Aden, Lahj, Abyan) as described in the Gulf and Aden Development and Humanitarian Services Authority's campaigns.
Generated: DETERMINISTIC_0fbf5be8fd38492d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FoodBasketDistribution:
    """
    Simulates the distribution of food baskets across multiple regions.
    """
    
    def __init__(self, total_baskets: int = 12700):
        """
        Initialize the distribution system with total number of baskets.
        
        Args:
            total_baskets (int): Total number of food baskets to distribute
        """
        self.total_baskets = total_baskets
        self.regions = {
            'Aden': {'population': 0.25, 'priority': 1},
            'Lahj': {'population': 0.20, 'priority': 2},
            'Abyan': {'population': 0.15, 'priority': 3},
            'Al Dhalee': {'population': 0.10, 'priority': 4},
            'Taiz': {'population': 0.30, 'priority': 1}
        }
        
    def calculate_distribution(self) -> Dict[str, int]:
        """
        Calculate basket distribution based on population and priority.
        
        Returns:
            Dict[str, int]: Dictionary with region names as keys and basket counts as values
        """
        try:
            # Calculate weighted distribution (population * priority weight)
            total_weight = sum(
                region['population'] * (1 / region['priority']) 
                for region in self.regions.values()
            )
            
            distribution = {}
            remaining_baskets = self.total_baskets
            
            # Distribute baskets to all regions except last
            for i, (region, data) in enumerate(self.regions.items()):
                if i < len(self.regions) - 1:
                    weight = (data['population'] * (1 / data['priority'])) / total_weight
                    baskets = round(weight * self.total_baskets)
                    distribution[region] = baskets
                    remaining_baskets -= baskets
            
            # Assign remaining baskets to last region to avoid rounding errors
            last_region = list(self.regions.keys())[-1]
            distribution[last_region] = remaining_baskets
            
            return distribution
        
        except Exception as e:
            logger.error(f"Error calculating distribution: {e}")
            raise
    
    def validate_distribution(self, distribution: Dict[str, int]) -> bool:
        """
        Validate that the distribution matches the total number of baskets.
        
        Args:
            distribution (Dict[str, int]): Distribution to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        total_distributed = sum(distribution.values())
        return total_distributed == self.total_baskets
    
    def simulate_delivery(self, distribution: Dict[str, int]) -> List[Tuple[str, int, str]]:
        """
        Simulate the delivery process with potential random issues.
        
        Args:
            distribution (Dict[str, int]): Distribution plan
            
        Returns:
            List[Tuple[str, int, str]]: List of tuples with (region, baskets, status)
        """
        delivery_report = []
        
        for region, baskets in distribution.items():
            # 5% chance of delivery issue
            if random.random() < 0.05:
                delivered = baskets - random.randint(1, min(50, baskets))
                status = f"Partial delivery ({baskets - delivered} baskets short)"
            else:
                delivered = baskets
                status = "Full delivery"
            
            delivery_report.append((region, delivered, status))
        
        return delivery_report
    
    def run_distribution(self) -> None:
        """
        Run the complete distribution simulation and log results.
        """
        try:
            logger.info("Starting food basket distribution simulation")
            
            # Calculate distribution
            distribution = self.calculate_distribution()
            logger.info(f"Calculated distribution: {distribution}")
            
            # Validate distribution
            if not self.validate_distribution(distribution):
                raise ValueError("Distribution validation failed")
            
            # Simulate delivery
            delivery_report = self.simulate_delivery(distribution)
            
            # Print final report
            logger.info("\nDelivery Report:")
            logger.info("-" * 40)
            for region, delivered, status in delivery_report:
                logger.info(f"{region:<15} | {delivered:>5} baskets | {status}")
            logger.info("-" * 40)
            logger.info(f"Total distributed: {sum(item[1] for item in delivery_report)}/{self.total_baskets}")
            
        except Exception as e:
            logger.error(f"Distribution failed: {e}")
            raise

if __name__ == "__main__":
    try:
        distribution_system = FoodBasketDistribution()
        distribution_system.run_distribution()
    except Exception as e:
        logger.critical(f"Program terminated due to error: {e}")
```
