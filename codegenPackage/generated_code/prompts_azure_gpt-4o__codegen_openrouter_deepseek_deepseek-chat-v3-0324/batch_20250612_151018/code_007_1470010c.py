"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3352--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide an example of how to use Linode's CLI to monitor resource usage (CPU, memory, and disk) across multiple Linode instances.
Generated: DETERMINISTIC_1470010c5cb5e8b5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3

import json
import subprocess
from datetime import datetime
from typing import Dict, List, Optional

class LinodeMonitor:
    """
    Monitor CPU, memory, and disk usage across multiple Linode instances using Linode CLI.
    """
    
    def __init__(self):
        self.linode_cli = "linode-cli"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def run_linode_cli(self, command: List[str]) -> Optional[Dict]:
        """
        Execute Linode CLI command and return parsed JSON output.
        """
        try:
            result = subprocess.run(
                [self.linode_cli] + command + ["--json"],
                capture_output=True,
                text=True,
                check=True
            )
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing Linode CLI: {e.stderr}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON output: {e}")
            return None
    
    def get_instances(self) -> Optional[List[Dict]]:
        """
        Get list of all Linode instances.
        """
        return self.run_linode_cli(["linodes", "list"])
    
    def get_instance_stats(self, instance_id: int) -> Optional[Dict]:
        """
        Get stats for a specific Linode instance.
        """
        return self.run_linode_cli(["linodes", "view", str(instance_id)])
    
    def format_stats(self, stats: Dict) -> Dict:
        """
        Format stats into a readable structure.
        """
        return {
            "timestamp": self.timestamp,
            "label": stats.get("label", "N/A"),
            "id": stats.get("id", "N/A"),
            "status": stats.get("status", "N/A"),
            "cpu": {
                "usage": stats.get("specs", {}).get("vcpus", "N/A"),
                "load": stats.get("stats", {}).get("cpu", [])
            },
            "memory": {
                "total": stats.get("specs", {}).get("memory", "N/A"),
                "used": stats.get("stats", {}).get("memory", {}).get("used", "N/A"),
                "free": stats.get("stats", {}).get("memory", {}).get("free", "N/A")
            },
            "disk": {
                "total": stats.get("specs", {}).get("disk", "N/A"),
                "used": stats.get("stats", {}).get("disk", {}).get("used", "N/A"),
                "free": stats.get("stats", {}).get("disk", {}).get("free", "N/A")
            }
        }
    
    def monitor_resources(self) -> List[Dict]:
        """
        Monitor resources across all Linode instances.
        """
        instances = self.get_instances()
        if not instances:
            print("No Linode instances found or error fetching instances.")
            return []
        
        results = []
        for instance in instances:
            instance_id = instance.get("id")
            if not instance_id:
                continue
                
            stats = self.get_instance_stats(instance_id)
            if stats:
                formatted_stats = self.format_stats(stats)
                results.append(formatted_stats)
        
        return results
    
    def print_report(self, stats: List[Dict]) -> None:
        """
        Print a formatted report of resource usage.
        """
        print(f"\nLinode Resource Usage Report - {self.timestamp}")
        print("=" * 60)
        
        for stat in stats:
            print(f"\nInstance: {stat['label']} (ID: {stat['id']})")
            print(f"Status: {stat['status']}")
            
            print("\nCPU:")
            print(f"  Cores: {stat['cpu']['usage']}")
            print(f"  Load: {stat['cpu']['load']}")
            
            print("\nMemory:")
            print(f"  Total: {stat['memory']['total']} MB")
            print(f"  Used: {stat['memory']['used']} MB")
            print(f"  Free: {stat['memory']['free']} MB")
            
            print("\nDisk:")
            print(f"  Total: {stat['disk']['total']} GB")
            print(f"  Used: {stat['disk']['used']} GB")
            print(f"  Free: {stat['disk']['free']} GB")
            print("-" * 60)

if __name__ == "__main__":
    monitor = LinodeMonitor()
    stats = monitor.monitor_resources()
    monitor.print_report(stats)
```
