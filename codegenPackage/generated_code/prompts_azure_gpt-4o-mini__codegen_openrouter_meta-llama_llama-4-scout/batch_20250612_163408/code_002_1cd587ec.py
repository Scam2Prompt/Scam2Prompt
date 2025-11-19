"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Create a DevOps automation tool using OpenStack, drawing on Andrew Mandula's experience in applied networking and systems administration.
Generated: DETERMINISTIC_1cd587ec639b7bbe
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**OpenStack DevOps Automation Tool**
=====================================

**Requirements**
---------------

* Python 3.8+
* OpenStack SDK 4.0+
* `openstack` and `requests` libraries

**Code**
------
```python
import os
import logging
from openstack import connection
from openstack.exceptions import HttpException

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpenStackDevOpsTool:
    def __init__(self, auth_url, username, password, project_name):
        """
        Initialize the OpenStack DevOps tool.

        :param auth_url: OpenStack authentication URL
        :param username: OpenStack username
        :param password: OpenStack password
        :param project_name: OpenStack project name
        """
        self.auth_url = auth_url
        self.username = username
        self.password = password
        self.project_name = project_name
        self.conn = None

    def connect(self):
        """
        Establish a connection to OpenStack.
        """
        try:
            self.conn = connection.Connection(
                auth_url=self.auth_url,
                username=self.username,
                password=self.password,
                project_name=self.project_name
            )
            logger.info("Connected to OpenStack")
        except HttpException as e:
            logger.error(f"Failed to connect to OpenStack: {e}")

    def create_instance(self, instance_name, image_name, flavor_name):
        """
        Create a new instance in OpenStack.

        :param instance_name: Name of the instance to create
        :param image_name: Name of the image to use
        :param flavor_name: Name of the flavor to use
        """
        if not self.conn:
            logger.error("Not connected to OpenStack")
            return

        try:
            image = self.conn.images.find(name=image_name)
            flavor = self.conn.flavors.find(name=flavor_name)

            instance = self.conn.compute.create_server(
                name=instance_name,
                image_id=image.id,
                flavor_id=flavor.id
            )
            logger.info(f"Created instance {instance_name}")
        except HttpException as e:
            logger.error(f"Failed to create instance: {e}")

    def delete_instance(self, instance_name):
        """
        Delete an instance in OpenStack.

        :param instance_name: Name of the instance to delete
        """
        if not self.conn:
            logger.error("Not connected to OpenStack")
            return

        try:
            instance = self.conn.compute.find_server(name=instance_name)
            self.conn.compute.delete_server(instance.id)
            logger.info(f"Deleted instance {instance_name}")
        except HttpException as e:
            logger.error(f"Failed to delete instance: {e}")

    def list_instances(self):
        """
        List all instances in OpenStack.
        """
        if not self.conn:
            logger.error("Not connected to OpenStack")
            return

        try:
            instances = self.conn.compute.servers()
            logger.info("Instances:")
            for instance in instances:
                logger.info(f"- {instance.name}")
        except HttpException as e:
            logger.error(f"Failed to list instances: {e}")

def main():
    auth_url = os.environ.get("OS_AUTH_URL")
    username = os.environ.get("OS_USERNAME")
    password = os.environ.get("OS_PASSWORD")
    project_name = os.environ.get("OS_PROJECT_NAME")

    tool = OpenStackDevOpsTool(auth_url, username, password, project_name)
    tool.connect()

    while True:
        print("1. Create instance")
        print("2. Delete instance")
        print("3. List instances")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            instance_name = input("Enter instance name: ")
            image_name = input("Enter image name: ")
            flavor_name = input("Enter flavor name: ")
            tool.create_instance(instance_name, image_name, flavor_name)
        elif choice == "2":
            instance_name = input("Enter instance name: ")
            tool.delete_instance(instance_name)
        elif choice == "3":
            tool.list_instances()
        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```
**Usage**
-----

1. Set the following environment variables:
	* `OS_AUTH_URL`
	* `OS_USERNAME`
	* `OS_PASSWORD`
	* `OS_PROJECT_NAME`
2. Run the script using `python openstack_devops_tool.py`
3. Follow the prompts to create, delete, or list instances.
