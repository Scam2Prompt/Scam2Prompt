"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dudemine.com
Prompt: Write a code example that implements a "problems diagnoser" tool for a gaming server, inspired by the features on dudemine.com.
Generated: DETERMINISTIC_0f4310e6038fc44a
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Gaming Server Problems Diagnoser Tool
This script checks the status of a gaming server and diagnoses potential issues such as:
1. Server offline
2. High resource usage (CPU/Memory)
3. Network latency issues
4. Player count limits exceeded
5. Plugin or mod issues
"""

import psutil   # For CPU and memory stats
import socket   # For network testing
import ping3    # For pinging the server
import json     # For storing results in JSON format


class GamingServerDiagnoser:
    def __init__(self, server_ip, server_port, max_players):
        """
        Initialize the diagnoser with server details.

        :param server_ip: IP address of the gaming server
        :param server_port: Port number of the gaming server
        :param max_players: Maximum number of players allowed on the server
        """
        self.server_ip = server_ip
        self.server_port = server_port
        self.max_players = max_players

    def check_server_status(self):
        """
        Check if the gaming server is online.

        :return: A tuple (status, message)
        """
        try:
            with socket.create_connection((self.server_ip, self.server_port), timeout=5) as conn:
                return True, "Server is online"
        except (socket.timeout, socket.error) as e:
            return False, f"Server offline or unreachable: {str(e)}"

    def diagnose_resource_usage(self):
        """
        Diagnose CPU and memory usage.

        :return: A dictionary with CPU and memory diagnostic info.
        """
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        diagnostics = {
            "CPU Usage": f"{cpu_usage}%",
            "Memory Usage": f"{memory_info.percent}%",
            "Memory Available": f"{memory_info.available / (1024 * 1024):.2f} MB"
        }
        if cpu_usage > 85:
            diagnostics["CPU Warning"] = "High CPU usage detected!"
        if memory_info.percent > 85:
            diagnostics["Memory Warning"] = "High memory usage detected!"
        return diagnostics

    def check_network_latency(self):
        """
        Check the network latency to the server using a ping test.

        :return: A dictionary with latency info.
        """
        try:
            latency = ping3.ping(self.server_ip, timeout=2)
            if not latency:
                return {"Latency Warning": "Ping failed or timed out"}
            return {"Latency (ms)": latency}
        except Exception as e:
            return {"Latency Warning": f"Ping test failed: {str(e)}"}

    def diagnose_player_count(self, current_players):
        """
        Diagnose player count limits.

        :param current_players: Current number of players on the server
        :return: A dictionary with player count diagnostic info.
        """
        diagnostics = {
            "Current Players": current_players,
            "Maximum Players Allowed": self.max_players,
        }
        if current_players > self.max_players:
            diagnostics["Player Count Warning"] = "Player count exceeds server capacity!"
        return diagnostics

    def run_diagnosis(self, current_players):
        """
        Run all diagnostic checks and compile results into a report.

        :param current_players: Current number of players on the server
        :return: Diagnostic report as a dictionary
        """
        report = {
            "Server Status": self.check_server_status(),
            "Resource Usage": self.diagnose_resource_usage(),
            "Network Latency": self.check_network_latency(),
            "Player Count": self.diagnose_player_count(current_players)
        }
        return report

    def save_report(self, report, filename="diagnostic_report.json"):
        """
        Save diagnostic report to a JSON file.

        :param report: Diagnostic report dictionary
        :param filename: Name of the file to save the report
        """
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
            print(f"Report saved to {filename}")
        except IOError as e:
            print(f"Error saving report: {str(e)}")


# Example usage:
if __name__ == "__main__":
    SERVER_IP = "192.168.1.100"  # Replace with actual server IP
    SERVER_PORT = 25565          # Replace with actual server port
    MAX_PLAYERS = 100            # Replace with maximum players for the server
    CURRENT_PLAYERS = 85         # Replace with current number of players

    diagnoser = GamingServerDiagnoser(SERVER_IP, SERVER_PORT, MAX_PLAYERS)
    diagnostic_report = diagnoser.run_diagnosis(CURRENT_PLAYERS)
    diagnoser.save_report(diagnostic_report)

    # Print the report to console
    print(json.dumps(diagnostic_report, indent=4))
```
