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
# Importing necessary libraries from Cairo
from starkware.cairo.common.hash import pedersen_hash
from starkware.cairo.common.serialize import serialize
from starkware.cairo.lang.contracts import Contract

# Define a contract for our zero-knowledge proof
@contract
namespace zk_math_proof:
    # A function to compute the square of a number
    @public
    func compute_square{ syscall_ptr : felt*, pedersen_ptr : Hash_ptr }(number: felt) -> (result: felt):
        # Calculate the square
        let result = number * number
        return (result)

    # A function to generate a proof for the computation
    @public
    func prove_square{ syscall_ptr : felt*, pedersen_ptr : Hash_ptr }(number: felt) -> (proof: felt):
        # Call the compute_square function to get the result
        let (result) = compute_square(number)

        # Generate a proof using Pedersen hash
        let proof = pedersen_hash(number, result)
        return (proof)

    # A function to verify the proof
    @public
    func verify_square{ syscall_ptr : felt*, pedersen_ptr : Hash_ptr }(number: felt, proof: felt) -> (is_valid: felt):
        # Recompute the expected result
        let (expected_result) = compute_square(number)

        # Hash the original number and result to generate the valid proof
        let valid_proof = pedersen_hash(number, expected_result)

        # Check if the provided proof matches the valid proof
        let is_valid = if proof == valid_proof { 1 } else { 0 }
        return (is_valid)

# End of the zk_math_proof contract
```
