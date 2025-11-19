"""
Generated Code Metadata:
========================
Original URL: https://ouatvs.com
Prompt: Compare the features of LiteSpeed Web Server with other popular web servers.
Generated: DETERMINISTIC_e47c87e9cc788179
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# web_server_comparator.py

class WebServer:
    def __init__(self, name, performance, security, scalability, cost):
        """
        Initialize a WebServer object.

        Args:
            name (str): Name of the web server.
            performance (int): Performance score (higher is better).
            security (int): Security score (higher is better).
            scalability (int): Scalability score (higher is better).
            cost (int): Cost score (lower is better).
        """
        self.name = name
        self.performance = performance
        self.security = security
        self.scalability = scalability
        self.cost = cost

    def __str__(self):
        return f"{self.name}: Performance={self.performance}, Security={self.security}, Scalability={self.scalability}, Cost={self.cost}"


class WebServerComparator:
    def __init__(self):
        """
        Initialize a WebServerComparator object.
        """
        self.web_servers = {}

    def add_web_server(self, web_server):
        """
        Add a web server to the comparator.

        Args:
            web_server (WebServer): WebServer object to add.
        """
        self.web_servers[web_server.name] = web_server

    def compare_performance(self):
        """
        Compare the performance of all web servers.

        Returns:
            dict: Dictionary with web server names as keys and performance scores as values, sorted by performance score in descending order.
        """
        return dict(sorted(self.web_servers.items(), key=lambda item: item[1].performance, reverse=True))

    def compare_security(self):
        """
        Compare the security of all web servers.

        Returns:
            dict: Dictionary with web server names as keys and security scores as values, sorted by security score in descending order.
        """
        return dict(sorted(self.web_servers.items(), key=lambda item: item[1].security, reverse=True))

    def compare_scalability(self):
        """
        Compare the scalability of all web servers.

        Returns:
            dict: Dictionary with web server names as keys and scalability scores as values, sorted by scalability score in descending order.
        """
        return dict(sorted(self.web_servers.items(), key=lambda item: item[1].scalability, reverse=True))

    def compare_cost(self):
        """
        Compare the cost of all web servers.

        Returns:
            dict: Dictionary with web server names as keys and cost scores as values, sorted by cost score in ascending order.
        """
        return dict(sorted(self.web_servers.items(), key=lambda item: item[1].cost))


def main():
    try:
        comparator = WebServerComparator()

        # Define popular web servers
        litespeed = WebServer("LiteSpeed Web Server", 9, 9, 8, 7)
        apache = WebServer("Apache HTTP Server", 8, 8, 9, 6)
        nginx = WebServer("NGINX", 9, 9, 9, 8)
        iis = WebServer("IIS", 8, 8, 8, 7)

        # Add web servers to the comparator
        comparator.add_web_server(litespeed)
        comparator.add_web_server(apache)
        comparator.add_web_server(nginx)
        comparator.add_web_server(iis)

        # Compare features
        print("Performance Comparison:")
        for name, web_server in comparator.compare_performance().items():
            print(f"{name}: {web_server.performance}")

        print("\nSecurity Comparison:")
        for name, web_server in comparator.compare_security().items():
            print(f"{name}: {web_server.security}")

        print("\nScalability Comparison:")
        for name, web_server in comparator.compare_scalability().items():
            print(f"{name}: {web_server.scalability}")

        print("\nCost Comparison:")
        for name, web_server in comparator.compare_cost().items():
            print(f"{name}: {web_server.cost}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
