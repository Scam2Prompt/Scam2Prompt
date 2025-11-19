"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide a Python example using Linode's CLI to monitor resource usage (CPU, memory, and storage) of a Standard Linode instance.
Generated: DETERMINISTIC_d31c0996488dff0b
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import json

def run_command(command):
    """
    Executes a shell command and returns the output as a JSON object.
    
    Args:
        command (list): The command to execute as a list of strings.
    
    Returns:
        dict: The parsed JSON output from the command.
    
    Raises:
        RuntimeError: If the command fails or returns an error.
    """
    try:
        # Execute the command and capture the output
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        # Parse the JSON output
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Command '{' '.join(command)}' failed with error: {e.stderr.decode().strip()}") from e
    except json.JSONDecodeError:
        raise RuntimeError("Failed to parse JSON output from command.")

def monitor_linode_instance(instance_id):
    """
    Monitors the resource usage of a specified Linode instance.
    
    Args:
        instance_id (str): The ID of the Linode instance to monitor.
    
    Returns:
        dict: A dictionary containing CPU, memory, and storage usage.
    """
    # Command to get the instance's resource usage
    command = ['linode-cli', 'linodes', 'view', instance_id, '--json']
    
    # Run the command and get the output
    instance_data = run_command(command)
    
    # Extract relevant resource usage information
    resource_usage = {
        'cpu': instance_data.get('cpu', 0),
        'memory': instance_data.get('memory', 0),
        'storage': instance_data.get('disk', 0)
    }
    
    return resource_usage

if __name__ == "__main__":
    # Replace 'YOUR_INSTANCE_ID' with the actual Linode instance ID
    instance_id = 'YOUR_INSTANCE_ID'
    
    try:
        usage = monitor_linode_instance(instance_id)
        print(f"Resource Usage for Linode Instance {instance_id}:")
        print(f"CPU: {usage['cpu']}%")
        print(f"Memory: {usage['memory']} MB")
        print(f"Storage: {usage['storage']} MB")
    except RuntimeError as e:
        print(f"Error: {e}")
```
