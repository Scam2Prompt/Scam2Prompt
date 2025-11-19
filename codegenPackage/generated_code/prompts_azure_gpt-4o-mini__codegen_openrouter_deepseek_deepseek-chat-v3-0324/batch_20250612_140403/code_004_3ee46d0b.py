"""
Generated Code Metadata:
========================
Original URL: https://njax.pages.dev
Prompt: How can I create a function to handle slippage errors during token swaps on a decentralized exchange?
Generated: DETERMINISTIC_3ee46d0b4e4226c8
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Tuple, Optional
from web3 import Web3
from web3.contract import Contract
from eth_abi import encode_abi
import math

def calculate_min_amount_out(
    amount_in: int,
    slippage_percentage: float,
    decimals: int
) -> int:
    """
    Calculate the minimum amount out considering slippage.
    
    Args:
        amount_in: The input token amount.
        slippage_percentage: The acceptable slippage percentage (e.g., 0.5 for 0.5%).
        decimals: The token decimals for proper scaling.
    
    Returns:
        The minimum acceptable amount out after slippage.
    """
    if slippage_percentage < 0 or slippage_percentage > 100:
        raise ValueError("Slippage percentage must be between 0 and 100")
    
    slippage_factor = 1 - (slippage_percentage / 100)
    min_amount_out = amount_in * slippage_factor
    return int(min_amount_out * (10 ** decimals))

def execute_swap_with_slippage(
    web3: Web3,
    router_contract: Contract,
    token_in: str,
    token_out: str,
    amount_in: int,
    slippage_percentage: float,
    sender_address: str,
    gas_limit: int = 200000,
    deadline: Optional[int] = None
) -> Tuple[bool, str]:
    """
    Execute a token swap with slippage protection.
    
    Args:
        web3: Web3 instance.
        router_contract: Initialized router contract instance.
        token_in: Address of input token.
        token_out: Address of output token.
        amount_in: Amount of input token to swap.
        slippage_percentage: Acceptable slippage percentage.
        sender_address: Address executing the swap.
        gas_limit: Gas limit for the transaction.
        deadline: Optional deadline timestamp for the swap.
    
    Returns:
        Tuple of (success, transaction_hash).
    """
    try:
        # Get token decimals
        token_in_contract = web3.eth.contract(
            address=token_in,
            abi=[{"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"}]
        )
        decimals = token_in_contract.functions.decimals().call()
        
        # Calculate min amount out
        min_amount_out = calculate_min_amount_out(
            amount_in,
            slippage_percentage,
            decimals
        )
        
        # Set deadline if not provided (20 minutes from now)
        if deadline is None:
            deadline = int(web3.eth.get_block('latest').timestamp) + 1200
        
        # Build transaction
        swap_tx = router_contract.functions.swapExactTokensForTokens(
            amount_in,
            min_amount_out,
            [token_in, token_out],
            sender_address,
            deadline
        ).build_transaction({
            'from': sender_address,
            'gas': gas_limit,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(sender_address),
        })
        
        # Sign and send transaction
        signed_tx = web3.eth.account.sign_transaction(swap_tx, private_key=None)  # Private key should be handled securely
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Wait for transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.status == 1, tx_hash.hex()
    
    except ValueError as ve:
        raise ValueError(f"Value error during swap: {ve}")
    except Exception as e:
        raise Exception(f"Error executing swap: {e}")
```
