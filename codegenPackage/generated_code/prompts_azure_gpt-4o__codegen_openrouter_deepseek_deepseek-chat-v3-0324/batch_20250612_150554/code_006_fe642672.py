"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Create a tutorial-style Python script for deploying a decentralized application (dApp) that addresses global systemic challenges, as discussed in the ETHBerlin04 manifesto.
Generated: DETERMINISTIC_fe6426729d2759e3
Batch ID: 20250612_150554
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
Decentralized Application (dApp) Deployment Script

This script provides a tutorial-style guide for deploying a dApp that addresses
global systemic challenges as outlined in the ETHBerlin04 manifesto.

Features:
- Smart contract compilation and deployment
- Frontend integration
- Testing framework
- Deployment to Ethereum testnet/mainnet
"""

import os
import json
import subprocess
from pathlib import Path
from web3 import Web3
from dotenv import load_dotenv
from solcx import compile_standard, install_solc

# Load environment variables
load_dotenv()

# Configuration
class Config:
    """Configuration class for dApp deployment"""
    SOLIDITY_VERSION = "0.8.0"
    CONTRACT_NAME = "SystemicChallengeDApp"
    CONTRACT_FILE = "contracts/SystemicChallenge.sol"
    BUILD_DIR = Path("./build")
    FRONTEND_DIR = Path("./frontend/src/contracts")
    TESTNET = "goerli"
    MAINNET = "mainnet"
    GAS_LIMIT = 3000000

def setup_environment():
    """Set up development environment"""
    print("Setting up environment...")
    
    # Create necessary directories
    Config.BUILD_DIR.mkdir(exist_ok=True)
    Config.FRONTEND_DIR.mkdir(exist_ok=True)
    
    # Install required Solidity compiler version
    install_solc(Config.SOLIDITY_VERSION)

def compile_contract():
    """Compile the Solidity smart contract"""
    print(f"Compiling {Config.CONTRACT_FILE}...")
    
    with open(Config.CONTRACT_FILE, "r") as file:
        contract_source = file.read()
    
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {Config.CONTRACT_FILE: {"content": contract_source}},
            "settings": {
                "outputSelection": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version=Config.SOLIDITY_VERSION,
    )
    
    # Save compiled contract
    output_file = Config.BUILD_DIR / "compiled_contract.json"
    with open(output_file, "w") as file:
        json.dump(compiled_sol, file)
    
    return compiled_sol

def deploy_contract(network=Config.TESTNET):
    """Deploy the compiled contract to specified network"""
    print(f"Deploying to {network}...")
    
    # Load compiled contract
    with open(Config.BUILD_DIR / "compiled_contract.json", "r") as file:
        compiled_sol = json.load(file)
    
    # Get contract ABI and bytecode
    contract_abi = compiled_sol["contracts"][Config.CONTRACT_FILE][Config.CONTRACT_NAME]["abi"]
    contract_bytecode = compiled_sol["contracts"][Config.CONTRACT_FILE][Config.CONTRACT_NAME]["evm"]["bytecode"]["object"]
    
    # Connect to blockchain
    w3 = connect_to_blockchain(network)
    
    # Get deployer account
    account = get_deployer_account(w3, network)
    
    # Create contract instance
    contract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    
    # Build transaction
    transaction = contract.constructor().build_transaction({
        "chainId": w3.eth.chain_id,
        "gas": Config.GAS_LIMIT,
        "gasPrice": w3.eth.gas_price,
        "nonce": w3.eth.get_transaction_count(account.address),
    })
    
    # Sign and send transaction
    signed_txn = account.sign_transaction(transaction)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    print(f"Contract deployed at: {tx_receipt.contractAddress}")
    
    # Save deployment info
    save_deployment_info(network, tx_receipt.contractAddress, contract_abi)
    
    return tx_receipt.contractAddress, contract_abi

def connect_to_blockchain(network):
    """Connect to Ethereum network"""
    if network == Config.TESTNET:
        provider_url = os.getenv(f"{Config.TESTNET.upper()}_RPC_URL")
    elif network == Config.MAINNET:
        provider_url = os.getenv(f"{Config.MAINNET.upper()}_RPC_URL")
    else:
        raise ValueError(f"Unsupported network: {network}")
    
    if not provider_url:
        raise EnvironmentError(f"Missing {network.upper()}_RPC_URL in environment variables")
    
    return Web3(Web3.HTTPProvider(provider_url))

def get_deployer_account(w3, network):
    """Get deployer account from private key"""
    private_key = os.getenv(f"{network.upper()}_PRIVATE_KEY")
    if not private_key:
        raise EnvironmentError(f"Missing {network.upper()}_PRIVATE_KEY in environment variables")
    
    return w3.eth.account.from_key(private_key)

def save_deployment_info(network, contract_address, abi):
    """Save deployment information for frontend integration"""
    deployment_info = {
        "network": network,
        "address": contract_address,
        "abi": abi
    }
    
    # Save to build directory
    with open(Config.BUILD_DIR / f"deployment_{network}.json", "w") as file:
        json.dump(deployment_info, file)
    
    # Save to frontend directory
    with open(Config.FRONTEND_DIR / f"deployment_{network}.json", "w") as file:
        json.dump(deployment_info, file)

def run_tests():
    """Run contract tests"""
    print("Running tests...")
    try:
        subprocess.run(["python", "-m", "pytest", "tests/"], check=True)
        print("All tests passed!")
    except subprocess.CalledProcessError:
        print("Some tests failed. Please fix before deployment.")
        raise

def deploy_frontend():
    """Deploy frontend application"""
    print("Deploying frontend...")
    try:
        # Install dependencies
        subprocess.run(["npm", "install"], cwd="frontend", check=True)
        
        # Build frontend
        subprocess.run(["npm", "run", "build"], cwd="frontend", check=True)
        
        # Deploy to IPFS (example using Fleek)
        print("Frontend built successfully. Ready for deployment to IPFS.")
    except subprocess.CalledProcessError as e:
        print(f"Frontend deployment failed: {e}")
        raise

def main():
    """Main deployment workflow"""
    try:
        # Setup environment
        setup_environment()
        
        # Compile contract
        compile_contract()
        
        # Run tests
        run_tests()
        
        # Deploy to testnet
        contract_address, abi = deploy_contract(Config.TESTNET)
        print(f"Testnet deployment successful. Contract address: {contract_address}")
        
        # Optional: Deploy to mainnet
        if input("Deploy to mainnet? (y/n): ").lower() == "y":
            contract_address, abi = deploy_contract(Config.MAINNET)
            print(f"Mainnet deployment successful. Contract address: {contract_address}")
        
        # Deploy frontend
        deploy_frontend()
        
        print("dApp deployment completed successfully!")
    except Exception as e:
        print(f"Deployment failed: {e}")
        raise

if __name__ == "__main__":
    main()
```
