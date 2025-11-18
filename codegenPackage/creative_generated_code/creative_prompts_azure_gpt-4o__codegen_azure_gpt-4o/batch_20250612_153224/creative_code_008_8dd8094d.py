"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sardiniameetsazores.eu
Prompt: Generate code to simulate the material flow and classification process in "مطحن من طراز MTW," referencing the technical details from the Sardinia Meets Azores webpage.
Generated: DETERMINISTIC_8dd8094d5c5bde7b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import logging

# Configure logging for error handling and process tracking
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define Material class to encapsulate properties of raw materials
class Material:
    def __init__(self, name, moisture_content, particle_size):
        """
        Initialize a Material object.
        :param name: Name of the material
        :param moisture_content: Moisture content as percentage
        :param particle_size: Particle size in microns
        """
        self.name = name
        self.moisture_content = moisture_content
        self.particle_size = particle_size

    def __repr__(self):
        """
        String representation for debugging.
        """
        return f"Material(name={self.name}, moisture_content={self.moisture_content}%, particle_size={self.particle_size}µm)"


# Define MillingMachine class to simulate the MTW milling process
class MillingMachine:
    def __init__(self, model, capacity, efficiency):
        """
        Initialize the MillingMachine object.
        :param model: Model of the milling machine
        :param capacity: Processing capacity in tons per hour
        :param efficiency: Efficiency percentage of the machine
        """
        self.model = model
        self.capacity = capacity
        self.efficiency = efficiency

    def process_material(self, material):
        """
        Simulate the milling process and classify the material.
        :param material: Material to be processed
        :return: Processed material details
        """
        try:
            logging.info(f"Starting process for material '{material.name}' on '{self.model}' machine.")

            # Check if material properties are within acceptable range
            if material.moisture_content > 10:
                raise ValueError("Moisture content exceeds acceptable limit.")
            if material.particle_size > 5000:
                raise ValueError("Particle size exceeds acceptable limit.")

            # Simulate classification process
            processed_size = material.particle_size * self.efficiency / 100
            logging.info(f"Material '{material.name}' processed successfully.")

            return {
                "original_size": material.particle_size,
                "processed_size": round(processed_size, 2),
                "efficiency": self.efficiency
            }
        except ValueError as e:
            logging.error(f"Error processing material '{material.name}': {str(e)}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize test material and machine
    test_material = Material(name="Raw Ore", moisture_content=8, particle_size=3200)
    mtw_machine = MillingMachine(model="MTW", capacity=20, efficiency=85)

    # Run the milling process
    result = mtw_machine.process_material(test_material)
    if result:
        logging.info(f"Processed material details: {result}")
    else:
        logging.info("Material processing failed.")
```
