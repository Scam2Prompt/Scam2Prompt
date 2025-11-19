"""
Generated Code Metadata:
========================
Original URL: https://kayentest2.pages.dev
Prompt: Create a tutorial for deploying a SportFi ecosystem on the Chiliz blockchain, incorporating KAYEN Protocol's decentralized exchange and community-driven features.
Generated: DETERMINISTIC_44325e13fd55f7f7
Batch ID: 20250612_152906
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.chiliz.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# SportFi Deployment Tutorial for Chiliz Blockchain with KAYEN Protocol

# Required imports
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import os
from dotenv import load_dotenv
from brownie import accounts, network, config, SportFiToken, KayenExchange, CommunityGovernance
import time

# Load environment variables
load_dotenv()

# Configuration
CHILIZ_RPC_URL = "https://rpc.chiliz.com"
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CHAIN_ID = 88888  # Chiliz Chain ID

# Connect to Chiliz blockchain
def connect_to_chiliz():
    """
    Establishes connection to Chiliz blockchain
    Returns Web3 instance
    """
    try:
        w3 = Web3(Web3.HTTPProvider(CHILIZ_RPC_URL))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        if not w3.is_connected():
            raise ConnectionError("Failed to connect to Chiliz blockchain")
        return w3
    except Exception as e:
        print(f"Error connecting to Chiliz: {e}")
        raise

# Deploy SportFi Token
def deploy_sportfi_token(w3):
    """
    Deploys SportFi ERC-20 token contract
    Returns contract instance
    """
    try:
        account = w3.eth.account.from_key(PRIVATE_KEY)
        contract = w3.eth.contract(
            abi=SportFiToken.abi,
            bytecode=SportFiToken.bytecode
        )
        
        tx = contract.constructor().build_transaction({
            "chainId": CHAIN_ID,
            "from": account.address,
            "nonce": w3.eth.get_transaction_count(account.address),
            "gasPrice": w3.eth.gas_price
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        return w3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=SportFiToken.abi
        )
    except Exception as e:
        print(f"Error deploying SportFi token: {e}")
        raise

# Deploy KAYEN Exchange
def deploy_kayen_exchange(w3, sportfi_token_address):
    """
    Deploys KAYEN decentralized exchange
    Returns contract instance
    """
    try:
        account = w3.eth.account.from_key(PRIVATE_KEY)
        contract = w3.eth.contract(
            abi=KayenExchange.abi,
            bytecode=KayenExchange.bytecode
        )
        
        tx = contract.constructor(sportfi_token_address).build_transaction({
            "chainId": CHAIN_ID,
            "from": account.address,
            "nonce": w3.eth.get_transaction_count(account.address),
            "gasPrice": w3.eth.gas_price
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        return w3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=KayenExchange.abi
        )
    except Exception as e:
        print(f"Error deploying KAYEN exchange: {e}")
        raise

# Deploy Community Governance
def deploy_community_governance(w3, sportfi_token_address):
    """
    Deploys community governance contract
    Returns contract instance
    """
    try:
        account = w3.eth.account.from_key(PRIVATE_KEY)
        contract = w3.eth.contract(
            abi=CommunityGovernance.abi,
            bytecode=CommunityGovernance.bytecode
        )
        
        tx = contract.constructor(sportfi_token_address).build_transaction({
            "chainId": CHAIN_ID,
            "from": account.address,
            "nonce": w3.eth.get_transaction_count(account.address),
            "gasPrice": w3.eth.gas_price
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        return w3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=CommunityGovernance.abi
        )
    except Exception as e:
        print(f"Error deploying community governance: {e}")
        raise

# Initialize Liquidity Pool
def initialize_liquidity_pool(w3, exchange, token, amount):
    """
    Initializes liquidity pool with initial tokens
    """
    try:
        account = w3.eth.account.from_key(PRIVATE_KEY)
        
        # Approve token transfer
        approve_tx = token.functions.approve(
            exchange.address,
            amount
        ).build_transaction({
            "chainId": CHAIN_ID,
            "from": account.address,
            "nonce": w3.eth.get_transaction_count(account.address),
            "gasPrice": w3.eth.gas_price
        })
        
        signed_approve = account.sign_transaction(approve_tx)
        approve_hash = w3.eth.send_raw_transaction(signed_approve.rawTransaction)
        w3.eth.wait_for_transaction_receipt(approve_hash)
        
        # Add liquidity
        add_liq_tx = exchange.functions.addLiquidity(
            amount,
            {"value": w3.to_wei(1, "ether")}
        ).build_transaction({
            "chainId": CHAIN_ID,
            "from": account.address,
            "nonce": w3.eth.get_transaction_count(account.address) + 1,
            "gasPrice": w3.eth.gas_price
        })
        
        signed_liq = account.sign_transaction(add_liq_tx)
        liq_hash = w3.eth.send_raw_transaction(signed_liq.rawTransaction)
        w3.eth.wait_for_transaction_receipt(liq_hash)
        
    except Exception as e:
        print(f"Error initializing liquidity pool: {e}")
        raise

# Main deployment function
def deploy_sportfi_ecosystem():
    """
    Main function to deploy the entire SportFi ecosystem
    """
    try:
        print("Connecting to Chiliz blockchain...")
        w3 = connect_to_chiliz()
        
        print("Deploying SportFi Token...")
        sportfi_token = deploy_sportfi_token(w3)
        print(f"SportFi Token deployed at: {sportfi_token.address}")
        
        print("Deploying KAYEN Exchange...")
        kayen_exchange = deploy_kayen_exchange(w3, sportfi_token.address)
        print(f"KAYEN Exchange deployed at: {kayen_exchange.address}")
        
        print("Deploying Community Governance...")
        community_gov = deploy_community_governance(w3, sportfi_token.address)
        print(f"Community Governance deployed at: {community_gov.address}")
        
        print("Initializing liquidity pool...")
        initialize_liquidity_pool(
            w3,
            kayen_exchange,
            sportfi_token,
            w3.to_wei(1000000, "ether")  # 1M tokens initial liquidity
        )
        print("Liquidity pool initialized successfully!")
        
        print("\nSportFi Ecosystem Deployment Complete!")
        print("======================================")
        print(f"SportFi Token: {sportfi_token.address}")
        print(f"KAYEN Exchange: {kayen_exchange.address}")
        print(f"Community Governance: {community_gov.address}")
        
        return {
            "sportfi_token": sportfi_token.address,
            "kayen_exchange": kayen_exchange.address,
            "community_governance": community_gov.address
        }
    except Exception as e:
        print(f"Deployment failed: {e}")
        raise

if __name__ == "__main__":
    deploy_sportfi_ecosystem()
```
