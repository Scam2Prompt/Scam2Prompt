"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solananpcs.pages.dev
Prompt: Write a Solana-based smart contract for the $NPCS token that includes governance voting functionality for token holders, referencing the contract address `5ToDNkiBAK6k697RRyngTburU7yZNFZFx7jzsD1Uc7pK`.
Generated: DETERMINISTIC_09e3e09ca51f0b64
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;
use std::collections::HashMap;

// Define the program ID
declare_id!("5ToDNkiBAK6k697RRyngTburU7yZNFZFx7jzsD1Uc7pK");

#[program]
pub mod governance {
    use super::*;

    // Initialize the governance contract
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let governance_account = &mut ctx.accounts.governance;
        governance_account.votes = HashMap::new();
        governance_account.proposals = Vec::new();
        Ok(())
    }

    // Create a new proposal
    pub fn create_proposal(ctx: Context<CreateProposal>, title: String, description: String) -> Result<()> {
        let governance_account = &mut ctx.accounts.governance;
        let proposal = Proposal {
            title,
            description,
            votes: HashMap::new(),
            total_votes: 0,
        };
        governance_account.proposals.push(proposal);
        Ok(())
    }

    // Vote on a proposal
    pub fn vote(ctx: Context<Vote>, proposal_index: usize, vote_value: bool) -> Result<()> {
        let governance_account = &mut ctx.accounts.governance;
        let voter = &ctx.accounts.voter.key();
        
        // Ensure the proposal exists
        if proposal_index >= governance_account.proposals.len() {
            return Err(ErrorCode::ProposalNotFound.into());
        }

        let proposal = &mut governance_account.proposals[proposal_index];

        // Check if the voter has already voted on this proposal
        if proposal.votes.contains_key(voter) {
            return Err(ErrorCode::AlreadyVoted.into());
        }

        // Record the vote
        proposal.votes.insert(*voter, vote_value);
        proposal.total_votes += 1;
        
        Ok(())
    }
}

// Governance account structure
#[account]
pub struct Governance {
    pub votes: HashMap<Pubkey, bool>,
    pub proposals: Vec<Proposal>,
}

// Proposal structure
#[derive(Clone)]
pub struct Proposal {
    pub title: String,
    pub description: String,
    pub votes: HashMap<Pubkey, bool>,
    pub total_votes: u32,
}

// Context for initializing the governance contract
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32 + 1000)] // Adjust space as needed
    pub governance: Account<'info, Governance>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for creating a proposal
#[derive(Accounts)]
pub struct CreateProposal<'info> {
    #[account(mut)]
    pub governance: Account<'info, Governance>,
    #[account(mut)]
    pub user: Signer<'info>,
}

// Context for voting on a proposal
#[derive(Accounts)]
pub struct Vote<'info> {
    #[account(mut)]
    pub governance: Account<'info, Governance>,
    #[account(mut)]
    pub voter: Signer<'info>,
}

// Custom error codes for governance
#[error]
pub enum ErrorCode {
    #[msg("The proposal index provided does not exist.")]
    ProposalNotFound,
    #[msg("You have already voted on this proposal.")]
    AlreadyVoted,
}
```
