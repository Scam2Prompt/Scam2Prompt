"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nepmigration.pages.dev
Prompt: Write a Python smart contract using the Neo blockchain's NEP-17 standard to implement token transfer functionality, ensuring compliance with Neo N3's built-in features like `check_witness` and `onPayment`.
Generated: DETERMINISTIC_e8d5faa6249bdc76
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from boa3.builtin import public, CreateNewEvent
from boa3.builtin.contract import abort
from boa3.builtin.interop.blockchain import check_witness, get_calling_script_hash
from boa3.builtin.interop.runtime import calling_script_hash
from boa3.builtin.interop.storage import get, put, delete
from boa3.builtin.type import UInt160

# Events for logging successful transfers and notifications
on_transfer = CreateNewEvent(
    [
        ('from', UInt160), 
        ('to', UInt160), 
        ('amount', int)
    ],
    'Transfer'
)
on_payment = CreateNewEvent(
    [
        ('from', UInt160), 
        ('amount', int)
    ],
    'Payment'
)

TOKEN_NAME = 'MyToken'
TOKEN_SYMBOL = 'MTK'
TOKEN_DECIMALS = 8

# Total supply of the token (example: 100,000 tokens with 8 decimal places)
TOTAL_SUPPLY = 10_000_000_000_000_000

# Storage keys
TOTAL_SUPPLY_KEY = 'total_supply'

@public
def deploy() -> bool:
    """
    Deploys the smart contract, initializes the total supply, and assigns it
    to the contract's owner. This should only be run once during deployment.
    """
    owner = get_owner()
    if owner is None:
        put_owner(UInt160())  # Replace with the owner's address
        put(TOTAL_SUPPLY_KEY, TOTAL_SUPPLY)
        put_balance(owner, TOTAL_SUPPLY)
        return True
    return False

@public
def name() -> str:
    """
    Returns the name of the token.
    """
    return TOKEN_NAME

@public
def symbol() -> str:
    """
    Returns the symbol of the token.
    """
    return TOKEN_SYMBOL

@public
def decimals() -> int:
    """
    Returns the number of decimals the token uses.
    """
    return TOKEN_DECIMALS

@public
def total_supply() -> int:
    """
    Returns the total supply of the token.
    """
    return get(TOTAL_SUPPLY_KEY).to_int()

@public
def balance_of(account: UInt160) -> int:
    """
    Returns the balance of the specified account.
    """
    validate_address(account)
    return get_balance(account)

@public
def transfer(from_address: UInt160, to_address: UInt160, amount: int) -> bool:
    """
    Transfers the specified amount of tokens from one account to another.
    Ensures the sender has enough balance and is authenticated.
    """
    validate_address(from_address)
    validate_address(to_address)
    if not check_witness(from_address):
        abort()

    if amount <= 0:
        abort()

    from_balance = get_balance(from_address)
    if from_balance < amount:
        abort()

    to_balance = get_balance(to_address)

    # Deduct from sender
    put_balance(from_address, from_balance - amount)

    # Add to receiver
    put_balance(to_address, to_balance + amount)

    on_transfer(from_address, to_address, amount)
    return True

@public
def on_payment(from_address: UInt160, amount: int):
    """
    Triggered when tokens are sent to the contract. Handles incoming payments.
    """
    validate_address(from_address)
    if amount <= 0:
        abort()

    if not check_witness(from_address):
        abort()

    on_payment(from_address, amount)

# Helper functions
def get_owner() -> UInt160:
    """
    Returns the owner address stored in contract storage.
    """
    return get('owner')

def put_owner(owner: UInt160):
    """
    Stores the owner address in contract storage.
    """
    put('owner', owner)

def get_balance(account: UInt160) -> int:
    """
    Fetches the balance of the specified account from storage.
    """
    return get(account).to_int()

def put_balance(account: UInt160, balance: int):
    """
    Updates the balance of the specified account in storage.
    """
    put(account, balance)

def validate_address(address: UInt160):
    """
    Validates that the provided address is a valid UInt160 type.
    """
    if len(address) != 20:
        abort()
```
