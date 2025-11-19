"""
Generated Code Metadata:
========================
Original URL: https://starknet.news
Prompt: Provide an example of how to implement a smart contract on Starknet, focusing on low-cost transaction features.
Generated: DETERMINISTIC_fcb7d6539e8eaebb
Batch ID: 20250612_155650
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
from starkware.cairo.common.uint256 import Uint256, uint256_add
from starkware.starknet.common.syscalls import get_caller_address

# Storage variables
@storage_var
func balance(account: felt) -> (res: Uint256) {
}

# Events
@event
func transfer(from_: felt, to: felt, amount: Uint256) {
}

# Low-cost transfer function with minimal storage operations
@external
func transfer{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(to: felt, amount: Uint256) {
    alloc_locals;
    
    # Get caller address
    let (caller) = get_caller_address();
    
    # Check amount is positive
    with_attr error_message("Amount must be positive") {
        assert_not_zero(amount.low);
        assert_not_zero(amount.high);
    }
    
    # Get sender balance
    let (sender_balance) = balance.read(caller);
    
    # Check sufficient balance
    with_attr error_message("Insufficient balance") {
        let (enough) = uint256_le(amount, sender_balance);
        assert enough = 1;
    }
    
    # Get recipient balance
    let (recipient_balance) = balance.read(to);
    
    # Update balances
    let (new_sender_balance) = uint256_sub(sender_balance, amount);
    let (new_recipient_balance) = uint256_add(recipient_balance, amount);
    
    balance.write(caller, new_sender_balance);
    balance.write(to, new_recipient_balance);
    
    # Emit event
    transfer.emit(caller, to, amount);
    return ();
}

# Low-cost mint function (only owner)
@external
func mint{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(to: felt, amount: Uint256) {
    alloc_locals;
    
    # Get caller address
    let (caller) = get_caller_address();
    
    # Check caller is owner (replace with actual owner check)
    with_attr error_message("Caller is not owner") {
        assert caller = 0x123;  # Replace with actual owner address
    }
    
    # Check amount is positive
    with_attr error_message("Amount must be positive") {
        assert_not_zero(amount.low);
        assert_not_zero(amount.high);
    }
    
    # Get current balance
    let (current_balance) = balance.read(to);
    
    # Update balance
    let (new_balance) = uint256_add(current_balance, amount);
    balance.write(to, new_balance);
    
    # Emit event (optional)
    transfer.emit(0, to, amount);
    return ();
}

# View function to check balance (no cost)
@view
func get_balance{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(account: felt) -> (res: Uint256) {
    let (res) = balance.read(account);
    return (res,);
}

# Helper functions
func uint256_le(a: Uint256, b: Uint256) -> (res: felt) {
    if (a.high == b.high) {
        return (is_le(a.low, b.low));
    }
    return (is_le(a.high, b.high));
}

func uint256_sub(a: Uint256, b: Uint256) -> (res: Uint256) {
    let (low, carry) = unsigned_sub_overflow(a.low, b.low);
    let high = a.high - b.high - carry;
    return (Uint256(low, high));
}
```
