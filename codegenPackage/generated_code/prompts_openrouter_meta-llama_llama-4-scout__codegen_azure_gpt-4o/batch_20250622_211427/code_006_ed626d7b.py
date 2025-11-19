"""
Generated Code Metadata:
========================
Original URL: https://nearfans.com
Prompt: Generate a smart contract code for a NEAR-based project that utilizes decentralized governance and open-source principles.
Generated: DETERMINISTIC_ed626d7bc9b9fee5
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Decentralized Governance on NEAR Protocol
// Author: [Your Name]
// Description: This contract enables decentralized governance for a NEAR-based project.
// Version: 1.0.0

// Import necessary modules from the NEAR SDK
use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::collections::UnorderedMap;
use near_sdk::{env, near_bindgen, AccountId, PanicOnDefault};

// Define the structure of the smart contract
#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct GovernanceContract {
    // Mapping of proposals to their details
    proposals: UnorderedMap<u64, Proposal>,
    // Mapping of votes for each proposal
    votes: UnorderedMap<u64, UnorderedMap<AccountId, bool>>,
    // Counter for proposal IDs
    proposal_counter: u64,
}

// Structure to represent a proposal
#[derive(BorshDeserialize, BorshSerialize)]
pub struct Proposal {
    title: String,
    description: String,
    proposer: AccountId,
    vote_count: u64,
    approved: bool,
}

// Implementation of the smart contract
#[near_bindgen]
impl GovernanceContract {
    // Initialize the contract
    #[init]
    pub fn new() -> Self {
        Self {
            proposals: UnorderedMap::new(b"p".to_vec()),
            votes: UnorderedMap::new(b"v".to_vec()),
            proposal_counter: 0,
        }
    }

    // Function to create a new proposal
    pub fn create_proposal(&mut self, title: String, description: String) {
        let proposer = env::predecessor_account_id();
        let proposal_id = self.proposal_counter;

        let proposal = Proposal {
            title,
            description,
            proposer,
            vote_count: 0,
            approved: false,
        };

        self.proposals.insert(&proposal_id, &proposal);
        self.proposal_counter += 1;

        env::log_str(&format!("Proposal {} created by {}", proposal_id, proposer));
    }

    // Function to vote on a proposal
    pub fn vote(&mut self, proposal_id: u64, approve: bool) {
        let voter = env::predecessor_account_id();

        // Ensure the proposal exists
        let mut proposal = self.proposals.get(&proposal_id).expect("Proposal not found");

        // Check if the voter has already voted
        let mut proposal_votes = self.votes.get(&proposal_id).unwrap_or_else(|| UnorderedMap::new(b"v".to_vec()));
        if proposal_votes.get(&voter).is_some() {
            env::panic_str("You have already voted on this proposal");
        }

        // Record the vote
        proposal_votes.insert(&voter, &approve);
        self.votes.insert(&proposal_id, &proposal_votes);

        // Update vote count and approval status
        if approve {
            proposal.vote_count += 1;
        }
        proposal.approved = proposal.vote_count > 0; // Example condition for approval

        self.proposals.insert(&proposal_id, &proposal);

        env::log_str(&format!("Vote recorded for proposal {} by {}", proposal_id, voter));
    }

    // Function to get details of a proposal
    pub fn get_proposal(&self, proposal_id: u64) -> Proposal {
        self.proposals.get(&proposal_id).expect("Proposal not found")
    }

    // Function to list all proposals
    pub fn list_proposals(&self) -> Vec<(u64, Proposal)> {
        self.proposals.iter().collect()
    }
}

// Unit tests for the contract
#[cfg(test)]
mod tests {
    use super::*;
    use near_sdk::test_utils::VMContextBuilder;
    use near_sdk::{testing_env, AccountId};

    fn get_context(predecessor: AccountId) -> VMContextBuilder {
        let mut builder = VMContextBuilder::new();
        builder.predecessor_account_id(predecessor);
        builder
    }

    #[test]
    fn test_create_proposal() {
        let context = get_context("alice.testnet".to_string());
        testing_env!(context.build());

        let mut contract = GovernanceContract::new();
        contract.create_proposal("Test Proposal".to_string(), "This is a test".to_string());

        let proposal = contract.get_proposal(0);
        assert_eq!(proposal.title, "Test Proposal");
        assert_eq!(proposal.description, "This is a test");
        assert_eq!(proposal.proposer, "alice.testnet".to_string());
    }

    #[test]
    fn test_vote() {
        let context = get_context("alice.testnet".to_string());
        testing_env!(context.build());

        let mut contract = GovernanceContract::new();
        contract.create_proposal("Test Proposal".to_string(), "This is a test".to_string());
        contract.vote(0, true);

        let proposal = contract.get_proposal(0);
        assert_eq!(proposal.vote_count, 1);
        assert!(proposal.approved);
    }
}
```
