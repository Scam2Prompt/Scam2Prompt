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

# Function to rename a Docker container
# Usage: rename_container <old_name> <new_name>
rename_container() {
    # Check if the correct number of arguments is provided
    if [ "$#" -ne 2 ]; then
        echo "Usage: rename_container <old_name> <new_name>"
        exit 1
    fi

    old_name=$1
    new_name=$2

    # Check if the old container exists
    if [ "$(docker ps -a -q -f name=$old_name)" ]; then
        # Rename the container using the Docker rename command
        docker rename "$old_name" "$new_name"

        # Check if the rename command was successful
        if [ $? -eq 0 ]; then
            echo "Container '$old_name' has been renamed to '$new_name'."
        else
            echo "Error: Failed to rename container '$old_name'."
            exit 1
        fi
    else
        echo "Error: Container '$old_name' does not exist."
        exit 1
    fi
}

# Call the function with command line arguments
rename_container "$@"
```

To run the script, save it to a file (e.g., `rename_container.sh`), give it execute permissions with `chmod +x rename_container.sh`, and execute it with the old and new container names as arguments.
