"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daotops.web.app
Prompt: Create a smart contract on Solana that tracks and distributes rewards in $TNSR tokens based on user activity metrics, as implemented on the Tensor platform.
Generated: DETERMINISTIC_a161f2950585ab1b
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary crates and modules for Solana smart contract development
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

declare_id!("YourProgramIdHere");

#[program]
pub mod token_reward_tracker {
    use super::*;

    // Initializes the contract with the admin's public key
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let reward_account = &mut ctx.accounts.reward_account;
        reward_account.admin = *ctx.accounts.admin.key;
        reward_account.total_rewards = 0;
        Ok(())
    }

    // Records user activity and calculates rewards based on defined metrics
    pub fn record_activity(ctx: Context<RecordActivity>, user: Pubkey, activity_metric: u64) -> Result<()> {
        let reward_account = &mut ctx.accounts.reward_account;

        // Calculate rewards based on activity metrics
        let rewards = calculate_rewards(activity_metric);
        
        // Update total rewards in the account
        reward_account.total_rewards += rewards;

        // Update user rewards, or initialize if not present
        let user_rewards = reward_account.user_rewards.entry(user).or_insert(0);
        *user_rewards += rewards;

        Ok(())
    }

    // Distributes available rewards to all users based on their activity metrics
    pub fn distribute_rewards(ctx: Context<DistributeRewards>) -> Result<()> {
        let reward_account = &mut ctx.accounts.reward_account;
        for (user, &rewards) in &reward_account.user_rewards {
            // Logic to transfer $TNSR tokens to the user
            // Placeholder: Implement actual token transfer logic here
            msg!("Distributing {} tokens to user: {:?}", rewards, user);
        }
        Ok(())
    }
}

// Context struct for the initialize function
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = admin, space = RewardAccount::LEN)]
    pub reward_account: Account<'info, RewardAccount>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context struct for the record_activity function
#[derive(Accounts)]
pub struct RecordActivity<'info> {
    #[account(mut)]
    pub reward_account: Account<'info, RewardAccount>,
}

// Context struct for the distribute_rewards function
#[derive(Accounts)]
pub struct DistributeRewards<'info> {
    #[account(mut)]
    pub reward_account: Account<'info, RewardAccount>,
}

// RewardAccount structure to hold administration and rewards data
#[account]
pub struct RewardAccount {
    pub admin: Pubkey,
    pub total_rewards: u64,
    pub user_rewards: std::collections::HashMap<Pubkey, u64>,
}

// Calculate rewards based on user activity metrics
fn calculate_rewards(activity_metric: u64) -> u64 {
    // Placeholder: Implement actual reward logic based on metrics
    activity_metric * 10 // Example: 10 $TNSR tokens per activity unit
}

// Error Definitions
#[error]
pub enum ErrorCode {
    #[msg("User already exists")]
    UserAlreadyExists,
    #[msg("Unauthorized access")]
    UnauthorizedAccess,
}
```

**Note:** Replace `"YourProgramIdHere"` with the actual program ID generated when deploying the smart contract. The placeholder section for token transfer should be implemented based on the specific token transfer logic for your $TNSR token.
