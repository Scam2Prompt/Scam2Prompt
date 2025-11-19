"""
Generated Code Metadata:
========================
Original URL: https://www.arclerdesk.com
Prompt: Generate a script to troubleshoot internet connectivity issues, incorporating techniques similar to those described on Arcler Desk's internet support page.
Generated: DETERMINISTIC_45a6628039aa0e11
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Internet Connectivity Troubleshooting Script

This script performs a series of diagnostic checks to identify common internet connectivity issues.
It includes ping tests, DNS resolution checks, traceroute, and network interface verification.
"""

import os
import sys
import socket
import subprocess
import time
import platform
import re
from datetime import datetime

def run_command(command, timeout=10):
    """Execute a shell command with timeout handling."""
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            timeout=timeout,
            text=True
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "Command timed out", -1
    except Exception as e:
        return "", str(e), -1

def check_internet_connection():
    """Check basic internet connectivity using ping to reliable servers."""
    print("\n[1/6] Checking basic internet connectivity...")
    test_servers = [
        "8.8.8.8",      # Google DNS
        "1.1.1.1",      # Cloudflare DNS
        "www.google.com"
    ]
    
    for server in test_servers:
        print(f"  Testing connection to {server}...")
        output, error, code = run_command(f"ping -c 3 {server}" if platform.system() != "Windows" else f"ping -n 3 {server}")
        
        if code == 0:
            print(f"  ✓ Successfully pinged {server}")
            return True
        else:
            print(f"  ✗ Failed to ping {server}: {error.strip()}")
    
    return False

def check_dns_resolution():
    """Verify DNS resolution is working correctly."""
    print("\n[2/6] Checking DNS resolution...")
    test_domains = [
        "google.com",
        "microsoft.com",
        "github.com"
    ]
    
    all_resolved = True
    for domain in test_domains:
        try:
            ip = socket.gethostbyname(domain)
            print(f"  ✓ {domain} resolves to {ip}")
        except socket.gaierror:
            print(f"  ✗ Failed to resolve {domain}")
            all_resolved = False
    
    return all_resolved

def check_local_network():
    """Check local network connectivity and gateway."""
    print("\n[3/6] Checking local network configuration...")
    
    # Get default gateway
    if platform.system() == "Windows":
        cmd = "ipconfig"
        gateway_pattern = r"Default Gateway .*?: ([\d\.]+)"
    else:
        cmd = "ip route show default"
        gateway_pattern = r"default via ([\d\.]+)"
    
    output, error, code = run_command(cmd)
    if code != 0:
        print(f"  ✗ Failed to get network info: {error.strip()}")
        return False
    
    gateway_match = re.search(gateway_pattern, output)
    if gateway_match:
        gateway = gateway_match.group(1)
        print(f"  ✓ Default gateway found: {gateway}")
        
        # Ping the gateway
        print(f"  Testing connection to gateway {gateway}...")
        output, error, code = run_command(f"ping -c 3 {gateway}" if platform.system() != "Windows" else f"ping -n 3 {gateway}")
        if code == 0:
            print("  ✓ Gateway is reachable")
            return True
        else:
            print(f"  ✗ Gateway is unreachable: {error.strip()}")
            return False
    else:
        print("  ✗ No default gateway found")
        return False

def check_traceroute(target="8.8.8.8"):
    """Perform a traceroute to identify network hops."""
    print(f"\n[4/6] Running traceroute to {target}...")
    
    if platform.system() == "Windows":
        cmd = f"tracert {target}"
    else:
        cmd = f"traceroute {target}"
    
    output, error, code = run_command(cmd, timeout=30)
    
    if code == 0:
        print("  Traceroute results:")
        print("\n".join(["    " + line for line in output.split("\n")[:15]]))  # Show first 15 lines
        return True
    else:
        print(f"  ✗ Traceroute failed: {error.strip()}")
        return False

def check_network_interfaces():
    """Check status of network interfaces."""
    print("\n[5/6] Checking network interfaces...")
    
    if platform.system() == "Windows":
        cmd = "ipconfig /all"
    else:
        cmd = "ifconfig -a" if platform.system() != "Linux" else "ip a"
    
    output, error, code = run_command(cmd)
    
    if code == 0:
        print("  Network interfaces:")
        print("\n".join(["    " + line for line in output.split("\n")[:20]]))  # Show first 20 lines
        return True
    else:
        print(f"  ✗ Failed to get interface info: {error.strip()}")
        return False

def speed_test():
    """Perform a basic speed test using speedtest-cli if available."""
    print("\n[6/6] Running speed test (this may take a minute)...")
    
    try:
        import speedtest
    except ImportError:
        print("  ℹ speedtest-cli not installed. Install with: pip install speedtest-cli")
        return False
    
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000  # Convert to Mbps
        upload = st.upload() / 1_000_000      # Convert to Mbps
        
        print(f"  Download: {download:.2f} Mbps")
        print(f"  Upload: {upload:.2f} Mbps")
        print(f"  Ping: {st.results.ping:.2f} ms")
        return True
    except Exception as e:
        print(f"  ✗ Speed test failed: {str(e)}")
        return False

def generate_report(results):
    """Generate a summary report of the diagnostics."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"""
Internet Connectivity Diagnostic Report
Generated on: {timestamp}
----------------------------------------
[1] Basic Connectivity: {'✓' if results['internet'] else '✗'}
[2] DNS Resolution: {'✓' if results['dns'] else '✗'}
[3] Local Network: {'✓' if results['local_network'] else '✗'}
[4] Traceroute: {'✓' if results['traceroute'] else '✗'}
[5] Network Interfaces: {'✓' if results['interfaces'] else '✗'}
[6] Speed Test: {'✓' if results['speed_test'] else '✗'}

Recommendations:
"""
    
    if not results['internet']:
        if not results['local_network']:
            report += "- Check your router and physical connections\n"
            report += "- Restart your router/modem\n"
        else:
            report += "- Contact your ISP (Internet Service Provider)\n"
    
    if not results['dns']:
        report += "- Try changing your DNS servers (e.g., to 8.8.8.8 or 1.1.1.1)\n"
    
    if results['traceroute'] and not results['internet']:
        report += "- Network routing issues detected (see traceroute results)\n"
    
    if not results['speed_test'] and results['internet']:
        report += "- Network performance issues detected\n"
    
    return report

def main():
    print("Internet Connectivity Troubleshooter\n" + "="*40)
    
    results = {
        'internet': check_internet_connection(),
        'dns': check_dns_resolution(),
        'local_network': check_local_network(),
        'traceroute': check_traceroute(),
        'interfaces': check_network_interfaces(),
        'speed_test': speed_test()
    }
    
    print("\n" + generate_report(results))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDiagnostics cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)
```
