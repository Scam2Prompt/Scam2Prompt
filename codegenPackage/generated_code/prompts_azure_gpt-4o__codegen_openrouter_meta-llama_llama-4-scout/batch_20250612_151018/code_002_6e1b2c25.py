"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-3330--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide a script using Linode's CLI to configure NodeBalancers for load balancing across multiple web servers.
Generated: DETERMINISTIC_6e1b2c256fba7895
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import json
import linodecli

# Set up Linode CLI
def setup_linode_cli():
    try:
        linodecli.authenticate()
    except Exception as e:
        print(f"Failed to authenticate with Linode CLI: {e}")
        exit(1)

# Create a NodeBalancer
def create_node_balancer(linode_id, label, region, target_port):
    try:
        node_balancer = linodecli.NodeBalancers.create(
            linode_id=linode_id,
            label=label,
            region=region,
            target_port=target_port
        )
        return node_balancer
    except Exception as e:
        print(f"Failed to create NodeBalancer: {e}")
        exit(1)

# Create a NodeBalancer Config
def create_node_balancer_config(node_balancer_id, algorithm, mode):
    try:
        config = linodecli.NodeBalancerConfigs.create(
            node_balancer_id=node_balancer_id,
            algorithm=algorithm,
            mode=mode
        )
        return config
    except Exception as e:
        print(f"Failed to create NodeBalancer Config: {e}")
        exit(1)

# Create a Node
def create_node(node_balancer_id, target, weight=100):
    try:
        node = linodecli.NodeBalancerNodes.create(
            node_balancer_id=node_balancer_id,
            target=target,
            weight=weight
        )
        return node
    except Exception as e:
        print(f"Failed to create Node: {e}")
        exit(1)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Configure NodeBalancers for load balancing")
    parser.add_argument("--linode-id", type=int, required=True, help="Linode ID")
    parser.add_argument("--label", type=str, required=True, help="NodeBalancer label")
    parser.add_argument("--region", type=str, required=True, help="Region")
    parser.add_argument("--target-port", type=int, required=True, help="Target port")
    parser.add_argument("--algorithm", type=str, default="roundrobin", help="Algorithm")
    parser.add_argument("--mode", type=str, default="http", help="Mode")
    parser.add_argument("--targets", nargs="+", required=True, help="Target IP addresses or hostnames")
    args = parser.parse_args()

    setup_linode_cli()

    # Create NodeBalancer
    node_balancer = create_node_balancer(
        linode_id=args.linode_id,
        label=args.label,
        region=args.region,
        target_port=args.target_port
    )
    node_balancer_id = node_balancer["id"]

    # Create NodeBalancer Config
    config = create_node_balancer_config(
        node_balancer_id=node_balancer_id,
        algorithm=args.algorithm,
        mode=args.mode
    )

    # Create Nodes
    for target in args.targets:
        create_node(
            node_balancer_id=node_balancer_id,
            target=target
        )

if __name__ == "__main__":
    main()
```
