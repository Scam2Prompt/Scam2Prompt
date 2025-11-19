"""
Generated Code Metadata:
========================
Original URL: https://sui.direct
Prompt: Generate a sample command-line interface (CLI) command for customizing a node in the sui.storage protocol.
Generated: DETERMINISTIC_3fd78e028208ebca
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
import argparse
import sys
import json
from typing import Optional, Dict, Any

def configure_node(
    node_id: str,
    storage_path: Optional[str] = None,
    max_capacity: Optional[int] = None,
    network_port: Optional[int] = None,
    config_file: Optional[str] = None
) -> Dict[str, Any]:
    """
    Configures a node in the sui.storage protocol with the given parameters.
    
    Args:
        node_id: Unique identifier for the node (required)
        storage_path: Path to storage directory (optional)
        max_capacity: Maximum storage capacity in GB (optional)
        network_port: Network port for communication (optional)
        config_file: Path to existing config file to update (optional)
    
    Returns:
        Dictionary containing the node configuration
    
    Raises:
        ValueError: If invalid parameters are provided
        IOError: If config file operations fail
    """
    config = {}
    
    # Load existing config if file is provided
    if config_file:
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
        except FileNotFoundError:
            print(f"Warning: Config file {config_file} not found. Creating new config.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in config file: {config_file}")
    
    # Update configuration with new values
    config['node_id'] = node_id
    if storage_path:
        config['storage_path'] = storage_path
    if max_capacity:
        if max_capacity <= 0:
            raise ValueError("max_capacity must be a positive integer")
        config['max_capacity_gb'] = max_capacity
    if network_port:
        if not (1024 <= network_port <= 65535):
            raise ValueError("network_port must be between 1024 and 65535")
        config['network_port'] = network_port
    
    return config

def save_config(config: Dict[str, Any], output_file: str) -> None:
    """
    Saves the configuration to a JSON file.
    
    Args:
        config: Configuration dictionary to save
        output_file: Path to output file
    
    Raises:
        IOError: If file operations fail
    """
    try:
        with open(output_file, 'w') as f:
            json.dump(config, f, indent=2)
    except IOError as e:
        raise IOError(f"Failed to save config to {output_file}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(
        description="SUI.Storage Node Configuration Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Required arguments
    parser.add_argument(
        '--node-id',
        required=True,
        help="Unique identifier for the node"
    )
    
    # Optional arguments
    parser.add_argument(
        '--storage-path',
        help="Path to storage directory"
    )
    parser.add_argument(
        '--max-capacity',
        type=int,
        help="Maximum storage capacity in GB"
    )
    parser.add_argument(
        '--network-port',
        type=int,
        help="Network port for communication (1024-65535)"
    )
    parser.add_argument(
        '--config-file',
        help="Path to existing config file to update"
    )
    parser.add_argument(
        '--output-file',
        default='node_config.json',
        help="Path to save the configuration"
    )
    
    args = parser.parse_args()
    
    try:
        config = configure_node(
            node_id=args.node_id,
            storage_path=args.storage_path,
            max_capacity=args.max_capacity,
            network_port=args.network_port,
            config_file=args.config_file
        )
        
        save_config(config, args.output_file)
        print(f"Successfully saved node configuration to {args.output_file}")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
