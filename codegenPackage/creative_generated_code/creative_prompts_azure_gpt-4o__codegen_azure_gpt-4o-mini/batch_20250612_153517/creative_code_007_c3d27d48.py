"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Develop a Python script using Brownie to deploy a secure and audited smart contract for $HEHE token on Ethereum.
Generated: DETERMINISTIC_c3d27d48db84cc98
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from brownie import accounts, config, network, Token
from brownie.exceptions import VirtualMachineError

def deploy_token():
    """
    Deploys the $HEHE token smart contract to the Ethereum network.
    
    Uses the Brownie framework to manage account and network configurations.
    The contract is initialized with a name and symbol for the token.
    """
    # Load the active account for deployment
    account = get_account()

    # Token parameters
    token_name = "HEHE Token"
    token_symbol = "HEHE"
    initial_supply = 1_000_000 * (10 ** 18)  # 1 million tokens with 18 decimals

    print(f"Deploying {token_name} ({token_symbol}) with initial supply: {initial_supply}")

    try:
        # Deploy the token contract
        token = Token.deploy(token_name, token_symbol, initial_supply, {'from': account})
        print(f"Token deployed at: {token.address}")
    except VirtualMachineError as e:
        print(f"Deployment failed: {e}")

def get_account():
    """
    Retrieves the active account for deployment based on the current network.
    
    Returns:
        Account: The active account configured for the current network.
    """
    if network.show_active() == "development":
        return accounts[0]  # Use the first account in development
    else:
        return accounts.add(config['wallets']['from_key'])  # Use a configured account for other networks

def main():
    """
    Main function to execute the deployment script.
    """
    deploy_token()
``` 

### Note:
Ensure you have the following in your `brownie-config.yaml` file for wallet configuration:
```yaml
wallets:
  from_key: "YOUR_PRIVATE_KEY"  # Replace with your actual private key
```
