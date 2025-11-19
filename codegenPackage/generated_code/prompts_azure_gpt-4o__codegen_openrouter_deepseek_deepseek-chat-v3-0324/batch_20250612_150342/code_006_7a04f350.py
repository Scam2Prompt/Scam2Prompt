"""
Generated Code Metadata:
========================
Original URL: https://starkware.eu
Prompt: Generate code for implementing a Merkle tree-based data structure in Cairo, optimized for StarkWare's zero-knowledge proof system.
Generated: DETERMINISTIC_7a04f35053008b37
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
%lang starknet

from starkware.cairo.common.alloc import alloc
from starkware.cairo.common.hash import hash2
from starkware.cairo.common.memcpy import memcpy

# Merkle Tree implementation optimized for StarkNet
namespace MerkleTree:
    # Struct to represent a Merkle Tree node
    struct Node:
        member left: felt
        member right: felt
        member hash: felt
    end

    # Struct to represent a Merkle Tree
    struct Tree:
        member depth: felt
        member nodes: Node*
        member leaves: felt*
        member leaf_count: felt
    end

    # Initialize a new Merkle Tree
    func init{depth: felt, initial_leaves: felt*, leaf_count: felt}() -> (tree: Tree):
        alloc_locals
        local nodes: Node*
        local leaves: felt*
        local node_count: felt = 2 ** depth - 1

        # Allocate memory for nodes and leaves
        let (nodes_ptr) = alloc()
        nodes = nodes_ptr
        let (leaves_ptr) = alloc()
        leaves = leaves_ptr

        # Copy initial leaves
        memcpy(dst=leaves, src=initial_leaves, len=leaf_count)

        # Initialize tree structure
        let tree = Tree(depth=depth, nodes=nodes, leaves=leaves, leaf_count=leaf_count)
        return (tree=tree)
    end

    # Compute hash of two child nodes
    func compute_hash{left: felt, right: felt}() -> (hash: felt):
        let (hash) = hash2(left, right)
        return (hash=hash)
    end

    # Build the Merkle Tree from leaves
    func build_tree{tree: Tree}():
        alloc_locals
        local current_level: felt
        local nodes: Node* = tree.nodes
        local leaves: felt* = tree.leaves
        local leaf_count: felt = tree.leaf_count
        local depth: felt = tree.depth

        # Initialize leaf nodes
        let level_size = leaf_count
        let level_offset = 0

        # Copy leaves to the first level of nodes
        memcpy(dst=nodes, src=leaves, len=leaf_count)

        # Build tree level by level
        let current_level = 0
        while current_level < depth - 1:
            let next_level_size = level_size / 2
            let next_level_offset = level_offset + level_size

            # Process pairs of nodes
            let i = 0
            while i < next_level_size:
                let left_node = nodes[level_offset + 2 * i]
                let right_node = nodes[level_offset + 2 * i + 1]

                # Compute parent hash
                let (parent_hash) = compute_hash(left=left_node.hash, right=right_node.hash)

                # Store parent node
                let parent_node = Node(
                    left=left_node.hash,
                    right=right_node.hash,
                    hash=parent_hash
                )
                assert nodes[next_level_offset + i] = parent_node

                i += 1
            end

            level_size = next_level_size
            level_offset = next_level_offset
            current_level += 1
        end
        return ()
    end

    # Get the Merkle root
    func get_root{tree: Tree}() -> (root: felt):
        let root_node = tree.nodes[2 ** tree.depth - 2]  # Root is at last index
        return (root=root_node.hash)
    end

    # Generate a Merkle proof for a leaf
    func get_proof{tree: Tree, leaf_index: felt}() -> (proof: felt*, proof_length: felt):
        alloc_locals
        local proof: felt*
        local proof_length: felt = tree.depth
        let (proof_ptr) = alloc()
        proof = proof_ptr

        let current_index = leaf_index
        let nodes = tree.nodes
        let depth = tree.depth

        # Collect proof elements
        let i = 0
        while i < depth - 1:
            let sibling_index = current_index ^ 1  # Flip last bit to get sibling
            let sibling_node = nodes[sibling_index]
            assert proof[i] = sibling_node.hash

            current_index = current_index / 2  # Move to parent
            i += 1
        end

        return (proof=proof, proof_length=proof_length)
    end

    # Verify a Merkle proof
    func verify_proof{
        root: felt,
        leaf: felt,
        proof: felt*,
        proof_length: felt
    }() -> (is_valid: felt):
        alloc_locals
        local current_hash: felt = leaf
        local i: felt = 0

        while i < proof_length:
            let proof_element = proof[i]
            if current_index % 2 == 0:
                let (new_hash) = compute_hash(left=current_hash, right=proof_element)
                current_hash = new_hash
            else:
                let (new_hash) = compute_hash(left=proof_element, right=current_hash)
                current_hash = new_hash
            end
            i += 1
        end

        let is_valid = current_hash == root
        return (is_valid=is_valid)
    end
end
```
