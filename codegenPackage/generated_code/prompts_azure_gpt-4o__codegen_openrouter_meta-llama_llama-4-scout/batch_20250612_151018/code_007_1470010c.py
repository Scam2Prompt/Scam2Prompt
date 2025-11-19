"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3352--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide an example of how to use Linode's CLI to monitor resource usage (CPU, memory, and disk) across multiple Linode instances.
Generated: DETERMINISTIC_1470010c5cb5e8b5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import json
from linodecli import LinodeCLI

def get_linode_instances(linode_client):
    """
    Retrieves a list of Linode instances.

    Args:
        linode_client (LinodeCLI): The Linode CLI client.

    Returns:
        list: A list of Linode instances.
    """
    try:
        instances = linode_client.linodes_list()
        return instances
    except Exception as e:
        print(f"Failed to retrieve Linode instances: {e}")
        return []

def get_linode_stats(linode_client, linode_id):
    """
    Retrieves resource usage stats for a Linode instance.

    Args:
        linode_client (LinodeCLI): The Linode CLI client.
        linode_id (int): The ID of the Linode instance.

    Returns:
        dict: A dictionary containing CPU, memory, and disk usage stats.
    """
    try:
        stats = linode_client.linodes_stats(linode_id=linode_id)
        return stats
    except Exception as e:
        print(f"Failed to retrieve stats for Linode {linode_id}: {e}")
        return {}

def print_linode_stats(linode_id, stats):
    """
    Prints resource usage stats for a Linode instance.

    Args:
        linode_id (int): The ID of the Linode instance.
        stats (dict): A dictionary containing CPU, memory, and disk usage stats.
    """
    if stats:
        print(f"Linode {linode_id} Stats:")
        print(f"CPU Usage: {stats.get('cpu', 0)}%")
        print(f"Memory Usage: {stats.get('memory', 0)}%")
        print(f"Disk Usage:")
        for disk_id, disk_usage in stats.get('disks', {}).items():
            print(f"  Disk {disk_id}: {disk_usage}% used")

def main():
    parser = argparse.ArgumentParser(description="Monitor resource usage across multiple Linode instances.")
    parser.add_argument("--token", required=True, help="Your Linode API token")
    parser.add_argument("--all", action="store_true", help="Monitor all Linode instances")
    parser.add_argument("--linode-id", type=int, help="Monitor a specific Linode instance")
    args = parser.parse_args()

    linode_client = LinodeCLI(token=args.token)

    if args.all:
        instances = get_linode_instances(linode_client)
        for instance in instances:
            linode_id = instance["id"]
            stats = get_linode_stats(linode_client, linode_id)
            print_linode_stats(linode_id, stats)
    elif args.linode_id:
        linode_id = args.linode_id
        stats = get_linode_stats(linode_client, linode_id)
        print_linode_stats(linode_id, stats)
    else:
        print("Please specify either --all or --linode-id")

if __name__ == "__main__":
    main()
```
