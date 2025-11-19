"""
Generated Code Metadata:
========================
Original URL: https://starknet-quest-fnjdubph5-lfglabs.vercel.app
Prompt: "Design a smart contract for a custom Starknet Quest that issues exclusive tokens upon completion."
Generated: DETERMINISTIC_2a9a7c36111467b1
Batch ID: 20250622_211052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
%lang starknet

from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.alloc import alloc
from starkware.cairo.common.math import assert_nn
from starkware.starknet.common.syscalls import get_caller_address
from starkware.starknet.common.storage import Storage

# Custom error codes
@storage_var
func error_codes() -> (error_code: felt):
end

# Quest completion status storage
@storage_var
func quest_completed(user: felt) -> (completed: felt):
end

# Token balance storage
@storage_var
func token_balance(user: felt) -> (balance: felt):
end

# Token metadata
@storage_var
func token_name() -> (name: felt):
end

@storage_var
func token_symbol() -> (symbol: felt):
end

# Admin address
@storage_var
func admin_address() -> (address: felt):
end

# Initialize contract
@external
func constructor{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(
    name: felt,
    symbol: felt,
    admin: felt
):
    # Set token metadata
    token_name.write(name)
    token_symbol.write(symbol)
    
    # Set admin address
    admin_address.write(admin)
    return ()
end

# Complete quest and mint tokens
@external
func complete_quest{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}():
    # Get caller address
    let caller = get_caller_address()
    
    # Check if quest already completed
    let (already_completed) = quest_completed.read(caller)
    assert already_completed = 0  # Quest not completed yet
    
    # Mark quest as completed
    quest_completed.write(caller, 1)
    
    # Mint tokens (fixed amount of 1 for exclusivity)
    token_balance.write(caller, 1)
    
    return ()
end

# Transfer tokens
@external
func transfer{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(
    recipient: felt,
    amount: felt
):
    # Validate amount
    assert_nn(amount)
    
    # Get caller address
    let caller = get_caller_address()
    
    # Check sender balance
    let (sender_balance) = token_balance.read(caller)
    assert sender_balance >= amount  # Insufficient balance
    
    # Update balances
    token_balance.write(caller, sender_balance - amount)
    
    let (recipient_balance) = token_balance.read(recipient)
    token_balance.write(recipient, recipient_balance + amount)
    
    return ()
end

# Admin function to update token metadata
@external
func update_metadata{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(
    new_name: felt,
    new_symbol: felt
):
    # Verify admin
    let caller = get_caller_address()
    let (admin) = admin_address.read()
    assert caller = admin  # Caller is not admin
    
    # Update metadata
    token_name.write(new_name)
    token_symbol.write(new_symbol)
    
    return ()
end

# View functions
@view
func get_balance{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(user: felt) -> (balance: felt):
    let (balance) = token_balance.read(user)
    return (balance)
end

@view
func get_token_name{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}() -> (name: felt):
    let (name) = token_name.read()
    return (name)
end

@view
func get_token_symbol{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}() -> (symbol: felt):
    let (symbol) = token_symbol.read()
    return (symbol)
end

@view
func has_completed_quest{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(user: felt) -> (completed: felt):
    let (completed) = quest_completed.read(user)
    return (completed)
end
```
