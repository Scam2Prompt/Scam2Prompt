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
import sys


def monitor_linode_resources(instance_label):
    """
    Monitors resource usage (CPU, memory, and storage) of a Standard Linode instance using Linode CLI.

    :param instance_label: str - Label of the Linode instance to monitor.
    """
    try:
        # Fetch instance details using Linode CLI
        result = subprocess.run(
            ["linode-cli", "linodes", "view", "--label", instance_label, "--json"],
            capture_output=True,
            text=True,
            check=True
        )
        # Parse the output as JSON
        instance_data = json.loads(result.stdout)

        if not instance_data:
            print(f"No Linode instance found with label {instance_label}.")
            return
        
        # Access resource usage metrics
        linode = instance_data[0]  # Assuming one instance matches the label
        print(f"Monitoring Linode Instance: {linode['label']} (ID: {linode['id']})")
        print(f"Status: {linode['status']}")
        print(f"Region: {linode['region']}")
        print("\nResource Usage:")
        print(f"  CPU: {linode['specs']['vcpus']} cores")
        print(f"  Memory: {linode['specs']['memory']} MB")
        print(f"  Storage: {linode['specs']['disk']} GB")

    except subprocess.CalledProcessError as e:
        # Handle errors from Linode CLI command
        print(f"Error while executing Linode CLI: {e.stderr.strip()}")
    except json.JSONDecodeError:
        # Handle JSON parsing errors
        print("Failed to parse the output from Linode CLI. Ensure it returns valid JSON.")
    except KeyError as e:
        # Handle missing keys in the Linode API response
        print(f"Missing expected key in Linode response: {e}")
    except Exception as e:
        # General error handling
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Verify CLI arguments
    if len(sys.argv) != 2:
        print("Usage: python monitor_linode.py <instance_label>")
        sys.exit(1)

    # Fetch Linode instance label from command-line arguments
    linode_instance_label = sys.argv[1]
    monitor_linode_resources(linode_instance_label)
```
