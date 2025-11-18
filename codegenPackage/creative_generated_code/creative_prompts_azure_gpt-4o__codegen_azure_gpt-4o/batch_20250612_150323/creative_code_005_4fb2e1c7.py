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
import threading
import time
import random

# Constants for the simulation
CHECK_INTERVAL = 0.005  # 5 milliseconds
SHIFT_DURATION = 8 * 60 * 60  # 8 hours in seconds
TOTAL_SPOT_CHECKS = 7200000000  # 7.2 billion

# Function to simulate a spot check
def spot_check(machine_id):
    # Simulate a random performance metric between 0 and 100
    performance_metric = random.uniform(0, 100)
    
    # Simulate a threshold that flags an issue
    threshold = 50.0
    
    # Log if the metric is below the threshold
    if performance_metric < threshold:
        print(f"Warning: Machine {machine_id} performance dropped to {performance_metric:.2f}!")

# Function to manage spot checks for a single machine
def machine_monitor(machine_id, stop_event):
    checks_completed = 0
    start_time = time.time()
    
    try:
        while not stop_event.is_set():
            # Perform a spot check
            spot_check(machine_id)
            checks_completed += 1
            
            # Wait for the next check interval
            time.sleep(CHECK_INTERVAL)
            
            # Stop if the total number of checks is reached
            if checks_completed >= TOTAL_SPOT_CHECKS:
                print(f"Machine {machine_id} completed all spot checks.")
                break
    except Exception as e:
        print(f"Error occurred while monitoring Machine {machine_id}: {e}")
    finally:
        elapsed_time = time.time() - start_time
        print(f"Machine {machine_id} completed {checks_completed} checks in {elapsed_time:.2f} seconds.")

# Main simulation function
def simulate_shift(machine_count=10):
    # Create a stop event to signal threads to stop
    stop_event = threading.Event()
    
    # Create a thread for each machine
    threads = []
    for machine_id in range(1, machine_count + 1):
        thread = threading.Thread(target=machine_monitor, args=(machine_id, stop_event))
        threads.append(thread)
        thread.start()
    
    # Allow the simulation to run for the shift duration
    try:
        time.sleep(SHIFT_DURATION)
    except KeyboardInterrupt:
        print("Simulation interrupted. Stopping all machines...")
    finally:
        # Signal all threads to stop
        stop_event.set()
        for thread in threads:
            thread.join()
        print("All machines have stopped.")

# Entry point for the simulation
if __name__ == "__main__":
    simulate_shift(machine_count=10)  # Simulate 10 sewing machines
```
