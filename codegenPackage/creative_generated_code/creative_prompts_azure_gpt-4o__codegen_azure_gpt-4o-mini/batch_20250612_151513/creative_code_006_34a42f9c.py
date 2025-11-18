"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Suggest libraries or tools for proactive monitoring of DX Link's internet services, focusing on packet loss and round trip delay metrics.
Generated: DETERMINISTIC_34a42f9c9ce399ff
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import statistics
import time

class InternetMonitor:
    """
    A class to monitor internet services for packet loss and round trip delay.
    """

    def __init__(self, host: str, interval: int = 60, count: int = 4):
        """
        Initializes the InternetMonitor with the target host, interval, and count of pings.
        
        :param host: The target host to ping (e.g., 'google.com').
        :param interval: Time in seconds between each monitoring check.
        :param count: Number of ping attempts per check.
        """
        self.host = host
        self.interval = interval
        self.count = count

    def ping(self) -> dict:
        """
        Pings the target host and collects round trip time and packet loss statistics.
        
        :return: A dictionary containing average round trip time and packet loss percentage.
        """
        try:
            # Run the ping command
            response = subprocess.run(
                ["ping", "-c", str(self.count), self.host],
                capture_output=True,
                text=True,
                check=True
            )
            
            output = response.stdout
            
            # Parse the output for average round trip time and packet loss percentage
            rtt_line = [line for line in output.splitlines() if 'avg' in line][0]
            packet_loss_line = output.splitlines()[-3]
            
            avg_rtt = float(rtt_line.split('/')[4])  # Extract average RTT
            packet_loss = float(packet_loss_line.split(',')[2].split()[0].strip('%'))  # Extract packet loss
            
            return {
                'average_rtt_ms': avg_rtt,
                'packet_loss_percent': packet_loss
            }
        
        except subprocess.CalledProcessError as e:
            print(f"Error executing ping command: {e}")
            return {'average_rtt_ms': None, 'packet_loss_percent': None}

    def monitor(self):
        """
        Continuously monitors the internet service at specified intervals.
        """
        while True:
            metrics = self.ping()
            print(f"Monitoring {self.host}: {metrics['average_rtt_ms']} ms avg RTT, {metrics['packet_loss_percent']}% packet loss")
            time.sleep(self.interval)

if __name__ == "__main__":
    # Example usage of the InternetMonitor class
    monitor = InternetMonitor(host='8.8.8.8', interval=60, count=4)
    monitor.monitor()
```
