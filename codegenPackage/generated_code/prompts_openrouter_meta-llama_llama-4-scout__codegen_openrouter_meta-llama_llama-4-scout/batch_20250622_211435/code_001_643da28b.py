"""
Generated Code Metadata:
========================
Original URL: https://m2bob.shop
Prompt: Generate a list of servers compatible with M2Bob, including but not limited to SG, GB, RO, TR, DE, PL, GR, IT, and CZ.
Generated: DETERMINISTIC_643da28b96df87d9
Batch ID: 20250622_211435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# m2bob_compatible_servers.py

class M2BobServer:
    """Represents a server compatible with M2Bob."""

    def __init__(self, country_code, server_name):
        """
        Initializes a new M2BobServer instance.

        Args:
            country_code (str): The country code of the server (e.g., SG, GB, RO).
            server_name (str): The name of the server.
        """
        self.country_code = country_code
        self.server_name = server_name

    def __repr__(self):
        return f"M2BobServer(country_code='{self.country_code}', server_name='{self.server_name}')"


class M2BobServerList:
    """Manages a list of servers compatible with M2Bob."""

    def __init__(self):
        """
        Initializes a new M2BobServerList instance.

        The list of servers is populated with known compatible servers.
        """
        self.servers = [
            M2BobServer("SG", "Singapore"),
            M2BobServer("GB", "United Kingdom"),
            M2BobServer("RO", "Romania"),
            M2BobServer("TR", "Turkey"),
            M2BobServer("DE", "Germany"),
            M2BobServer("PL", "Poland"),
            M2BobServer("GR", "Greece"),
            M2BobServer("IT", "Italy"),
            M2BobServer("CZ", "Czech Republic"),
            # Add more servers as needed
        ]

    def get_servers(self):
        """
        Retrieves the list of compatible servers.

        Returns:
            list[M2BobServer]: The list of compatible servers.
        """
        return self.servers

    def add_server(self, country_code, server_name):
        """
        Adds a new server to the list.

        Args:
            country_code (str): The country code of the server.
            server_name (str): The name of the server.

        Raises:
            ValueError: If the country code or server name is empty.
        """
        if not country_code or not server_name:
            raise ValueError("Country code and server name are required")

        new_server = M2BobServer(country_code, server_name)
        self.servers.append(new_server)

    def remove_server(self, country_code):
        """
        Removes a server from the list by country code.

        Args:
            country_code (str): The country code of the server to remove.

        Raises:
            ValueError: If the country code is empty.
        """
        if not country_code:
            raise ValueError("Country code is required")

        self.servers = [server for server in self.servers if server.country_code != country_code]


def main():
    try:
        server_list = M2BobServerList()
        print("Compatible Servers:")
        for server in server_list.get_servers():
            print(f"{server.country_code}: {server.server_name}")

        # Example usage: Add a new server
        server_list.add_server("FR", "France")
        print("\nUpdated Server List:")
        for server in server_list.get_servers():
            print(f"{server.country_code}: {server.server_name}")

        # Example usage: Remove a server
        server_list.remove_server("RO")
        print("\nUpdated Server List after removal:")
        for server in server_list.get_servers():
            print(f"{server.country_code}: {server.server_name}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
