"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Develop code to simulate the scaling of vaccine production from pilot-scale to large-scale manufacturing, referencing the expertise of CSL Seqirus employees in transforming small-scale products.
Generated: DETERMINISTIC_0e4c9f465476894f
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ProductionStage(Enum):
    """Enum representing different stages of vaccine production scaling."""
    PILOT = "Pilot-scale"
    SMALL_SCALE = "Small-scale"
    LARGE_SCALE = "Large-scale"

class VaccineProductionSimulator:
    """
    Simulates the scaling of vaccine production from pilot to large-scale manufacturing.
    Incorporates expertise from CSL Seqirus in transforming small-scale production.
    """
    
    def __init__(self, 
                 initial_yield: float = 0.8, 
                 initial_capacity: float = 1000,
                 scale_factors: Dict[ProductionStage, float] = None):
        """
        Initialize the vaccine production simulator.
        
        Args:
            initial_yield: Initial production yield (0-1)
            initial_capacity: Initial production capacity in doses
            scale_factors: Dictionary of scale factors for each production stage
        """
        self.current_stage = ProductionStage.PILOT
        self.current_yield = initial_yield
        self.current_capacity = initial_capacity
        
        # Default scale factors if none provided
        if scale_factors is None:
            self.scale_factors = {
                ProductionStage.PILOT: 1.0,
                ProductionStage.SMALL_SCALE: 5.0,
                ProductionStage.LARGE_SCALE: 20.0
            }
        else:
            self.scale_factors = scale_factors
            
        # Yield improvement factors based on CSL Seqirus expertise
        self.yield_improvements = {
            ProductionStage.PILOT: 1.0,
            ProductionStage.SMALL_SCALE: 1.2,  # 20% yield improvement
            ProductionStage.LARGE_SCALE: 1.5   # 50% yield improvement from pilot
        }
        
        logger.info("Vaccine production simulator initialized")
        
    def scale_production(self, target_stage: ProductionStage) -> bool:
        """
        Scale production to the target stage.
        
        Args:
            target_stage: Target production stage to scale to
            
        Returns:
            bool: True if scaling was successful, False otherwise
        """
        try:
            if target_stage.value <= self.current_stage.value:
                logger.warning(f"Cannot scale to {target_stage.value} from {self.current_stage.value}")
                return False
                
            # Calculate new capacity and yield
            scale_factor = self.scale_factors[target_stage] / self.scale_factors[self.current_stage]
            yield_improvement = self.yield_improvements[target_stage] / self.yield_improvements[self.current_stage]
            
            self.current_capacity *= scale_factor
            self.current_yield *= yield_improvement
            self.current_stage = target_stage
            
            logger.info(f"Successfully scaled to {target_stage.value} production")
            logger.info(f"New capacity: {self.current_capacity:,.0f} doses")
            logger.info(f"New yield: {self.current_yield:.1%}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error scaling production: {str(e)}")
            return False
    
    def simulate_production_run(self, batch_size: float) -> Tuple[int, int]:
        """
        Simulate a production run at current scale.
        
        Args:
            batch_size: Size of the production batch in doses
            
        Returns:
            Tuple of (successful_doses, failed_doses)
        """
        try:
            if batch_size > self.current_capacity:
                logger.warning(f"Batch size {batch_size} exceeds current capacity {self.current_capacity}")
                batch_size = self.current_capacity
                
            successful = int(batch_size * self.current_yield)
            failed = batch_size - successful
            
            logger.info(f"Production run: {successful:,} successful doses, {failed:,} failed doses")
            return successful, failed
            
        except Exception as e:
            logger.error(f"Error in production simulation: {str(e)}")
            return 0, 0
    
    def plot_production_scaling(self, stages: List[ProductionStage] = None):
        """
        Plot the production scaling across different stages.
        
        Args:
            stages: List of production stages to plot (defaults to all stages)
        """
        try:
            if stages is None:
                stages = list(ProductionStage)
                
            # Simulate scaling through each stage
            capacities = []
            yields = []
            current_sim = VaccineProductionSimulator(
                initial_yield=self.current_yield,
                initial_capacity=self.current_capacity,
                scale_factors=self.scale_factors
            )
            
            for stage in stages:
                current_sim.scale_production(stage)
                capacities.append(current_sim.current_capacity)
                yields.append(current_sim.current_yield * 100)  # Convert to percentage
                
            # Create plot
            fig, ax1 = plt.subplots(figsize=(10, 6))
            
            color = 'tab:blue'
            ax1.set_xlabel('Production Stage')
            ax1.set_ylabel('Production Capacity (doses)', color=color)
            ax1.plot([s.value for s in stages], capacities, 'o-', color=color)
            ax1.tick_params(axis='y', labelcolor=color)
            ax1.set_yscale('log')
            
            ax2 = ax1.twinx()
            color = 'tab:red'
            ax2.set_ylabel('Yield (%)', color=color)
            ax2.plot([s.value for s in stages], yields, 's--', color=color)
            ax2.tick_params(axis='y', labelcolor=color)
            
            plt.title('Vaccine Production Scaling Simulation')
            fig.tight_layout()
            plt.show()
            
        except Exception as e:
            logger.error(f"Error generating plot: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize simulator with pilot-scale parameters
        simulator = VaccineProductionSimulator(
            initial_yield=0.75,
            initial_capacity=5000,
            scale_factors={
                ProductionStage.PILOT: 1.0,
                ProductionStage.SMALL_SCALE: 10.0,
                ProductionStage.LARGE_SCALE: 100.0
            }
        )
        
        # Simulate scaling up production
        simulator.scale_production(ProductionStage.SMALL_SCALE)
        simulator.simulate_production_run(20000)
        
        simulator.scale_production(ProductionStage.LARGE_SCALE)
        simulator.simulate_production_run(100000)
        
        # Plot the scaling process
        simulator.plot_production_scaling()
        
    except Exception as e:
        logger.error(f"Error in example execution: {str(e)}")
```
