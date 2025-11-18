"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Write a script to monitor and analyze network performance for security systems, inspired by the security and network services offered by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_e8e0379b3a4d8269
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import time
import datetime
import logging

# Configure logging to record network performance data and errors
logging.basicConfig(
    filename="network_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def ping_host(host: str) -> dict:
    """
    Ping a host to check its availability and response time.
    
    Args:
        host (str): The hostname or IP address to ping.
        
    Returns:
        dict: A dictionary containing success status, latency (ms), and error message (if any).
    """
    try:
        # Execute a ping command and capture output
        completed_process = subprocess.run(
            ["ping", "-c", "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        if completed_process.returncode == 0:
            # Extract round-trip time (latency) from output
            output_lines = completed_process.stdout.split("\n")
            for line in output_lines:
                if "time=" in line:
                    latency = float(line.split("time=")[1].split(" ")[0])
                    return {"success": True, "latency_ms": latency, "error": None}
        else:
            # If ping fails, log the error details
            return {"success": False, "latency_ms": None, "error": completed_process.stderr.strip()}
    except Exception as e:
        # Catch any other exceptions and log them
        return {"success": False, "latency_ms": None, "error": str(e)}

def monitor_network(host: str, interval: int = 5):
    """
    Continuously monitor the network performance of a given host.
    
    Args:
        host (str): The hostname or IP address to monitor.
        interval (int): The time interval (in seconds) between checks.
    """
    logging.info(f"Starting network monitoring for host: {host}")
    
    try:
        while True:
            # Perform a ping test
            result = ping_host(host)
            
            if result["success"]:
                logging.info(f"Host {host} is reachable. Latency: {result['latency_ms']} ms")
            else:
                logging.error(f"Host {host} is unreachable. Error: {result['error']}")
            
            # Wait for the specified interval before the next check
            time.sleep(interval)
    except KeyboardInterrupt:
        # Gracefully handle termination via Ctrl+C
        logging.info("Network monitoring terminated by user.")
    except Exception as e:
        # Log any unexpected exceptions
        logging.error(f"Unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify the host to monitor and interval (in seconds)
    target_host = "8.8.8.8"  # Example: Google Public DNS server
    monitoring_interval = 10  # Time interval in seconds
    
    # Validate user input
    if not isinstance(monitoring_interval, int) or monitoring_interval <= 0:
        print("Monitoring interval must be a positive integer.")
        logging.error("Invalid monitoring interval provided.")
        exit(1)

    if not target_host:
        print("Target host must be specified.")
        logging.error("No target host provided.")
        exit(1)
    
    # Start monitoring
    monitor_network(target_host, monitoring_interval)
```
