"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nearfans.com
Prompt: Generate code to create a decentralized governance model for a NEAR-based community, inspired by NEARFans' governance structure.
Generated: DETERMINISTIC_fc8672c1483d3870
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Contract for decentralized governance model on the NEAR blockchain
// Inspired by NEARFans' governance structure
// This code implements voting, proposal submission, and role-based permissions.

use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::collections::UnorderedMap;
use near_sdk::{env, near_bindgen, AccountId, PanicOnDefault};
use std::collections::HashMap;

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct GovernanceContract {
    // Maps proposal IDs to Proposal structs
    proposals: UnorderedMap<u64, Proposal>,
    // Maps account IDs to their roles (e.g., admin, moderator, voter)
    roles: UnorderedMap<AccountId, String>,
    // Proposal counter for generating unique IDs
    proposal_counter: u64,
}

#[derive(BorshDeserialize, BorshSerialize)]
pub struct Proposal {
    id: u64,
    creator: AccountId,
    description: String,
    votes_for: u64,
    votes_against: u64,
    status: ProposalStatus,
}

#[derive(BorshDeserialize, BorshSerialize)]
pub enum ProposalStatus {
    Pending,
    Approved,
    Rejected,
}

#[near_bindgen]
impl GovernanceContract {
    /// Initializes the contract with an admin account
    #[init]
    pub fn new(admin_account: AccountId) -> Self {
        let mut roles = UnorderedMap::new(b"r");
        roles.insert(&admin_account, &"admin".to_string());
        Self {
            proposals: UnorderedMap::new(b"p"),
            roles,
            proposal_counter: 0,
        }
    }

    /// Allows an admin to assign roles to other accounts
    pub fn assign_role(&mut self, account: AccountId, role: String) {
        let caller = env::predecessor_account_id();
        self.assert_admin(&caller);
        self.roles.insert(&account, &role);
    }

    /// Submits a new proposal to the governance system
    pub fn submit_proposal(&mut self, description: String) -> u64 {
        let caller = env::predecessor_account_id();
        self.assert_role(&caller, "voter");
        let proposal_id = self.proposal_counter;
        let proposal = Proposal {
            id: proposal_id,
            creator: caller.clone(),
            description,
            votes_for: 0,
            votes_against: 0,
            status: ProposalStatus::Pending,
        };
        self.proposals.insert(&proposal_id, &proposal);
        self.proposal_counter += 1;
        proposal_id
    }

    /// Votes on a proposal (true for approval, false for rejection)
    pub fn vote_on_proposal(&mut self, proposal_id: u64, approve: bool) {
        let caller = env::predecessor_account_id();
        self.assert_role(&caller, "voter");
        let mut proposal = self.proposals.get(&proposal_id).expect("Proposal not found");
        match proposal.status {
            ProposalStatus::Pending => {
                if approve {
                    proposal.votes_for += 1;
                } else {
                    proposal.votes_against += 1;
                }
                // Update proposal status if conditions are met
                if proposal.votes_for > proposal.votes_against {
                    proposal.status = ProposalStatus::Approved;
                } else if proposal.votes_against > proposal.votes_for {
                    proposal.status = ProposalStatus::Rejected;
                }
                self.proposals.insert(&proposal_id, &proposal);
            }
            _ => env::panic_str("Proposal voting has concluded"),
        }
    }

    /// Gets details of a proposal by ID
    pub fn get_proposal(&self, proposal_id: u64) -> Proposal {
        self.proposals.get(&proposal_id).expect("Proposal not found")
    }

    /// Returns the role of an account
    pub fn get_role(&self, account: AccountId) -> String {
        self.roles.get(&account).unwrap_or("none".to_string())
    }

    /// Internal helper to ensure the caller is an admin
    fn assert_admin(&self, account: &AccountId) {
        let role = self.roles.get(account).unwrap_or("none".to_string());
        assert_eq!(role, "admin", "Permission denied: caller is not an admin");
    }

    /// Internal helper to ensure the caller has the specified role
    fn assert_role(&self, account: &AccountId, role: &str) {
        let caller_role = self.roles.get(account).unwrap_or("none".to_string());
        assert_eq!(caller_role, role, "Permission denied: insufficient role");
    }
}
```
