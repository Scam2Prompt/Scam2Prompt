"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dudemine.com
Prompt: Develop a Python-based tool that mimics the functionality of the "dudeminecraft server problems diagnoser" from dudemine.com, with features for troubleshooting server crashes and latency issues.
Generated: DETERMINISTIC_5846a00348cd9a16
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import socket
import time
from subprocess import Popen, PIPE

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("server_diagnoser.log"), logging.StreamHandler()],
)

class MinecraftServerDiagnoser:
    def __init__(self, server_ip, server_port):
        """
        Initializes the diagnoser with the server's IP and port.

        :param server_ip: IP address of the Minecraft server.
        :param server_port: Port of the Minecraft server.
        """
        self.server_ip = server_ip
        self.server_port = server_port

    def check_server_availability(self):
        """
        Checks if the server is reachable over the network.
        """
        logging.info("Checking server availability...")
        try:
            with socket.create_connection((self.server_ip, self.server_port), timeout=5):
                logging.info("Server is reachable.")
                return True
        except socket.error as e:
            logging.error(f"Server is not reachable: {e}")
            return False

    def check_cpu_usage(self):
        """
        Checks the server's CPU usage.
        """
        logging.info("Checking server CPU usage...")
        try:
            process = Popen(["mpstat", "-P", "ALL"], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                logging.info("CPU usage details retrieved successfully.")
                return stdout.decode('utf-8')
            else:
                logging.error(f"Failed to retrieve CPU usage: {stderr.decode('utf-8')}")
                return None
        except FileNotFoundError:
            logging.error("The 'mpstat' utility is not installed. Please install it to check CPU usage.")
            return None

    def check_latency(self):
        """
        Measures latency to the server using ping.
        """
        logging.info("Checking server latency...")
        try:
            process = Popen(["ping", "-c", "4", self.server_ip], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                logging.info("Latency details retrieved successfully.")
                return stdout.decode('utf-8')
            else:
                logging.error(f"Failed to measure latency: {stderr.decode('utf-8')}")
                return None
        except FileNotFoundError:
            logging.error("The 'ping' utility is not available on this system.")
            return None

    def diagnose_server(self):
        """
        Runs all diagnostic checks on the server.
        """
        logging.info("Starting server diagnostics...")
        if not self.check_server_availability():
            logging.warning("Server is unavailable. Further diagnostics cannot be performed.")
            return

        cpu_usage = self.check_cpu_usage()
        if cpu_usage:
            logging.info(f"CPU Usage:\n{cpu_usage}")

        latency = self.check_latency()
        if latency:
            logging.info(f"Latency:\n{latency}")

        logging.info("Server diagnostics completed.")

if __name__ == "__main__":
    # Modify these parameters to suit your server's details
    SERVER_IP = "your.server.ip.address"
    SERVER_PORT = 25565  # Default Minecraft server port

    # Create an instance of the diagnoser
    diagnoser = MinecraftServerDiagnoser(SERVER_IP, SERVER_PORT)

    # Run diagnostics
    diagnoser.diagnose_server()
```

### Notes:
1. Ensure that `mpstat` is installed for CPU usage checking (available in `sysstat` package on Linux).
2. Modify `SERVER_IP` and `SERVER_PORT` in the code with your Minecraft server's details.
3. This code demonstrates robust error handling and logging. Ensure necessary utilities like `ping` and `mpstat` are accessible on the system running the script.
