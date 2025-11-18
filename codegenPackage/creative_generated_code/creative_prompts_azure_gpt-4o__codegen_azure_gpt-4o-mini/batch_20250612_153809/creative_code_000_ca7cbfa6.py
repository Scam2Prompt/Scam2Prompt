"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Write a Sui Move smart contract for a decentralized governance application that aligns with the Sui Foundation's suggested themes for developer grants.
Generated: DETERMINISTIC_ca7cbfa68d0c73e3
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
// Move smart contract for a decentralized governance application
// This contract allows stakeholders to create and vote on governance proposals.

// Import necessary modules
module Governance {
    // Define the structure of a governance proposal
    struct Proposal has key {
        creator: address,
        description: vector<u8>,
        votes_for: u64,
        votes_against: u64,
        is_active: bool,
        voters: vector<address>,
    }

    // Store the proposals in a vector
    resource struct GovernanceResource {
        proposals: vector<Proposal>,
    }

    public fun initialize_resources(account: &signer) {
        // Initialize governance resource
        move_to(account, GovernanceResource { proposals: vector::empty<Proposal>() });
    }

    // Create a new proposal
    public fun create_proposal(account: &signer, description: vector<u8>) {
        let governance_resource = borrow_global_mut<GovernanceResource>(signer::address_of(account));
        let new_proposal = Proposal {
            creator: signer::address_of(account),
            description: description,
            votes_for: 0,
            votes_against: 0,
            is_active: true,
            voters: vector::empty<address>(),
        };
        vector::push_back(&mut governance_resource.proposals, new_proposal);
    }

    // Vote on a proposal
    public fun vote(account: &signer, proposal_index: u64, vote_for: bool) {
        let governance_resource = borrow_global_mut<GovernanceResource>(signer::address_of(account));
        
        // Check if the proposal index is valid
        assert!(proposal_index < vector::length(&governance_resource.proposals), 0);
        
        // Fetch the proposal and check voting eligibility
        let proposal = &mut vector::borrow_mut(&mut governance_resource.proposals, proposal_index);
        assert!(proposal.is_active, 1); // Ensure the proposal is active
        let voter_address = signer::address_of(account);
        
        // Check if the voter has already voted
        if (vector::contains(&proposal.voters, voter_address)) {
            abort(2); // Voter has already voted
        }
        
        // Record the vote
        vector::push_back(&mut proposal.voters, voter_address);
        if (vote_for) {
            proposal.votes_for += 1;
        } else {
            proposal.votes_against += 1;
        }
    }

    // Close the proposal
    public fun close_proposal(account: &signer, proposal_index: u64) {
        let governance_resource = borrow_global_mut<GovernanceResource>(signer::address_of(account));
        
        // Validate proposal index
        assert!(proposal_index < vector::length(&governance_resource.proposals), 0);
        
        let proposal = &mut vector::borrow_mut(&mut governance_resource.proposals, proposal_index);
        assert!(proposal.creator == signer::address_of(account), 3); // Only the creator can close the proposal
        proposal.is_active = false;
    }

    // Get proposal details
    public fun get_proposal_details(proposal_index: u64): Proposal {
        let governance_resource = borrow_global<GovernanceResource>(signer::address_of(account));
        
        // Validate proposal index
        assert!(proposal_index < vector::length(&governance_resource.proposals), 0);
        
        return vector::borrow(&governance_resource.proposals, proposal_index);
    }
}
```
