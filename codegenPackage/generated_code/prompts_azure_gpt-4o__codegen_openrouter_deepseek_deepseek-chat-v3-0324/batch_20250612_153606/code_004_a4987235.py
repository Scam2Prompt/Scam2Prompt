"""
Generated Code Metadata:
========================
Original URL: https://starknet-homepage-kappa.vercel.app
Prompt: Create a smart contract on Starknet that allows users to mint NFTs representing individual pixels on a grid.
Generated: DETERMINISTIC_a49872350ee4acab
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
%lang starknet

from starkware.cairo.common.math import assert_nn_le
from starkware.cairo.common.uint256 import Uint256, uint256_add, uint256_sub
from starkware.starknet.common.syscalls import get_caller_address
from starkware.cairo.common.bool import TRUE, FALSE

# Constants
const GRID_WIDTH = 1000
const GRID_HEIGHT = 1000
const PRICE_PER_PIXEL = 1000000000000000  # 0.001 ETH

# Storage variables
@storage_var
func pixel_owner(x: felt, y: felt) -> (owner: felt):
end

@storage_var
func pixel_color(x: felt, y: felt) -> (color: felt):
end

@storage_var
func total_pixels_minted() -> (count: Uint256):
end

@storage_var
func contract_owner() -> (owner: felt):
end

# Events
@event
func PixelMinted(x: felt, y: felt, owner: felt, color: felt):
end

@event
func PixelColorChanged(x: felt, y: felt, new_color: felt):
end

# Constructor
@constructor
func constructor{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }():
    let (caller) = get_caller_address()
    contract_owner.write(caller)
    total_pixels_minted.write(Uint256(0, 0))
    return ()
end

# External functions
@external
func mint_pixel{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(x: felt, y: felt, color: felt):
    # Validate coordinates
    assert_nn_le(x, GRID_WIDTH - 1)
    assert_nn_le(y, GRID_HEIGHT - 1)

    # Check if pixel is available
    let (current_owner) = pixel_owner.read(x, y)
    assert current_owner = 0  # 0 means unowned

    # Get caller address
    let (caller) = get_caller_address()

    # Update storage
    pixel_owner.write(x, y, caller)
    pixel_color.write(x, y, color)

    # Update total pixels minted
    let (current_total) = total_pixels_minted.read()
    let (new_total, _) = uint256_add(current_total, Uint256(1, 0))
    total_pixels_minted.write(new_total)

    # Emit event
    PixelMinted.emit(x, y, caller, color)
    return ()
end

@external
func change_pixel_color{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(x: felt, y: felt, new_color: felt):
    # Validate coordinates
    assert_nn_le(x, GRID_WIDTH - 1)
    assert_nn_le(y, GRID_HEIGHT - 1)

    # Get caller address
    let (caller) = get_caller_address()

    # Check ownership
    let (owner) = pixel_owner.read(x, y)
    assert owner = caller

    # Update color
    pixel_color.write(x, y, new_color)

    # Emit event
    PixelColorChanged.emit(x, y, new_color)
    return ()
end

@view
func get_pixel_info{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }(x: felt, y: felt) -> (owner: felt, color: felt):
    # Validate coordinates
    assert_nn_le(x, GRID_WIDTH - 1)
    assert_nn_le(y, GRID_HEIGHT - 1)

    let (owner) = pixel_owner.read(x, y)
    let (color) = pixel_color.read(x, y)
    return (owner, color)
end

@view
func get_total_pixels_minted{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }() -> (count: Uint256):
    let (count) = total_pixels_minted.read()
    return (count)
end

@external
func withdraw_funds{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr
    }():
    # Only owner can withdraw
    let (caller) = get_caller_address()
    let (owner) = contract_owner.read()
    assert caller = owner

    # Get contract balance
    let (balance_low, balance_high) = get_balance(get_contract_address())

    # Transfer funds to owner
    let (success) = transfer(owner, Uint256(balance_low, balance_high))
    assert success = TRUE
    return ()
end
```
