"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.eu
Prompt: Generate code for implementing a Merkle tree-based data structure in Cairo, optimized for StarkWare's zero-knowledge proof system.
Generated: DETERMINISTIC_7a04f35053008b37
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cairo
# Merkle Tree implementation in Cairo for StarkWare's zero-knowledge proof system

# Import necessary libraries
from starkware.cairo.common.hash import pedersen_hash
from starkware.cairo.common.serialize import serialize

# Merkle Tree Node structure
struct Node:
    value: felt  # Hash of the node
    left: felt  # Left child
    right: felt  # Right child

# Merkle Tree class
@external
func create_merkle_tree(data: felt*) -> felt:
    # Constructs a Merkle tree from the provided data
    alloc_locals
    let (n) = array_len(data)

    # Base case for an empty input
    if n == 0:
        return 0  # Return 0 if no data is provided

    # Create leaf nodes and hash them
    local leaf_hashes: felt* = alloc()
    
    for i in range(n):
        let hash_value = pedersen_hash(data[i], 0)  # Hash the leaf data
        leaf_hashes[i] = hash_value

    # Build the Merkle tree
    let tree_root = build_tree(leaf_hashes, n)
    return tree_root

# Recursive function to build the Merkle tree
func build_tree(leaf_hashes: felt*, n: felt) -> felt:
    # Base case for a single leaf
    if n == 1:
        return leaf_hashes[0]

    # Allocate memory for the parent nodes
    local parent_hashes: felt* = alloc()
    local parent_count = (n + 1) // 2  # Calculate number of parent nodes

    for i in range(parent_count):
        # Hashing two child nodes or a single child with zero if odd
        let left_child = leaf_hashes[i * 2]
        let right_child = if (i * 2 + 1 < n) { leaf_hashes[i * 2 + 1] } else { 0 }
        let parent_hash = pedersen_hash(left_child, right_child)
        parent_hashes[i] = parent_hash

    # Recursively build the next level of the tree
    return build_tree(parent_hashes, parent_count)

# Function to generate a Merkle proof
@external
func generate_proof(data: felt*, index: felt) -> felt*:
    # Generates a Merkle proof for a specific index in the input data
    alloc_locals
    let (n) = array_len(data)

    # Verify index is within bounds
    if index >= n:
        return 0  # Return error code for out of bounds

    local proof: felt* = alloc()
    let mut current_index = index

    # Construct the proof by traversing the tree
    while n > 1:
        let sibling_index = if (current_index % 2 == 0) { current_index + 1 } else { current_index - 1 }
        if sibling_index < n:
            proof = array_append(proof, pedersen_hash(data[sibling_index], 0))
        current_index //= 2
        n = (n + 1) // 2  # Update the number of nodes at the next level

    return proof

# Function to verify a Merkle proof
@external
func verify_proof(root: felt, proof: felt*, leaf: felt, index: felt) -> felt:
    # Verify if a leaf node is part of the Merkle tree
    alloc_locals
    let mut computed_hash = pedersen_hash(leaf, 0)
    
    let (proof_length) = array_len(proof)
    
    for i in range(proof_length):
        let sibling_hash = proof[i]
        computed_hash = if (index % 2 == 0) {
            pedersen_hash(computed_hash, sibling_hash)  # Combine with right sibling
        } else {
            pedersen_hash(sibling_hash, computed_hash)  # Combine with left sibling
        }
        index //= 2  # Move up the tree

    return computed_hash == root  # Return true if computed hash matches root
```
