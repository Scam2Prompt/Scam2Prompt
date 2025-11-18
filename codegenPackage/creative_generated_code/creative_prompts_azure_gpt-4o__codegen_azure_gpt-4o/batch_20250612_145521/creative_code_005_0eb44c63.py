"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-france.fr
Prompt: Create a tutorial for setting up a Polkadot node and querying data about DOT token circulation using the information provided on Polkadot France.
Generated: DETERMINISTIC_0eb44c6331eb2f76
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Polkadot Node Setup and Query Script
# This script provides a way to set up a local Polkadot node and query token circulation data
# using the official Polkadot API (connected to a local or remote node).
#
# Requirements:
# - Python 3.8+
# - `substrate-interface` library for interacting with the Polkadot/Substrate API
# - A running Polkadot node (local or remote)

import subprocess
import os
import sys
from substrateinterface import SubstrateInterface, SubstrateRequestException

# Function to start a local Polkadot node
def start_polkadot_node():
    """
    Starts a Polkadot node locally. This requires the Polkadot binary to be installed and added to PATH.
    """
    try:
        # Check if Polkadot binary is available
        if not shutil.which("polkadot"):
            raise FileNotFoundError("Polkadot binary not found. Please install it and add to PATH.")

        print("Starting Polkadot node...")

        # Start Polkadot node in development mode
        subprocess.Popen(
            ["polkadot", "--chain=kusama", "--dev"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print("Polkadot node started successfully. Waiting for the node to initialize...")
        print("You can connect to it locally via ws://127").
  
 ```
