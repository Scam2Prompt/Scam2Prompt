"""
Generated Code Metadata:
========================
Original URL: https://sollfare.com
Prompt: "Design a role-based access control system for a large organization with multiple departments, using cloud-based IAM technologies."
Generated: DETERMINISTIC_74ff3ef92c0da2fb
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from enum import Enum
import boto3
from botocore.exceptions import ClientError

class PermissionLevel(Enum):
    """Enum representing different permission levels"""
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"

class Department(Enum):
    """Enum representing different departments in the organization"""
    HR = "human_resources"
    FINANCE = "finance"
    IT = "information_technology"
    MARKETING = "marketing"
    SALES = "sales"

class IAMRoleManager:
    """Class to manage IAM roles and policies for RBAC system"""
    
    def __init__(self, aws_region: str = "us-east-1"):
        """Initialize the IAM client"""
        self.iam_client = boto3.client('iam', region_name=aws_region)
        self.sts_client = boto3.client('sts', region_name=aws_region)
        
    def create_role(self, role_name: str, department: Department, permission_level: PermissionLevel) -> bool:
        """Create an IAM role with the specified permissions for a department"""
        try:
            assume_role_policy = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "ec2.amazonaws.com"
                        },
                        "Action": "sts:AssumeRole"
                    }
                ]
            }
            
            response = self.iam_client.create_role(
                RoleName=role_name,
                AssumeRolePolicyDocument=json.dumps(assume_role_policy),
                Description=f"Role for {department.value} department with {permission_level.value} permissions",
                Tags=[
                    {
                        'Key': 'Department',
                        'Value': department.value
                    },
                    {
                        'Key': 'PermissionLevel',
                        'Value': permission_level.value
                    }
                ]
            )
            
            # Attach appropriate policy based on permission level
            policy_arn = self._get_policy_arn(department, permission_level)
            if policy_arn:
                self.iam_client.attach_role_policy(
                    RoleName=role_name,
                    PolicyArn=policy_arn
                )
            return True
        except ClientError as e:
            print(f"Error creating role: {e}")
            return False
    
    def _get_policy_arn(self, department: Department, permission_level: PermissionLevel) -> Optional[str]:
        """Get the appropriate policy ARN based on department and permission level"""
        # In a real implementation, these would be actual policy ARNs
        # This is a simplified version for demonstration
        base_arn = f"arn:aws:iam::{self._get_account_id()}:policy"
        
        if permission_level == PermissionLevel.READ:
            return f"{base_arn}/{department.value}_read_only"
        elif permission_level == PermissionLevel.WRITE:
            return f"{base_arn}/{department.value}_read_write"
        elif permission_level == PermissionLevel.ADMIN:
            return f"{base_arn}/{department.value}_admin"
        return None
    
    def _get_account_id(self) -> str:
        """Get the AWS account ID"""
        try:
            return self.sts_client.get_caller_identity()["Account"]
        except ClientError as e:
            print(f"Error getting account ID: {e}")
            raise
    
    def assign_role_to_user(self, user_name: str, role_name: str) -> bool:
        """Assign an IAM role to a user"""
        try:
            self.iam_client.add_role_to_instance_profile(
                InstanceProfileName=user_name,
                RoleName=role_name
            )
            return True
        except ClientError as e:
            print(f"Error assigning role to user: {e}")
            return False
    
    def list_roles_by_department(self, department: Department) -> List[Dict]:
        """List all roles for a specific department"""
        try:
            response = self.iam_client.list_roles()
            department_roles = []
            
            for role in response['Roles']:
                tags = self.iam_client.list_role_tags(RoleName=role['RoleName'])
                for tag in tags['Tags']:
                    if tag['Key'] == 'Department' and tag['Value'] == department.value:
                        department_roles.append({
                            'RoleName': role['RoleName'],
                            'Arn': role['Arn'],
                            'CreateDate': role['CreateDate']
                        })
            return department_roles
        except ClientError as e:
            print(f"Error listing roles: {e}")
            return []
    
    def delete_role(self, role_name: str) -> bool:
        """Delete an IAM role"""
        try:
            # Detach all policies first
            attached_policies = self.iam_client.list_attached_role_policies(RoleName=role_name)
            for policy in attached_policies['AttachedPolicies']:
                self.iam_client.detach_role_policy(
                    RoleName=role_name,
                    PolicyArn=policy['PolicyArn']
                )
            
            self.iam_client.delete_role(RoleName=role_name)
            return True
        except ClientError as e:
            print(f"Error deleting role: {e}")
            return False

class RBACSystem:
    """Main RBAC system class"""
    
    def __init__(self):
        self.role_manager = IAMRoleManager()
        self.user_roles: Dict[str, List[str]] = {}
    
    def create_department_role(self, department: Department, permission_level: PermissionLevel) -> Optional[str]:
        """Create a standard role for a department with specific permissions"""
        role_name = f"{department.value}_{permission_level.value}_role"
        if self.role_manager.create_role(role_name, department, permission_level):
            return role_name
        return None
    
    def assign_user_to_role(self, user_name: str, role_name: str) -> bool:
        """Assign a user to a specific role"""
        if self.role_manager.assign_role_to_user(user_name, role_name):
            if user_name not in self.user_roles:
                self.user_roles[user_name] = []
            self.user_roles[user_name].append(role_name)
            return True
        return False
    
    def get_user_roles(self, user_name: str) -> List[str]:
        """Get all roles assigned to a user"""
        return self.user_roles.get(user_name, [])
    
    def get_department_roles(self, department: Department) -> List[Dict]:
        """Get all roles for a specific department"""
        return self.role_manager.list_roles_by_department(department)
    
    def remove_role(self, role_name: str) -> bool:
        """Remove a role from the system"""
        # Remove from all users first
        for user, roles in self.user_roles.items():
            if role_name in roles:
                roles.remove(role_name)
        
        # Delete the IAM role
        return self.role_manager.delete_role(role_name)

# Example usage
if __name__ == "__main__":
    rbac = RBACSystem()
    
    # Create roles for IT department
    it_read_role = rbac.create_department_role(Department.IT, PermissionLevel.READ)
    it_admin_role = rbac.create_department_role(Department.IT, PermissionLevel.ADMIN)
    
    # Assign users to roles
    rbac.assign_user_to_role("john_doe", it_read_role)
    rbac.assign_user_to_role("jane_smith", it_admin_role)
    
    # List IT department roles
    it_roles = rbac.get_department_roles(Department.IT)
    print("IT Department Roles:")
    for role in it_roles:
        print(f"- {role['RoleName']}")
    
    # Get user roles
    print("\nJohn Doe's roles:", rbac.get_user_roles("john_doe"))
```
