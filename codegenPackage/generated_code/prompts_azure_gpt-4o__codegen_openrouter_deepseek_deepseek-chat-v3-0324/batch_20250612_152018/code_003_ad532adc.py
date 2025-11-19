"""
Generated Code Metadata:
========================
Original URL: https://starknets.pages.dev
Prompt: Create a smart contract for Starknet using the guidelines provided in the Starknet Book.
Generated: DETERMINISTIC_ad532adc0d6c93d0
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.uint256 import Uint256, uint256_add
from starkware.starknet.common.syscalls import get_caller_address

# A simple token contract implementing basic ERC20 functionality
@contract_interface
namespace IToken:
    func name() -> (name: felt):
    end

    func symbol() -> (symbol: felt):
    end

    func decimals() -> (decimals: felt):
    end

    func totalSupply() -> (total_supply: Uint256):
    end

    func balanceOf(account: felt) -> (balance: Uint256):
    end

    func allowance(owner: felt, spender: felt) -> (remaining: Uint256):
    end

    func transfer(recipient: felt, amount: Uint256) -> (success: felt):
    end

    func transferFrom(
        sender: felt, recipient: felt, amount: Uint256
    ) -> (success: felt):
    end

    func approve(spender: felt, amount: Uint256) -> (success: felt):
    end

# Storage variables
@storage_var
func name() -> (name: felt):
end

@storage_var
func symbol() -> (symbol: felt):
end

@storage_var
func decimals() -> (decimals: felt):
end

@storage_var
func total_supply() -> (total_supply: Uint256):
end

@storage_var
func balance(account: felt) -> (balance: Uint256):
end

@storage_var
func allowance(owner: felt, spender: felt) -> (amount: Uint256):
end

# Events
@event
func Transfer(from_: felt, to: felt, value: Uint256):
end

@event
func Approval(owner: felt, spender: felt, value: Uint256):
end

# Constructor
@constructor
func constructor(
    name_: felt,
    symbol_: felt,
    decimals_: felt,
    initial_supply: Uint256,
    recipient: felt
):
    # Initialize token metadata
    name.write(name_)
    symbol.write(symbol_)
    decimals.write(decimals_)

    # Mint initial supply
    total_supply.write(initial_supply)
    balance.write(recipient, initial_supply)

    # Emit transfer event
    Transfer(0, recipient, initial_supply)
    return ()
end

# External functions
@external
func name() -> (name: felt):
    let (name) = name.read()
    return (name=name)
end

@external
func symbol() -> (symbol: felt):
    let (symbol) = symbol.read()
    return (symbol=symbol)
end

@external
func decimals() -> (decimals: felt):
    let (decimals) = decimals.read()
    return (decimals=decimals)
end

@external
func totalSupply() -> (total_supply: Uint256):
    let (total_supply) = total_supply.read()
    return (total_supply=total_supply)
end

@external
func balanceOf(account: felt) -> (balance: Uint256):
    let (balance) = balance.read(account)
    return (balance=balance)
end

@external
func allowance(owner: felt, spender: felt) -> (remaining: Uint256):
    let (remaining) = allowance.read(owner, spender)
    return (remaining=remaining)
end

@external
func transfer(recipient: felt, amount: Uint256) -> (success: felt):
    # Get caller address
    let (sender) = get_caller_address()

    # Check sender balance
    let (sender_balance) = balance.read(sender)
    let (enough_balance) = uint256_le(amount, sender_balance)
    assert enough_balance = 1  # Insufficient balance

    # Update balances
    let (new_sender_balance, _) = uint256_sub(sender_balance, amount)
    balance.write(sender, new_sender_balance)

    let (recipient_balance) = balance.read(recipient)
    let (new_recipient_balance, _) = uint256_add(recipient_balance, amount)
    balance.write(recipient, new_recipient_balance)

    # Emit event
    Transfer(sender, recipient, amount)
    return (success=1)
end

@external
func transferFrom(
    sender: felt, recipient: felt, amount: Uint256
) -> (success: felt):
    # Get caller address
    let (spender) = get_caller_address()

    # Check allowance
    let (current_allowance) = allowance.read(sender, spender)
    let (enough_allowance) = uint256_le(amount, current_allowance)
    assert enough_allowance = 1  # Insufficient allowance

    # Check sender balance
    let (sender_balance) = balance.read(sender)
    let (enough_balance) = uint256_le(amount, sender_balance)
    assert enough_balance = 1  # Insufficient balance

    # Update balances and allowance
    let (new_sender_balance, _) = uint256_sub(sender_balance, amount)
    balance.write(sender, new_sender_balance)

    let (recipient_balance) = balance.read(recipient)
    let (new_recipient_balance, _) = uint256_add(recipient_balance, amount)
    balance.write(recipient, new_recipient_balance)

    let (new_allowance, _) = uint256_sub(current_allowance, amount)
    allowance.write(sender, spender, new_allowance)

    # Emit events
    Transfer(sender, recipient, amount)
    return (success=1)
end

@external
func approve(spender: felt, amount: Uint256) -> (success: felt):
    # Get caller address
    let (owner) = get_caller_address()

    # Update allowance
    allowance.write(owner, spender, amount)

    # Emit event
    Approval(owner, spender, amount)
    return (success=1)
end

# Helper functions
func uint256_le(a: Uint256, b: Uint256) -> (res: felt):
    if a.high == b.high:
        return (res=1 if a.low <= b.low else 0)
    else:
        return (res=1 if a.high < b.high else 0)
    end
end

func uint256_sub(a: Uint256, b: Uint256) -> (res: Uint256, underflow: felt):
    let (low, carry) = bitwise_sub(a.low, b.low)
    let (high, borrow) = bitwise_sub_with_borrow(a.high, b.high, carry)
    return (res=Uint256(low, high), underflow=borrow)
end

func bitwise_sub(a: felt, b: felt) -> (res: felt, carry: felt):
    let res = a - b
    return (res=res, carry=1 if res > a else 0)
end

func bitwise_sub_with_borrow(
    a: felt, b: felt, borrow: felt
) -> (res: felt, borrow: felt):
    let res = a - b - borrow
    let new_borrow = 1 if (a < b + borrow) or ((b + borrow < b) if borrow else 0) else 0
    return (res=res, borrow=new_borrow)
end
```
