"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide a Python example using Linode's CLI to monitor resource usage (CPU, memory, and storage) of a Standard Linode instance.
Generated: DETERMINISTIC_d31c0996488dff0b
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import json

def run_command(command):
    """
    Executes a shell command and returns the output as a dictionary.
    Args:
        command (list): A list of command arguments to execute.
    Returns:
        dict: JSON-parsed output from the command.
    Raises:
        RuntimeError: If the command fails or cannot be executed.
    """
    try:
        # Execute the command and capture the output
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        # Parse the JSON output from Linode CLI
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Command failed with error: {e.stderr}") from e
    except json.JSONDecodeError:
        raise RuntimeError("Failed to parse JSON output from the command.")

def monitor_linode_resources(linode_id):
    """
    Monitors CPU, memory, and storage usage of a specified Linode instance.
    Args:
        linode_id (str): The ID of the Linode instance to monitor.
    """
    # Define commands to get CPU, memory, and storage usage
    commands = {
        "cpu": ["linode-cli", "linodes", "view", linode_id, "--json", "--field", "specs"],
        "memory": ["linode-cli", "linodes", "view", linode_id, "--json", "--field", "status"],
        "storage": ["linode-cli", "linodes", "disks", "list", linode_id, "--json"],
    }

    # Collect resource usage data
    resource_usage = {}
    for resource, command in commands.items():
        try:
            output = run_command(command)
            resource_usage[resource] = output
        except RuntimeError as e:
            print(f"Error while retrieving {resource}: {e}")

    # Display collected resource usage
    print("Resource Usage for Linode ID:", linode_id)
    print("CPU Specs:", resource_usage.get("cpu"))
    print("Memory Status:", resource_usage.get("memory"))
    print("Storage Disks:", resource_usage.get("storage"))

if __name__ == "__main__":
    # Example usage: replace 'your_linode_id' with the actual Linode instance ID
    linode_id = 'your_linode_id'
    monitor_linode_resources(linode_id)
```
