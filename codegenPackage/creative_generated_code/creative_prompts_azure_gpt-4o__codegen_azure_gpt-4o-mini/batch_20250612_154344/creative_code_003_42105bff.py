"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Write code to perform penetration testing and threat detection for a business network, inspired by the cybersecurity services detailed on the IMTS website.
Generated: DETERMINISTIC_42105bff2be39c5f
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import nmap
import socket
import subprocess
import json
import threading
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkScanner:
    def __init__(self, target):
        """Initialize the network scanner with the target."""
        self.target = target
        self.scanner = nmap.PortScanner()

    def scan_ports(self):
        """Scan the target for open ports using nmap."""
        logging.info(f"Starting port scan on {self.target}")
        try:
            self.scanner.scan(self.target, arguments='-sV')
            logging.info(f"Scan completed for {self.target}")
            return self.scanner[self.target]
        except Exception as e:
            logging.error(f"Error scanning ports: {e}")
            return None


class ThreatDetector:
    def __init__(self):
        """Initialize the threat detector."""
        pass

    def check_threats(self):
        """Check system for potential threats."""
        # This is a placeholder for actual threat detection logic
        try:
            # Simulating a threat check
            output = subprocess.check_output(['ps', '-aux'], universal_newlines=True)
            logging.info("Threat detection completed.")
            return self.process_threats(output)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error checking threats: {e}")
            return None

    def process_threats(self, output):
        """Process the output for potential threats."""
        threats = []
        for line in output.splitlines():
            if "malicious" in line:  # Replace with actual threat detection logic
                threats.append(line)
        return threats


class PenetrationTester:
    def __init__(self, target):
        """Initialize the penetration tester."""
        self.target = target
        self.scanner = NetworkScanner(target)
        self.detector = ThreatDetector()

    def perform_tests(self):
        """Perform penetration testing and threat detection."""
        # Run port scanning in a separate thread
        port_scan_thread = threading.Thread(target=self.scanner.scan_ports)
        port_scan_thread.start()

        # Run threat detection
        threats = self.detector.check_threats()

        # Wait for the port scan to complete
        port_scan_thread.join()

        # Output results
        logging.info(f"Threats detected: {json.dumps(threats, indent=2)}")


if __name__ == "__main__":
    # Example usage
    try:
        target_ip = socket.gethostbyname(input("Enter the target IP address: "))
        tester = PenetrationTester(target_ip)
        tester.perform_tests()
    except socket.gaierror as e:
        logging.error(f"Invalid target IP address: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

Make sure to install the required libraries before running this code:

```bash
pip install python-nmap
```

Also, ensure that you have the necessary permissions to run network scans and threat detections on your target network.
