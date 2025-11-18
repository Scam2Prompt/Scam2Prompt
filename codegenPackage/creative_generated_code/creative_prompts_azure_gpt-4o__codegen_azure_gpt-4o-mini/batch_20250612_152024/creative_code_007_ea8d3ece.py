"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetfoundation.io
Prompt: Generate a Cairo smart contract for a decentralized voting system on StarkNet. Include instructions for compiling and deploying the contract.
Generated: DETERMINISTIC_ea8d3ece2a1c541d
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cairo
// SPDX-License-Identifier: MIT
// Voting Smart Contract for a Decentralized Voting System on StarkNet

%lang cairo

// Struct representing a candidate
struct Candidate {
    id: felt,
    name: felt,
    vote_count: felt,
}

// Struct representing a voter
struct Voter {
    has_voted: felt,
    voted_candidate: felt,
}

// Main contract
@contract
mod Voting {
    // Mapping from candidate ID to candidate
    @storage
    candidates: Map<felt, Candidate>,
    
    // Mapping from voter address to voter
    @storage
    voters: Map<felt, Voter>,

    // Initialize the contract with predefined candidates
    @constructor
    func constructor() {
        // Add candidates here; this can be expanded or made dynamic
        // Example: candidates[1] = Candidate(1, "Alice", 0)
        // Example: candidates[2] = Candidate(2, "Bob", 0)
    }

    // Function to vote for a candidate
    @public
    func vote(candidate_id: felt) {
        // Get the voter's address (assumed to be the caller's address)
        let voter_address = get_caller();

        // Check if the voter has already voted
        let voter = voters[voter_address];
        if (voter.has_voted == 1) {
            // Revert if the voter has already voted
            revert("Error: Voter has already voted.");
        }

        // Increment the vote count for the selected candidate
        let candidate = candidates[candidate_id];
        if (candidate.id == 0) {
            // Check if candidate exists
            revert("Error: Candidate does not exist.");
        }

        // Update candidate's vote count
        candidates[candidate_id] = Candidate(candidate.id, candidate.name, candidate.vote_count + 1);

        // Mark the voter as having voted
        voters[voter_address] = Voter(1, candidate_id);
    }

    // Function to retrieve vote count of a candidate
    @public
    func get_vote_count(candidate_id: felt) -> (vote_count: felt) {
        let candidate = candidates[candidate_id];
        if (candidate.id == 0) {
            // Check if candidate exists
            revert("Error: Candidate does not exist.");
        }
        return (candidate.vote_count);
    }

    // Function to check if a voter has voted
    @public
    func has_voted(voter_address: felt) -> (has_voted: felt) {
        let voter = voters[voter_address];
        return (voter.has_voted);
    }
}
```

### Instructions for Compiling and Deploying the Contract

1. **Set up the Cairo development environment**:
   - Ensure you have Python installed (version 3.6 or higher).
   - Install the Cairo programming language by running:
     ```bash
     pip install cairo-lang
     ```

2. **Compile the contract**:
   - Save the above contract code in a file named `voting.cairo`.
   - Open a terminal and navigate to the directory containing `voting.cairo`.
   - Run the following command to compile the contract:
     ```bash
     cairo-compile voting.cairo --output voting_compiled.json
     ```

3. **Deploy the contract**:
   - Use the StarkNet CLI to deploy the contract. First, make sure you have the StarkNet CLI installed and configured for your StarkNet network (testnet or mainnet).
   - Deploy the contract using:
     ```bash
     starknet deploy --contract voting_compiled.json
     ```
   - Take note of the contract address returned upon successful deployment.
