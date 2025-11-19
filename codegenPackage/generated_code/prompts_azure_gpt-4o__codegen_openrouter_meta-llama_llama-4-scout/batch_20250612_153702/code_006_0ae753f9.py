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
// Import required libraries
use anchor_lang::prelude::*;

// Define the program ID
declare_id!("");

// Define the TNSR token mint address
const TNSR_MINT_ADDRESS: Pubkey = Pubkey::new_from_array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]);

// Define the Tensor platform program ID
const TENSOR_PROGRAM_ID: Pubkey = Pubkey::new_from_array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]);

// Define the TNSR token reward distributor program
#[program]
pub mod tnsr_reward_distributor {
    use super::*;

    // Define the trading activity struct
    #[account]
    pub struct TradingActivity {
        pub user: Pubkey,
        pub trading_volume: u64,
        pub reward_claimed: bool,
    }

    // Define the reward distributor struct
    #[account]
    pub struct RewardDistributor {
        pub authority: Pubkey,
        pub tnsr_mint: Pubkey,
        pub reward_amount: u64,
    }

    // Initialize the reward distributor account
    pub fn initialize_reward_distributor(
        ctx: Context<InitializeRewardDistributor>,
        reward_amount: u64,
    ) -> Result<()> {
        let reward_distributor = &mut ctx.accounts.reward_distributor;
        reward_distributor.authority = ctx.accounts.authority.key();
        reward_distributor.tnsr_mint = TNSR_MINT_ADDRESS;
        reward_distributor.reward_amount = reward_amount;
        Ok(())
    }

    // Record trading activity
    pub fn record_trading_activity(
        ctx: Context<RecordTradingActivity>,
        trading_volume: u64,
    ) -> Result<()> {
        let trading_activity = &mut ctx.accounts.trading_activity;
        trading_activity.user = ctx.accounts.user.key();
        trading_activity.trading_volume = trading_volume;
        trading_activity.reward_claimed = false;
        Ok(())
    }

    // Distribute TNSR token rewards
    pub fn distribute_rewards(ctx: Context<DistributeRewards>) -> Result<()> {
        let reward_distributor = &ctx.accounts.reward_distributor;
        let trading_activity = &ctx.accounts.trading_activity;
        if !trading_activity.reward_claimed {
            let reward_amount = reward_distributor.reward_amount;
            let tnsr_mint = reward_distributor.tnsr_mint;
            // Transfer TNSR tokens to user
            let transfer_instruction = spl_token::instruction::transfer(
                &TNSR_MINT_ADDRESS,
                &ctx.accounts.reward_distributor.tnsr_token_account,
                &ctx.accounts.user_tnsr_token_account,
                &reward_distributor.authority,
                &[],
                reward_amount,
            )?;
            solana_program::program::invoke(
                &transfer_instruction,
                &[
                    TNSR_MINT_ADDRESS,
                    ctx.accounts.reward_distributor.tnsr_token_account,
                    ctx.accounts.user_tnsr_token_account,
                    reward_distributor.authority,
                ],
            )?;
            // Update trading activity account
            let trading_activity = &mut ctx.accounts.trading_activity;
            trading_activity.reward_claimed = true;
        }
        Ok(())
    }
}

// Define the InitializeRewardDistributor instruction
#[derive(Accounts)]
pub struct InitializeRewardDistributor<'info> {
    #[account(init, payer = authority, space = 8 + 40)]
    pub reward_distributor: Account<'info, RewardDistributor>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the RecordTradingActivity instruction
#[derive(Accounts)]
pub struct RecordTradingActivity<'info> {
    #[account(init, payer = user, space = 8 + 40)]
    pub trading_activity: Account<'info, TradingActivity>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the DistributeRewards instruction
#[derive(Accounts)]
pub struct DistributeRewards<'info> {
    #[account(mut)]
    pub reward_distributor: Account<'info, RewardDistributor>,
    #[account(mut)]
    pub trading_activity: Account<'info, TradingActivity>,
    #[account(mut)]
    pub user_tnsr_token_account: Account<'info, spl_token::TokenAccount>,
    pub tnsr_mint: Program<'info, spl_token::Token>,
    pub system_program: Program<'info, System>,
}
```
