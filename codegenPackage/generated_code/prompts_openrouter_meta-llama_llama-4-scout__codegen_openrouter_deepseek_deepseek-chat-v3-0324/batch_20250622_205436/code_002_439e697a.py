"""
Generated Code Metadata:
========================
Original URL: https://xrpdistributions.web.app
Prompt: Generate a tutorial on how to build a decentralized exchange using the XRP Ledger's decentralized peer-to-peer multi-currency exchange feature.
Generated: DETERMINISTIC_439e697a7026cc2d
Batch ID: 20250622_205436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://s.altnet.rippletest.net:51234": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

# XRP Ledger Decentralized Exchange Tutorial

```python
import json
import xrpl
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.transactions import Payment, OfferCreate, OfferCancel
from xrpl.models.requests import AccountOffers, BookOffers
from xrpl.utils import xrp_to_drops

# Connect to the XRP Ledger testnet
TESTNET_URL = "https://s.altnet.rippletest.net:51234"
client = JsonRpcClient(TESTNET_URL)

def generate_wallet():
    """Generate a new wallet with funded account on testnet."""
    wallet = Wallet.create()
    print(f"New wallet created - Address: {wallet.address} Seed: {wallet.seed}")
    
    # Fund the account (testnet faucet)
    response = client.request(xrpl.models.requests.AccountInfo(
        account=wallet.address,
        ledger_index="validated"
    ))
    
    if response.result.get("account_data"):
        print("Account already funded")
    else:
        print("Funding account...")
        fund_response = xrpl.wallet.fund_wallet(client, wallet)
        print(f"Account funded. Balance: {fund_response.balance} XRP")
    
    return wallet

def create_offer(wallet, sell_currency, sell_amount, buy_currency, buy_amount):
    """Create a new offer on the decentralized exchange."""
    offer = OfferCreate(
        account=wallet.address,
        taker_gets={
            "currency": sell_currency["currency"],
            "value": str(sell_amount),
            "issuer": sell_currency["issuer"]
        },
        taker_pays={
            "currency": buy_currency["currency"],
            "value": str(buy_amount),
            "issuer": buy_currency["issuer"]
        },
        sequence=0  # Will be filled automatically
    )
    
    # Sign and submit the transaction
    signed_tx = xrpl.transaction.safe_sign_and_submit(
        offer, wallet, client
    )
    result = xrpl.transaction.get_transaction_from_hash(signed_tx.hash, client)
    
    if result.is_successful():
        print(f"Offer created successfully. TX Hash: {signed_tx.hash}")
    else:
        print(f"Error creating offer: {result.result['meta']['TransactionResult']}")

def cancel_offer(wallet, offer_sequence):
    """Cancel an existing offer."""
    cancel = OfferCancel(
        account=wallet.address,
        offer_sequence=offer_sequence
    )
    
    # Sign and submit the transaction
    signed_tx = xrpl.transaction.safe_sign_and_submit(
        cancel, wallet, client
    )
    result = xrpl.transaction.get_transaction_from_hash(signed_tx.hash, client)
    
    if result.is_successful():
        print(f"Offer canceled successfully. TX Hash: {signed_tx.hash}")
    else:
        print(f"Error canceling offer: {result.result['meta']['TransactionResult']}")

def get_account_offers(wallet):
    """Retrieve all offers for an account."""
    request = AccountOffers(account=wallet.address)
    response = client.request(request)
    
    if response.is_successful():
        return response.result.get("offers", [])
    else:
        print(f"Error retrieving offers: {response.result}")
        return []

def get_order_book(sell_currency, buy_currency):
    """Get the order book between two currencies."""
    request = BookOffers(
        taker_gets=sell_currency,
        taker_pays=buy_currency,
        limit=10
    )
    response = client.request(request)
    
    if response.is_successful():
        return response.result.get("offers", [])
    else:
        print(f"Error retrieving order book: {response.result}")
        return []

def execute_trade(wallet, offer_sequence, amount):
    """Execute a trade by accepting an existing offer."""
    # First get the offer details
    offers = get_account_offers(wallet)
    target_offer = next((o for o in offers if o["seq"] == offer_sequence), None)
    
    if not target_offer:
        print("Offer not found")
        return
    
    payment = Payment(
        account=wallet.address,
        destination=target_offer["Account"],
        amount={
            "currency": target_offer["TakerGets"]["currency"],
            "value": str(amount),
            "issuer": target_offer["TakerGets"]["issuer"]
        },
        sequence=0
    )
    
    # Sign and submit the transaction
    signed_tx = xrpl.transaction.safe_sign_and_submit(
        payment, wallet, client
    )
    result = xrpl.transaction.get_transaction_from_hash(signed_tx.hash, client)
    
    if result.is_successful():
        print(f"Trade executed successfully. TX Hash: {signed_tx.hash}")
    else:
        print(f"Error executing trade: {result.result['meta']['TransactionResult']}")

# Example usage
if __name__ == "__main__":
    print("XRP Ledger Decentralized Exchange Demo")
    
    # Create and fund a wallet
    wallet = generate_wallet()
    
    # Define currencies (example: USD issued by testnet gateway)
    usd_currency = {
        "currency": "USD",
        "issuer": "rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe"
    }
    xrp_currency = {
        "currency": "XRP",
        "issuer": ""
    }
    
    # Create an offer to sell 100 USD for 50 XRP
    print("\nCreating offer...")
    create_offer(wallet, usd_currency, 100, xrp_currency, 50)
    
    # View account offers
    print("\nAccount offers:")
    offers = get_account_offers(wallet)
    for offer in offers:
        print(f"Offer {offer['seq']}: {offer['TakerGets']['value']} {offer['TakerGets']['currency']} for {offer['TakerPays']['value']} {offer['TakerPays']['currency']}")
    
    # View order book
    print("\nOrder book (USD/XRP):")
    order_book = get_order_book(usd_currency, xrp_currency)
    for offer in order_book:
        print(f"{offer['TakerGets']['value']} {offer['TakerGets']['currency']} for {offer['TakerPays']['value']} {offer['TakerPays']['currency']}")
    
    # Cancel an offer (example - would need a valid sequence number)
    if offers:
        print("\nCanceling offer...")
        cancel_offer(wallet, offers[0]["seq"])
    
    # Execute a trade (example - would need another wallet with offers)
    # execute_trade(wallet, offer_sequence, amount)
```
