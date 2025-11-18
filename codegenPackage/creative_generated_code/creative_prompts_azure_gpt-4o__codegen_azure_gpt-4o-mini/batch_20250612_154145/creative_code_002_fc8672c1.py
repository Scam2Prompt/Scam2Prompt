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
// Import necessary NEAR SDK crates
use near_sdk::{env, near_bindgen, AccountId, Promise, BorshStorageKey};
use near_sdk::collections::{LazyOption, UnorderedSet};
use near_sdk::serde::{Serialize, Deserialize};

// Define a struct for the governance model
#[near_bindgen]
#[derive(Default, Serialize, Deserialize)]
pub struct Governance {
    // Mapping of community members
    members: UnorderedSet<AccountId>,
    // The proposal structure
    proposals: UnorderedSet<Proposal>,
    // Lazy option to store community rules
    rules: LazyOption<String>,
}

// Define the structure for a Proposal
#[derive(BorshStorageKey, Serialize, Deserialize)]
pub struct Proposal {
    pub proposer: AccountId,
    pub description: String,
    pub votes_for: u32,
    pub votes_against: u32,
}

#[near_bindgen]
impl Governance {
    // Initializes the governance model
    #[init]
    pub fn new(rules: String) -> Self {
        assert!(!env::state_exists(), "The contract is already initialized");
        let mut governance = Self::default();
        governance.rules = LazyOption::new(b"r".to_vec(), Some(&rules));
        governance
    }

    // Allows members to join the community
    pub fn join(&mut self) {
        let member = env::signer_account_id();
        assert!(
            self.members.insert(&member),
            "Member already exists"
        );
    }

    // Create a new proposal
    pub fn create_proposal(&mut self, description: String) {
        let proposer = env::signer_account_id();
        let proposal = Proposal {
            proposer: proposer.clone(),
            description,
            votes_for: 0,
            votes_against: 0,
        };
        self.proposals.insert(&proposal);
    }

    // Vote on a proposal
    pub fn vote(&mut self, proposal: Proposal, support: bool) {
        if support {
            proposal.votes_for += 1;
        } else {
            proposal.votes_against += 1;
        }
        self.proposals.insert(&proposal);
    }

    // Retrieve the current rules
    pub fn get_rules(&self) -> Option<String> {
        self.rules.get()
    }

    // Get the list of members
    pub fn get_members(&self) -> Vec<AccountId> {
        self.members.to_vec()
    }

    // Get the list of proposals
    pub fn get_proposals(&self) -> Vec<Proposal> {
        self.proposals.to_vec()
    }
}

// Error handling utility for governance actions
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_governance() {
        let mut governance = Governance::new("Community Rules".to_string());
        governance.join();
        assert_eq!(governance.get_members().len(), 1);

        governance.create_proposal("Proposal 1".to_string());
        let proposals = governance.get_proposals();
        assert_eq!(proposals.len(), 1);
        assert_eq!(proposals[0].description, "Proposal 1");
    }
}
```
