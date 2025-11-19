"""
Generated Code Metadata:
========================
Original URL: https://taiko-net.com
Prompt: Compare the features of LiteSpeed Web Server with other popular web servers, focusing on CGI support and performance.
Generated: DETERMINISTIC_c2b7e9fcf733aaa1
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# web_server_comparator.py

import requests
import json

class WebServer:
    def __init__(self, name, cgi_support, performance_rating):
        """
        Initialize a WebServer object.

        Args:
            name (str): Name of the web server.
            cgi_support (bool): Whether the web server supports CGI.
            performance_rating (float): Performance rating of the web server.
        """
        self.name = name
        self.cgi_support = cgi_support
        self.performance_rating = performance_rating

class WebServerComparator:
    def __init__(self):
        """
        Initialize a WebServerComparator object.
        """
        self.web_servers = []

    def add_web_server(self, web_server):
        """
        Add a web server to the comparator.

        Args:
            web_server (WebServer): WebServer object to add.
        """
        self.web_servers.append(web_server)

    def compare_cgi_support(self):
        """
        Compare CGI support of the web servers.

        Returns:
            dict: Dictionary with web server names as keys and CGI support status as values.
        """
        cgi_support_comparison = {}
        for web_server in self.web_servers:
            cgi_support_comparison[web_server.name] = web_server.cgi_support
        return cgi_support_comparison

    def compare_performance(self):
        """
        Compare performance ratings of the web servers.

        Returns:
            dict: Dictionary with web server names as keys and performance ratings as values.
        """
        performance_comparison = {}
        for web_server in self.web_servers:
            performance_comparison[web_server.name] = web_server.performance_rating
        return performance_comparison

def get_web_server_data():
    """
    Get data for popular web servers.

    Returns:
        list: List of WebServer objects.
    """
    web_servers = [
        WebServer("LiteSpeed Web Server", True, 9.5),
        WebServer("Apache HTTP Server", True, 8.5),
        WebServer("Nginx", False, 9.8),
        WebServer("IIS", True, 8.8)
    ]
    return web_servers

def main():
    try:
        comparator = WebServerComparator()
        web_servers = get_web_server_data()
        for web_server in web_servers:
            comparator.add_web_server(web_server)

        print("CGI Support Comparison:")
        print(json.dumps(comparator.compare_cgi_support(), indent=4))
        print("\nPerformance Comparison:")
        print(json.dumps(comparator.compare_performance(), indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
