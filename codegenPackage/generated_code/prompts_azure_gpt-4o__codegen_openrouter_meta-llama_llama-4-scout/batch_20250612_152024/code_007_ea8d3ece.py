"""
Generated Code Metadata:
========================
Original URL: https://starknetfoundation.io
Prompt: Generate a Cairo smart contract for a decentralized voting system on StarkNet. Include instructions for compiling and deploying the contract.
Generated: DETERMINISTIC_ea8d3ece2a1c541d
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Voting Contract**
```cairo
// SPDX-License-Identifier: MIT
// This contract implements a simple decentralized voting system on StarkNet.

%lang starknet

// Define the voting contract
contract Voting {
    // Mapping of voters to their voting status
    mapping voter_status { address: felt, status: felt }

    // Mapping of proposals to their vote counts
    mapping proposal_votes { proposal_id: felt, vote_count: felt }

    // Event emitted when a voter casts a vote
    event VoteCasted { 
        voter: felt, 
        proposal_id: felt, 
        vote: felt 
    }

    // Event emitted when a proposal is created
    event ProposalCreated { 
        proposal_id: felt, 
        description: felt 
    }

    // Function to create a new proposal
    func create_proposal(
        proposal_id: felt, 
        description: felt
    ) -> () {
        // Only allow the contract owner to create proposals
        assert_caller() == 0;

        // Initialize the proposal vote count to 0
        proposal_votes[proposal_id] = 0;

        // Emit a ProposalCreated event
        emit ProposalCreated { 
            proposal_id: proposal_id, 
            description: description 
        };
    }

    // Function to cast a vote on a proposal
    func cast_vote(
        proposal_id: felt, 
        vote: felt
    ) -> () {
        // Get the caller's address
        let caller = get_caller();

        // Check if the voter has already voted
        assert voter_status[caller].status == 0;

        // Update the voter's status to voted
        voter_status[caller] = (caller, 1);

        // Increment the proposal's vote count
        proposal_votes[proposal_id] += vote;

        // Emit a VoteCasted event
        emit VoteCasted { 
            voter: caller, 
            proposal_id: proposal_id, 
            vote: vote 
        };
    }

    // Function to get the vote count for a proposal
    func get_vote_count(
        proposal_id: felt
    ) -> felt {
        return proposal_votes[proposal_id];
    }
}
```

**Compiling and Deploying the Contract**

### Prerequisites

*   Install the StarkNet CLI tool: `pip install starknet-cli`
*   Set up a StarkNet account and obtain an API key

### Compile the Contract

```bash
starknet-compile Voting.cairo --output Voting.json
```

### Deploy the Contract

```bash
starknet deploy --contract Voting.json --account <your_account_address> --network <network_name>
```

### Verify the Deployment

```bash
starknet declare --contract Voting.json --account <your_account_address> --network <network_name>
```

Replace `<your_account_address>` and `<network_name>` with your actual StarkNet account address and network name.

**Interact with the Contract**

### Create a Proposal

```bash
starknet invoke --contract Voting --function create_proposal --inputs <proposal_id> <description> --account <your_account_address> --network <network_name>
```

### Cast a Vote

```bash
starknet invoke --contract Voting --function cast_vote --inputs <proposal_id> <vote> --account <your_account_address> --network <network_name>
```

### Get the Vote Count

```bash
starknet call --contract Voting --function get_vote_count --inputs <proposal_id> --network <network_name>
```
