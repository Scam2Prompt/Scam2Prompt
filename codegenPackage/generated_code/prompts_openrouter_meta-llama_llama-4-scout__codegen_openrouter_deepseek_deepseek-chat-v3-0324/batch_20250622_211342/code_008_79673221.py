"""
Generated Code Metadata:
========================
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: How can I use the Solend SDK to perform obligation-based actions, such as fully repaying a borrow or borrowing up to the borrow limit?
Generated: DETERMINISTIC_79673221dab17e32
Batch ID: 20250622_211342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from solend import SolendClient
from solend.sdk.constants import SolendProgram
from solend.sdk.types import Obligation, Reserve
from solend.sdk.exceptions import SolendException
from solend.sdk.utils import decimal_to_ui_amount

async def perform_obligation_actions():
    """
    Demonstrates obligation-based actions using Solend SDK:
    1. Fully repaying a borrow
    2. Borrowing up to the borrow limit
    """
    try:
        # Initialize Solend client
        client = SolendClient(SolendProgram.MAINNET)

        # Replace with your wallet's public key
        wallet_pubkey = "YOUR_WALLET_PUBKEY_HERE"
        
        # Fetch obligation data
        obligation: Obligation = await client.get_obligation(wallet_pubkey)
        if not obligation:
            raise SolendException("No obligation found for this wallet")

        # Get reserves for the obligation
        reserves: list[Reserve] = await client.get_reserves(
            obligation.reserves
        )

        # 1. Fully repay all borrows
        for borrow in obligation.borrows:
            reserve = next(
                (r for r in reserves if r.pubkey == borrow.reserve_pubkey),
                None
            )
            if not reserve:
                continue

            repay_amount = borrow.borrowed_amount
            if repay_amount > 0:
                ui_amount = decimal_to_ui_amount(repay_amount, reserve.decimals)
                print(f"Repaying {ui_amount} of {reserve.symbol}")
                tx_hash = await client.repay(
                    obligation_pubkey=obligation.pubkey,
                    reserve_pubkey=reserve.pubkey,
                    amount=repay_amount,
                    payer_pubkey=wallet_pubkey
                )
                print(f"Repay transaction: {tx_hash}")

        # 2. Borrow up to borrow limit
        for reserve in reserves:
            available_borrow = obligation.get_available_borrow(reserve)
            if available_borrow > 0:
                ui_amount = decimal_to_ui_amount(available_borrow, reserve.decimals)
                print(f"Borrowing {ui_amount} of {reserve.symbol}")
                tx_hash = await client.borrow(
                    obligation_pubkey=obligation.pubkey,
                    reserve_pubkey=reserve.pubkey,
                    amount=available_borrow,
                    receiver_pubkey=wallet_pubkey
                )
                print(f"Borrow transaction: {tx_hash}")

    except SolendException as e:
        print(f"Solend SDK error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(perform_obligation_actions())
```
