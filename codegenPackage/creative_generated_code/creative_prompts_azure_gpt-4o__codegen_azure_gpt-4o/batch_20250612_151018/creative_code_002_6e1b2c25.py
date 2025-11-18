"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3330--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide a script using Linode's CLI to configure NodeBalancers for load balancing across multiple web servers.
Generated: DETERMINISTIC_6e1b2c256fba7895
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3

import subprocess
import json
import sys

# Function to execute Linode CLI commands and handle errors
def run_linode_cli(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e.stderr}", file=sys.stderr)
        sys.exit(1)

# Configuration variables
NODEBALANCER_LABEL = "web-nodebalancer"
REGION = "us-east"  # Change this to your preferred region
PORT = 80  # Port for HTTP traffic
PROTOCOL = "http"  # Protocol (http or https)
STICKINESS = "none"  # Options: none, table, or http_cookie
WEB_SERVERS = [
    {"address": "192.168.1.101", "port": 80, "weight": 100},
    {"address": "192.168.1.102", "port": 80, "weight": 100},
    {"address": "192.168.1.103", "port": 80, "weight": 100},
]

# Step 1: Create a NodeBalancer
print("Creating NodeBalancer...")
nodebalancer = run_linode_cli([
    "linode-cli", "nodebalancers", "create",
    "--label", NODEBALANCER_LABEL,
    "--region", REGION,
    "--json"
])
nodebalancer_id = nodebalancer[0]['id']
print(f"NodeBalancer created with ID: {nodebalancer_id}")

# Step 2: Configure a NodeBalancer configuration for the backend pool
print("Configuring backend pool...")
config = run_linode_cli([
    "linode-cli", "nodebalancer-configs", "create",
    "--nodebalancer-id", str(nodebalancer_id),
    "--port", str(PORT),
    "--protocol", PROTOCOL,
    "--stickiness", STICKINESS,
    "--json"
])
config_id = config[0]['id']
print(f"Backend pool configured with ID: {config_id}")

# Step 3: Add nodes to the backend pool
for server in WEB_SERVERS:
    print(f"Adding server {server['address']}:{server['port']} to backend pool...")
    run_linode_cli([
        "linode-cli", "nodebalancer-nodes", "create",
        "--nodebalancer-id", str(nodebalancer_id),
        "--config-id", str(config_id),
        "--address", f"{server['address']}:{server['port']}",
        "--weight", str(server['weight']),
        "--json"
    ])
    print(f"Server {server['address']} added successfully.")

print("NodeBalancer setup complete.")
```

Make sure you have `linode-cli` installed and configured on the machine running this script. It requires an API token to authenticate with Linode's API. Update the configuration variables to match your setup.
