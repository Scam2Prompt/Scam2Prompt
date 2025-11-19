"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Write code to simulate spot checks on sewing machine performance every 5 milliseconds, as described in OpenSeam's 7.2 billion spot checks per shift example.
Generated: DETERMINISTIC_4fb2e1c7b256b3e8
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import threading

class SewingMachine:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.performance_data = []

    def perform_spot_check(self):
        """
        Simulates a performance check on the sewing machine.
        Records the performance metric (e.g., stitch quality).
        """
        # Simulate a performance metric (e.g., stitch quality)
        stitch_quality = random.uniform(0, 100)  # Random quality score between 0 and 100
        self.performance_data.append(stitch_quality)
        print(f"Machine {self.machine_id}: Spot check performed. Stitch quality: {stitch_quality:.2f}")

    def start_spot_checks(self, duration_ms):
        """
        Starts performing spot checks every 5 milliseconds for a specified duration.
        
        :param duration_ms: Total duration for which to perform spot checks in milliseconds.
        """
        end_time = time.time() + (duration_ms / 1000)  # Convert ms to seconds
        while time.time() < end_time:
            self.perform_spot_check()
            time.sleep(0.005)  # Sleep for 5 milliseconds

def main():
    # Create a list of sewing machines
    machines = [SewingMachine(machine_id=i) for i in range(1, 6)]  # 5 machines

    # Duration for spot checks in milliseconds
    duration_ms = 1000  # 1 second of checks

    # Create and start threads for each machine
    threads = []
    for machine in machines:
        thread = threading.Thread(target=machine.start_spot_checks, args=(duration_ms,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All spot checks completed.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
