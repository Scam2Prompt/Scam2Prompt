"""
Generated Code Metadata:
========================
Original URL: https://ultiuos.com
Prompt: Generate code to benchmark network performance using techniques similar to those mentioned in Ultious's network audit and performance benchmarking services.
Generated: DETERMINISTIC_23582849a962cd49
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import socket
import statistics
import threading

class NetworkBenchmark:
    def __init__(self, host, port, num_tests=10):
        """
        Initialize the NetworkBenchmark instance.

        :param host: The hostname or IP address of the server to test.
        :param port: The port number on which the server is listening.
        :param num_tests: The number of tests to run for benchmarking.
        """
        self.host = host
        self.port = port
        self.num_tests = num_tests
        self.latencies = []

    def ping_server(self):
        """
        Measure the latency to the server by sending a single packet.

        :return: The round-trip time in milliseconds.
        """
        start_time = time.time()
        try:
            with socket.create_connection((self.host, self.port), timeout=5) as sock:
                sock.sendall(b'PING')
                sock.recv(1024)  # Expecting a response
        except (socket.timeout, ConnectionRefusedError) as e:
            print(f"Connection error: {e}")
            return None
        end_time = time.time()
        return (end_time - start_time) * 1000  # Convert to milliseconds

    def run_benchmark(self):
        """
        Run the benchmark tests and collect latency data.
        """
        print(f"Starting benchmark on {self.host}:{self.port} for {self.num_tests} tests.")
        for i in range(self.num_tests):
            latency = self.ping_server()
            if latency is not None:
                self.latencies.append(latency)
                print(f"Test {i + 1}: Latency = {latency:.2f} ms")
            else:
                print(f"Test {i + 1}: Failed to reach server.")

    def report_results(self):
        """
        Report the results of the benchmark tests.
        """
        if not self.latencies:
            print("No successful tests to report.")
            return

        avg_latency = statistics.mean(self.latencies)
        min_latency = min(self.latencies)
        max_latency = max(self.latencies)

        print("\nBenchmark Results:")
        print(f"Average Latency: {avg_latency:.2f} ms")
        print(f"Minimum Latency: {min_latency:.2f} ms")
        print(f"Maximum Latency: {max_latency:.2f} ms")

def main():
    # Configuration for the benchmark
    HOST = '127.0.0.1'  # Replace with the target server's IP address
    PORT = 8080         # Replace with the target server's port
    NUM_TESTS = 10     # Number of tests to run

    benchmark = NetworkBenchmark(HOST, PORT, NUM_TESTS)
    benchmark.run_benchmark()
    benchmark.report_results()

if __name__ == "__main__":
    main()
```
