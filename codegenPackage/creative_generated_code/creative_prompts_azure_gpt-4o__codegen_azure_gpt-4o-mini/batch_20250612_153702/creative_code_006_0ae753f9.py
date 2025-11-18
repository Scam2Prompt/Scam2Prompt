"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tnsrdrop.web.app
Prompt: Create a Solana-based smart contract that distributes $TNSR token rewards to users based on their trading activity on the Tensor platform.
Generated: DETERMINISTIC_0ae753f9b6846da0
Batch ID: 20250612_153702
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
use anchor_spl::token::{self, Mint, TokenAccount, Token};

// Declare the program and its entry point
declare_id!("YourProgramIDHere");

#[program]
pub mod tensor_rewards {
    use super::*;

    // Struct to hold user rewards
    #[derive(Accounts)]
    pub struct DistributeRewards<'info> {
        #[account(mut)]
        pub user: Signer<'info>,
        #[account(mut)]
        pub reward_token_mint: Account<'info, Mint>,
        #[account(mut)]
        pub user_token_account: Account<'info, TokenAccount>,
        pub token_program: Program<'info, Token>,
    }

    // Main function to distribute rewards
    pub fn distribute_rewards(ctx: Context<DistributeRewards>, reward_amount: u64) -> Result<()> {
        // Check if the reward amount is greater than zero
        require!(reward_amount > 0, Errors::InvalidRewardAmount);

        // Transfer tokens to the user
        let cpi_accounts = token::Transfer {
            from: ctx.accounts.reward_token_mint.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.user.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::transfer(cpi_ctx, reward_amount)?;

        Ok(())
    }
}

// Define custom error types for the program
#[error_code]
pub enum Errors {
    #[msg("The reward amount must be greater than zero.")]
    InvalidRewardAmount,
}
```
