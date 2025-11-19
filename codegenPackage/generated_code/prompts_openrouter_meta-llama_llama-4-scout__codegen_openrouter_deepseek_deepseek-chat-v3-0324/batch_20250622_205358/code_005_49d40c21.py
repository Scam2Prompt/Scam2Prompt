"""
Generated Code Metadata:
========================
Original URL: https://btc-tools.org
Prompt: What are the system requirements for using BTC Tools, and how can I troubleshoot common issues with miner configuration and monitoring using this software?
Generated: DETERMINISTIC_49d40c2112791f7c
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
BTC Tools System Requirements Checker and Troubleshooter

This script checks system requirements for BTC Tools and provides
troubleshooting steps for common miner configuration and monitoring issues.
"""

import platform
import psutil
import socket
import subprocess
import sys
from typing import Dict, List, Tuple

# Constants
MIN_RAM_GB = 4
MIN_CPU_CORES = 2
MIN_DISK_SPACE_GB = 10
RECOMMENDED_OS = ['Windows', 'Linux']
MIN_PYTHON_VERSION = (3, 6)
BTC_TOOLS_PORTS = [3333, 4028, 8080]  # Common ports used by mining software

def check_system_requirements() -> Dict[str, Tuple[bool, str]]:
    """
    Check if the system meets BTC Tools requirements.
    Returns a dictionary with check results and messages.
    """
    results = {}
    
    # Check OS
    current_os = platform.system()
    os_supported = current_os in RECOMMENDED_OS
    results['os'] = (
        os_supported,
        f"OS: {current_os} {'is supported' if os_supported else 'not supported'}"
    )
    
    # Check RAM
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    ram_ok = ram_gb >= MIN_RAM_GB
    results['ram'] = (
        ram_ok,
        f"RAM: {ram_gb:.1f}GB {'>= ' if ram_ok else '< '}{MIN_RAM_GB}GB"
    )
    
    # Check CPU cores
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_ok = cpu_cores >= MIN_CPU_CORES if cpu_cores else False
    results['cpu'] = (
        cpu_ok,
        f"CPU Cores: {cpu_cores if cpu_cores else 'N/A'} {'>= ' if cpu_ok else '< '}{MIN_CPU_CORES}"
    )
    
    # Check disk space
    try:
        disk = psutil.disk_usage('/')
        disk_gb = disk.free / (1024 ** 3)
        disk_ok = disk_gb >= MIN_DISK_SPACE_GB
        results['disk'] = (
            disk_ok,
            f"Disk Space: {disk_gb:.1f}GB {'>= ' if disk_ok else '< '}{MIN_DISK_SPACE_GB}GB"
        )
    except Exception as e:
        results['disk'] = (False, f"Disk check failed: {str(e)}")
    
    # Check Python version
    py_version = sys.version_info[:2]
    py_ok = py_version >= MIN_PYTHON_VERSION
    results['python'] = (
        py_ok,
        f"Python: {py_version[0]}.{py_version[1]} {'>= ' if py_ok else '< '}{MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]}"
    )
    
    return results

def check_network_ports() -> Dict[int, Tuple[bool, str]]:
    """
    Check if required network ports are available.
    Returns a dictionary with port statuses.
    """
    port_status = {}
    for port in BTC_TOOLS_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()
        port_status[port] = (
            result != 0,
            f"Port {port} is {'available' if result != 0 else 'in use'}"
        )
    return port_status

def troubleshoot_miner_issues() -> List[str]:
    """
    Provide troubleshooting steps for common miner issues.
    Returns a list of troubleshooting steps.
    """
    steps = [
        "1. Verify miner configuration file paths and permissions",
        "2. Check miner logs for error messages",
        "3. Ensure your mining pool credentials are correct",
        "4. Verify your wallet address is properly formatted",
        "5. Check GPU/CPU temperature and cooling",
        "6. Update mining software to latest version",
        "7. Verify internet connection stability",
        "8. Check for conflicting software (antivirus/firewall)",
        "9. Restart mining software and monitor initial output",
        "10. Consult BTC Tools documentation for specific miner settings"
    ]
    return steps

def display_results(system_checks: Dict[str, Tuple[bool, str]], 
                    port_checks: Dict[int, Tuple[bool, str]], 
                    troubleshooting_steps: List[str]) -> None:
    """
    Display formatted results of system checks and troubleshooting steps.
    """
    print("\n=== BTC Tools System Requirements Check ===")
    for check, (status, msg) in system_checks.items():
        status_icon = "✓" if status else "✗"
        print(f"{status_icon} {msg}")
    
    print("\n=== Network Port Availability ===")
    for port, (status, msg) in port_checks.items():
        status_icon = "✓" if status else "✗"
        print(f"{status_icon} {msg}")
    
    print("\n=== Common Miner Troubleshooting Steps ===")
    for step in troubleshooting_steps:
        print(f"- {step}")

def main():
    """Main function to run checks and display results."""
    try:
        print("BTC Tools Diagnostic Tool")
        print("Checking system requirements...")
        
        system_checks = check_system_requirements()
        port_checks = check_network_ports()
        troubleshooting_steps = troubleshoot_miner_issues()
        
        display_results(system_checks, port_checks, troubleshooting_steps)
        
        # Check if all system requirements are met
        all_checks_passed = all(status for status, _ in system_checks.values())
        
        if all_checks_passed:
            print("\n✅ Your system meets all BTC Tools requirements")
        else:
            print("\n⚠️ Some system requirements are not met. See above for details.")
        
    except Exception as e:
        print(f"\n❌ An error occurred during diagnostics: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
