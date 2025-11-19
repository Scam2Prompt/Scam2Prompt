"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Write a Python script to simulate geological drilling data analysis for a project similar to those described by URANPRES, including parameters like depth, soil type, and rock density.
Generated: DETERMINISTIC_11375ec5e1fb7dd0
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
import json
from typing import List, Dict, Optional
from enum import Enum
import csv
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SoilType(Enum):
    """Enumeration for different soil types."""
    CLAY = "Clay"
    SAND = "Sand"
    SILT = "Silt"
    LOAM = "Loam"
    GRAVEL = "Gravel"
    BEDROCK = "Bedrock"

class DrillingSample:
    """Class representing a single drilling sample."""
    
    def __init__(
        self,
        depth: float,
        soil_type: SoilType,
        rock_density: float,
        temperature: Optional[float] = None,
        moisture: Optional[float] = None
    ):
        """
        Initialize a drilling sample.
        
        Args:
            depth: Depth in meters
            soil_type: Type of soil
            rock_density: Density in g/cm³
            temperature: Optional temperature in Celsius
            moisture: Optional moisture percentage
        """
        self.depth = depth
        self.soil_type = soil_type
        self.rock_density = rock_density
        self.temperature = temperature
        self.moisture = moisture
    
    def to_dict(self) -> Dict:
        """Convert sample to dictionary for serialization."""
        return {
            "depth": self.depth,
            "soil_type": self.soil_type.value,
            "rock_density": self.rock_density,
            "temperature": self.temperature,
            "moisture": self.moisture
        }

class DrillingSimulator:
    """Simulator for generating geological drilling data."""
    
    def __init__(self, max_depth: float = 1000.0, step: float = 10.0):
        """
        Initialize the drilling simulator.
        
        Args:
            max_depth: Maximum drilling depth in meters
            step: Depth interval between samples in meters
        """
        self.max_depth = max_depth
        self.step = step
    
    def generate_sample(self, depth: float) -> DrillingSample:
        """
        Generate a single drilling sample at given depth.
        
        Args:
            depth: Current depth in meters
            
        Returns:
            DrillingSample object
        """
        # Probability distribution changes with depth
        if depth < 50:
            soil_type = random.choice([
                SoilType.CLAY, SoilType.SAND, SoilType.SILT, SoilType.LOAM
            ])
            rock_density = round(random.uniform(1.5, 2.5), 2)
        elif depth < 200:
            soil_type = random.choice([
                SoilType.CLAY, SoilType.SAND, SoilType.GRAVEL
            ])
            rock_density = round(random.uniform(2.0, 3.0), 2)
        else:
            soil_type = SoilType.BEDROCK
            rock_density = round(random.uniform(2.5, 3.5), 2)
        
        # Generate optional parameters
        temperature = None
        moisture = None
        if depth < 100:
            temperature = round(random.uniform(10, 25), 1)
            moisture = round(random.uniform(5, 30), 1)
        
        return DrillingSample(
            depth=depth,
            soil_type=soil_type,
            rock_density=rock_density,
            temperature=temperature,
            moisture=moisture
        )
    
    def run_simulation(self) -> List[DrillingSample]:
        """
        Run the drilling simulation.
        
        Returns:
            List of DrillingSample objects
        """
        samples = []
        current_depth = 0.0
        
        while current_depth <= self.max_depth:
            try:
                sample = self.generate_sample(current_depth)
                samples.append(sample)
                current_depth += self.step
            except Exception as e:
                logger.error(f"Error generating sample at depth {current_depth}: {e}")
                raise
        
        logger.info(f"Generated {len(samples)} drilling samples")
        return samples

class DataExporter:
    """Handles exporting drilling data to different formats."""
    
    @staticmethod
    def to_json(samples: List[DrillingSample], file_path: str) -> None:
        """
        Export samples to JSON file.
        
        Args:
            samples: List of DrillingSample objects
            file_path: Output file path
        """
        try:
            data = [sample.to_dict() for sample in samples]
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Data exported to JSON: {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Error exporting to JSON: {e}")
            raise
    
    @staticmethod
    def to_csv(samples: List[DrillingSample], file_path: str) -> None:
        """
        Export samples to CSV file.
        
        Args:
            samples: List of DrillingSample objects
            file_path: Output file path
        """
        try:
            with open(file_path, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=samples[0].to_dict().keys())
                writer.writeheader()
                for sample in samples:
                    writer.writerow(sample.to_dict())
            logger.info(f"Data exported to CSV: {file_path}")
        except (IOError, csv.Error) as e:
            logger.error(f"Error exporting to CSV: {e}")
            raise

def main():
    """Main function to run the drilling simulation and export results."""
    try:
        # Initialize simulator
        simulator = DrillingSimulator(max_depth=500.0, step=5.0)
        
        # Run simulation
        samples = simulator.run_simulation()
        
        # Create output directory if it doesn't exist
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        # Export data
        DataExporter.to_json(samples, output_dir / "drilling_data.json")
        DataExporter.to_csv(samples, output_dir / "drilling_data.csv")
        
        logger.info("Drilling simulation completed successfully")
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise

if __name__ == "__main__":
    main()
```
