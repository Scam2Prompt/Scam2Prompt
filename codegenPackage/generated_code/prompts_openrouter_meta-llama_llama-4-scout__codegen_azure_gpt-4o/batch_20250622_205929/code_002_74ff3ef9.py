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
"""
Role-Based Access Control System using AWS IAM
This script demonstrates how to set up a role-based access control system for a large organization
with multiple departments using AWS IAM. It uses the Boto3 library to interact with AWS services.

Prerequisites:
- AWS account with IAM permissions to create roles, policies, and users.
- Boto3 library installed (`pip install boto3`).
"""

import boto3
from botocore.exceptions import ClientError

# Initialize AWS IAM client
iam_client = boto3.client('iam')

def create_iam_role(role_name, policy_document):
    """
    Create an IAM role with the specified name and policy document.

    :param role_name: Name of the IAM role to create.
    :param policy_document: JSON policy document defining permissions for the role.
    :return: ARN of the created role.
    """
    try:
        response = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=policy_document
        )
        print(f"Role '{role_name}' created successfully.")
        return response['Role']['Arn']
    except ClientError as e:
        print(f"Error creating role '{role_name}': {e}")
        return None

def attach_policy_to_role(role_name, policy_arn):
    """
    Attach a managed policy to an IAM role.

    :param role_name: Name of the IAM role.
    :param policy_arn: ARN of the managed policy to attach.
    """
    try:
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        print(f"Policy '{policy_arn}' attached to role '{role_name}'.")
    except ClientError as e:
        print(f"Error attaching policy to role '{role_name}': {e}")

def create_user(user_name):
    """
    Create an IAM user.

    :param user_name: Name of the IAM user to create.
    :return: ARN of the created user.
    """
    try:
        response = iam_client.create_user(
            UserName=user_name
        )
        print(f"User '{user_name}' created successfully.")
        return response['User']['Arn']
    except ClientError as e:
        print(f"Error creating user '{user_name}': {e}")
        return None

def add_user_to_group(user_name, group_name):
    """
    Add an IAM user to a group.

    :param user_name: Name of the IAM user.
    :param group_name: Name of the IAM group.
    """
    try:
        iam_client.add_user_to_group(
            UserName=user_name,
            GroupName=group_name
        )
        print(f"User '{user_name}' added to group '{group_name}'.")
    except ClientError as e:
        print(f"Error adding user '{user_name}' to group '{group_name}': {e}")

def create_group(group_name):
    """
    Create an IAM group.

    :param group_name: Name of the IAM group to create.
    :return: ARN of the created group.
    """
    try:
        response = iam_client.create_group(
            GroupName=group_name
        )
        print(f"Group '{group_name}' created successfully.")
        return response['Group']['Arn']
    except ClientError as e:
        print(f"Error creating group '{group_name}': {e}")
        return None

def attach_policy_to_group(group_name, policy_arn):
    """
    Attach a managed policy to an IAM group.

    :param group_name: Name of the IAM group.
    :param policy_arn: ARN of the managed policy to attach.
    """
    try:
        iam_client.attach_group_policy(
            GroupName=group_name,
            PolicyArn=policy_arn
        )
        print(f"Policy '{policy_arn}' attached to group '{group_name}'.")
    except ClientError as e:
        print(f"Error attaching policy to group '{group_name}': {e}")

# Example usage
if __name__ == "__main__":
    # Define a sample policy document for role creation
    sample_policy_document = """
    {
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
    """

    # Create roles for departments
    finance_role_arn = create_iam_role("FinanceRole", sample_policy_document)
    hr_role_arn = create_iam_role("HRRole", sample_policy_document)

    # Attach policies to roles
    attach_policy_to_role("FinanceRole", "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")
    attach_policy_to_role("HRRole", "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess")

    # Create groups for departments
    finance_group_arn = create_group("FinanceGroup")
    hr_group_arn = create_group("HRGroup")

    # Attach policies to groups
    attach_policy_to_group("FinanceGroup", "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")
    attach_policy_to_group("HRGroup", "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess")

    # Create users and add them to groups
    finance_user_arn = create_user("FinanceUser")
    hr_user_arn = create_user("HRUser")

    add_user_to_group("FinanceUser", "FinanceGroup")
    add_user_to_group("HRUser", "HRGroup")
```
