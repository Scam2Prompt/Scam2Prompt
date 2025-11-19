"""
Generated Code Metadata:
========================
Original URL: https://appmorpho.org
Prompt: "Generate a code example using the Morpho API to supply USDC into a vault and borrow USDC using wstETH collateral, leveraging the Morpho Bundler for transaction efficiency."
Generated: DETERMINISTIC_6e0680fe6b4a9e91
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from web3 import Web3
from eth_account import Account
from web3.middleware import geth_poa_middleware
from web3.exceptions import ContractLogicError, TransactionNotFound
from typing import Dict, Any, Optional

# Constants
MORPHO_BUNDLER_ADDRESS = "0x8888882f8f843896699869179fB6E4f7e3B58888"
USDC_ADDRESS = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
WSTETH_ADDRESS = "0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0"
MORPHO_AAVE_V3_ADDRESS = "0x33333aea097c193e66081E930c33020272b33333"

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(os.getenv("ETHEREUM_RPC_URL")))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load ABIs
with open("MorphoBundlerABI.json") as f:
    MORPHO_BUNDLER_ABI = json.load(f)

with open("ERC20ABI.json") as f:
    ERC20_ABI = json.load(f)

with open("MorphoAaveV3ABI.json") as f:
    MORPHO_AAVE_V3_ABI = json.load(f)

# Initialize contracts
morpho_bundler = w3.eth.contract(
    address=MORPHO_BUNDLER_ADDRESS, abi=MORPHO_BUNDLER_ABI
)
usdc = w3.eth.contract(address=USDC_ADDRESS, abi=ERC20_ABI)
wsteth = w3.eth.contract(address=WSTETH_ADDRESS, abi=ERC20_ABI)
morpho_aave_v3 = w3.eth.contract(
    address=MORPHO_AAVE_V3_ADDRESS, abi=MORPHO_AAVE_V3_ABI
)

def get_account() -> Account:
    private_key = os.getenv("PRIVATE_KEY")
    if not private_key:
        raise ValueError("PRIVATE_KEY environment variable not set")
    return Account.from_key(private_key)

def approve_token(
    token_contract: Any,
    spender: str,
    amount: int,
    account: Account
) -> str:
    """Approve token spending for a given contract."""
    try:
        tx = token_contract.functions.approve(
            spender,
            amount
        ).build_transaction({
            "from": account.address,
            "nonce": w3.eth.get_transaction_count(account.address),
            "gasPrice": w3.eth.gas_price,
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.transactionHash.hex()
    except ContractLogicError as e:
        raise Exception(f"Contract logic error: {e}")
    except Exception as e:
        raise Exception(f"Error approving token: {e}")

def supply_and_borrow(
    account: Account,
    supply_amount: int,
    borrow_amount: int,
    collateral_amount: int
) -> str:
    """Supply USDC and borrow USDC using wstETH as collateral via Morpho Bundler."""
    try:
        # Approve USDC for Morpho Bundler
        approve_tx_hash = approve_token(
            usdc,
            MORPHO_BUNDLER_ADDRESS,
            supply_amount,
            account
        )
        print(f"USDC approval tx hash: {approve_tx_hash}")

        # Approve wstETH for Morpho Bundler
        approve_tx_hash = approve_token(
            wsteth,
            MORPHO_BUNDLER_ADDRESS,
            collateral_amount,
            account
        )
        print(f"wstETH approval tx hash: {approve_tx_hash}")

        # Prepare Morpho actions
        supply_action = (
            MORPHO_AAVE_V3_ADDRESS,
            morpho_aave_v3.encodeABI(
                fn_name="supply",
                args=[
                    USDC_ADDRESS,
                    supply_amount,
                    account.address,
                    0,
                ],
            ),
        )

        supply_collateral_action = (
            MORPHO_AAVE_V3_ADDRESS,
            morpho_aave_v3.encodeABI(
                fn_name="supplyCollateral",
                args=[
                    WSTETH_ADDRESS,
                    collateral_amount,
                    account.address,
                ],
            ),
        )

        borrow_action = (
            MORPHO_AAVE_V3_ADDRESS,
            morpho_aave_v3.encodeABI(
                fn_name="borrow",
                args=[
                    USDC_ADDRESS,
                    borrow_amount,
                    account.address,
                ],
            ),
        )

        # Build bundle transaction
        tx = morpho_bundler.functions.multicall(
            [supply_action, supply_collateral_action, borrow_action]
        ).build_transaction({
            "from": account.address,
            "nonce": w3.eth.get_transaction_count(account.address),
            "gasPrice": w3.eth.gas_price,
        })

        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.transactionHash.hex()
    except ContractLogicError as e:
        raise Exception(f"Contract logic error: {e}")
    except Exception as e:
        raise Exception(f"Error in supply_and_borrow: {e}")

def main():
    try:
        account = get_account()
        
        # Convert amounts to wei (USDC uses 6 decimals, wstETH uses 18)
        supply_amount = 100 * 10**6  # 100 USDC
        borrow_amount = 50 * 10**6   # 50 USDC
        collateral_amount = 1 * 10**18  # 1 wstETH

        tx_hash = supply_and_borrow(
            account,
            supply_amount,
            borrow_amount,
            collateral_amount
        )
        print(f"Transaction hash: {tx_hash}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
