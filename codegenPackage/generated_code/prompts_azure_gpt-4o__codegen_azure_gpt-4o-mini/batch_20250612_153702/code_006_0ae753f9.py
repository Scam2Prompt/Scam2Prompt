"""
Generated Code Metadata:
========================
Original URL: https://tnsrdrop.web.app
Prompt: Create a Solana-based smart contract that distributes $TNSR token rewards to users based on their trading activity on the Tensor platform.
Generated: DETERMINISTIC_0ae753f9b6846da0
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the state of the contract
#[program]
pub mod tensor_reward_distributor {
    use super::*;

    // Initialize the contract
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let reward_state = &mut ctx.accounts.reward_state;
        reward_state.total_rewards = 0;
        Ok(())
    }

    // Distribute rewards based on trading activity
    pub fn distribute_rewards(ctx: Context<DistributeRewards>, user: Pubkey, amount: u64) -> Result<()> {
        let reward_state = &mut ctx.accounts.reward_state;

        // Ensure the amount is positive
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Update the total rewards distributed
        reward_state.total_rewards += amount;

        // Transfer tokens to the user
        let cpi_accounts = token::Transfer {
            from: ctx.accounts.reward_pool.to_account_info(),
            to: ctx.accounts.user_token_account.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        token::transfer(cpi_ctx, amount)?;

        Ok(())
    }
}

// Define the context for initializing the contract
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub reward_state: Account<'info, RewardState>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for distributing rewards
#[derive(Accounts)]
pub struct DistributeRewards<'info> {
    #[account(mut)]
    pub reward_state: Account<'info, RewardState>,
    #[account(mut)]
    pub reward_pool: AccountInfo<'info>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

// Define the state structure for rewards
#[account]
pub struct RewardState {
    pub total_rewards: u64,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("The amount must be greater than zero.")]
    InvalidAmount,
}
```
