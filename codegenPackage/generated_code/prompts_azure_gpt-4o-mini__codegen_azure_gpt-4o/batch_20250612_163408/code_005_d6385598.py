"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3330--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide an example of using Linode's CLI to create and manage high memory Linodes.
Generated: DETERMINISTIC_d638559879abd03e
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Script to create and manage high memory Linodes using Linode CLI
# Ensure you have Linode CLI installed and configured with your API token before running this script.

# Function to create a high memory Linode
create_high_memory_linode() {
  # Parameters
  LINODE_LABEL="high-memory-linode"  # Label for the Linode
  REGION="us-east"                  # Region where the Linode will be created
  TYPE="g6-highmem-2"               # High memory Linode type (e.g., 32GB RAM)
  IMAGE="linode/ubuntu22.04"        # Image to use for the Linode
  ROOT_PASS="YourSecurePassword123" # Root password for the Linode

  echo "Creating a high memory Linode..."
  linode-cli linodes create \
    --label "$LINODE_LABEL" \
    --region "$REGION" \
    --type "$TYPE" \
    --image "$IMAGE" \
    --root_pass "$ROOT_PASS" \
    --booted true \
    --authorized_keys "$(cat ~/.ssh/id_rsa.pub)" # Add your SSH public key for secure access

  if [ $? -eq 0 ]; then
    echo "High memory Linode created successfully!"
  else
    echo "Failed to create Linode. Please check your parameters and try again."
    exit 1
  fi
}

# Function to list all Linodes
list_linodes() {
  echo "Listing all Linodes..."
  linode-cli linodes list
}

# Function to delete a Linode by ID
delete_linode() {
  LINODE_ID=$1

  if [ -z "$LINODE_ID" ]; then
    echo "Error: Linode ID is required to delete a Linode."
    exit 1
  fi

  echo "Deleting Linode with ID: $LINODE_ID..."
  linode-cli linodes delete "$LINODE_ID"

  if [ $? -eq 0 ]; then
    echo "Linode deleted successfully!"
  else
    echo "Failed to delete Linode. Please check the ID and try again."
    exit 1
  fi
}

# Main menu for managing Linodes
echo "Linode Management Script"
echo "1. Create High Memory Linode"
echo "2. List Linodes"
echo "3. Delete Linode"
echo "4. Exit"
read -p "Choose an option: " OPTION

case $OPTION in
  1)
    create_high_memory_linode
    ;;
  2)
    list_linodes
    ;;
  3)
    read -p "Enter Linode ID to delete: " LINODE_ID
    delete_linode "$LINODE_ID"
    ;;
  4)
    echo "Exiting script."
    exit 0
    ;;
  *)
    echo "Invalid option. Please try again."
    exit 1
    ;;
esac
```
