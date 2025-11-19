"""
Generated Code Metadata:
========================
Original URL: https://starknet-homepage-kappa.vercel.app
Prompt: Generate a simple smart contract using Starknet that allows users to purchase and own pixels on a digital artwork, with the owner being responsible for the content.
Generated: DETERMINISTIC_61d9434a5bb6c762
Batch ID: 20250622_210918
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
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.starknet.common.syscalls import get_caller_address

# Constants
const MAX_WIDTH = 1000
const MAX_HEIGHT = 1000
const PRICE_PER_PIXEL = 1000000000000000  # 0.001 ETH

# Storage variables
@storage_var
func pixel_owner(width: felt, height: felt) -> (owner: felt):
end

@storage_var
func pixel_content(width: felt, height: felt) -> (content: felt):
end

@storage_var
func total_pixels_sold() -> (count: felt):
end

# Events
@event
func pixel_purchased(
    buyer: felt,
    width: felt,
    height: felt,
    content: felt
):
end

@event
func pixel_updated(
    owner: felt,
    width: felt,
    height: felt,
    new_content: felt
):
end

# External functions
@external
func purchase_pixel{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(
    width: felt,
    height: felt,
    initial_content: felt
):
    # Validate input
    assert_nn_le(width, MAX_WIDTH)
    assert_nn_le(height, MAX_HEIGHT)

    # Check if pixel is already owned
    let (current_owner) = pixel_owner.read(width, height)
    assert current_owner == 0, "Pixel already owned"

    # Get caller address
    let (caller) = get_caller_address()

    # Store ownership and content
    pixel_owner.write(width, height, caller)
    pixel_content.write(width, height, initial_content)

    # Update total pixels sold
    let (current_total) = total_pixels_sold.read()
    total_pixels_sold.write(current_total + 1)

    # Emit event
    pixel_purchased.emit(caller, width, height, initial_content)
    return ()
end

@external
func update_pixel_content{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(
    width: felt,
    height: felt,
    new_content: felt
):
    # Validate input
    assert_nn_le(width, MAX_WIDTH)
    assert_nn_le(height, MAX_HEIGHT)

    # Get caller address
    let (caller) = get_caller_address()

    # Verify ownership
    let (owner) = pixel_owner.read(width, height)
    assert owner == caller, "Only owner can update content"

    # Update content
    pixel_content.write(width, height, new_content)

    # Emit event
    pixel_updated.emit(caller, width, height, new_content)
    return ()
end

# View functions
@view
func get_pixel_owner{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(
    width: felt,
    height: felt
) -> (owner: felt):
    let (owner) = pixel_owner.read(width, height)
    return (owner)
end

@view
func get_pixel_content{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(
    width: felt,
    height: felt
) -> (content: felt):
    let (content) = pixel_content.read(width, height)
    return (content)
end

@view
func get_total_pixels_sold{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}() -> (count: felt):
    let (count) = total_pixels_sold.read()
    return (count)
end
```
