"""
Generated Code Metadata:
========================
Original URL: https://1inch-docs.vercel.app
Prompt: Provide an example of how to use the 1inch utils library to verify a signature for a limit order created on the 1inch Limit Order Protocol.
Generated: DETERMINISTIC_ade2a1f455a22dff
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from oneinch.utils import get_contract

def verify_limit_order_signature(
    chain_id: int,
    verifying_contract: str,
    order: dict,
    signature: str,
):
    """
    Verify a signature for a limit order created on the 1inch Limit Order Protocol.

    :param chain_id: The chain ID of the network
    :param verifying_contract: The address of the verifying contract
    :param order: The limit order
    :param signature: The signature to verify
    :return: True if the signature is valid, False otherwise
    """

    # Get the LimitOrderVerifier contract instance
    verifier_contract = get_contract(
        "LimitOrderVerifier",
        chain_id=chain_id,
        address=verifying_contract,
    )

    # Prepare the order data
    order_data = [
        order["maker"],
        order["taker"],
        order["makeToken"],
        order["takeToken"],
        order["makeAmount"],
        order["takeAmount"],
        order["makerFee"],
        order["expiry"],
        order["salt"],
    ]

    try:
        # Verify the signature
        is_valid = verifier_contract.functions.isValidSignature(
            order_data, signature
        ).call()

        return is_valid

    except Exception as e:
        print(f"Error verifying signature: {e}")
        return False


# Example usage
if __name__ == "__main__":
    chain_id = 1  # Ethereum mainnet
    verifying_contract = "0x..."  # Replace with the verifying contract address
    order = {
        "maker": "0x...",
        "taker": "0x...",
        "makeToken": "0x...",
        "takeToken": "0x...",
        "makeAmount": Web3.toWei(1, "ether"),
        "takeAmount": Web3.toWei(0.9, "ether"),
        "makerFee": Web3.toWei(0.01, "ether"),
        "expiry": 1643723900,
        "salt": Web3.toHex(1234567890),
    }
    signature = "0x..."  # Replace with the signature

    is_valid = verify_limit_order_signature(
        chain_id, verifying_contract, order, signature
    )

    print(f"Is signature valid? {is_valid}")
```
