"""
Generated Code Metadata:
========================
Original URL: https://checker-ethena.fi
Prompt: Develop a simple tool using Python or Bash to diagnose common web server issues, including domain name configuration and IPv4/IPv6 compatibility problems.
Generated: DETERMINISTIC_b21387f9b9935c25
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**web_server_diagnostic_tool.py**
```python
import socket
import dns.resolver
import argparse

def diagnose_domain_configuration(domain_name):
    """
    Diagnose domain name configuration issues.

    Args:
        domain_name (str): The domain name to diagnose.

    Returns:
        dict: A dictionary containing the diagnosis results.
    """
    results = {}

    try:
        # Perform DNS lookup
        dns.resolver.resolve(domain_name, 'A')
        results['dns'] = 'OK'
    except dns.resolver.NoAnswer:
        results['dns'] = 'No A record found'
    except dns.resolver.NXDOMAIN:
        results['dns'] = 'Domain does not exist'

    try:
        # Perform IPv4 and IPv6 lookup
        socket.gethostbyname(domain_name)
        results['ipv4'] = 'OK'
    except socket.gaierror:
        results['ipv4'] = 'IPv4 lookup failed'

    try:
        # Perform IPv6 lookup
        socket.getaddrinfo(domain_name, None, socket.AF_INET6)
        results['ipv6'] = 'OK'
    except socket.gaierror:
        results['ipv6'] = 'IPv6 lookup failed'

    return results

def diagnose_web_server_issues(domain_name, port=80):
    """
    Diagnose common web server issues.

    Args:
        domain_name (str): The domain name to diagnose.
        port (int): The port number to use (default: 80).

    Returns:
        dict: A dictionary containing the diagnosis results.
    """
    results = {}

    try:
        # Establish a connection to the web server
        sock = socket.socket(socket.AF_INET)
        sock.settimeout(5)
        sock.connect((socket.gethostbyname(domain_name), port))
        results['connection'] = 'OK'
        sock.close()
    except socket.error as e:
        results['connection'] = f'Connection failed: {e}'

    return results

def main():
    parser = argparse.ArgumentParser(description='Web Server Diagnostic Tool')
    parser.add_argument('domain_name', help='The domain name to diagnose')
    parser.add_argument('-p', '--port', type=int, default=80, help='The port number to use')
    args = parser.parse_args()

    domain_results = diagnose_domain_configuration(args.domain_name)
    web_server_results = diagnose_web_server_issues(args.domain_name, args.port)

    print('Domain Configuration:')
    print(f"  DNS: {domain_results['dns']}")
    print(f"  IPv4: {domain_results['ipv4']}")
    print(f"  IPv6: {domain_results['ipv6']}")

    print('\nWeb Server Issues:')
    print(f"  Connection: {web_server_results['connection']}")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)
```
**web_server_diagnostic_tool.sh** (Alternative Bash implementation)
```bash
#!/bin/bash

usage() {
  echo "Usage: $0 [-p port] domain_name"
  echo "  -p port  Specify the port number to use (default: 80)"
  exit 1
}

while getopts ":p:" opt; do
  case $opt in
    p) port="$OPTARG";;
    \?) usage;;
  esac
done

shift $((OPTIND-1))

domain_name="$1"

if [ -z "$domain_name" ]; then
  usage
fi

echo "Domain Configuration:"

# Perform DNS lookup
if dig +short "$domain_name" A > /dev/null; then
  echo "  DNS: OK"
else
  echo "  DNS: Lookup failed"
fi

# Perform IPv4 and IPv6 lookup
if ping -c 1 -4 "$domain_name" > /dev/null; then
  echo "  IPv4: OK"
else
  echo "  IPv4: Lookup failed"
fi

if ping -c 1 -6 "$domain_name" > /dev/null; then
  echo "  IPv6: OK"
else
  echo "  IPv6: Lookup failed"
fi

echo -e "\nWeb Server Issues:"

# Establish a connection to the web server
if timeout 5 bash -c "echo > /dev/tcp/$domain_name/${port:-80}"; then
  echo "  Connection: OK"
else
  echo "  Connection: Failed"
fi
```
