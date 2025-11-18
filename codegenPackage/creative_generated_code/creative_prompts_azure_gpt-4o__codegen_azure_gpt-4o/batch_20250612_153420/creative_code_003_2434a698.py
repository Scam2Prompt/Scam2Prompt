"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Write code to simulate the blending process of color masterbatches, including black and white masterbatches, using the specifications provided by M J Pigment & Additives.
Generated: DETERMINISTIC_2434a6983366d1b4
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MasterbatchBlender:
    """
    Class to simulate the blending process of color masterbatches, including black and white masterbatches.
    """
    
    def __init__(self):
        """
        Initialize the MasterbatchBlender with available masterbatch types.
        """
        self.masterbatch_types = {
            "black": {"density": 1.8},  # Density in g/cm³
            "white": {"density": 1.5},  # Density in g/cm³
            "red": {"density": 1.6},
            "blue": {"density": 1.7},
            "yellow": {"density": 1.4}
        }
    
    def blend_masterbatches(self, batch_spec):
        """
        Blend the masterbatches based on the given specifications.
        
        :param batch_spec: Dictionary specifying the percentage of each masterbatch to blend.
        :return: Dictionary with the final blended properties.
        """
        try:
            # Validate batch_spec input
            if not isinstance(batch_spec, dict):
                raise ValueError("Batch specifications must be provided as a dictionary.")
            
            total_percentage = sum(batch_spec.values())
            if total_percentage != 100:
                raise ValueError("Batch percentages must add up to 100.")
            
            # Initialize blended properties
            blended_density = 0.0
            
            # Calculate blended properties based on batch specification
            for color, percentage in batch_spec.items():
                if color not in self.masterbatch_types:
                    raise ValueError(f"Unknown masterbatch type: {color}")
                blended_density += self.masterbatch_types[color]["density"] * (percentage / 100)
            
            # Return blended properties as dictionary
            return {
                "blended_density": round(blended_density, 2),
                "composition": batch_spec
            }
        except Exception as e:
            print(f"Error during blending: {e}")
            return None
    
    def simulate_blending(self):
        """
        Simulate the blending process with random specifications.
        
        :return: Dictionary with the final blended properties of a random simulation.
        """
        try:
            # Generate random batch specification
            colors = list(self.masterbatch_types.keys())
            percentages = [random.randint(10, 40) for _ in range(len(colors))]
            
            # Normalize percentages to sum up to 100
            total = sum(percentages)
            normalized_percentages = [round(p / total * 100) for p in percentages]
            
            # Create a batch specification dictionary
            batch_spec = {color: normalized_percentages[i] for i, color in enumerate(colors)}
            
            # Blend masterbatches based on random specifications
            return self.blend_masterbatches(batch_spec)
        except Exception as e:
            print(f"Error during simulation: {e}")
            return None


# Main execution logic
if __name__ == "__main__":
    # Initialize the MasterbatchBlender
    blender = MasterbatchBlender()
    
    # Example 1: Blend masterbatches with user-defined specifications
    user_spec = {
        "black": 40,
        "white": 30,
        "red": 20,
        "blue": 10
    }
    result = blender.blend_masterbatches(user_spec)
    if result:
        print("User-defined blending result:")
        print(result)
    
    # Example 2: Simulate blending with random specifications
    simulated_result = blender.simulate_blending()
    if simulated_result:
        print("\nRandom simulation blending result:")
        print(simulated_result)
```
