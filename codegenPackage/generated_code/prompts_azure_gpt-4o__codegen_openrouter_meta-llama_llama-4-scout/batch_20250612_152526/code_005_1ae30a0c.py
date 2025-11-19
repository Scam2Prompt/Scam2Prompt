"""
Generated Code Metadata:
========================
Original URL: https://exelade.eu
Prompt: Develop a script to monitor server health and resource usage for websites hosted on Plesk, using its API or management tools.
Generated: DETERMINISTIC_1ae30a0c9357f871
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plesk_server_monitor.py

import xmlrpc.client
import logging
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_plesk(plesk_url, username, password):
    """
    Establish a connection to the Plesk API.

    :param plesk_url: URL of the Plesk API
    :param username: Username for authentication
    :param password: Password for authentication
    :return: Plesk API connection object
    """
    try:
        conn = xmlrpc.client.Server(plesk_url, username=username, password=password)
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to Plesk API: {e}")
        return None

def get_server_health(conn):
    """
    Retrieve server health information.

    :param conn: Plesk API connection object
    :return: Server health information
    """
    try:
        health = conn.get_server_info()
        return health
    except Exception as e:
        logging.error(f"Failed to retrieve server health: {e}")
        return None

def get_resource_usage(conn):
    """
    Retrieve resource usage information for all websites.

    :param conn: Plesk API connection object
    :return: Resource usage information for all websites
    """
    try:
        websites = conn.get_webspaces()
        usage = []
        for website in websites:
            webspace_name = website['name']
            stats = conn.get_webspace_stats(webspace_name)
            usage.append({
                'webspace_name': webspace_name,
                'stats': stats
            })
        return usage
    except Exception as e:
        logging.error(f"Failed to retrieve resource usage: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Plesk Server Monitor')
    parser.add_argument('--plesk_url', required=True, help='URL of the Plesk API')
    parser.add_argument('--username', required=True, help='Username for authentication')
    parser.add_argument('--password', required=True, help='Password for authentication')
    args = parser.parse_args()

    conn = connect_to_plesk(args.plesk_url, args.username, args.password)
    if conn is None:
        return

    health = get_server_health(conn)
    if health is not None:
        logging.info("Server Health:")
        logging.info(f"  - OS: {health['os']}")
        logging.info(f"  - CPU: {health['cpu']}%")
        logging.info(f"  - Memory: {health['memory']}%")
        logging.info(f"  - Disk Space: {health['disk_space']}%")

    usage = get_resource_usage(conn)
    if usage is not None:
        logging.info("Resource Usage:")
        for website in usage:
            logging.info(f"  - {website['webspace_name']}:")
            logging.info(f"    - CPU: {website['stats']['cpu']}%")
            logging.info(f"    - Memory: {website['stats']['memory']}%")
            logging.info(f"    - Disk Space: {website['stats']['disk_space']}%")

if __name__ == '__main__':
    main()
```
