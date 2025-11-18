"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.eu
Prompt: Write a code snippet using StarkWare's Cairo programming language to implement a simple zero-knowledge proof for verifying a mathematical computation.
Generated: DETERMINISTIC_f6c9d742114b10ec
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cairo
# File: zk_proof_example.cairo

# Import necessary libraries
from starkware.cairo.common.serialize import serialize_word

# Define the Cairo program for zero-knowledge proof over a simple computation
# This program proves that the prover knows two numbers `a` and `b` such that `a * b = c`.

# The main function serves as the entry point for the zero-knowledge proof.
func main{
    syscall_ptr : felt*,
    pedersen_ptr : HashBuiltin*,
    range_check_ptr : felt*
}(
    a : felt,  # Input: First number
    b : felt,  # Input: Second number
    c : felt   # Input: Result of the computation (product)
) -> (valid_proof : felt):
    # Validate the computation
    # Ensure that `a * b == c`
    let computation = a * b
    if computation == c:
        # If the computation is valid, return 1 (proof is valid)
        return (1)
    else:
        # If the computation is invalid, return 0 (proof fails)
        return (0)
    end
end

# Test function for verifying the proof
func test_proof{
    syscall_ptr : felt*,
    pedersen_ptr : HashBuiltin*,
    range_check_ptr : felt*
}() -> ():
    # Example values
    let a = 3
    let b = 4
    let c = 12  # Expected product

    # Call the main function with example inputs
    let (valid_proof) = main(a, b, c)

    # Serialize the result to make it easier to verify the output
    serialize_word(valid_proof)

    # Assertions (only for internal testing, not production)
    assert valid_proof == 1  # Expect proof to be valid for this example
    return ()
end
```
