"""
Generated Code Metadata:
========================
Original URL: https://pengwu.io
Prompt: Implement a voting system using PENGWU tokens on the Solana blockchain, allowing community members to influence crucial decisions.
Generated: DETERMINISTIC_dc90059b17faf678
Batch ID: 20250622_211032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod voting_system {
    use super::*;

    // Initialize the voting system
    pub fn initialize(ctx: Context<Initialize>, proposal: String) -> Result<()> {
        let voting_account = &mut ctx.accounts.voting_account;
        voting_account.proposal = proposal;
        voting_account.yes_votes = 0;
        voting_account.no_votes = 0;
        voting_account.voters = vec![];
        Ok(())
    }

    // Cast a vote
    pub fn vote(ctx: Context<Vote>, vote: bool) -> Result<()> {
        let voting_account = &mut ctx.accounts.voting_account;
        let voter = ctx.accounts.voter.key();

        // Check if the voter has already voted
        if voting_account.voters.contains(&voter) {
            return Err(ErrorCode::AlreadyVoted.into());
        }

        // Record the vote
        if vote {
            voting_account.yes_votes += 1;
        } else {
            voting_account.no_votes += 1;
        }
        voting_account.voters.push(voter);
        Ok(())
    }

    // Finalize the voting and get results
    pub fn finalize(ctx: Context<Finalize>) -> Result<VotingResults> {
        let voting_account = &ctx.accounts.voting_account;

        // Return the voting results
        Ok(VotingResults {
            proposal: voting_account.proposal.clone(),
            yes_votes: voting_account.yes_votes,
            no_votes: voting_account.no_votes,
        })
    }
}

// Define the voting account structure
#[account]
pub struct VotingAccount {
    pub proposal: String,
    pub yes_votes: u64,
    pub no_votes: u64,
    pub voters: Vec<Pubkey>,
}

// Define the context for initializing the voting system
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 64 + 8 + 8 + 32)]
    pub voting_account: Account<'info, VotingAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for voting
#[derive(Accounts)]
pub struct Vote<'info> {
    #[account(mut)]
    pub voting_account: Account<'info, VotingAccount>,
    pub voter: Signer<'info>,
}

// Define the context for finalizing the voting
#[derive(Accounts)]
pub struct Finalize<'info> {
    pub voting_account: Account<'info, VotingAccount>,
}

// Define the structure for voting results
#[derive(Clone, AnchorSerialize, AnchorDeserialize)]
pub struct VotingResults {
    pub proposal: String,
    pub yes_votes: u64,
    pub no_votes: u64,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("You have already voted.")]
    AlreadyVoted,
}
```
