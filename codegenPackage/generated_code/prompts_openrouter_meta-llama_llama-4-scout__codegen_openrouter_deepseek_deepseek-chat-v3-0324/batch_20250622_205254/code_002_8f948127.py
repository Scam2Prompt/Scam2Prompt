"""
Generated Code Metadata:
========================
Original URL: https://starknet-homepage.vercel.app
Prompt: Generate a simple smart contract using Starknet that allows users to purchase and own pixels on a digital artwork, with the image ownership stored as an NFT.
Generated: DETERMINISTIC_8f948127f1ef6c21
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
%lang starknet

from starkware.cairo.common.math import assert_nn
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.starknet.common.syscalls import get_caller_address
from starkware.starknet.common.storage import Storage, storage_read, storage_write

# Constants
const MAX_WIDTH = 1000
const MAX_HEIGHT = 1000
const PIXEL_PRICE = 1000000000000000  # 0.001 ETH

# Structs
struct Pixel {
    owner: felt,
    color: felt,
}

struct PixelPosition {
    x: felt,
    y: felt,
}

# Storage
@storage_var
func pixel_map(x: felt, y: felt) -> (pixel: Pixel) {
}

@storage_var
func owner_pixels(owner: felt, index: felt) -> (position: PixelPosition) {
}

@storage_var
func owner_pixel_count(owner: felt) -> (count: felt) {
}

@storage_var
func total_pixels_sold() -> (count: felt) {
}

# Events
@event
func PixelPurchased(owner: felt, x: felt, y: felt, color: felt) {
}

@event
func PixelColorChanged(owner: felt, x: felt, y: felt, new_color: felt) {
}

# External functions
@external
func purchase_pixel{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr,
    }(x: felt, y: felt, color: felt) {
    alloc_locals;
    let (caller) = get_caller_address();

    # Validate position
    assert_nn(x);
    assert_nn(y);
    assert x < MAX_WIDTH;
    assert y < MAX_HEIGHT;

    # Validate color (24-bit RGB)
    assert_nn(color);
    assert color < 0x1000000;

    # Check if pixel is already owned
    let (current_pixel) = pixel_map.read(x, y);
    assert current_pixel.owner = 0;

    # Transfer funds (simplified for example)
    # In production, use proper token transfer

    # Update pixel ownership
    pixel_map.write(x, y, Pixel(owner=caller, color=color));

    # Update owner's pixel list
    let (count) = owner_pixel_count.read(caller);
    owner_pixels.write(caller, count, PixelPosition(x=x, y=y));
    owner_pixel_count.write(caller, count + 1);

    # Update total pixels sold
    let (total) = total_pixels_sold.read();
    total_pixels_sold.write(total + 1);

    # Emit event
    PixelPurchased.emit(caller, x, y, color);
    return ();
}

@external
func change_pixel_color{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr,
    }(x: felt, y: felt, new_color: felt) {
    alloc_locals;
    let (caller) = get_caller_address();

    # Validate color
    assert_nn(new_color);
    assert new_color < 0x1000000;

    # Check ownership
    let (pixel) = pixel_map.read(x, y);
    assert pixel.owner = caller;

    # Update color
    pixel_map.write(x, y, Pixel(owner=caller, color=new_color));

    # Emit event
    PixelColorChanged.emit(caller, x, y, new_color);
    return ();
}

@view
func get_pixel{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr,
    }(x: felt, y: felt) -> (pixel: Pixel) {
    let (pixel) = pixel_map.read(x, y);
    return (pixel=pixel);
}

@view
func get_owner_pixel_count{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr,
    }(owner: felt) -> (count: felt) {
    let (count) = owner_pixel_count.read(owner);
    return (count=count);
}

@view
func get_total_pixels_sold{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr,
    }() -> (count: felt) {
    let (count) = total_pixels_sold.read();
    return (count=count);
}

@view
func get_owner_pixel_at_index{
        syscall_ptr: felt*,
        pedersen_ptr: HashBuiltin*,
        range_check_ptr,
    }(owner: felt, index: felt) -> (position: PixelPosition) {
    let (position) = owner_pixels.read(owner, index);
    return (position=position);
}
```
