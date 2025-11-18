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

```python
# File: merkle_tree.cairo
# Purpose: Implementation of a Merkle Tree data structure in Cairo, optimized for StarkWare's zero-knowledge proof system.

from starkware.cairo.common.hash2 import hash2

# Constants
# MAX_LEAVES defines the maximum number of leaves permissible in the Merkle tree.
# Adjust this value based on application-specific requirements.
const MAX_LEAVES = 1024

@contract
namespace MerkleTree:
    # Define the storage for the Merkle Tree.
    @storage_var
    func leaf(index: felt) -> felt {}

    @storage_var
    func node(level: felt, index: felt) -> felt {}

    @view
    func get_leaf(index: felt) -> felt {
        return leaf.read(index=index);
    }

    @view
    func get_node(level: felt, index: felt) -> felt {
        return node.read(level=level, index=index);
    }

    # Function to compute the hash of two felt values.
    @pure
    func compute_hash(value1: felt, value2: felt) -> felt {
        # Use the Cairo native hash2 function for hash computation.
        return hash2(value1, value2);
    }

    # Function to set a leaf in the Merkle tree.
    @external
    func set_leaf(index: felt, value: felt) {
        assert(index < MAX_LEAVES, 'Index exceeds MAX_LEAVES.');
        leaf.write(index=index, value=value);
    }

    # Function to build a Merkle Tree from given leaves.
    @external
    func build_tree(num_leaves: felt) {
        assert(num_leaves <= MAX_LEAVES, 'Number of leaves exceeds MAX_LEAVES.');

        let n_levels = log2(MAX_LEAVES);  # Compute the number of levels in the tree.

        # Build each level of the tree.
        for level in range(0, n_levels):
            let nodes_in_level = MAX_LEAVES / (2 ** level);
            for index in range(0, nodes_in_level / 2):
                # Compute the hash of two child nodes.
                let left_child = if level == 0 { leaf.read(index=2 * index) } else { node.read(level=level - 1, index=2 * index) };
                let right_child = if level == 0 { leaf.read(index=2 * index + 1) } else { node.read(level=level - 1, index=2 * index + 1) };

                let parent_hash = compute_hash(value1=left_child, value2=right_child);
                node.write(level=level, index=index, value=parent_hash);
            end;
        end;
    }

    # Function to compute the Merkle root.
    @view
    func get_root() -> felt {
        let n_levels = log2(MAX_LEAVES);

        # The root is the only node at the highest level.
        return node.read(level=n_levels - 1, index=0);
    }

    # Function to generate a Merkle proof for a leaf.
    @view
    func generate_proof(leaf_index: felt) -> (proof: felt*) {
        assert(leaf_index < MAX_LEAVES, 'Leaf index exceeds MAX_LEAVES.');

        let n_levels = log2(MAX_LEAVES);
        let proof = alloc_array(n_levels);

        let index = leaf_index;
        for level in range(0, n_levels):
            let sibling_index = if index % 2 == 0 { index + 1 } else { index - 1 };
            proof[level] = if level == 0 { leaf.read(index=sibling_index) } else { node.read(level=level - 1, index=sibling_index) };
            index = index // 2;
        end;

        return proof;
    }

    # Function to verify a Merkle proof.
    @view
    func verify_proof(root: felt, leaf: felt, proof: felt*) -> felt {
        let computed_hash = leaf;

        for sibling_hash in proof {
            computed_hash = if computed_hash < sibling_hash {
                compute_hash(value1=computed_hash, value2=sibling_hash);
            } else {
                compute_hash(value1=sibling_hash, value2=computed_hash);
            };
        end;

        return computed_hash == root;
    }
end
```
