"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Python script to manage Linode instances, including creating, listing, and deleting instances, using Linode's API.
Generated: DETERMINISTIC_54184ad032554bde
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import argparse
from linode_api4 import LinodeClient, Instance
from typing import List, Optional, Dict, Any

class LinodeManager:
    """
    A class to manage Linode instances using the Linode API.
    """

    def __init__(self, api_token: str):
        """
        Initialize the LinodeManager with an API token.

        Args:
            api_token (str): The Linode API token.
        """
        self.client = LinodeClient(api_token)

    def create_instance(
        self,
        label: str,
        region: str,
        image: str,
        type: str,
        root_pass: str,
        tags: Optional[List[str]] = None,
        **kwargs: Any
    ) -> Optional[Instance]:
        """
        Create a new Linode instance.

        Args:
            label (str): The label for the new instance.
            region (str): The region where the instance will be deployed.
            image (str): The image to deploy to the instance.
            type (str): The Linode type (plan) for the instance.
            root_pass (str): The root password for the instance.
            tags (Optional[List[str]]): Optional tags for the instance.
            **kwargs: Additional arguments to pass to the instance creation.

        Returns:
            Optional[Instance]: The created instance or None if creation failed.
        """
        try:
            instance = self.client.linode.instance_create(
                type=type,
                region=region,
                image=image,
                label=label,
                root_pass=root_pass,
                tags=tags if tags else [],
                **kwargs
            )
            print(f"Instance {label} created successfully with ID {instance.id}")
            return instance
        except Exception as e:
            print(f"Failed to create instance: {e}")
            return None

    def list_instances(self) -> List[Instance]:
        """
        List all Linode instances.

        Returns:
            List[Instance]: A list of all instances.
        """
        try:
            instances = self.client.linode.instances()
            return list(instances)
        except Exception as e:
            print(f"Failed to list instances: {e}")
            return []

    def delete_instance(self, instance_id: int) -> bool:
        """
        Delete a Linode instance.

        Args:
            instance_id (int): The ID of the instance to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        try:
            instance = Instance(self.client, instance_id)
            instance.delete()
            print(f"Instance {instance_id} deleted successfully")
            return True
        except Exception as e:
            print(f"Failed to delete instance {instance_id}: {e}")
            return False

    def get_instance_details(self, instance_id: int) -> Optional[Dict[str, Any]]:
        """
        Get details of a specific Linode instance.

        Args:
            instance_id (int): The ID of the instance.

        Returns:
            Optional[Dict[str, Any]]: A dictionary of instance details or None if not found.
        """
        try:
            instance = Instance(self.client, instance_id)
            return {
                "id": instance.id,
                "label": instance.label,
                "status": instance.status,
                "region": instance.region.id,
                "type": instance.type.id,
                "ipv4": instance.ipv4,
                "created": instance.created,
                "tags": instance.tags,
            }
        except Exception as e:
            print(f"Failed to get instance details: {e}")
            return None

def main():
    parser = argparse.ArgumentParser(description="Manage Linode instances")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Create instance command
    create_parser = subparsers.add_parser("create", help="Create a new Linode instance")
    create_parser.add_argument("--label", required=True, help="Label for the instance")
    create_parser.add_argument("--region", required=True, help="Region for the instance")
    create_parser.add_argument("--image", required=True, help="Image for the instance")
    create_parser.add_argument("--type", required=True, help="Type (plan) for the instance")
    create_parser.add_argument("--root-pass", required=True, help="Root password for the instance")
    create_parser.add_argument("--tags", nargs="+", help="Tags for the instance")

    # List instances command
    subparsers.add_parser("list", help="List all Linode instances")

    # Delete instance command
    delete_parser = subparsers.add_parser("delete", help="Delete a Linode instance")
    delete_parser.add_argument("--id", type=int, required=True, help="ID of the instance to delete")

    # Get instance details command
    details_parser = subparsers.add_parser("details", help="Get details of a Linode instance")
    details_parser.add_argument("--id", type=int, required=True, help="ID of the instance")

    args = parser.parse_args()

    api_token = os.getenv("LINODE_API_TOKEN")
    if not api_token:
        print("Error: LINODE_API_TOKEN environment variable not set")
        return

    manager = LinodeManager(api_token)

    if args.command == "create":
        manager.create_instance(
            label=args.label,
            region=args.region,
            image=args.image,
            type=args.type,
            root_pass=args.root_pass,
            tags=args.tags,
        )
    elif args.command == "list":
        instances = manager.list_instances()
        for instance in instances:
            print(f"ID: {instance.id}, Label: {instance.label}, Status: {instance.status}")
    elif args.command == "delete":
        manager.delete_instance(args.id)
    elif args.command == "details":
        details = manager.get_instance_details(args.id)
        if details:
            for key, value in details.items():
                print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```
