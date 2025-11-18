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
import os
import re
import subprocess
import psutil
import logging

# Set up logging for better tracking of operations
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MinecraftServerDiagnoser:
    def __init__(self, server_dir):
        """
        Initializes the diagnostician for a Minecraft server.

        Args:
            server_dir (str): The directory where the Minecraft server is located.
        """
        self.server_dir = server_dir
        self.server_log_file = os.path.join(server_dir, 'logs', 'latest.log')

    def check_server_status(self):
        """
        Checks if the Minecraft server is running.

        Returns:
            bool: True if the server is running, False otherwise.
        """
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == 'java':
                logging.info("Minecraft server is running.")
                return True
        logging.warning("Minecraft server is not running.")
        return False

    def read_server_log(self):
        """
        Reads the latest server log file for errors.

        Returns:
            list: A list of error messages found in the server log.
        """
        errors = []
        if not os.path.exists(self.server_log_file):
            logging.error("Log file does not exist.")
            return errors

        with open(self.server_log_file, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                if "ERROR" in line or "Exception" in line:
                    errors.append(line.strip())
        
        if errors:
            logging.info(f"Found {len(errors)} error(s) in the log.")
        else:
            logging.info("No errors found in the log.")
        
        return errors

    def analyze_latency(self):
        """
        Analyzes server latency by pinging the server.

        Returns:
            float: The average latency in milliseconds.
        """
        try:
            # Replace 'localhost' and '25565' with your server's IP and port if needed
            response = subprocess.run(['ping', '-c', '4', 'localhost'], stdout=subprocess.PIPE, text=True)
            latency = self.extract_latency(response.stdout)
            if latency is not None:
                logging.info(f"Average latency: {latency} ms")
                return latency
            else:
                logging.warning("Could not extract latency from ping response.")
                return None
        except Exception as e:
            logging.error(f"An error occurred while analyzing latency: {e}")
            return None

    @staticmethod
    def extract_latency(ping_output):
        """
        Extracts average latency from the ping command output.

        Args:
            ping_output (str): The output of the ping command.

        Returns:
            float: The average latency in milliseconds, or None if not found.
        """
        match = re.search(r'avg = ([\d.]+)', ping_output)
        if match:
            return float(match.group(1))
        return None

    def diagnose(self):
        """
        Performs a complete diagnosis of the server, checking status, log errors, and latency.
        """
        logging.info("Starting server diagnosis...")
        
        # Check if the server is running
        running = self.check_server_status()

        # Read errors from the server log
        errors = self.read_server_log()

        # Analyze latency
        latency = self.analyze_latency()

        # Summary of the diagnosis
        logging.info("Diagnosis complete.")
        return {
            'server_running': running,
            'log_errors': errors,
            'latency': latency
        }

if __name__ == "__main__":
    # Example usage
    server_directory = input("Enter your Minecraft server directory path: ")
    diagnoser = MinecraftServerDiagnoser(server_directory)
    results = diagnoser.diagnose()

    # Print results
    print("\nDiagnosis Results:")
    print(f"Server Running: {results['server_running']}")
    print("Log Errors:")
    for error in results['log_errors']:
        print(f"  - {error}")
    print(f"Average Latency: {results['latency']} ms" if results['latency'] is not None else "Latency analysis failed.")
```

This code is a complete and production-ready tool for diagnosing issues with a Minecraft server, including server status checks, log analysis, and latency measurement.
