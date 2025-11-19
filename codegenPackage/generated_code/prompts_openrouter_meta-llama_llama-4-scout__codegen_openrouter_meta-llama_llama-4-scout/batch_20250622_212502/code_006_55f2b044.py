"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Describe how Polkadot's governance model enables token holders to participate in decision-making, and propose a code implementation for on-chain governance.
Generated: DETERMINISTIC_55f2b044ec60b27d
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries
use std::collections::HashMap;
use std::error::Error;
use std::fmt;

// Define custom errors
#[derive(Debug)]
enum GovernanceError {
    InvalidProposal,
    InsufficientVotes,
    VotingPeriodNotStarted,
    ProposalAlreadyExists,
}

impl fmt::Display for GovernanceError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            GovernanceError::InvalidProposal => write!(f, "Invalid proposal"),
            GovernanceError::InsufficientVotes => write!(f, "Insufficient votes"),
            GovernanceError::VotingPeriodNotStarted => write!(f, "Voting period not started"),
            GovernanceError::ProposalAlreadyExists => write!(f, "Proposal already exists"),
        }
    }
}

impl Error for GovernanceError {}

// Define a struct to represent a proposal
#[derive(Debug)]
struct Proposal {
    id: u64,
    description: String,
    votes: HashMap<bool, u64>, // true for yes, false for no
}

// Define a struct to represent the governance system
#[derive(Debug)]
struct Governance {
    proposals: HashMap<u64, Proposal>,
    voting_period: u64,
    token_supply: u64,
}

impl Governance {
    // Create a new governance system
    fn new(voting_period: u64, token_supply: u64) -> Governance {
        Governance {
            proposals: HashMap::new(),
            voting_period,
            token_supply,
        }
    }

    // Submit a new proposal
    fn submit_proposal(&mut self, id: u64, description: String) -> Result<(), GovernanceError> {
        if self.proposals.contains_key(&id) {
            return Err(GovernanceError::ProposalAlreadyExists);
        }
        self.proposals.insert(id, Proposal {
            id,
            description,
            votes: HashMap::from([(true, 0), (false, 0)]),
        });
        Ok(())
    }

    // Cast a vote on a proposal
    fn cast_vote(&mut self, id: u64, voter: bool) -> Result<(), GovernanceError> {
        if let Some(proposal) = self.proposals.get_mut(&id) {
            *proposal.votes.get_mut(&voter).unwrap() += 1;
            Ok(())
        } else {
            Err(GovernanceError::InvalidProposal)
        }
    }

    // Check if a proposal has passed
    fn has_passed(&self, id: u64) -> Result<bool, GovernanceError> {
        if let Some(proposal) = self.proposals.get(&id) {
            let yes_votes = *proposal.votes.get(&true).unwrap();
            let total_votes = proposal.votes.values().sum::<u64>();
            if total_votes < self.token_supply * self.voting_period {
                return Err(GovernanceError::VotingPeriodNotStarted);
            }
            Ok(yes_votes > total_votes / 2)
        } else {
            Err(GovernanceError::InvalidProposal)
        }
    }
}

fn main() -> Result<(), GovernanceError> {
    let mut governance = Governance::new(10, 100);
    governance.submit_proposal(1, "Test proposal".to_string())?;
    governance.cast_vote(1, true)?;
    governance.cast_vote(1, false)?;
    println!("Has proposal 1 passed? {}", governance.has_passed(1)?);
    Ok(())
}
```
