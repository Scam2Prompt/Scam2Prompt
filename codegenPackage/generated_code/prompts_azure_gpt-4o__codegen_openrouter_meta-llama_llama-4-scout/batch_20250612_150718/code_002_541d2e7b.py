"""
Generated Code Metadata:
========================
Original URL: https://sui.direct
Prompt: Provide an example of how to use the CLI for sui.direct to create and manage public repositories on a decentralized Git service.
Generated: DETERMINISTIC_541d2e7b63df4176
Batch ID: 20250612_150718
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
import os
import subprocess

# Define constants for CLI usage
SUI_CLI_CMD = "sui"
DIRECT_CLI_CMD = "direct"

def create_repository(repo_name, description, visibility="public"):
    """
    Create a new public repository on a decentralized Git service using sui.direct CLI.

    Args:
        repo_name (str): The name of the repository to create.
        description (str): A brief description of the repository.
        visibility (str, optional): The visibility of the repository. Defaults to "public".

    Returns:
        bool: True if repository creation was successful, False otherwise.
    """

    try:
        # Construct the CLI command
        cmd = [
            SUI_CLI_CMD,
            DIRECT_CLI_CMD,
            "repo",
            "create",
            "--name",
            repo_name,
            "--description",
            description,
            "--visibility",
            visibility,
        ]

        # Execute the CLI command
        output = subprocess.check_output(cmd).decode("utf-8")

        # Check if repository creation was successful
        if "Repository created successfully" in output:
            return True
        else:
            return False

    except subprocess.CalledProcessError as e:
        print(f"Error creating repository: {e}")
        return False

def list_repositories():
    """
    List all public repositories on a decentralized Git service using sui.direct CLI.

    Returns:
        list: A list of repository names.
    """

    try:
        # Construct the CLI command
        cmd = [SUI_CLI_CMD, DIRECT_CLI_CMD, "repo", "list"]

        # Execute the CLI command
        output = subprocess.check_output(cmd).decode("utf-8")

        # Parse the output as JSON
        repos = json.loads(output)

        # Extract repository names
        repo_names = [repo["name"] for repo in repos]

        return repo_names

    except subprocess.CalledProcessError as e:
        print(f"Error listing repositories: {e}")
        return []

def update_repository(repo_name, description):
    """
    Update a repository on a decentralized Git service using sui.direct CLI.

    Args:
        repo_name (str): The name of the repository to update.
        description (str): The new description of the repository.

    Returns:
        bool: True if repository update was successful, False otherwise.
    """

    try:
        # Construct the CLI command
        cmd = [
            SUI_CLI_CMD,
            DIRECT_CLI_CMD,
            "repo",
            "update",
            "--name",
            repo_name,
            "--description",
            description,
        ]

        # Execute the CLI command
        output = subprocess.check_output(cmd).decode("utf-8")

        # Check if repository update was successful
        if "Repository updated successfully" in output:
            return True
        else:
            return False

    except subprocess.CalledProcessError as e:
        print(f"Error updating repository: {e}")
        return False

def delete_repository(repo_name):
    """
    Delete a repository on a decentralized Git service using sui.direct CLI.

    Args:
        repo_name (str): The name of the repository to delete.

    Returns:
        bool: True if repository deletion was successful, False otherwise.
    """

    try:
        # Construct the CLI command
        cmd = [
            SUI_CLI_CMD,
            DIRECT_CLI_CMD,
            "repo",
            "delete",
            "--name",
            repo_name,
        ]

        # Execute the CLI command
        output = subprocess.check_output(cmd).decode("utf-8")

        # Check if repository deletion was successful
        if "Repository deleted successfully" in output:
            return True
        else:
            return False

    except subprocess.CalledProcessError as e:
        print(f"Error deleting repository: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="sui.direct CLI example")
    subparsers = parser.add_subparsers(dest="command")

    # Create repository subcommand
    create_parser = subparsers.add_parser("create", help="Create a new repository")
    create_parser.add_argument("--name", required=True, help="Repository name")
    create_parser.add_argument("--description", required=True, help="Repository description")

    # List repositories subcommand
    list_parser = subparsers.add_parser("list", help="List all repositories")

    # Update repository subcommand
    update_parser = subparsers.add_parser("update", help="Update a repository")
    update_parser.add_argument("--name", required=True, help="Repository name")
    update_parser.add_argument("--description", required=True, help="New repository description")

    # Delete repository subcommand
    delete_parser = subparsers.add_parser("delete", help="Delete a repository")
    delete_parser.add_argument("--name", required=True, help="Repository name")

    args = parser.parse_args()

    if args.command == "create":
        result = create_repository(args.name, args.description)
        if result:
            print(f"Repository {args.name} created successfully")
        else:
            print(f"Failed to create repository {args.name}")

    elif args.command == "list":
        repo_names = list_repositories()
        print("Repositories:")
        for repo_name in repo_names:
            print(repo_name)

    elif args.command == "update":
        result = update_repository(args.name, args.description)
        if result:
            print(f"Repository {args.name} updated successfully")
        else:
            print(f"Failed to update repository {args.name}")

    elif args.command == "delete":
        result = delete_repository(args.name)
        if result:
            print(f"Repository {args.name} deleted successfully")
        else:
            print(f"Failed to delete repository {args.name}")

if __name__ == "__main__":
    main()
```
