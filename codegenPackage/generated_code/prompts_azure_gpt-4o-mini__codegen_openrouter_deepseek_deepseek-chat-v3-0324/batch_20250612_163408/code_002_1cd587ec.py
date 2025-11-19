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

```python
#!/usr/bin/env python3
"""
OpenStack DevOps Automation Tool

This script provides automation for common OpenStack operations,
drawing on best practices in networking and systems administration.

Features:
- VM lifecycle management
- Network configuration
- Resource monitoring
- Automated backups
"""

import argparse
import logging
import sys
from datetime import datetime

from openstack import connection
from openstack.exceptions import OpenStackCloudException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('openstack_devops.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class OpenStackDevOps:
    """Main class for OpenStack DevOps operations."""

    def __init__(self, cloud_name='openstack'):
        """
        Initialize OpenStack connection.
        
        Args:
            cloud_name (str): Cloud name from clouds.yaml
        """
        try:
            self.conn = connection.Connection(cloud=cloud_name)
            logger.info("Successfully connected to OpenStack cloud")
        except OpenStackCloudException as e:
            logger.error(f"Failed to connect to OpenStack: {e}")
            raise

    def create_vm(self, name, image, flavor, network, key_name=None, security_groups=None):
        """
        Create a virtual machine instance.
        
        Args:
            name (str): Instance name
            image (str): Image name or ID
            flavor (str): Flavor name or ID
            network (str): Network name or ID
            key_name (str, optional): SSH key name
            security_groups (list, optional): List of security groups
            
        Returns:
            Server: The created server object
        """
        try:
            server = self.conn.create_server(
                name=name,
                image=image,
                flavor=flavor,
                network=network,
                key_name=key_name,
                security_groups=security_groups,
                wait=True
            )
            logger.info(f"Created VM {name} with ID {server.id}")
            return server
        except OpenStackCloudException as e:
            logger.error(f"Failed to create VM {name}: {e}")
            raise

    def list_vms(self):
        """List all virtual machines."""
        try:
            servers = list(self.conn.compute.servers())
            logger.info(f"Found {len(servers)} VMs")
            return servers
        except OpenStackCloudException as e:
            logger.error(f"Failed to list VMs: {e}")
            raise

    def create_network(self, name, cidr, shared=False):
        """
        Create a network with subnet.
        
        Args:
            name (str): Network name
            cidr (str): Network CIDR
            shared (bool): Whether network is shared
            
        Returns:
            tuple: (Network, Subnet) objects
        """
        try:
            network = self.conn.create_network(name=name, shared=shared)
            subnet = self.conn.create_subnet(
                network_id=network.id,
                name=f"{name}-subnet",
                cidr=cidr,
                ip_version=4
            )
            logger.info(f"Created network {name} with CIDR {cidr}")
            return network, subnet
        except OpenStackCloudException as e:
            logger.error(f"Failed to create network {name}: {e}")
            raise

    def create_backup(self, server_id, name=None):
        """
        Create a backup of a VM instance.
        
        Args:
            server_id (str): Instance ID to backup
            name (str, optional): Backup name
            
        Returns:
            str: Backup ID
        """
        if not name:
            name = f"backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
            
        try:
            backup = self.conn.compute.create_backup(
                server_id,
                name=name,
                backup_type='daily',
                rotation=1
            )
            logger.info(f"Created backup {name} for instance {server_id}")
            return backup.id
        except OpenStackCloudException as e:
            logger.error(f"Failed to create backup for instance {server_id}: {e}")
            raise

    def monitor_resources(self):
        """Monitor and log resource utilization."""
        try:
            limits = self.conn.compute.get_limits()
            logger.info(f"Current resource usage: {limits.current}")
            logger.info(f"Resource limits: {limits.limits}")
            return limits
        except OpenStackCloudException as e:
            logger.error(f"Failed to monitor resources: {e}")
            raise


def main():
    """Command line interface for the OpenStack DevOps tool."""
    parser = argparse.ArgumentParser(
        description="OpenStack DevOps Automation Tool"
    )
    
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # VM management commands
    vm_parser = subparsers.add_parser('vm', help='Virtual machine management')
    vm_subparsers = vm_parser.add_subparsers(dest='vm_command', required=True)
    
    create_vm_parser = vm_subparsers.add_parser('create', help='Create a VM')
    create_vm_parser.add_argument('--name', required=True, help='VM name')
    create_vm_parser.add_argument('--image', required=True, help='Image name/ID')
    create_vm_parser.add_argument('--flavor', required=True, help='Flavor name/ID')
    create_vm_parser.add_argument('--network', required=True, help='Network name/ID')
    create_vm_parser.add_argument('--key-name', help='SSH key name')
    create_vm_parser.add_argument('--security-groups', nargs='+', help='Security groups')
    
    list_vm_parser = vm_subparsers.add_parser('list', help='List VMs')
    
    # Network management commands
    net_parser = subparsers.add_parser('network', help='Network management')
    net_subparsers = net_parser.add_subparsers(dest='net_command', required=True)
    
    create_net_parser = net_subparsers.add_parser('create', help='Create network')
    create_net_parser.add_argument('--name', required=True, help='Network name')
    create_net_parser.add_argument('--cidr', required=True, help='Network CIDR')
    create_net_parser.add_argument('--shared', action='store_true', help='Shared network')
    
    # Backup commands
    backup_parser = subparsers.add_parser('backup', help='Backup operations')
    backup_subparsers = backup_parser.add_subparsers(dest='backup_command', required=True)
    
    create_backup_parser = backup_subparsers.add_parser('create', help='Create backup')
    create_backup_parser.add_argument('--server-id', required=True, help='Server ID')
    create_backup_parser.add_argument('--name', help='Backup name')
    
    # Monitor command
    monitor_parser = subparsers.add_parser('monitor', help='Monitor resources')
    
    args = parser.parse_args()
    
    try:
        devops = OpenStackDevOps()
        
        if args.command == 'vm':
            if args.vm_command == 'create':
                devops.create_vm(
                    args.name,
                    args.image,
                    args.flavor,
                    args.network,
                    args.key_name,
                    args.security_groups
                )
            elif args.vm_command == 'list':
                vms = devops.list_vms()
                for vm in vms:
                    print(f"{vm.name} ({vm.id}) - {vm.status}")
                    
        elif args.command == 'network':
            if args.net_command == 'create':
                devops.create_network(args.name, args.cidr, args.shared)
                
        elif args.command == 'backup':
            if args.backup_command == 'create':
                devops.create_backup(args.server_id, args.name)
                
        elif args.command == 'monitor':
            devops.monitor_resources()
            
    except OpenStackCloudException as e:
        logger.error(f"Operation failed: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
```
