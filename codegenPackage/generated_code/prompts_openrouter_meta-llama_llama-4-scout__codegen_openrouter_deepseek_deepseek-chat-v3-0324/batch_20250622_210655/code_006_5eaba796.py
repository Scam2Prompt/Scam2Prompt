"""
Generated Code Metadata:
========================
Original URL: https://fullport.net
Prompt: Develop a code to configure and test a network cable (e.g., CAT5, CAT6) using a network testing device.
Generated: DETERMINISTIC_5eaba796a0bc5934
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import subprocess
import time
from typing import Optional, Tuple

class NetworkCableTester:
    """
    A class to configure and test network cables using system commands and socket connections.
    Supports basic connectivity tests for CAT5, CAT6 cables.
    """
    
    def __init__(self, target_ip: str = "8.8.8.8", target_port: int = 80, timeout: int = 3):
        """
        Initialize the NetworkCableTester with target IP, port, and timeout.
        
        Args:
            target_ip (str): IP address to test connectivity (default: 8.8.8.8)
            target_port (int): Port number to test (default: 80)
            timeout (int): Connection timeout in seconds (default: 3)
        """
        self.target_ip = target_ip
        self.target_port = target_port
        self.timeout = timeout
    
    def check_interface_status(self, interface: str = "eth0") -> Tuple[bool, Optional[str]]:
        """
        Check the status of a network interface using system commands.
        
        Args:
            interface (str): Network interface name (default: eth0)
            
        Returns:
            Tuple[bool, Optional[str]]: (True if interface is up, error message if any)
        """
        try:
            result = subprocess.run(
                ["ip", "link", "show", interface],
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            if "state UP" in result.stdout:
                return True, None
            return False, f"Interface {interface} is down"
        except subprocess.TimeoutExpired:
            return False, "Command timed out"
        except subprocess.CalledProcessError as e:
            return False, f"Command failed: {e.stderr}"
        except Exception as e:
            return False, f"Unexpected error: {str(e)}"
    
    def test_ping(self) -> Tuple[bool, Optional[str]]:
        """
        Test basic connectivity using ping.
        
        Returns:
            Tuple[bool, Optional[str]]: (True if ping succeeds, error message if any)
        """
        try:
            result = subprocess.run(
                ["ping", "-c", "3", "-W", str(self.timeout), self.target_ip],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return True, None
            return False, f"Ping failed: {result.stderr}"
        except Exception as e:
            return False, f"Ping error: {str(e)}"
    
    def test_tcp_connection(self) -> Tuple[bool, Optional[str]]:
        """
        Test TCP connectivity to target IP and port.
        
        Returns:
            Tuple[bool, Optional[str]]: (True if connection succeeds, error message if any)
        """
        try:
            with socket.create_connection(
                (self.target_ip, self.target_port),
                timeout=self.timeout
            ):
                return True, None
        except socket.timeout:
            return False, "Connection timed out"
        except ConnectionRefusedError:
            return False, "Connection refused"
        except Exception as e:
            return False, f"Connection error: {str(e)}"
    
    def run_diagnostic(self, interface: str = "eth0") -> dict:
        """
        Run a full diagnostic test on the network cable.
        
        Args:
            interface (str): Network interface name (default: eth0)
            
        Returns:
            dict: Test results with status and messages
        """
        results = {
            "interface": interface,
            "interface_status": None,
            "ping_test": None,
            "tcp_test": None,
            "overall_status": False
        }
        
        # Check interface status
        interface_up, interface_msg = self.check_interface_status(interface)
        results["interface_status"] = {
            "status": interface_up,
            "message": interface_msg
        }
        
        if not interface_up:
            results["overall_status"] = False
            return results
        
        # Run ping test
        ping_success, ping_msg = self.test_ping()
        results["ping_test"] = {
            "status": ping_success,
            "message": ping_msg
        }
        
        # Run TCP test
        tcp_success, tcp_msg = self.test_tcp_connection()
        results["tcp_test"] = {
            "status": tcp_success,
            "message": tcp_msg
        }
        
        # Determine overall status
        results["overall_status"] = all([
            interface_up,
            ping_success,
            tcp_success
        ])
        
        return results

if __name__ == "__main__":
    tester = NetworkCableTester()
    results = tester.run_diagnostic()
    
    print("Network Cable Diagnostic Results:")
    print(f"Interface Status: {'OK' if results['interface_status']['status'] else 'FAIL'} - {results['interface_status']['message']}")
    print(f"Ping Test: {'OK' if results['ping_test']['status'] else 'FAIL'} - {results['ping_test']['message']}")
    print(f"TCP Test: {'OK' if results['tcp_test']['status'] else 'FAIL'} - {results['tcp_test']['message']}")
    print(f"\nOverall Status: {'PASS' if results['overall_status'] else 'FAIL'}")
```
