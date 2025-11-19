"""
Generated Code Metadata:
========================
Original URL: https://thebase.network
Prompt: Write a basic code snippet to simulate network traffic analysis for a simple network setup.
Generated: DETERMINISTIC_12e0f65309624526
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class NetworkTrafficAnalyzer:
    """
    A class to simulate and analyze network traffic for a simple network setup.
    """

    def __init__(self, devices):
        """
        Initialize the network traffic analyzer with a list of devices.

        :param devices: List of device names in the network.
        """
        self.devices = devices
        self.traffic_data = {device: [] for device in devices}

    def simulate_traffic(self):
        """
        Simulate network traffic by generating random data packets for each device.
        """
        for device in self.devices:
            # Simulate random packet size (in KB) and timestamp
            packet_size = random.randint(1, 100)  # Packet size between 1KB and 100KB
            timestamp = time.time()
            self.traffic_data[device].append({"size": packet_size, "timestamp": timestamp})

    def analyze_traffic(self):
        """
        Analyze the network traffic and print a summary for each device.
        """
        for device, packets in self.traffic_data.items():
            total_packets = len(packets)
            total_data = sum(packet["size"] for packet in packets)
            print(f"Device: {device}")
            print(f"  Total Packets: {total_packets}")
            print(f"  Total Data: {total_data} KB")
            print(f"  Average Packet Size: {total_data / total_packets if total_packets > 0 else 0:.2f} KB")
            print("-" * 40)

    def run(self, iterations=5, interval=1):
        """
        Run the traffic simulation and analysis.

        :param iterations: Number of simulation iterations.
        :param interval: Time interval (in seconds) between iterations.
        """
        try:
            for i in range(iterations):
                print(f"--- Iteration {i + 1} ---")
                self.simulate_traffic()
                self.analyze_traffic()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nSimulation interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Define a simple network setup with 3 devices
    devices = ["Device_A", "Device_B", "Device_C"]

    # Create an instance of the NetworkTrafficAnalyzer
    analyzer = NetworkTrafficAnalyzer(devices)

    # Run the simulation for 5 iterations with a 2-second interval
    analyzer.run(iterations=5, interval=2)
```
