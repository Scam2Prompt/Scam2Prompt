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

```cairo
// Merkle Tree implementation in Cairo

// Import necessary libraries
use starknet::core::types::felt::Felt;
use starknet::core::types::hash::pedersen::PedersenHash;

// Define the Merkle Tree struct
struct MerkleTree {
    leaves: Array<Felt>,
    layers: Array<Array<Felt>>,
}

// Implement the Merkle Tree
impl MerkleTree {
    // Initialize a new Merkle Tree with given leaves
    fn new(leaves: Array<Felt>) -> Self {
        // Calculate the number of layers required
        let mut num_layers = 0;
        let mut n = leaves.len();
        while n > 1 {
            n = (n + 1) / 2;
            num_layers += 1;
        }

        // Initialize the layers array
        let mut layers = Array::new(num_layers + 1);
        layers[0] = leaves;

        // Compute the Merkle tree layers
        for i in 1..=num_layers {
            let mut layer = Array::new(layers[i - 1].len() / 2);
            for j in 0..layer.len() {
                let left = layers[i - 1][j * 2];
                let right = if j * 2 + 1 < layers[i - 1].len() {
                    layers[i - 1][j * 2 + 1]
                } else {
                    layers[i - 1][j * 2]
                };
                layer[j] = PedersenHash::hash(left, right);
            }
            layers[i] = layer;
        }

        MerkleTree { leaves, layers }
    }

    // Get the Merkle root
    fn get_root(&self) -> Felt {
        *self.layers[self.layers.len() - 1][0]
    }

    // Get the Merkle proof for a given leaf
    fn get_proof(&self, index: usize) -> Array<Felt> {
        let mut proof = Array::new(self.layers.len() - 1);
        let mut idx = index;
        for i in 0..self.layers.len() - 1 {
            let sibling_idx = if idx % 2 == 0 { idx + 1 } else { idx - 1 };
            if sibling_idx < self.layers[i].len() {
                proof[i] = self.layers[i][sibling_idx];
            } else {
                proof[i] = self.layers[i][idx];
            }
            idx = idx / 2;
        }
        proof
    }

    // Verify a Merkle proof
    fn verify_proof(&self, leaf: Felt, proof: Array<Felt>, root: Felt) -> bool {
        let mut hash = leaf;
        for i in 0..proof.len() {
            let sibling = proof[i];
            hash = PedersenHash::hash(hash, sibling);
        }
        hash == root
    }
}

// Example usage
fn main() {
    // Create a new Merkle Tree
    let leaves = Array::new(4);
    leaves[0] = Felt::from(1);
    leaves[1] = Felt::from(2);
    leaves[2] = Felt::from(3);
    leaves[3] = Felt::from(4);
    let tree = MerkleTree::new(leaves);

    // Get the Merkle root
    let root = tree.get_root();

    // Get the Merkle proof for a leaf
    let proof = tree.get_proof(0);

    // Verify the Merkle proof
    let verified = tree.verify_proof(Felt::from(1), proof, root);

    // Assert that the proof is valid
    assert(verified);
}
```
