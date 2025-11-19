"""
Generated Code Metadata:
========================
Original URL: https://nearfans.com
Prompt: Generate code to create a decentralized governance model for a NEAR-based community, inspired by NEARFans' governance structure.
Generated: DETERMINISTIC_fc8672c1483d3870
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import required libraries
use near_sdk::borsh::{BorshDeserialize, BorshSerialize};
use near_sdk::collections::{LazyMap, UnorderedMap};
use near_sdk::json_types::U128;
use near_sdk::{near_bindgen, AccountId, Balance, PanicOnDefault, Promise};

// Define the governance structure
#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct Governance {
    // Mapping of proposals to their votes
    pub proposals: LazyMap<u64, Proposal>,
    // Mapping of users to their voting power
    pub voting_power: UnorderedMap<AccountId, u64>,
    // Total voting power
    pub total_voting_power: u64,
    // Proposal counter
    pub proposal_counter: u64,
}

// Define a proposal
#[derive(BorshDeserialize, BorshSerialize)]
pub struct Proposal {
    // Proposal ID
    pub id: u64,
    // Proposal description
    pub description: String,
    // Yes votes
    pub yes_votes: u64,
    // No votes
    pub no_votes: u64,
    // Status of the proposal (pending, passed, failed)
    pub status: ProposalStatus,
}

// Define the status of a proposal
#[derive(BorshDeserialize, BorshSerialize)]
pub enum ProposalStatus {
    Pending,
    Passed,
    Failed,
}

// Implement the governance structure
impl Governance {
    // Initialize the governance structure
    #[init]
    pub fn new() -> Self {
        Self {
            proposals: LazyMap::new(),
            voting_power: UnorderedMap::new(),
            total_voting_power: 0,
            proposal_counter: 0,
        }
    }

    // Add a new user with voting power
    pub fn add_user(&mut self, user: AccountId, power: u64) {
        self.voting_power.insert(user, power);
        self.total_voting_power += power;
    }

    // Create a new proposal
    pub fn create_proposal(&mut self, description: String) -> u64 {
        let id = self.proposal_counter;
        self.proposal_counter += 1;
        self.proposals.insert(id, Proposal {
            id,
            description,
            yes_votes: 0,
            no_votes: 0,
            status: ProposalStatus::Pending,
        });
        id
    }

    // Vote on a proposal
    pub fn vote(&mut self, proposal_id: u64, user: AccountId, vote: bool) -> Result<(), String> {
        let proposal = self.proposals.get_mut(&proposal_id).ok_or("Proposal not found".to_string())?;
        let power = self.voting_power.get(&user).ok_or("User not found".to_string())?;
        if proposal.status != ProposalStatus::Pending {
            return Err("Proposal is not pending".to_string());
        }
        if vote {
            proposal.yes_votes += power;
        } else {
            proposal.no_votes += power;
        }
        // Check if proposal has passed or failed
        if proposal.yes_votes > self.total_voting_power / 2 {
            proposal.status = ProposalStatus::Passed;
        } else if proposal.no_votes > self.total_voting_power / 2 {
            proposal.status = ProposalStatus::Failed;
        }
        Ok(())
    }

    // Execute a proposal
    pub fn execute_proposal(&mut self, proposal_id: u64) -> Result<Promise, String> {
        let proposal = self.proposals.get_mut(&proposal_id).ok_or("Proposal not found".to_string())?;
        if proposal.status != ProposalStatus::Passed {
            return Err("Proposal has not passed".to_string());
        }
        // Execute the proposal (NEAR-specific logic here)
        // For example, transfer NEAR tokens
        Promise::new(proposal.description.clone())
    }
}
```
