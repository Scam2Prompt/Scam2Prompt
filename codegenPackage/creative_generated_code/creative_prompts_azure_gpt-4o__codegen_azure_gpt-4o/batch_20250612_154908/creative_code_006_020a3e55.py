"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkdrops.xyz
Prompt: Write a smart contract on Solana that utilizes zkdrops for proof of participation in a blockchain-based voting system.
Generated: DETERMINISTIC_020a3e554de229a1
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary crates
use anchor_lang::prelude::*;
use solana_program::program_error::ProgramError;
use zkdrops::proof::{Proof, verify_proof};

// Program ID declaration
declare_id!("YourProgramIDHere12345678901234567890123");

#[program]
pub mod voting_system {
    use super::*;

    // Initializes the voting process
    pub fn initialize_voting(ctx: Context<InitializeVoting>, admin: Pubkey) -> Result<()> {
        let voting_state = &mut ctx.accounts.voting_state;
        voting_state.admin = admin;
        voting_state.is_active = true;
        voting_state.total_votes = 0;
        Ok(())
    }

    // Cast a vote with proof of participation using zkDrops
    pub fn cast_vote(ctx: Context<CastVote>, proof: Proof) -> Result<()> {
        let voting_state = &ctx.accounts.voting_state;

        // Ensure voting is active
        if !voting_state.is_active {
            return Err(ProgramError::Custom(100).into()); // Voting is not active
        }

        // Verify proof using zkDrops
        if !verify_proof(&proof) {
            return Err(ProgramError::Custom(101).into()); // Invalid proof
        }

        let voter_account = &ctx.accounts.voter_account;

        // Mark voter as having voted
        voter_account.has_voted = true;

        // Increment total votes
        let voting_state = &mut ctx.accounts.voting_state;
        voting_state.total_votes += 1;

        Ok(())
    }

    // End voting process
    pub fn end_voting(ctx: Context<EndVoting>) -> Result<()> {
        let voting_state = &mut ctx.accounts.voting_state;

        // Ensure only admin can end voting
        if ctx.accounts.admin.key() != voting_state.admin {
            return Err(ProgramError::Custom(102).into()); // Only admin can end voting
        }

        voting_state.is_active = false;
        Ok(())
    }
}

// Context for initializing voting
#[derive(Accounts)]
pub struct InitializeVoting<'info> {
    #[account(init, payer = admin, space = 8 + 32 + 1 + 8)]
    pub voting_state: Account<'info, VotingState>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for casting votes
#[derive(Accounts)]
pub struct CastVote<'info> {
    #[account(mut)]
    pub voting_state: Account<'info, VotingState>,
    #[account(mut)]
    pub voter_account: Account<'info, VoterAccount>,
}

// Context for ending voting
#[derive(Accounts)]
pub struct EndVoting<'info> {
    #[account(mut)]
    pub voting_state: Account<'info, VotingState>,
    pub admin: Signer<'info>,
}

// Data structure for voting state
#[account]
pub struct VotingState {
    pub admin: Pubkey,            // Admin account
    pub is_active: bool,          // Is voting active
    pub total_votes: u64,         // Total votes cast
}

// Data structure for voter account
#[account]
pub struct VoterAccount {
    pub has_voted: bool,          // Has the voter participated
}
```
