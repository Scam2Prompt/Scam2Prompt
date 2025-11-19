"""
Generated Code Metadata:
========================
Original URL: https://hyperlane-c77043.webflow.io
Prompt: Write code to deploy Hyperlane on a blockchain to enable sending and receiving messages across chains using the Hyperlane framework. Include steps for setting up Warp Routes for token bridging.
Generated: DETERMINISTIC_934680fd177f565f
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from web3 import Web3
from hyperlane import HyperlaneDeployer, WarpRouteDeployer
from hyperlane.constants import Chain
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration class
class HyperlaneConfig:
    def __init__(self):
        self.rpc_urls = {
            Chain.ETHEREUM: os.getenv('ETHEREUM_RPC_URL'),
            Chain.POLYGON: os.getenv('POLYGON_RPC_URL'),
            Chain.ARBITRUM: os.getenv('ARBITRUM_RPC_URL'),
            Chain.OPTIMISM: os.getenv('OPTIMISM_RPC_URL'),
        }
        self.private_key = os.getenv('PRIVATE_KEY')
        self.token_address = os.getenv('TOKEN_ADDRESS')  # ERC20 token to bridge
        self.chain_ids = {
            Chain.ETHEREUM: 1,
            Chain.POLYGON: 137,
            Chain.ARBITRUM: 42161,
            Chain.OPTIMISM: 10,
        }

# Initialize Hyperlane deployment
def deploy_hyperlane(config):
    try:
        # Initialize Web3 providers for each chain
        providers = {
            chain: Web3(Web3.HTTPProvider(url))
            for chain, url in config.rpc_urls.items()
        }

        # Deploy Hyperlane core contracts
        deployer = HyperlaneDeployer(
            providers=providers,
            chain_ids=config.chain_ids,
            private_key=config.private_key
        )

        print("Deploying Hyperlane core contracts...")
        core_contracts = deployer.deploy_core()
        print("Core contracts deployed:", core_contracts)

        # Deploy Warp Routes for token bridging
        warp_deployer = WarpRouteDeployer(
            providers=providers,
            chain_ids=config.chain_ids,
            private_key=config.private_key,
            token_address=config.token_address
        )

        print("Deploying Warp Routes...")
        warp_routes = warp_deployer.deploy_routes()
        print("Warp Routes deployed:", warp_routes)

        return {
            'core_contracts': core_contracts,
            'warp_routes': warp_routes
        }

    except Exception as e:
        print(f"Error deploying Hyperlane: {e}")
        raise

# Main execution
if __name__ == "__main__":
    config = HyperlaneConfig()
    deployment = deploy_hyperlane(config)
    
    # Save deployment details to file
    with open('hyperlane_deployment.json', 'w') as f:
        json.dump(deployment, f, indent=2)
    
    print("Hyperlane deployment completed successfully!")
```
