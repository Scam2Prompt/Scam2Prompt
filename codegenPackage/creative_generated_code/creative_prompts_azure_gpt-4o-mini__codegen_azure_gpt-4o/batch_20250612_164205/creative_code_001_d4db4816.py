"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.himsdemo.bste.live
Prompt: How can I implement a progress bar in a Health Information Management System using the Utility.ProgressBarPercent feature?
Generated: DETERMINISTIC_d4db4816b24cdcec
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import time

class Utility:
    @staticmethod
    def ProgressBarPercent(percentage, bar_width=50):
        """
        Renders a progress bar based on the given percentage.
        
        Args:
            percentage (float): Progress percentage (0 to 100).
            bar_width (int): The width of the progress bar in characters (default: 50).
        
        Returns:
            None
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")

        # Calculate the number of filled and unfilled segments
        filled_length = int(bar_width * (percentage / 100))
        empty_length = bar_width - filled_length
        
        # Create the progress bar string
        bar = "[" + "#" * filled_length + " " * empty_length + "]"
        print(f"\r{bar} {percentage:.2f}%", end="", flush=True)

# Simulate a task for the Health Information Management System (HIMS)
def simulate_hims_task():
    """
    Simulates a task in the Health Information Management System with a progress bar.
    
    Returns:
        None
    """
    print("Processing Health Information Management System Data...")
    total_steps = 100

    try:
        for step in range(total_steps + 1):  # Includes 100% completion
            # Simulate some work (e.g., data processing)
            time.sleep(0.05)  # Pause for simulation

            # Update progress bar
            Utility.ProgressBarPercent(percentage=step)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    else:
        print("\nTask completed successfully!")
    finally:
        print("\nExiting...")

# Run the simulation
if __name__ == "__main__":
    simulate_hims_task()
```
