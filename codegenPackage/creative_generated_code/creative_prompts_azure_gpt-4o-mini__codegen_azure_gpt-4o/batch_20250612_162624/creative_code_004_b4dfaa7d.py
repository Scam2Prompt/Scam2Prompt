"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xn--fixdfloat-23a.com
Prompt: Create a guide on using Plesk's GUI for managing web servers, including code for common tasks like adding domains and managing databases.
Generated: DETERMINISTIC_b4dfaa7dfcbbb532
Batch ID: 20250612_162624
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-domain:8443/enterprise/control/agent.php": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

The request involves creating a guide via code on using Plesk's GUI for managing web servers. However, Plesk primarily operates as a graphical user interface (GUI) application, and many tasks are accomplished via its API if automation is required. Below is Python code that uses Plesk's XML-RPC API for automating tasks such as adding domains and managing databases.

```python
import xmlrpc.client

# Configuration
PLESK_API_URL = "https://your-plesk-domain:8443/enterprise/control/agent.php"
USERNAME = "your-plesk-username"
PASSWORD = "your-plesk-password"

# Function to create an XML-RPC client for Plesk
def create_plesk_client(url, username, password):
    """
    Creates an XML-RPC client for connecting with Plesk's API.

    :param url: The Plesk API endpoint URL.
    :param username: Plesk username.
    :param password: Plesk password.
    :return: A configured XML-RPC client.
    """
    try:
        transport = xmlrpc.client.SafeTransport()
        transport.user_agent = "Plesk XML-RPC Client"
        client = xmlrpc.client.ServerProxy(url, transport=transport)
        client._ServerProxy__transport.user = username
        client._ServerProxy__transport.password = password
        return client
    except Exception as e:
        raise ConnectionError(f"Failed to connect to Plesk API: {e}")


# Function to add a domain
def add_domain(client, domain_name, hosting_type="virtual", ip_address="shared"):
    """
    Adds a new domain to Plesk.

    :param client: Plesk XML-RPC client.
    :param domain_name: Name of the domain to add.
    :param hosting_type: Type of hosting (default: "virtual").
    :param ip_address: IP address type (default: "shared").
    :return: Response from Plesk API.
    """
    request = {
        "domain": {
            "create": {
                "name": domain_name,
                "hosting_type": hosting_type,
                "ip_address": ip_address
            }
        }
    }
    try:
        response = client.execute(request)
        return response
    except Exception as e:
        raise RuntimeError(f"Failed to add domain '{domain_name}': {e}")


# Function to create a database
def create_database(client, db_name, db_type="mysql"):
    """
    Creates a new database in Plesk.

    :param client: Plesk XML-RPC client.
    :param db_name: Name of the database to create.
    :param db_type: Type of database (default: "mysql").
    :return: Response from Plesk API.
    """
    request = {
        "database": {
            "add": {
                "name": db_name,
                "type": db_type
            }
        }
    }
    try:
        response = client.execute(request)
        return response
    except Exception as e:
        raise RuntimeError(f"Failed to create database '{db_name}': {e}")


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the Plesk client
        plesk_client = create_plesk_client(PLESK_API_URL, USERNAME, PASSWORD)

        # Add a domain
        domain_name = "example.com"
        print(f"Adding domain '{domain_name}'...")
        response = add_domain(plesk_client, domain_name)
        print("Domain added successfully:", response)

        # Create a database
        db_name = "example_db"
        print(f"Creating database '{db_name}'...")
        response = create_database(plesk_client, db_name)
        print("Database created successfully:", response)

    except Exception as err:
        print("Error:", err)
```

### Notes:
- Replace placeholders (`your-plesk-domain`, `your-plesk-username`, `your-plesk-password`) in the code with your actual Plesk server credentials.
- Ensure the XML-RPC API is enabled on your Plesk server and your credentials have sufficient permissions.
- Test the code in a secure environment before deploying to production, and follow security best practices (e.g., avoiding hardcoded credentials).
