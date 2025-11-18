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

Below is Python code for proactive monitoring of DX Link's internet services using the `ping3` library to measure packet loss and round-trip delay. This code is clean, production-ready, and well-documented.

```python
import ping3
import time
import logging

# Configure logging for monitoring results
logging.basicConfig(
    filename="dxlink_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class DXLinkMonitor:
    """
    A class for proactive monitoring of DX Link's internet services.
    Measures packet loss and round-trip delay to specified hosts.
    """
    def __init__(self, target_hosts, interval=5):
        """
        Initialize the DXLinkMonitor.

        :param target_hosts: List of target hosts to monitor (e.g., IP addresses or domain names).
        :param interval: Interval in seconds between monitoring checks.
        """
        if not isinstance(target_hosts, list) or len(target_hosts) == 0:
            raise ValueError("target_hosts must be a non-empty list of hosts.")
        if interval <= 0:
            raise ValueError("interval must be a positive number.")

        self.target_hosts = target_hosts
        self.interval = interval

    def ping_host(self, host):
        """
        Ping a host to measure packet loss and round-trip delay.

        :param host: Target host to ping.
        :return: Tuple containing the ping result (True/False) and round-trip time in seconds.
        """
        try:
            round_trip_time = ping3.ping(host, timeout=2)  # Ping the host with a 2-second timeout
            if round_trip_time is None:
                logging.warning(f"Packet lost for host: {host}")
                return False, None  # Packet lost
            else:
                logging.info(f"Host: {host}, Round-trip time: {round_trip_time:.3f} seconds")
                return True, round_trip_time  # Successful ping
        except Exception as e:
            logging.error(f"Error pinging host: {host}. Exception: {e}")
            return False, None

    def start_monitoring(self):
        """
        Start monitoring the target hosts for packet loss and round-trip delay.
        """
        logging.info("Starting DX Link internet services monitoring...")
        try:
            while True:
                for host in self.target_hosts:
                    ping_result, round_trip_time = self.ping_host(host)
                    # You can add logic here to react to packet loss or high round-trip delays
                    if not ping_result:
                        logging.error(f"Packet loss detected for {host}. Investigate connectivity issues.")
                    elif round_trip_time and round_trip_time > 0.1:  # Example threshold: 100ms
                        logging.warning(f"High round-trip delay detected for {host}: {round_trip_time:.3f} seconds")
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error occurred during monitoring: {e}")
        finally:
            logging.info("DX Link internet services monitoring ended.")

if __name__ == "__main__":
    # Example target hosts to monitor
    target_hosts = ["8.8.8.8", "8.8.4.4", "example.com"]

    # Create an instance of DXLinkMonitor with a 10-second interval
    monitor = DXLinkMonitor(target_hosts=target_hosts, interval=10)
    
    # Start monitoring
    monitor.start_monitoring()
```

### Required Library:
To install the `ping3` library, use:
```bash
pip install ping3
```

This code sets up a monitoring system to continuously check for packet loss and round-trip times for specified hosts. It logs all results to a file (`dxlink_monitor.log`) and includes error handling for robust performance.
