"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homeworkproject.vercel.app
Prompt: Recommend best practices for implementing a first-come, first-served whitelist claim system on the Solana blockchain, including handling high transaction volumes.
Generated: DETERMINISTIC_1aceb3aeee4ee842
Batch ID: 20250612_153647
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
use std::collections::HashMap;

declare_id!("YourProgramIdHere");

#[program]
pub mod whitelist_claim {
    use super::*;

    // Initialize the program state
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let state = &mut ctx.accounts.state;
        state.claimed_count = 0;
        Ok(())
    }

    // Function to allow users to claim
    pub fn claim(ctx: Context<Claim>) -> Result<()> {
        let state = &mut ctx.accounts.state;

        // Check if the user is already whitelisted
        if !state.whitelisted_users.contains(&ctx.accounts.user.key()) {
            return Err(ErrorCode::NotWhitelisted.into());
        }

        // Check if the claim limit has been reached
        if state.claimed_count >= state.claim_limit {
            return Err(ErrorCode::ClaimLimitReached.into());
        }

        // Mark the user as having claimed
        state.claimed_users.push(ctx.accounts.user.key());
        state.claimed_count += 1;

        Ok(())
    }
}

// Define the state of the contract
#[account]
pub struct State {
    pub claimed_count: u64,              // Total number of claims made
    pub claim_limit: u64,                // Maximum number of claims allowed
    pub whitelisted_users: Vec<Pubkey>,   // List of whitelisted users
    pub claimed_users: Vec<Pubkey>,       // List of users that have claimed
}

// Context for initializing the program
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = State::LEN)]
    pub state: Account<'info, State>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for claiming
#[derive(Accounts)]
pub struct Claim<'info> {
    pub state: Account<'info, State>,
    #[account(mut)]
    pub user: Signer<'info>,
}

// Error codes for the contract
#[error]
pub enum ErrorCode {
    #[msg("You are not whitelisted to claim.")]
    NotWhitelisted,
    #[msg("The claim limit has been reached.")]
    ClaimLimitReached,
}

// Implement the length function for State
impl State {
    const LEN: usize = 8 + 8 + 8 + 4 * 32; // 8 bytes for u64 x3 + 4 bytes for vectors
}
```
