"""
Generated Code Metadata:
========================
Original URL: https://hyperlane-c77043.webflow.io
Prompt: "Generate code to create a Warp Route for token bridging between two chains using Hyperlane's CLI commands."
Generated: DETERMINISTIC_50207ea4fd92596e
Batch ID: 20250622_212307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import sys

def create_warp_route(origin_chain, destination_chain, token_address, warp_route_name):
    """
    Creates a Warp Route for token bridging between two chains using Hyperlane's CLI commands.

    Parameters:
        origin_chain (str): The name of the origin chain.
        destination_chain (str): The name of the destination chain.
        token_address (str): The address of the token to be bridged.
        warp_route_name (str): The name of the warp route.

    Returns:
        None
    """
    try:
        # Validate input parameters
        if not origin_chain or not destination_chain or not token_address or not warp_route_name:
            raise ValueError("All parameters (origin_chain, destination_chain, token_address, warp_route_name) are required.")

        # Construct the Hyperlane CLI command
        command = [
            "hyperlane",
            "warp-route",
            "create",
            "--origin-chain", origin_chain,
            "--destination-chain", destination_chain,
            "--token-address", token_address,
            "--name", warp_route_name
        ]

        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Check for errors during execution
        if result.returncode != 0:
            raise RuntimeError(f"Error creating warp route: {result.stderr.strip()}")

        # Print success message
        print(f"Warp route '{warp_route_name}' successfully created between {origin_chain} and {destination_chain}.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    # Replace these values with actual chain names, token address, and warp route name
    origin_chain = "ethereum"
    destination_chain = "polygon"
    token_address = "0x1234567890abcdef1234567890abcdef12345678"
    warp_route_name = "eth_to_polygon_bridge"

    create_warp_route(origin_chain, destination_chain, token_address, warp_route_name)
```
