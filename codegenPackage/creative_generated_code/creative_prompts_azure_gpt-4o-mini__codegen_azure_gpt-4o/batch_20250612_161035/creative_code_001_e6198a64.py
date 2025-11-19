"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicc34wxgmwfldpiehsmb6azuurx52lonvbu63phtv6fto7rbacmja.ipfs.dweb.link
Prompt: Write a script using Hyperlane's CLI commands to create a Warp Route for token bridging.
Generated: DETERMINISTIC_e6198a644df393b9
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys

def run_command(command):
    """
    Runs a shell command and returns the output and error, if any.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return None, f"Command failed with error: {e.stderr.strip()}"

def create_warp_route(route_name, token_address, source_chain, destination_chain):
    """
    Creates a Warp Route for token bridging using Hyperlane's CLI.
    
    Parameters:
        route_name (str): Name of the warp route.
        token_address (str): Address of the token to be bridged.
        source_chain (str): Name of the source chain.
        destination_chain (str): Name of the destination chain.
    """
    # Construct the Hyperlane CLI command
    command = (
        f"hyperlane warp-route create "
        f"--name {route_name} "
        f"--token {token_address} "
        f"--source {source_chain} "
        f"--destination {destination_chain}"
    )

    # Execute the command
    print(f"Executing command: {command}")
    output, error = run_command(command)

    if error:
        print(f"Error creating warp route: {error}")
        sys.exit(1)
    else:
        print(f"Warp route created successfully: {output}")

def main():
    """
    Main function to create a Warp Route.
    Modify the parameters below as needed for your use case.
    """
    # Input parameters (modify these for your needs)
    route_name = "my-warp-route"
    token_address = "0xYourTokenAddressHere"
    source_chain = "ethereum"
    destination_chain = "polygon"

    print("Starting Warp Route creation...")
    create_warp_route(route_name, token_address, source_chain, destination_chain)
    print("Warp Route creation script completed.")

if __name__ == "__main__":
    main()
```
