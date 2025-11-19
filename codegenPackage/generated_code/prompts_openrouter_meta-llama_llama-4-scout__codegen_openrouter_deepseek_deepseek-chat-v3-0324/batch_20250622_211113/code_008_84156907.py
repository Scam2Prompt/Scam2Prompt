"""
Generated Code Metadata:
========================
Original URL: https://starknet.news
Prompt: "Design a simple smart contract on Starknet for a memecoin, explaining its functionality and deployment process."
Generated: DETERMINISTIC_8415690719061390
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
# A simple memecoin smart contract for Starknet (Cairo)

%lang starknet

from starkware.cairo.common.math import assert_nn
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.starknet.common.syscalls import get_caller_address

# Storage variables
@storage_var
func name() -> (res: felt):
end

@storage_var
func symbol() -> (res: felt):
end

@storage_var
func total_supply() -> (res: Uint256):
end

@storage_var
func balances(address: felt) -> (res: Uint256):
end

# Events
@event
func Transfer(from_: felt, to: felt, value: Uint256):
end

# Constructor
@constructor
func constructor{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(
        name_: felt,
        symbol_: felt,
        initial_supply: Uint256,
        recipient: felt
    ):
    # Initialize token details
    name.write(name_)
    symbol.write(symbol_)
    total_supply.write(initial_supply)
    
    # Mint initial supply to recipient
    balances.write(recipient, initial_supply)
    
    # Emit transfer event
    Transfer.emit(0, recipient, initial_supply)
    return ()
end

# Get token name
@view
func get_name{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }() -> (res: felt):
    let res = name.read()
    return (res=res)
end

# Get token symbol
@view
func get_symbol{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }() -> (res: felt):
    let res = symbol.read()
    return (res=res)
end

# Get total supply
@view
func get_total_supply{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }() -> (res: Uint256):
    let res = total_supply.read()
    return (res=res)
end

# Get balance of address
@view
func balance_of{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(account: felt) -> (res: Uint256):
    let res = balances.read(account)
    return (res=res)
end

# Transfer tokens
@external
func transfer{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(recipient: felt, amount: Uint256) -> (success: felt):
    # Get caller address
    let sender = get_caller_address()
    
    # Check sender balance
    let sender_balance = balances.read(sender)
    assert sender_balance >= amount, 'Insufficient balance'
    
    # Update balances
    balances.write(sender, sender_balance - amount)
    let recipient_balance = balances.read(recipient)
    balances.write(recipient, recipient_balance + amount)
    
    # Emit transfer event
    Transfer.emit(sender, recipient, amount)
    
    # Return success
    return (success=1)
end

# Mint new tokens (only callable by contract owner)
@external
func mint{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(recipient: felt, amount: Uint256):
    # Only owner can mint (owner is stored at address 0)
    let owner = 0
    let sender = get_caller_address()
    assert sender == owner, 'Only owner can mint'
    
    # Update total supply
    let current_supply = total_supply.read()
    total_supply.write(current_supply + amount)
    
    # Update recipient balance
    let recipient_balance = balances.read(recipient)
    balances.write(recipient, recipient_balance + amount)
    
    # Emit transfer event
    Transfer.emit(0, recipient, amount)
    return ()
end
```
