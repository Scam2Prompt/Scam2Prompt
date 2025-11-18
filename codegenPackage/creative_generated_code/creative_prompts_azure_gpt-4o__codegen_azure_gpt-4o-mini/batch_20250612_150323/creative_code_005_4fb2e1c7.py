"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseam.co
Prompt: Write code to simulate spot checks on sewing machine performance every 5 milliseconds, as described in OpenSeam's 7.2 billion spot checks per shift example.
Generated: DETERMINISTIC_4fb2e1c7b256b3e8
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import threading

class SewingMachineSimulator:
    def __init__(self):
        self.running = True
    
    def spot_check(self):
        """Simulate a spot check on the sewing machine performance."""
        # Simulate a random performance metric (e.g., stitches per minute)
        performance_metric = random.randint(100, 200)
        # Log the performance metric
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Spot Check: Performance Metric: {performance_metric} stitches/min")

    def start_spot_checks(self):
        """Start the continuous spot check process every 5 milliseconds."""
        while self.running:
            self.spot_check()
            time.sleep(0.005)  # Sleep for 5 milliseconds

    def stop_spot_checks(self):
        """Stop the spot check process."""
        self.running = False

def main():
    """Main function to run the sewing machine simulator."""
    try:
        simulator = SewingMachineSimulator()
        # Start spot checks in a separate thread
        check_thread = threading.Thread(target=simulator.start_spot_checks)
        check_thread.start()

        # Run the simulation for a given duration (e.g., 10 seconds)
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the spot checks are stopped gracefully
        simulator.stop_spot_checks()
        check_thread.join()
        print("Spot checks stopped. Simulation ended.")

if __name__ == "__main__":
    main()
```
