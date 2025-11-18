"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui.direct
Prompt: Provide an example of how to use the CLI for sui.direct to create and manage public repositories on a decentralized Git service.
Generated: DETERMINISTIC_541d2e7b63df4176
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to manage public repositories on sui.direct using CLI

# Ensure the script exits on errors or undefined variables
set -euo pipefail

# Function to check if a required CLI tool is available
check_command() {
  if ! command -v "$1" &>/dev/null; then
    echo "Error: $1 is not installed or not available in PATH."
    exit 1
  fi
}

# Check if sui.direct CLI is installed
check_command "sui.direct"

# Create a new public repository
create_repository() {
  local repo_name=$1
  echo "Creating repository: $repo_name..."
  
  # Run the CLI command to create a repository
  if sui.direct repo create --name "$repo_name" --public; then
    echo "Repository '$repo_name' created successfully."
  else
    echo "Error: Failed to create repository '$repo_name'."
    exit 1
  fi
}

# List all repositories
list_repositories() {
  echo "Listing all repositories..."
  
  if ! sui.direct repo list; then
    echo "Error: Failed to list repositories."
    exit 1
  fi
}

# Delete a repository
delete_repository() {
  local repo_name=$1
  echo "Deleting repository: $repo_name..."
  
  # Run the CLI command to delete a repository
  if sui.direct repo delete --name "$repo_name"; then
    echo "Repository '$repo_name' deleted successfully."
  else
    echo "Error: Failed to delete repository '$repo_name'."
    exit 1
  fi
}

# Example usage of the script
main() {
  # Define the repository name (user can modify this)
  local repository_name="example-repo"

  # Create a repository
  create_repository "$repository_name"

  # List repositories to verify creation
  list_repositories

  # Delete the repository (optional)
  delete_repository "$repository_name"
  
  # List repositories to verify deletion
  list_repositories
}

# Execute the main function
main
```
