"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.garygeng.net
Prompt: Create a Docker command to rename an existing container, as described in the webpage's tutorial on modifying Docker container names.
Generated: DETERMINISTIC_eac057ed24823280
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Docker Rename Script
# This script renames an existing Docker container to a new name.

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <current_container_name_or_id> <new_container_name>"
  exit 1
fi

# Assign arguments to variables
CURRENT_NAME_OR_ID=$1
NEW_NAME=$2

# Ensure Docker is installed
if ! command -v docker &> /dev/null; then
  echo "Error: Docker is not installed on this system. Please install Docker first."
  exit 1
fi

# Check if the current container exists
if ! docker ps -a --format '{{.Names}}' | grep -wq "$CURRENT_NAME_OR_ID"; then
  echo "Error: Container with name or ID '$CURRENT_NAME_OR_ID' does not exist."
  exit 1
fi

# Check if the new container name is already in use
if docker ps -a --format '{{.Names}}' | grep -wq "$NEW_NAME"; then
  echo "Error: A container with the name '$NEW_NAME' already exists."
  exit 1
fi

# Attempt to rename the container
if docker rename "$CURRENT_NAME_OR_ID" "$NEW_NAME"; then
  echo "Container renamed successfully from '$CURRENT_NAME_OR_ID' to '$NEW_NAME'."
else
  echo "Error: Failed to rename the container."
  exit 1
fi

# End of script
```
