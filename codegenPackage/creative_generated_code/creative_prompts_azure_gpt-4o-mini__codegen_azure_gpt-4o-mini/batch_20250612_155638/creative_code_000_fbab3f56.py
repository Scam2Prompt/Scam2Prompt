"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultiuos.com
Prompt: Generate code for a network performance management tool that incorporates RF engineering principles as described on the Ultious website.
Generated: DETERMINISTIC_fbab3f5674722be4
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import time
import logging
import statistics
from typing import List, Tuple

# Configure logging for monitoring and troubleshooting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkPerformanceManager:
    def __init__(self, target_ip: str, target_port: int):
        """
        Initializes the NetworkPerformanceManager with the target IP and port.

        :param target_ip: IP address of the target server
        :param target_port: Port number of the target service
        """
        self.target_ip = target_ip
        self.target_port = target_port

    def ping(self, count: int = 4) -> List[float]:
        """
        Sends ICMP echo requests to the target IP address and measures response times.

        :param count: Number of ping requests to send
        :return: A list of response times in milliseconds
        """
        response_times = []

        for i in range(count):
            start_time = time.time()
            try:
                # Create a socket and set a timeout for the connection
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(1)  # 1 second timeout
                    sock.connect((self.target_ip, self.target_port))
                    response_times.append((time.time() - start_time) * 1000)  # Convert to ms
                    logging.info(f"Ping {i + 1}: Response time {response_times[-1]:.2f} ms")
            except socket.timeout:
                logging.error(f"Ping {i + 1}: Request timed out.")
            except socket.error as e:
                logging.error(f"Ping {i + 1}: Socket error - {e}")

            time.sleep(1)  # Wait before sending the next ping

        return response_times

    def analyze_performance(self, response_times: List[float]) -> Tuple[float, float, float]:
        """
        Analyzes the ping response times for performance metrics.

        :param response_times: A list of response times in milliseconds
        :return: A tuple containing the average, minimum, and maximum response times
        """
        if not response_times:
            logging.warning("No response times to analyze.")
            return 0.0, 0.0, 0.0

        average = statistics.mean(response_times)
        minimum = min(response_times)
        maximum = max(response_times)

        logging.info(f"Performance Analysis: Average = {average:.2f} ms, Min = {minimum:.2f} ms, Max = {maximum:.2f} ms")
        return average, minimum, maximum

if __name__ == "__main__":
    # Example usage of the NetworkPerformanceManager
    target_ip = "8.8.8.8"  # Google Public DNS
    target_port = 53  # DNS service

    manager = NetworkPerformanceManager(target_ip, target_port)
    
    # Perform ping test
    response_times = manager.ping(count=5)
    
    # Analyze the performance
    if response_times:
        manager.analyze_performance(response_times)
```
