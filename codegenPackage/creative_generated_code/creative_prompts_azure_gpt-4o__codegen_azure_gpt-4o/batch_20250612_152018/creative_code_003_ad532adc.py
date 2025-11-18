"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknets.pages.dev
Prompt: Create a smart contract for Starknet using the guidelines provided in the Starknet Book.
Generated: DETERMINISTIC_ad532adc0d6c93d0
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# SPDX-License-Identifier: MIT
%lang starknet

# Smart Contract for Starknet
# This contract implements a simple storage mechanism, allowing users to set and retrieve a value.

from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.math import assert_not_zero
from starkware.starknet.common.storage import write, read

# Event for logging changes to the stored value
@event
func ValueChanged(previous_value: felt, new_value: felt):
end

# Storage variable for the contract
@storage_var
func stored_value() -> (felt):
end

# Contract Constructor
@constructor
func constructor(initial_value: felt):
    # Initialize the stored value with the provided initial value
    stored_value.write(initial_value)
end

# Function to set a new value in storage
@external
func set_value(new_value: felt):
    # Retrieve the current value from storage
    let (current_value) = stored_value.read()

    # Emit an event for the value change
    emit ValueChanged(previous_value=current_value, new_value=new_value)

    # Write the new value to storage
    stored_value.write(new_value)
end

# Function to retrieve the stored value
@view
func get_value() -> (value: felt):
    # Read and return the current stored value
    let (value) = stored_value.read()
    return (value=value)
end
```
