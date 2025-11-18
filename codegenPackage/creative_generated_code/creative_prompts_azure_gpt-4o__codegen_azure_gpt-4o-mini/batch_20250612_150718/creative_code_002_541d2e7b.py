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

# This script demonstrates how to use the CLI for sui.direct
# to create and manage public repositories on a decentralized Git service.

# Function to display usage
usage() {
    echo "Usage: $0 {create|list|delete} [repo_name]"
    echo "Commands:"
    echo "  create    Create a new public repository"
    echo "  list      List all public repositories"
    echo "  delete    Delete a public repository"
    exit 1
}

# Check if the correct number of arguments is provided
if [ $# -lt 1 ]; then
    usage
fi

# Command variable
COMMAND=$1
REPO_NAME=$2

# Function to create a new public repository
create_repo() {
    if [ -z "$REPO_NAME" ]; then
        echo "Error: Please provide a repository name."
        exit 1
    fi
    
    # Command to create a new public repository
    echo "Creating public repository: $REPO_NAME..."
    sui.direct repo create --name "$REPO_NAME" --visibility public
    
    if [ $? -eq 0 ]; then
        echo "Repository '$REPO_NAME' created successfully."
    else
        echo "Error: Failed to create repository '$REPO_NAME'."
        exit 1
    fi
}

# Function to list all public repositories
list_repos() {
    echo "Listing all public repositories..."
    sui.direct repo list --visibility public
    
    if [ $? -ne 0 ]; then
        echo "Error: Failed to list repositories."
        exit 1
    fi
}

# Function to delete a public repository
delete_repo() {
    if [ -z "$REPO_NAME" ]; then
        echo "Error: Please provide a repository name to delete."
        exit 1
    fi
    
    # Command to delete the specified repository
    echo "Deleting repository: $REPO_NAME..."
    sui.direct repo delete --name "$REPO_NAME"
    
    if [ $? -eq 0 ]; then
        echo "Repository '$REPO_NAME' deleted successfully."
    else
        echo "Error: Failed to delete repository '$REPO_NAME'."
        exit 1
    fi
}

# Main logic to execute the appropriate command
case $COMMAND in
    create)
        create_repo
        ;;
    list)
        list_repos
        ;;
    delete)
        delete_repo
        ;;
    *)
        echo "Error: Unknown command '$COMMAND'."
        usage
        ;;
esac
```

**Usage Instructions:**
- Save the script to a file, for example, `manage_repos.sh`.
- Make the script executable: `chmod +x manage_repos.sh`.
- Execute the script with commands like:
  - To create a repository: `./manage_repos.sh create my-repo`
  - To list repositories: `./manage_repos.sh list`
  - To delete a repository: `./manage_repos.sh delete my-repo`
