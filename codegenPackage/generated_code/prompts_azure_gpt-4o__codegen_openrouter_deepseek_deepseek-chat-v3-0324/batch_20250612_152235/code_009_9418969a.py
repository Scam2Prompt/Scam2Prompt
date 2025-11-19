"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ie.pages.dev
Prompt: Create a script to simulate the WienerAI presale price increase mechanism, where the token price rises at defined intervals during the presale stages.
Generated: DETERMINISTIC_9418969a6ca6181f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from dataclasses import dataclass
from typing import List
from datetime import datetime, timedelta

@dataclass
class PresaleStage:
    """Represents a single stage in the presale with its duration and price."""
    name: str
    duration_hours: int
    start_price: float
    end_price: float
    price_increase_per_interval: float
    interval_minutes: int

class WienerAIPresaleSimulator:
    """Simulates the WienerAI token presale price increase mechanism."""
    
    def __init__(self, stages: List[PresaleStage]):
        """
        Initialize the simulator with presale stages.
        
        Args:
            stages: List of PresaleStage objects defining the presale structure
        """
        self.stages = stages
        self.current_stage_index = 0
        self.current_stage_start_time = datetime.now()
        self.current_price = stages[0].start_price if stages else 0.0
        
    def calculate_current_price(self) -> float:
        """Calculate the current token price based on elapsed time in current stage."""
        if not self.stages:
            return 0.0
        
        current_stage = self.stages[self.current_stage_index]
        elapsed_time = datetime.now() - self.current_stage_start_time
        elapsed_minutes = elapsed_time.total_seconds() / 60
        
        # Calculate number of completed intervals
        intervals_completed = int(elapsed_minutes / current_stage.interval_minutes)
        
        # Calculate price increase
        price_increase = intervals_completed * current_stage.price_increase_per_interval
        
        # Cap price at stage's end price
        new_price = min(
            current_stage.start_price + price_increase,
            current_stage.end_price
        )
        
        return new_price
    
    def update_stage_if_needed(self) -> bool:
        """Check if we need to move to the next stage and update if necessary."""
        if not self.stages:
            return False
            
        current_stage = self.stages[self.current_stage_index]
        elapsed_time = datetime.now() - self.current_stage_start_time
        
        if elapsed_time >= timedelta(hours=current_stage.duration_hours):
            # Move to next stage if available
            if self.current_stage_index + 1 < len(self.stages):
                self.current_stage_index += 1
                self.current_stage_start_time = datetime.now()
                self.current_price = self.stages[self.current_stage_index].start_price
                return True
        return False
    
    def run_simulation(self, update_interval_seconds: int = 60):
        """Run the presale simulation with periodic price updates."""
        print("Starting WienerAI Presale Simulation")
        print("===================================")
        
        try:
            while True:
                self.update_stage_if_needed()
                self.current_price = self.calculate_current_price()
                
                current_stage = self.stages[self.current_stage_index]
                elapsed_time = datetime.now() - self.current_stage_start_time
                
                print(
                    f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                    f"Stage: {current_stage.name} | "
                    f"Elapsed: {str(elapsed_time).split('.')[0]} | "
                    f"Current Price: ${self.current_price:.6f}"
                )
                
                time.sleep(update_interval_seconds)
                
        except KeyboardInterrupt:
            print("\nSimulation stopped by user.")
        except Exception as e:
            print(f"\nError occurred: {str(e)}")

def main():
    """Main function to configure and run the presale simulation."""
    # Define presale stages
    stages = [
        PresaleStage(
            name="Early Bird",
            duration_hours=24,
            start_price=0.0001,
            end_price=0.0003,
            price_increase_per_interval=0.00001,
            interval_minutes=30
        ),
        PresaleStage(
            name="Community Round",
            duration_hours=48,
            start_price=0.0003,
            end_price=0.0006,
            price_increase_per_interval=0.00002,
            interval_minutes=60
        ),
        PresaleStage(
            name="Final Round",
            duration_hours=72,
            start_price=0.0006,
            end_price=0.0010,
            price_increase_per_interval=0.00005,
            interval_minutes=120
        )
    ]
    
    simulator = WienerAIPresaleSimulator(stages)
    simulator.run_simulation()

if __name__ == "__main__":
    main()
```
