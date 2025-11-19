"""
Generated Code Metadata:
========================
Original URL: https://origin-eth.org
Prompt: Generate code to set up an Elastic Compute Service (ECS) instance on Alibaba Cloud, including specifying region, instance type, and security group settings.
Generated: DETERMINISTIC_899600ce1dcf588a
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
import logging
from alibabacloud.ecs import EcsClient, DescribeRegionsRequest, DescribeInstanceTypesRequest
from alibabacloud.ecs.models import CreateInstanceRequest, CreateSecurityGroupRequest, AuthorizeSecurityGroupRequest
from alibabacloud.core import RpcAcsRequest

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ECSInstanceSetup:
    def __init__(self, access_key_id, access_key_secret, region_id):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.region_id = region_id
        self.ecs_client = EcsClient(self.access_key_id, self.access_key_secret)

    def describe_regions(self):
        try:
            request = DescribeRegionsRequest()
            response = self.ecs_client.describe_regions(request)
            return response
        except Exception as e:
            logger.error(f"Error describing regions: {e}")
            return None

    def describe_instance_types(self):
        try:
            request = DescribeInstanceTypesRequest()
            request.region_id = self.region_id
            response = self.ecs_client.describe_instance_types(request)
            return response
        except Exception as e:
            logger.error(f"Error describing instance types: {e}")
            return None

    def create_security_group(self, security_group_name, description):
        try:
            request = CreateSecurityGroupRequest()
            request.region_id = self.region_id
            request.security_group_name = security_group_name
            request.description = description
            response = self.ecs_client.create_security_group(request)
            return response
        except Exception as e:
            logger.error(f"Error creating security group: {e}")
            return None

    def authorize_security_group(self, security_group_id, ip_protocol, nic_type, port_range, cidr_ip):
        try:
            request = AuthorizeSecurityGroupRequest()
            request.region_id = self.region_id
            request.security_group_id = security_group_id
            request.ip_protocol = ip_protocol
            request.nic_type = nic_type
            request.port_range = port_range
            request.cidr_ip = cidr_ip
            response = self.ecs_client.authorize_security_group(request)
            return response
        except Exception as e:
            logger.error(f"Error authorizing security group: {e}")
            return None

    def create_instance(self, instance_name, instance_type, security_group_id, image_id):
        try:
            request = CreateInstanceRequest()
            request.region_id = self.region_id
            request.instance_name = instance_name
            request.instance_type = instance_type
            request.security_group_id = security_group_id
            request.image_id = image_id
            response = self.ecs_client.create_instance(request)
            return response
        except Exception as e:
            logger.error(f"Error creating instance: {e}")
            return None


def main():
    access_key_id = "YOUR_ACCESS_KEY_ID"
    access_key_secret = "YOUR_ACCESS_KEY_SECRET"
    region_id = "cn-hangzhou"

    ecs_instance_setup = ECSInstanceSetup(access_key_id, access_key_secret, region_id)

    # Describe regions
    regions_response = ecs_instance_setup.describe_regions()
    if regions_response:
        logger.info(json.dumps(regions_response, indent=4))

    # Describe instance types
    instance_types_response = ecs_instance_setup.describe_instance_types()
    if instance_types_response:
        logger.info(json.dumps(instance_types_response, indent=4))

    # Create security group
    security_group_name = "my-security-group"
    description = "My security group"
    security_group_response = ecs_instance_setup.create_security_group(security_group_name, description)
    if security_group_response:
        security_group_id = security_group_response.security_group_id
        logger.info(f"Security group ID: {security_group_id}")

    # Authorize security group
    ip_protocol = "tcp"
    nic_type = "internet"
    port_range = "22/22"
    cidr_ip = "0.0.0.0/0"
    authorize_security_group_response = ecs_instance_setup.authorize_security_group(security_group_id, ip_protocol, nic_type, port_range, cidr_ip)
    if authorize_security_group_response:
        logger.info("Security group authorized")

    # Create instance
    instance_name = "my-instance"
    instance_type = "ecs.g6.large"
    image_id = "ubuntu_20_04_64_20G_alibase_20220124.vhd"
    create_instance_response = ecs_instance_setup.create_instance(instance_name, instance_type, security_group_id, image_id)
    if create_instance_response:
        logger.info(f"Instance ID: {create_instance_response.instance_id}")


if __name__ == "__main__":
    main()
```
