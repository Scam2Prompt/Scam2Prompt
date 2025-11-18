"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswapv2.epizy.com
Prompt: Write a Python script for testing bandwidth limits on a hosting service that claims unlimited bandwidth, such as iFastNet hosting.
Generated: DETERMINISTIC_080bea3f51cf6705
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import socket
import threading

class BandwidthTester:
    def __init__(self, host, port=80, duration=60):
        """
        Initializes the BandwidthTester with the target host and port.
        
        :param host: The hostname or IP address of the server to test.
        :param port: The port to connect to (default is 80 for HTTP).
        :param duration: The duration for which to run the test in seconds.
        """
        self.host = host
        self.port = port
        self.duration = duration
        self.stop_event = threading.Event()
        self.bytes_sent = 0

    def send_data(self):
        """
        Sends data to the host to test bandwidth.
        Continuously sends data until the duration expires or stopped.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                # Sending a large payload repeatedly
                payload = b'A' * 1024  # 1 KB of data
                start_time = time.time()

                while not self.stop_event.is_set():
                    sock.sendall(payload)
                    self.bytes_sent += len(payload)
                    # Check if duration has passed
                    if time.time() - start_time > self.duration:
                        break
        except Exception as e:
            print(f"Error during data transmission: {e}")

    def start_test(self):
        """
        Starts the bandwidth test in a separate thread.
        """
        self.thread = threading.Thread(target=self.send_data)
        self.thread.start()

    def stop_test(self):
        """
        Stops the bandwidth test and waits for the thread to finish.
        """
        self.stop_event.set()
        self.thread.join()
        print(f"Total bytes sent: {self.bytes_sent}")
        self.calculate_bandwidth()

    def calculate_bandwidth(self):
        """
        Calculates and prints the bandwidth in Mbps.
        """
        seconds = self.duration
        # Convert bytes to megabits
        megabits_sent = (self.bytes_sent * 8) / (1024 * 1024)
        bandwidth_mbps = megabits_sent / seconds
        print(f"Bandwidth: {bandwidth_mbps:.2f} Mbps")

if __name__ == "__main__":
    # Replace 'your.host.com' with the actual host you wish to test
    tester = BandwidthTester(host='your.host.com', duration=60)  # Run for 60 seconds
    tester.start_test()
    time.sleep(65)  # Allow some time to run the test
    tester.stop_test()
```
