"""
Generated Code Metadata:
========================
Original URL: https://wwwmorpho.org
Prompt: Write a script using the Morpho Bundler to bundle multiple actions into one transaction, such as using `wstETH` as collateral to borrow `USDC` and then supplying `USDC` into a vault.
Generated: DETERMINISTIC_190e0f433786a5f2
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from morpho_utils import MorphoBundler
from web3 import Web3
from eth_abi import encode
from typing import List, Dict, Any
import os

# Initialize Web3 provider
WEB3_PROVIDER_URL = os.getenv("WEB3_PROVIDER_URL")
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

# Contract addresses (example addresses - replace with actual ones)
WSTETH_ADDRESS = "0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0"
USDC_ADDRESS = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
MORPHO_AAVE_V2_ADDRESS = "0x777777c9898D384F785Ee44Acfe945efDFf5f3E0"
VAULT_ADDRESS = "0xBA12222222228d8Ba445958a75a0704d566BF2C8"

# Initialize Morpho Bundler
bundler = MorphoBundler(w3)

def bundle_wsteth_to_usdc_vault(
    user_address: str,
    wsteth_amount: int,
    borrow_amount: int,
    supply_amount: int,
    private_key: str
) -> Dict[str, Any]:
    """
    Bundle transaction to:
    1. Use wstETH as collateral
    2. Borrow USDC
    3. Supply USDC to vault
    
    Args:
        user_address: User's Ethereum address
        wsteth_amount: Amount of wstETH to supply as collateral (in wei)
        borrow_amount: Amount of USDC to borrow (in wei)
        supply_amount: Amount of USDC to supply to vault (in wei)
        private_key: User's private key for signing
        
    Returns:
        Transaction receipt
    """
    
    # 1. Supply wstETH as collateral
    supply_collateral_action = bundler.create_supply_collateral_action(
        market_address=MORPHO_AAVE_V2_ADDRESS,
        collateral_address=WSTETH_ADDRESS,
        amount=wsteth_amount,
        on_behalf=user_address
    )
    
    # 2. Borrow USDC
    borrow_action = bundler.create_borrow_action(
        market_address=MORPHO_AAVE_V2_ADDRESS,
        token_address=USDC_ADDRESS,
        amount=borrow_amount,
        on_behalf=user_address
    )
    
    # 3. Approve USDC for vault
    approve_action = bundler.create_approve_action(
        token_address=USDC_ADDRESS,
        spender=VAULT_ADDRESS,
        amount=supply_amount
    )
    
    # 4. Supply USDC to vault
    supply_to_vault_action = bundler.create_erc20_transfer_action(
        token_address=USDC_ADDRESS,
        recipient=VAULT_ADDRESS,
        amount=supply_amount
    )
    
    # Bundle all actions
    bundle = bundler.create_bundle(
        actions=[
            supply_collateral_action,
            borrow_action,
            approve_action,
            supply_to_vault_action
        ]
    )
    
    # Estimate gas
    gas_estimate = bundler.estimate_gas(bundle, user_address)
    
    # Build and sign transaction
    tx = bundler.build_transaction(
        bundle=bundle,
        gas_limit=int(gas_estimate * 1.2),  # 20% buffer
        nonce=w3.eth.get_transaction_count(user_address)
    )
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    
    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    # Wait for transaction receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    return receipt

# Example usage
if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv()
    
    USER_ADDRESS = os.getenv("USER_ADDRESS")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")
    
    # Convert amounts to wei
    WSTETH_AMOUNT = w3.to_wei(1, "ether")  # 1 wstETH
    BORROW_AMOUNT = 1000 * 10**6  # 1000 USDC (6 decimals)
    SUPPLY_AMOUNT = 1000 * 10**6  # 1000 USDC (6 decimals)
    
    try:
        receipt = bundle_wsteth_to_usdc_vault(
            user_address=USER_ADDRESS,
            wsteth_amount=WSTETH_AMOUNT,
            borrow_amount=BORROW_AMOUNT,
            supply_amount=SUPPLY_AMOUNT,
            private_key=PRIVATE_KEY
        )
        print(f"Transaction successful! Hash: {receipt.transactionHash.hex()}")
    except Exception as e:
        print(f"Transaction failed: {str(e)}")
```
