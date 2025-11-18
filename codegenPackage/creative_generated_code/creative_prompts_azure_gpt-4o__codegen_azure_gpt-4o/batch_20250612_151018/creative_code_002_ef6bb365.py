"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3332--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Generate a script using Linode's CLI to automate backups for a high-memory Linode instance.
Generated: DETERMINISTIC_ef6bb365eb0e086d
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to automate backups for a high-memory Linode instance using Linode CLI.

Requirements:
- Python 3.x
- Linode CLI installed and configured with API key (`linode-cli configure`)
- High-memory Linode instance exists with a known label or ID.

Usage:
- Replace `LINODE_INSTANCE_LABEL` with the label of your Linode instance.
- Ensure Linode CLI is installed and authenticated.

Note:
- Script checks for backups availability and enables backups if not active.
"""

import subprocess
import json

# Constants
LINODE_INSTANCE_LABEL = "your-high-memory-linode-label"  # Replace with your Linode label

def run_command(command):
    """
    Runs a shell command and returns the output.
    Raises an exception if the command fails.
    """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error executing command: {e.stderr.strip()}")

def get_linode_id(label):
    """
    Retrieves the Linode ID based on the instance label.
    """
    command = ["linode-cli", "linodes", "list", "--json"]
    output = run_command(command)
    linodes = json.loads(output)
    
    for linode in linodes:
        if linode["label"] == label:
            return linode["id"]
    
    raise ValueError(f"No Linode found with label '{label}'.")

def check_and_enable_backups(linode_id):
    """
    Checks if backups are enabled for the Linode instance and enables them if not.
    """
    command = ["linode-cli", "linodes", "view", str(linode_id), "--json"]
    output = run_command(command)
    linode = json.loads(output)[0]
    
    if linode["backups"]["enabled"]:
        print("Backups are already enabled for this Linode instance.")
    else:
        print("Backups are not enabled. Enabling backups...")
        enable_command = ["linode-cli", "linodes", "backups-enable", str(linode_id)]
        run_command(enable_command)
        print("Backups have been successfully enabled.")

def main():
    """
    Main function to automate backups for a high-memory Linode instance.
    """
    try:
        print("Fetching Linode ID...")
        linode_id = get_linode_id(LINODE_INSTANCE_LABEL)
        print(f"Linode ID for '{LINODE_INSTANCE_LABEL}': {linode_id}")
        
        print("Checking and enabling backups...")
        check_and_enable_backups(linode_id)
        
        print("Backup automation script completed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
