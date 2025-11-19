"""
Generated Code Metadata:
========================
Original URL: https://starkware.eu
Prompt: Generate code for deploying a StarkNet smart contract using the StarkWare CLI tools, including steps for compiling and deploying the contract.
Generated: DETERMINISTIC_f4b7c487b3d8c76c
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
import os
import subprocess
import json
from pathlib import Path

# Configuration
CONTRACT_SOURCE = "contract.cairo"
CONTRACT_NAME = "MyContract"
NETWORK = "alpha-goerli"
ACCOUNT_DIR = "~/.starknet_accounts"
ACCOUNT_NAME = "my_account"
WAIT_FOR_ACCEPTANCE = True

def check_starknet_cli_installed():
    """Check if StarkNet CLI is installed."""
    try:
        subprocess.run(["starknet", "--version"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        raise Exception("StarkNet CLI not found. Please install it first.")

def compile_contract():
    """Compile the Cairo contract."""
    print(f"Compiling {CONTRACT_SOURCE}...")
    try:
        result = subprocess.run(
            ["starknet-compile", CONTRACT_SOURCE, "--output", f"{CONTRACT_NAME}.json"],
            check=True,
            capture_output=True,
            text=True
        )
        print("Compilation successful")
        return f"{CONTRACT_NAME}.json"
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed: {e.stderr}")
        raise

def deploy_contract(compiled_contract):
    """Deploy the compiled contract to StarkNet."""
    print(f"Deploying {CONTRACT_NAME} to {NETWORK}...")
    
    command = [
        "starknet",
        "deploy",
        "--contract", compiled_contract,
        "--network", NETWORK,
        "--account_dir", ACCOUNT_DIR,
        "--account", ACCOUNT_NAME
    ]
    
    if WAIT_FOR_ACCEPTANCE:
        command.append("--wait_for_acceptance")
    
    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
        output = result.stdout.strip()
        print(f"Deployment successful. Transaction: {output}")
        return output
    except subprocess.CalledProcessError as e:
        print(f"Deployment failed: {e.stderr}")
        raise

def main():
    try:
        # Check prerequisites
        check_starknet_cli_installed()
        
        # Compile the contract
        compiled_contract = compile_contract()
        
        # Deploy the contract
        deploy_contract(compiled_contract)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
```
