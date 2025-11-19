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
// Import the necessary libraries
use starkware_crypto::hash::pedersen::PedersenHash;
use starkware_crypto::traits::{Hash, PedersenCompatible};

// Define a struct to hold the computation inputs and outputs
struct Computation {
    x: felt,
    y: felt,
    result: felt,
}

// Implement the computation function
fn compute(x: felt, y: felt) -> felt {
    // Simple addition computation
    x + y
}

// Define a function to generate a proof for the computation
fn generate_proof(computation: Computation) -> (felt, felt) {
    // Compute the result
    let result = compute(computation.x, computation.y);

    // Check if the result matches the provided output
    assert(result == computation.result);

    // Generate a random number for the proof (in a real implementation, this would be a secure random number)
    let r = 123;

    // Compute the Pedersen hash of the inputs and output
    let hash = PedersenHash::hash([
        computation.x,
        computation.y,
        computation.result,
    ]);

    // Compute the proof
    let proof = (r, hash);

    proof
}

// Define a function to verify a proof
fn verify_proof(proof: (felt, felt), computation: Computation) -> bool {
    // Compute the Pedersen hash of the inputs and output
    let hash = PedersenHash::hash([
        computation.x,
        computation.y,
        computation.result,
    ]);

    // Check if the proof is valid
    proof.1 == hash
}

// Define the main function
fn main() {
    // Create a computation
    let computation = Computation {
        x: 2,
        y: 3,
        result: 5,
    };

    // Generate a proof
    let proof = generate_proof(computation);

    // Verify the proof
    let is_valid = verify_proof(proof, computation);

    // Assert that the proof is valid
    assert(is_valid);
}
```
