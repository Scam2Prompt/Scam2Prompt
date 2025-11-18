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
# Script to track MoonBag's presale progress across stages.

# Import necessary modules
import sys

def track_presale_progress(current_meters, stage_meters):
    """
    Tracks the progress of MoonBag's presale stages.

    Parameters:
    current_meters (int): The number of meters completed so far.
    stage_meters (list): A list of integers representing the meter thresholds for each stage.

    Returns:
    str: A summary of the current progress and remaining meters until the next stage.
    """
    try:
        if current_meters < 0:
            raise ValueError("Current meters cannot be negative.")
        if not stage_meters or not all(isinstance(m, int) and m > 0 for m in stage_meters):
            raise ValueError("Stage meters must be a list of positive integers.")

        for idx, threshold in enumerate(stage_meters):
            if current_meters < threshold:
                remaining_meters = threshold - current_meters
                return f"Stage {idx + 1}: {current_meters} meters completed. {remaining_meters} meters remaining until the next stage."

        return f"All presale stages completed! Total meters: {current_meters}"
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    try:
        # Example input data
        current_meters = int(input("Enter the number of meters completed: "))
        stage_meters = [100, 200, 300, 400]  # Example thresholds for presale stages

        # Track progress and display result
        result = track_presale_progress(current_meters, stage_meters)
        print(result)
    except ValueError:
        print("Please enter a valid integer for the number of meters.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
