"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: How can I implement a foam recycling system using the XT500 EPS densifier to reduce waste hauling costs by 80%?
Generated: DETERMINISTIC_4da5112b21924eb8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class EPSDensifier:
    """
    A class representing the XT500 EPS densifier for foam recycling.
    The XT500 EPS densifier processes Expanded Polystyrene (EPS) foam to reduce waste volume.
    """
    
    def __init__(self, processing_capacity_per_hour_kg: float, efficiency_rate: float):
        """
        Initializes the EPSDensifier with processing capacity and efficiency rate.

        Args:
            processing_capacity_per_hour_kg (float): Maximum capacity in kilograms per hour.
            efficiency_rate (float): Efficiency rate as a percentage (e.g., 0.8 for 80%).
        """
        self.processing_capacity_per_hour_kg = processing_capacity_per_hour_kg
        self.efficiency_rate = efficiency_rate

    def densify(self, foam_weight_kg: float) -> float:
        """
        Processes the given weight of EPS foam and returns the densified weight.

        Args:
            foam_weight_kg (float): Weight of EPS foam to process in kilograms.

        Returns:
            float: Densified weight in kilograms after processing.
        """
        if foam_weight_kg <= 0:
            raise ValueError("Foam weight must be greater than zero.")
        
        if foam_weight_kg > self.processing_capacity_per_hour_kg:
            raise ValueError("Foam weight exceeds the maximum processing capacity.")

        # Reduced weight after densification (e.g., 80% reduction)
        densified_weight = foam_weight_kg * (1 - self.efficiency_rate)
        return densified_weight


class FoamRecyclingSystem:
    """
    A foam recycling system using the XT500 EPS densifier to reduce waste hauling costs.
    """

    def __init__(self, densifier: EPSDensifier):
        """
        Initializes the foam recycling system with an EPS densifier.

        Args:
            densifier (EPSDensifier): Instance of the EPSDensifier class.
        """
        self.densifier = densifier

    def process_foam_batch(self, foam_weights: list[float]) -> dict:
        """
        Processes a batch of foam weights and calculates total reduction.

        Args:
            foam_weights (list[float]): List of foam weights in kilograms to process.

        Returns:
            dict: Dictionary containing details of processing and total reduction.
        """
        if not foam_weights:
            raise ValueError("Foam weights list cannot be empty.")
        
        processed_batch = []
        total_initial_weight = 0
        total_final_weight = 0

        for weight in foam_weights:
            try:
                densified_weight = self.densifier.densify(weight)
                processed_batch.append({
                    "initial_weight": weight,
                    "densified_weight": densified_weight
                })
                total_initial_weight += weight
                total_final_weight += densified_weight
            except ValueError as e:
                print(f"Error processing weight {weight} kg: {e}")

        total_reduction = total_initial_weight - total_final_weight

        return {
            "processed_batch": processed_batch,
            "total_initial_weight_kg": total_initial_weight,
            "total_final_weight_kg": total_final_weight,
            "total_reduction_kg": total_reduction,
            "reduction_percentage": (total_reduction / total_initial_weight) * 100 if total_initial_weight > 0 else 0
        }


# Example usage:
if __name__ == "__main__":
    # Initialize the XT500 EPS densifier with 100 kg/hour capacity and 80% efficiency
    xt500_densifier = EPSDensifier(processing_capacity_per_hour_kg=100, efficiency_rate=0.8)

    # Create the foam recycling system
    foam_recycling_system = FoamRecyclingSystem(densifier=xt500_densifier)

    # Batch of foam weights to process (in kilograms)
    foam_weights_batch = [50, 30, 20, 10]

    # Process the batch and display results
    try:
        results = foam_recycling_system.process_foam_batch(foam_weights_batch)
        print("Foam Recycling Results:")
        print(results)
    except Exception as e:
        print(f"An error occurred: {e}")
```
