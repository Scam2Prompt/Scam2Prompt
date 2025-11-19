"""
Generated Code Metadata:
========================
Original URL: https://www.sardiniameetsazores.eu
Prompt: Generate code to simulate the material flow and classification process in "مطحن من طراز MTW," referencing the technical details from the Sardinia Meets Azores webpage.
Generated: DETERMINISTIC_8dd8094d5c5bde7b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulation of material flow and classification process in a MTW-type mill.
Reference: Technical details from Sardinia Meets Azores webpage.
"""

import numpy as np
from enum import Enum
from typing import List, Dict, Tuple

class MaterialType(Enum):
    """Types of materials processed in the mill."""
    COARSE = 1
    MEDIUM = 2
    FINE = 3
    ULTRA_FINE = 4

class MillStage(Enum):
    """Processing stages in the MTW mill."""
    FEEDING = 1
    GRINDING = 2
    CLASSIFICATION = 3
    COLLECTION = 4

class Particle:
    """Represents a material particle in the mill."""
    
    def __init__(self, size: float, material_type: MaterialType):
        self.size = size  # in microns
        self.type = material_type
        
    def __repr__(self):
        return f"Particle(size={self.size}µm, type={self.type.name})"

class MTWMillSimulator:
    """Simulates the material flow and classification process in an MTW-type mill."""
    
    def __init__(self):
        self.stages = {
            MillStage.FEEDING: self._feeding_stage,
            MillStage.GRINDING: self._grinding_stage,
            MillStage.CLASSIFICATION: self._classification_stage,
            MillStage.COLLECTION: self._collection_stage
        }
        self.classifier_efficiency = 0.95  # 95% classification efficiency
        self.grinding_reduction_factor = 0.7  # 30% size reduction per pass
        
    def simulate_process(self, input_particles: List[Particle]) -> Dict[MaterialType, List[Particle]]:
        """
        Simulate the complete milling process.
        
        Args:
            input_particles: List of input particles to process
            
        Returns:
            Dictionary of classified particles by material type
        """
        current_particles = input_particles.copy()
        
        for stage in MillStage:
            current_particles = self.stages[stage](current_particles)
            
        return self._classify_particles(current_particles)
    
    def _feeding_stage(self, particles: List[Particle]) -> List[Particle]:
        """Simulate the feeding stage of the mill."""
        # In a real system, this would involve conveyor systems, etc.
        # For simulation, we just pass through the particles
        return particles
    
    def _grinding_stage(self, particles: List[Particle]) -> List[Particle]:
        """Simulate the grinding process."""
        processed_particles = []
        for particle in particles:
            # Reduce particle size according to reduction factor
            new_size = particle.size * self.grinding_reduction_factor
            processed_particles.append(Particle(new_size, particle.type))
        return processed_particles
    
    def _classification_stage(self, particles: List[Particle]) -> List[Particle]:
        """Simulate the classification process."""
        classified_particles = []
        for particle in particles:
            # Simulate classifier efficiency with random chance
            if np.random.random() < self.classifier_efficiency:
                classified_particles.append(particle)
        return classified_particles
    
    def _collection_stage(self, particles: List[Particle]) -> List[Particle]:
        """Simulate the collection of processed material."""
        # In a real system, this would involve cyclones, bag filters, etc.
        # For simulation, we just pass through the particles
        return particles
    
    def _classify_particles(self, particles: List[Particle]) -> Dict[MaterialType, List[Particle]]:
        """Classify particles by their final size ranges."""
        classified = {mat_type: [] for mat_type in MaterialType}
        
        for particle in particles:
            if particle.size > 100:
                particle.type = MaterialType.COARSE
            elif 50 < particle.size <= 100:
                particle.type = MaterialType.MEDIUM
            elif 10 < particle.size <= 50:
                particle.type = MaterialType.FINE
            else:
                particle.type = MaterialType.ULTRA_FINE
                
            classified[particle.type].append(particle)
            
        return classified

def generate_sample_particles(num_particles: int = 1000) -> List[Particle]:
    """Generate sample particles for simulation."""
    particles = []
    for _ in range(num_particles):
        # Generate random particle sizes between 1 and 200 microns
        size = np.random.uniform(1, 200)
        # Initially all particles are considered coarse
        particles.append(Particle(size, MaterialType.COARSE))
    return particles

def main():
    """Run the mill simulation with sample data."""
    # Generate sample particles
    input_particles = generate_sample_particles()
    
    # Initialize and run the mill simulator
    mill = MTWMillSimulator()
    results = mill.simulate_process(input_particles)
    
    # Print summary of results
    print("MTW Mill Simulation Results:")
    print("----------------------------")
    for mat_type, particles in results.items():
        print(f"{mat_type.name}: {len(particles)} particles")
        
    # Calculate and print size distribution
    print("\nSize Distribution:")
    for mat_type, particles in results.items():
        if particles:
            avg_size = sum(p.size for p in particles) / len(particles)
            print(f"{mat_type.name}: Avg size = {avg_size:.2f}µm")

if __name__ == "__main__":
    main()
```
