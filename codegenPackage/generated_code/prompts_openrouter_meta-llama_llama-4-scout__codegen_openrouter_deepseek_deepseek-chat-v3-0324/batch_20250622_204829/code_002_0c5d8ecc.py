"""
Generated Code Metadata:
========================
Original URL: https://award-nostra.pages.dev
Prompt: Generate a smart contract code for a lending pool on Starknet, inspired by Nostra's lending feature.
Generated: DETERMINISTIC_0c5d8ecc27026bdd
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
%lang starknet

from starkware.cairo.common.math import (assert_nn, unsigned_div_rem)
from starkware.cairo.common.uint256 import (Uint256, uint256_add, uint256_sub, uint256_mul, uint256_div, uint256_lt)
from starkware.starknet.common.syscalls import (get_caller_address, get_block_number)

# Storage structure
@storage_var
func total_supply(token_address: felt) -> (supply: Uint256):
end

@storage_var
func total_borrowed(token_address: felt) -> (borrowed: Uint256):
end

@storage_var
func user_supply(user: felt, token_address: felt) -> (amount: Uint256):
end

@storage_var
func user_borrowed(user: felt, token_address: felt) -> (amount: Uint256):
end

@storage_var
func interest_rate_model(token_address: felt) -> (model_address: felt):
end

@storage_var
func reserve_factor(token_address: felt) -> (factor: Uint256):
end

@storage_var
func last_update_block(token_address: felt) -> (block_number: felt):
end

# Events
@event
func Supply(account: felt, token_address: felt, amount: Uint256):
end

@event
func Withdraw(account: felt, token_address: felt, amount: Uint256):
end

@event
func Borrow(account: felt, token_address: felt, amount: Uint256):
end

@event
func Repay(account: felt, token_address: felt, amount: Uint256):
end

# Constants
const MAX_UINT256 = 2**256 - 1
const SECONDS_PER_YEAR = 31536000  # 365 days
const SCALE = 10**18

# External functions
@external
func deposit{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    token_address: felt, amount: Uint256
):
    alloc_locals
    let (caller) = get_caller_address()
    
    # Validate amount
    let (is_zero) = uint256_eq(amount, Uint256(0, 0))
    assert is_zero = 0  # Amount must be > 0
    
    # Update interest indices
    let (current_block) = get_block_number()
    let (last_block) = last_update_block.read(token_address)
    if last_block != current_block:
        _update_interest(token_address, current_block)
    
    # Update user supply
    let (current_supply) = user_supply.read(caller, token_address)
    let (new_supply) = uint256_add(current_supply, amount)
    user_supply.write(caller, token_address, new_supply)
    
    # Update total supply
    let (total_supply_amount) = total_supply.read(token_address)
    let (new_total_supply) = uint256_add(total_supply_amount, amount)
    total_supply.write(token_address, new_total_supply)
    
    # Emit event
    Supply.emit(caller, token_address, amount)
    return ()
end

@external
func withdraw{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    token_address: felt, amount: Uint256
):
    alloc_locals
    let (caller) = get_caller_address()
    
    # Validate amount
    let (is_zero) = uint256_eq(amount, Uint256(0, 0))
    assert is_zero = 0  # Amount must be > 0
    
    # Update interest indices
    let (current_block) = get_block_number()
    let (last_block) = last_update_block.read(token_address)
    if last_block != current_block:
        _update_interest(token_address, current_block)
    
    # Check user has enough supply
    let (current_supply) = user_supply.read(caller, token_address)
    let (has_enough) = uint256_le(amount, current_supply)
    assert has_enough = 1  # Insufficient supply
    
    # Update user supply
    let (new_supply) = uint256_sub(current_supply, amount)
    user_supply.write(caller, token_address, new_supply)
    
    # Update total supply
    let (total_supply_amount) = total_supply.read(token_address)
    let (new_total_supply) = uint256_sub(total_supply_amount, amount)
    total_supply.write(token_address, new_total_supply)
    
    # Emit event
    Withdraw.emit(caller, token_address, amount)
    return ()
end

@external
func borrow{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    token_address: felt, amount: Uint256
):
    alloc_locals
    let (caller) = get_caller_address()
    
    # Validate amount
    let (is_zero) = uint256_eq(amount, Uint256(0, 0))
    assert is_zero = 0  # Amount must be > 0
    
    # Update interest indices
    let (current_block) = get_block_number()
    let (last_block) = last_update_block.read(token_address)
    if last_block != current_block:
        _update_interest(token_address, current_block)
    
    # Check available liquidity
    let (total_supply_amount) = total_supply.read(token_address)
    let (total_borrowed_amount) = total_borrowed.read(token_address)
    let (available) = uint256_sub(total_supply_amount, total_borrowed_amount)
    let (can_borrow) = uint256_le(amount, available)
    assert can_borrow = 1  # Insufficient liquidity
    
    # Update user borrowed
    let (current_borrowed) = user_borrowed.read(caller, token_address)
    let (new_borrowed) = uint256_add(current_borrowed, amount)
    user_borrowed.write(caller, token_address, new_borrowed)
    
    # Update total borrowed
    let (new_total_borrowed) = uint256_add(total_borrowed_amount, amount)
    total_borrowed.write(token_address, new_total_borrowed)
    
    # Emit event
    Borrow.emit(caller, token_address, amount)
    return ()
end

@external
func repay{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    token_address: felt, amount: Uint256
):
    alloc_locals
    let (caller) = get_caller_address()
    
    # Validate amount
    let (is_zero) = uint256_eq(amount, Uint256(0, 0))
    assert is_zero = 0  # Amount must be > 0
    
    # Update interest indices
    let (current_block) = get_block_number()
    let (last_block) = last_update_block.read(token_address)
    if last_block != current_block:
        _update_interest(token_address, current_block)
    
    # Check user has enough debt
    let (current_borrowed) = user_borrowed.read(caller, token_address)
    let (has_enough) = uint256_le(amount, current_borrowed)
    assert has_enough = 1  # Repayment exceeds debt
    
    # Update user borrowed
    let (new_borrowed) = uint256_sub(current_borrowed, amount)
    user_borrowed.write(caller, token_address, new_borrowed)
    
    # Update total borrowed
    let (total_borrowed_amount) = total_borrowed.read(token_address)
    let (new_total_borrowed) = uint256_sub(total_borrowed_amount, amount)
    total_borrowed.write(token_address, new_total_borrowed)
    
    # Emit event
    Repay.emit(caller, token_address, amount)
    return ()
end

# Internal functions
func _update_interest{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*, range_check_ptr}(
    token_address: felt, current_block: felt
):
    alloc_locals
    let (last_block) = last_update_block.read(token_address)
    let (blocks_passed) = assert_nn(current_block - last_block)
    
    if blocks_passed == 0:
        return ()
    
    # Get interest rate from model
    let (model) = interest_rate_model.read(token_address)
    let (rate) = IInterestRateModel.calculate_borrow_rate(model, token_address)
    
    # Calculate interest factor
    let (rate_scaled) = uint256_mul(rate, Uint256(blocks_passed, 0))
    let (rate_per_block) = uint256_div(rate_scaled, Uint256(SECONDS_PER_YEAR, 0))
    
    # Update total borrowed with interest
    let (total_borrowed_amount) = total_borrowed.read(token_address)
    let (interest) = uint256_mul(total_borrowed_amount, rate_per_block)
    let (
