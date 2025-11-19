"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide an example of using Linode's CLI to create a high memory instance for a database application.
Generated: DETERMINISTIC_c6b99cc75c3a3302
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Linode CLI example to create a high memory instance for a database application.

Requirements:
- linode-cli installed and configured with API token
- python3
"""

import subprocess
import json
import sys
from typing import Dict, Any, Optional

def run_linode_cli_command(args: list) -> Dict[str, Any]:
    """
    Execute a linode-cli command and return the JSON output.
    
    Args:
        args: List of arguments to pass to linode-cli
        
    Returns:
        Dictionary containing the command output
        
    Raises:
        RuntimeError: If command fails or returns invalid JSON
    """
    try:
        result = subprocess.run(
            ["linode-cli", "--json"] + args,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Command failed: {e.stderr}") from e
    except json.JSONDecodeError as e:
        raise RuntimeError("Failed to parse JSON output") from e

def get_region_id(region: str) -> Optional[str]:
    """Get the region ID for the given region label."""
    regions = run_linode_cli_command(["regions", "list"])
    for r in regions:
        if r["id"] == region:
            return r["id"]
    return None

def get_image_id(image: str) -> Optional[str]:
    """Get the image ID for the given image label."""
    images = run_linode_cli_command(["images", "list"])
    for img in images:
        if img["id"] == image:
            return img["id"]
    return None

def get_type_id(type_label: str) -> Optional[str]:
    """Get the type ID for the given instance type."""
    types = run_linode_cli_command(["linodes", "types"])
    for t in types:
        if t["id"] == type_label:
            return t["id"]
    return None

def create_high_memory_instance(
    label: str,
    region: str,
    image: str,
    type_label: str,
    root_pass: str,
    tags: list = None
) -> Dict[str, Any]:
    """
    Create a high memory Linode instance.
    
    Args:
        label: Instance label
        region: Region ID (e.g., 'us-east')
        image: Image ID (e.g., 'linode/ubuntu22.04')
        type_label: Instance type (e.g., 'g6-highmem-16')
        root_pass: Root password
        tags: Optional list of tags
        
    Returns:
        Dictionary containing the created instance info
    """
    if not tags:
        tags = ["database", "high-memory"]
    
    if not get_region_id(region):
        raise ValueError(f"Invalid region: {region}")
    
    if not get_image_id(image):
        raise ValueError(f"Invalid image: {image}")
    
    if not get_type_id(type_label):
        raise ValueError(f"Invalid type: {type_label}")
    
    create_args = [
        "linodes", "create",
        "--label", label,
        "--region", region,
        "--image", image,
        "--type", type_label,
        "--root_pass", root_pass,
        "--tags", ",".join(tags),
        "--authorized_users", "your_ssh_username",  # Replace with your SSH username
        "--private_ip", "true",
        "--backups_enabled", "true"
    ]
    
    return run_linode_cli_command(create_args)

def main():
    try:
        # Configuration - adjust these values as needed
        instance_config = {
            "label": "db-primary-01",
            "region": "us-east",
            "image": "linode/ubuntu22.04",
            "type_label": "g6-highmem-16",  # 16GB high memory instance
            "root_pass": "secure_password_123",  # In production, use a password manager
            "tags": ["production", "database", "postgresql"]
        }
        
        print("Creating high memory database instance...")
        instance = create_high_memory_instance(**instance_config)
        
        print("Instance created successfully:")
        print(json.dumps(instance, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
"Private IPv4: {instance['ipv4'][1] if len(instance['ipv4']) > 1 else 'None'}")
        print(f"Status: {instance['status']}")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
