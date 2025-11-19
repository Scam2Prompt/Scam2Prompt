"""
Generated Code Metadata:
========================
Original URL: https://cyberconnectit.com
Prompt: Provide a Python script to perform penetration testing for a medium-sized business, as mentioned in CyberConnect's services.
Generated: DETERMINISTIC_46fa2a8440322e82
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import nmap
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define a class for Penetration Testing
class PenetrationTester:
    def __init__(self, target_ip, target_ports):
        """
        Initialize the PenetrationTester with target IP and ports.

        :param target_ip: The IP address of the target to test.
        :param target_ports: A list of ports to scan.
        """
        self.target_ip = target_ip
        self.target_ports = target_ports
        self.scanner = nmap.PortScanner()

    def scan_ports(self):
        """
        Scan the specified ports on the target IP using nmap.

        :return: A dictionary with port status.
        """
        port_status = {}
        for port in self.target_ports:
            try:
                self.scanner.scan(self.target_ip, str(port))
                port_status[port] = self.scanner[self.target_ip]['tcp'][port]['state']
            except Exception as e:
                port_status[port] = f"Error: {str(e)}"
        return port_status

    def check_http(self):
        """
        Check if the target IP is serving HTTP and HTTPS.

        :return: A dictionary with HTTP and HTTPS status.
        """
        http_status = {}
        for protocol in ['http', 'https']:
            url = f"{protocol}://{self.target_ip}"
            try:
                response = requests.get(url, timeout=5)
                http_status[protocol] = response.status_code
            except requests.RequestException as e:
                http_status[protocol] = f"Error: {str(e)}"
        return http_status

    def run_tests(self):
        """
        Run all penetration tests and return the results.

        :return: A dictionary containing port scan and HTTP check results.
        """
        results = {}
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_port_scan = executor.submit(self.scan_ports)
            future_http_check = executor.submit(self.check_http)

            for future in as_completed([future_port_scan, future_http_check]):
                try:
                    results.update(future.result())
                except Exception as e:
                    results['Error'] = str(e)
        return results

if __name__ == "__main__":
    # Define target IP and ports for testing
    TARGET_IP = "192.168.1.1"  # Replace with the target IP
    TARGET_PORTS = [22, 80, 443, 8080]  # Common ports to scan

    # Create a PenetrationTester instance
    tester = PenetrationTester(TARGET_IP, TARGET_PORTS)

    # Run the penetration tests
    test_results = tester.run_tests()

    # Print the results
    print("Penetration Test Results:")
    for key, value in test_results.items():
        print(f"{key}: {value}")
```

**Note:** Ensure that you have the required libraries installed (`nmap`, `requests`) and that you have permission to perform penetration testing on the target IP.
