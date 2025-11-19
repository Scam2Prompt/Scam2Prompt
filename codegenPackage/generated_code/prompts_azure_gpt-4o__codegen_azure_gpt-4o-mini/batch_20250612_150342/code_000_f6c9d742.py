"""
Generated Code Metadata:
========================
Original URL: https://starkware.eu
Prompt: Write a code snippet using StarkWare's Cairo programming language to implement a simple zero-knowledge proof for verifying a mathematical computation.
Generated: DETERMINISTIC_f6c9d742114b10ec
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cairo
# Import necessary libraries
from starkware.cairo.common.serialize import serialize
from starkware.cairo.common.math import pedersen_hash
from starkware.cairo.common.hash import hash2

# Function to compute the square of a number
@view
func compute_square{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*}(x: felt) -> (result: felt):
    # Calculate the square of x
    let result = x * x
    return (result)

# Function to create a zero-knowledge proof for the square computation
@external
func prove_square{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*}(x: felt) -> (proof: felt):
    # Compute the square of x
    let (square_result) = compute_square(x)

    # Create a hash of the input and the result to serve as a proof
    let proof = pedersen_hash(x, square_result)

    return (proof)

# Function to verify the zero-knowledge proof
@view
func verify_square{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*}(x: felt, proof: felt) -> (is_valid: felt):
    # Compute the expected square
    let (expected_square) = compute_square(x)

    # Recreate the proof hash
    let expected_proof = pedersen_hash(x, expected_square)

    # Check if the provided proof matches the expected proof
    if proof == expected_proof:
        return (1)  # Proof is valid
    else:
        return (0)  # Proof is invalid

# Main function to demonstrate the zero-knowledge proof
@main
func main{syscall_ptr: felt*, pedersen_ptr: HashBuiltin*}():
    # Example input
    let x = 3

    # Generate proof for the square of x
    let (proof) = prove_square(x)

    # Verify the proof
    let (is_valid) = verify_square(x, proof)

    # Output the result of the verification
    assert is_valid == 1, "Proof verification failed!"

    return ()
```
