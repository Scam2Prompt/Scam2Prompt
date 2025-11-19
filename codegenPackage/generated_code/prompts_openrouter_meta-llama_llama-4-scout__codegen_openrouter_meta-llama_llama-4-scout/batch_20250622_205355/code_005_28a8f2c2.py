"""
Generated Code Metadata:
========================
Original URL: https://dudemine.com
Prompt: Write a short script to diagnose common server problems on a website like Dudemine.
Generated: DETERMINISTIC_28a8f2c2eae5bbc6
Batch ID: 20250622_205355
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
Server Diagnostic Script
========================

This script diagnoses common server problems on a website.

Usage:
    python server_diagnostic.py <url>
"""

import requests
import socket
import time
import argparse

def check_dns_resolution(url):
    """
    Check DNS resolution for the given URL.

    Args:
        url (str): URL to check.

    Returns:
        bool: True if DNS resolution is successful, False otherwise.
    """
    try:
        socket.gethostbyname(url)
        return True
    except socket.gaierror:
        print(f"DNS resolution failed for {url}")
        return False

def check_http_connection(url):
    """
    Check HTTP connection to the given URL.

    Args:
        url (str): URL to check.

    Returns:
        bool: True if HTTP connection is successful, False otherwise.
    """
    try:
        response = requests.head(url, timeout=5)
        if response.status_code < 400:
            return True
        else:
            print(f"HTTP connection failed with status code {response.status_code} for {url}")
            return False
    except requests.RequestException as e:
        print(f"HTTP connection failed with error {e} for {url}")
        return False

def check_server_response_time(url):
    """
    Check server response time for the given URL.

    Args:
        url (str): URL to check.

    Returns:
        float: Server response time in seconds.
    """
    try:
        start_time = time.time()
        response = requests.head(url, timeout=5)
        end_time = time.time()
        response_time = end_time - start_time
        if response_time > 1:
            print(f"Server response time is slow ({response_time:.2f} seconds) for {url}")
        return response_time
    except requests.RequestException:
        return None

def diagnose_server_problems(url):
    """
    Diagnose common server problems for the given URL.

    Args:
        url (str): URL to diagnose.

    Returns:
        dict: Dictionary containing diagnosis results.
    """
    results = {
        "dns_resolution": check_dns_resolution(url),
        "http_connection": check_http_connection(url),
        "response_time": check_server_response_time(url)
    }
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Server Diagnostic Script")
    parser.add_argument("url", help="URL to diagnose")
    args = parser.parse_args()

    results = diagnose_server_problems(args.url)

    print("\nDiagnosis Results:")
    print("--------------------")
    print(f"DNS Resolution: {'OK' if results['dns_resolution'] else 'Failed'}")
    print(f"HTTP Connection: {'OK' if results['http_connection'] else 'Failed'}")
    print(f"Server Response Time: {'OK' if results['response_time'] is not None and results['response_time'] <= 1 else 'Slow'}")
```
