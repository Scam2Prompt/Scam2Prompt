"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbags.pages.dev
Prompt: Write a script to track the progress of MoonBag's presale stages, including the number of meters completed and the remaining meters until the next stage.
Generated: DETERMINISTIC_515c254dc4fe2220
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MoonBagPresaleTracker:
    def __init__(self, total_distance, stage_distances):
        """
        Initialize the presale tracker with the total distance and stage distances.

        :param total_distance: Total distance (in meters) for the presale completion
        :param stage_distances: List of distances (in meters) for each presale stage
        """
        self.total_distance = total_distance
        self.stage_distances = stage_distances
        self.completed_distance = 0
        self.current_stage_index = 0

    def update_progress(self, meters):
        """
        Update the completed distance by adding the given meters.

        :param meters: The number of meters to add to the completed distance
        :raises ValueError: If the meters to add is negative or exceeds remaining distance
        """
        if meters < 0:
            raise ValueError("Meters to add must be a non-negative value.")
        
        if self.completed_distance + meters > self.total_distance:
            raise ValueError("Completed distance cannot exceed total distance.")
        
        self.completed_distance += meters
        self.check_stage_progress()

    def check_stage_progress(self):
        """
        Check if the completed distance has reached the next stage and update the stage index accordingly.
        """
        while (self.current_stage_index < len(self.stage_distances) and 
               self.completed_distance >= self.stage_distances[self.current_stage_index]):
            self.current_stage_index += 1

    def get_progress(self):
        """
        Get the current progress information including completed distance and remaining distance until the next stage.

        :return: Dictionary containing completed distance, current stage, and remaining distance to next stage
        """
        if self.current_stage_index >= len(self.stage_distances):
            return {
                "completed_distance": self.completed_distance,
                "current_stage": "Completed",
                "remaining_distance_to_next_stage": 0
            }

        remaining_distance_to_next_stage = (
            self.stage_distances[self.current_stage_index] - self.completed_distance
        )
        
        return {
            "completed_distance": self.completed_distance,
            "current_stage": self.current_stage_index + 1,
            "remaining_distance_to_next_stage": remaining_distance_to_next_stage
        }


# Example usage
if __name__ == "__main__":
    # Define total distance for presale stages and the respective stage distances
    total_distance = 1000  # Total distance in meters
    stage_distances = [200, 500, 800]  # Distances for each presale stage

    # Initialize the presale tracker
    presale_tracker = MoonBagPresaleTracker(total_distance, stage_distances)

    # Update progress and print current status
    try:
        presale_tracker.update_progress(250)
        print(presale_tracker.get_progress())  # Check progress after adding 250 meters

        presale_tracker.update_progress(300)
        print(presale_tracker.get_progress())  # Check progress after adding another 300 meters

        presale_tracker.update_progress(300)  # Attempt to exceed total distance
        print(presale_tracker.get_progress())
    except ValueError as e:
        print(f"Error: {e}")
```
