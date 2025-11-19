"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nepmigration.pages.dev
Prompt: Write a smart contract in Python for the Neo blockchain that implements the NEP-17 token standard.
Generated: DETERMINISTIC_c123410e2f590af1
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from boa3.builtin import public, NeoMetadata, metadata, CreateNewEvent
from boa3.builtin.contract import Nep17TransferEvent, abort
from boa3.builtin.interop.runtime import calling_script_hash, check_witness
from boa3.builtin.interop.storage import get, put, delete
from boa3.builtin.type import UInt160

# Define contract metadata
@metadata
def manifest() -> NeoMetadata:
    meta = NeoMetadata()
    meta.name = 'NEP-17 Token'
    meta.author = 'Your Name'
    meta.email = 'youremail@example.com'
    meta.description = 'An implementation of the NEP-17 token standard on Neo blockchain.'
    meta.supported_standards = ['NEP-17']
    return meta

# Define events
on_transfer = CreateNewEvent(
    [
        ('from', UInt160),
        ('to', UInt160),
        ('amount', int)
    ],
    'Transfer'
)
on_approval = CreateNewEvent(
    [
        ('owner', UInt160),
        ('spender', UInt160),
        ('amount', int)
    ],
    'Approval'
)

# Token details
TOKEN_NAME = 'ExampleToken'
TOKEN_SYMBOL = 'EXT'
TOKEN_DECIMALS = 8
TOTAL_SUPPLY = 1_000_000 * 10**TOKEN_DECIMALS  # 1 million tokens

# Keys for storage
TOTAL_SUPPLY_KEY = b'total_supply'
BALANCE_PREFIX = b'balance_'
APPROVAL_PREFIX = b'approval_'

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
    Returns the number of decimal places used by the token.
    """
    return TOKEN_DECIMALS

@public
def totalSupply() -> int:
    """
    Returns the total token supply.
    """
    supply = get(TOTAL_SUPPLY_KEY)
    if supply is None:
        return TOTAL_SUPPLY
    return int(supply)

@public
def balanceOf(account: UInt160) -> int:
    """
    Returns the balance of the specified account.
    """
    if not isinstance(account, UInt160):
        abort()
    balance = get(BALANCE_PREFIX + account)
    if balance is None:
        return 0
    return int(balance)

@public
def transfer(from_: UInt160, to_: UInt160, amount: int) -> bool:
    """
    Transfers tokens from one account to another.
    """
    if not _validate_address(from_) or not _validate_address(to_):
        abort()
    if amount <= 0:
        abort()
    if not check_witness(from_):
        abort()

    from_balance = balanceOf(from_)
    if from_balance < amount:
        return False

    to_balance = balanceOf(to_)
    put(BALANCE_PREFIX + from_, from_balance - amount)
    put(BALANCE_PREFIX + to_, to_balance + amount)

    on_transfer(from_, to_, amount)
    return True

@public
def transferFrom(owner: UInt160, to_: UInt160, amount: int) -> bool:
    """
    Transfers tokens on behalf of the owner.
    """
    if not _validate_address(owner) or not _validate_address(to_):
        abort()
    if amount <= 0:
        abort()
    if not check_witness(calling_script_hash):
        abort()

    allowance = _get_approval(owner, calling_script_hash)
    if allowance < amount:
        return False

    owner_balance = balanceOf(owner)
    if owner_balance < amount:
        return False

    to_balance = balanceOf(to_)
    put(BALANCE_PREFIX + owner, owner_balance - amount)
    put(BALANCE_PREFIX + to_, to_balance + amount)
    _set_approval(owner, calling_script_hash, allowance - amount)

    on_transfer(owner, to_, amount)
    return True

@public
def approve(spender: UInt160, amount: int) -> bool:
    """
    Approves a spender to transfer tokens on behalf of the owner.
    """
    if not _validate_address(spender):
        abort()
    if amount < 0:
        abort()
    owner = calling_script_hash
    _set_approval(owner, spender, amount)
    on_approval(owner, spender, amount)
    return True

@public
def allowance(owner: UInt160, spender: UInt160) -> int:
    """
    Returns the remaining approved balance for the spender.
    """
    return _get_approval(owner, spender)

def _get_approval(owner: UInt160, spender: UInt160) -> int:
    """
    Internal function to retrieve the approval amount.
    """
    approval = get(APPROVAL_PREFIX + owner + spender)
    if approval is None:
        return 0
    return int(approval)

def _set_approval(owner: UInt160, spender: UInt160, amount: int):
    """
    Internal function to set the approval amount.
    """
    put(APPROVAL_PREFIX + owner + spender, amount)

def _validate_address(address: UInt160) -> bool:
    """
    Validates that the given address is a valid Neo address.
    """
    return isinstance(address, UInt160)
```
