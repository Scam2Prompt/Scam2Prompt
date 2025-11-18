"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3352--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide an example of how to use Linode's CLI to monitor resource usage (CPU, memory, and disk) across multiple Linode instances.
Generated: DETERMINISTIC_1470010c5cb5e8b5
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

def get_linode_metrics():
    """
    Retrieves resource usage (CPU, memory, disk) for all Linode instances using Linode CLI.
    
    Returns:
        list: A list of dictionaries containing resource metrics for each Linode instance.
    """
    try:
        # Fetch all Linode instances using Linode CLI
        result = subprocess.run(
            ["linode-cli", "linodes", "list", "--json"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            raise RuntimeError(f"Linode CLI error: {result.stderr.strip()}")

        # Parse the JSON output
        linodes = json.loads(result.stdout)

        metrics = []
        for linode in linodes:
            instance_id = linode.get("id")
            instance_label = linode.get("label")
            
            # Fetch resource usage for each Linode instance
            monitor_result = subprocess.run(
                ["linode-cli", "linode-stats", instance_id, "--json"],
                capture_output=True,
                text=True
            )
            
            if monitor_result.returncode != 0:
                raise RuntimeError(f"Error fetching stats for Linode {instance_label}: {monitor_result.stderr.strip()}")

            stats = json.loads(monitor_result.stdout)
            
            # Extract relevant metrics
            metrics.append({
                "id": instance_id,
                "label": instance_label,
                "cpu_usage": stats.get("cpu", {}).get("usage"),
                "memory_usage": stats.get("memory", {}).get("usage"),
                "disk_usage": stats.get("disk", {}).get("usage")
            })

        return metrics

    except (subprocess.SubprocessError, json.JSONDecodeError, RuntimeError) as e:
        print(f"Error occurred: {e}")
        return []

def main():
    """
    Main function to execute monitoring of Linode instances and display results.
    """
    print("Fetching resource metrics for Linode instances...")
    metrics = get_linode_metrics()
    
    if not metrics:
        print("No metrics available or an error occurred.")
        return
    
    print("Resource Metrics for Linode Instances:")
    for metric in metrics:
        print(f"Instance: {metric['label']} (ID: {metric['id']})")
        print(f"  CPU Usage: {metric['cpu_usage']}%")
        print(f"  Memory Usage: {metric['memory_usage']} MB")
        print(f"  Disk Usage: {metric['disk_usage']} MB")
        print("-" * 40)

if __name__ == "__main__":
    main()
```

Ensure you have the `linode-cli` installed and properly configured with access to your Linode account for this script to work.
