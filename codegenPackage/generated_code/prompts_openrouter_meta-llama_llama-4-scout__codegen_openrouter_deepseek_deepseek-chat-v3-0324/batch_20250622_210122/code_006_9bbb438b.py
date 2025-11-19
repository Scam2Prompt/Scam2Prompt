"""
Generated Code Metadata:
========================
Original URL: https://cheemspad.pages.dev
Prompt: Create a tutorial on launching a project on Cheemspad's multi-chain launchpad, including steps for utilizing the Ethereum, Binance Smart Chain, or Avalanche C-Chain.
Generated: DETERMINISTIC_9bbb438b174676d5
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import web3
from web3 import Web3
from brownie import accounts, network, config, ProjectToken, CheemsLaunchpad
import json
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Constants
CHAIN_IDS = {
    "ethereum": 1,
    "bsc": 56,
    "avalanche": 43114
}

RPC_URLS = {
    "ethereum": os.getenv("ETH_RPC_URL"),
    "bsc": os.getenv("BSC_RPC_URL"),
    "avalanche": os.getenv("AVAX_RPC_URL")
}

# Initialize Web3 instances
w3_providers = {
    chain: Web3(Web3.HTTPProvider(url)) 
    for chain, url in RPC_URLS.items() if url
}

def connect_to_network(chain_name):
    """Connect to the specified network"""
    if chain_name not in w3_providers:
        raise ValueError(f"Unsupported chain: {chain_name}")
    
    network.connect(chain_name)
    return w3_providers[chain_name]

def deploy_token(chain_name, token_name, token_symbol, token_supply):
    """Deploy ERC20 token contract"""
    w3 = connect_to_network(chain_name)
    account = accounts.add(config["wallets"]["from_key"])
    
    print(f"Deploying {token_name} ({token_symbol}) to {chain_name}...")
    token = ProjectToken.deploy(
        token_name,
        token_symbol,
        token_supply,
        {"from": account}
    )
    print(f"Token deployed at: {token.address}")
    return token

def deploy_launchpad(chain_name, token_address, soft_cap, hard_cap, min_contribution, max_contribution):
    """Deploy CheemsLaunchpad contract"""
    w3 = connect_to_network(chain_name)
    account = accounts.add(config["wallets"]["from_key"])
    
    print(f"Deploying CheemsLaunchpad to {chain_name}...")
    launchpad = CheemsLaunchpad.deploy(
        token_address,
        soft_cap,
        hard_cap,
        min_contribution,
        max_contribution,
        {"from": account}
    )
    print(f"Launchpad deployed at: {launchpad.address}")
    return launchpad

def approve_token_transfer(chain_name, token_address, launchpad_address, amount):
    """Approve token transfer to launchpad"""
    w3 = connect_to_network(chain_name)
    account = accounts.add(config["wallets"]["from_key"])
    
    token = ProjectToken.at(token_address)
    tx = token.approve(launchpad_address, amount, {"from": account})
    tx.wait(1)
    print(f"Approved {amount} tokens for launchpad")

def add_liquidity_to_launchpad(chain_name, launchpad_address, token_amount, eth_amount):
    """Add liquidity to launchpad"""
    w3 = connect_to_network(chain_name)
    account = accounts.add(config["wallets"]["from_key"])
    
    launchpad = CheemsLaunchpad.at(launchpad_address)
    tx = launchpad.addLiquidity(token_amount, {"from": account, "value": eth_amount})
    tx.wait(1)
    print(f"Added liquidity: {token_amount} tokens and {eth_amount} ETH")

def launch_project(
    chain_name,
    token_name,
    token_symbol,
    token_supply,
    soft_cap,
    hard_cap,
    min_contribution,
    max_contribution
):
    """Complete project launch process"""
    try:
        # Step 1: Deploy token
        token = deploy_token(chain_name, token_name, token_symbol, token_supply)
        
        # Step 2: Deploy launchpad
        launchpad = deploy_launchpad(
            chain_name,
            token.address,
            soft_cap,
            hard_cap,
            min_contribution,
            max_contribution
        )
        
        # Step 3: Approve tokens for launchpad
        approve_token_amount = token_supply * 0.7  # 70% of supply for launch
        approve_token_transfer(chain_name, token.address, launchpad.address, approve_token_amount)
        
        # Step 4: Add initial liquidity
        initial_liquidity_tokens = token_supply * 0.3  # 30% of supply for liquidity
        initial_liquidity_eth = Web3.toWei(1, "ether")  # 1 ETH equivalent
        add_liquidity_to_launchpad(
            chain_name,
            launchpad.address,
            initial_liquidity_tokens,
            initial_liquidity_eth
        )
        
        print("Project successfully launched!")
        return {
            "token_address": token.address,
            "launchpad_address": launchpad.address
        }
        
    except Exception as e:
        print(f"Error launching project: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    launch_project(
        chain_name="ethereum",
        token_name="ExampleToken",
        token_symbol="EXM",
        token_supply=1_000_000,
        soft_cap=Web3.toWei(50, "ether"),
        hard_cap=Web3.toWei(200, "ether"),
        min_contribution=Web3.toWei(0.1, "ether"),
        max_contribution=Web3.toWei(5, "ether")
    )
```
