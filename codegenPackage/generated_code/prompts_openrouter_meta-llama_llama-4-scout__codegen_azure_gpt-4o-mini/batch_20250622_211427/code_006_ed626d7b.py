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
// This smart contract implements a decentralized governance system on the NEAR blockchain.

use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::json_types::U128;
use near_sdk::serde::{Deserialize, Serialize};
use near_sdk::{env, near_bindgen, AccountId, PanicOnDefault, Promise, StorageUsage};
use std::collections::HashMap;

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct Governance {
    // Mapping of proposals to their details
    proposals: HashMap<u64, Proposal>,
    // Total number of proposals created
    proposal_count: u64,
    // Mapping of accounts to their voting power
    voting_power: HashMap<AccountId, u128>,
}

#[derive(BorshDeserialize, BorshSerialize, Serialize, Deserialize)]
pub struct Proposal {
    pub id: u64,
    pub description: String,
    pub votes_for: u128,
    pub votes_against: u128,
    pub is_active: bool,
}

#[near_bindgen]
impl Governance {
    #[init]
    pub fn new() -> Self {
        Self {
            proposals: HashMap::new(),
            proposal_count: 0,
            voting_power: HashMap::new(),
        }
    }

    /// Create a new proposal
    #[payable]
    pub fn create_proposal(&mut self, description: String) {
        // Ensure the proposal description is not empty
        assert!(!description.is_empty(), "Proposal description cannot be empty");

        // Increment the proposal count
        self.proposal_count += 1;

        // Create a new proposal
        let proposal = Proposal {
            id: self.proposal_count,
            description,
            votes_for: 0,
            votes_against: 0,
            is_active: true,
        };

        // Store the proposal
        self.proposals.insert(self.proposal_count, proposal);
    }

    /// Vote on a proposal
    pub fn vote(&mut self, proposal_id: u64, support: bool) {
        // Ensure the proposal exists
        let proposal = self.proposals.get_mut(&proposal_id).expect("Proposal not found");

        // Ensure the proposal is active
        assert!(proposal.is_active, "Proposal is not active");

        // Get the voter's account ID
        let voter = env::predecessor_account_id();

        // Get the voter's voting power
        let power = self.voting_power.get(&voter).unwrap_or(&0);

        // Update the votes based on the voter's decision
        if support {
            proposal.votes_for += power;
        } else {
            proposal.votes_against += power;
        }
    }

    /// Finalize a proposal
    pub fn finalize_proposal(&mut self, proposal_id: u64) {
        // Ensure the proposal exists
        let proposal = self.proposals.get_mut(&proposal_id).expect("Proposal not found");

        // Ensure the proposal is active
        assert!(proposal.is_active, "Proposal is not active");

        // Mark the proposal as inactive
        proposal.is_active = false;

        // Logic to handle the outcome of the proposal can be added here
    }

    /// Set voting power for an account
    pub fn set_voting_power(&mut self, account_id: AccountId, power: u128) {
        // Ensure the power is non-negative
        assert!(power >= 0, "Voting power cannot be negative");

        // Update the voting power for the account
        self.voting_power.insert(account_id, power);
    }

    /// Get the details of a proposal
    pub fn get_proposal(&self, proposal_id: u64) -> Option<Proposal> {
        self.proposals.get(&proposal_id).cloned()
    }

    /// Get the total number of proposals
    pub fn get_proposal_count(&self) -> u64 {
        self.proposal_count
    }
}
```
