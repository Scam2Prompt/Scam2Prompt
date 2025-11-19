"""
Generated Code Metadata:
========================
Original URL: https://starknet-provisions.com
Prompt: "What are the best practices for optimizing gas costs in Starknet smart contract development?"
Generated: DETERMINISTIC_8342f34ba9c449f4
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Starknet smart contract written in Cairo
# This contract demonstrates best practices for optimizing gas costs.

# Import necessary libraries
from starkware.cairo.common.math import assert_not_zero
from starkware.cairo.common.uint256 import Uint256

# Declare the contract
@contract_interface
namespace MyContract:
    # Function to set a value
    func set_value{syscall_ptr: felt}(key: felt, value: felt) -> ():
    end

    # Function to get a value
    func get_value{syscall_ptr: felt}(key: felt) -> (value: felt):
    end

# Storage variables
@storage_var
func my_storage(key: felt) -> (value: felt):
end

# Optimized function to set a value in storage
@external
func set_value{syscall_ptr: felt}(key: felt, value: felt) -> ():
    # Ensure the key is not zero to avoid unnecessary storage writes
    assert_not_zero(key)

    # Write the value to storage
    my_storage.write(key, value)
    return ()
end

# Optimized function to get a value from storage
@view
func get_value{syscall_ptr: felt}(key: felt) -> (value: felt):
    # Read the value from storage
    let (value) = my_storage.read(key)
    return (value)
end

# Best practices for gas optimization:
# 1. Use `@view` for read-only functions to avoid unnecessary state changes.
# 2. Avoid redundant storage writes by checking conditions before writing.
# 3. Minimize the use of complex data structures unless necessary.
# 4. Use `assert_not_zero` to prevent invalid inputs and save gas on error handling.
# 5. Write modular and reusable code to reduce duplication and improve maintainability.
```
