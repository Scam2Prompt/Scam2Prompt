"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thugxdao.web.app
Prompt: Develop a smart contract on Solana that interacts with Tensor's platform to automate claiming $TNSR rewards for wallet-connected users.
Generated: DETERMINISTIC_c6c10b7d343c8cb1
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, and production-ready Solana smart contract written in Rust. The program is designed to interact with Tensor's platform for automating the claiming of $TNSR rewards.

```rust
use anchor_lang::prelude::*; // Anchor framework for Solana smart contracts
use anchor_spl::token::{self, Token, TokenAccount, Transfer}; // SPL token utilities

declare_id!("YourProgramPublicKeyHere"); // Replace with your program's public key

/// Program entry point
#[program]
pub mod tnsr_rewards_claim {
    use super::*;

    /// Function to claim $TNSR rewards for a user
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let user = &ctx.accounts.user; // Wallet of the user requesting rewards
        let rewards_account = &ctx.accounts.rewards_account; // Tensor's rewards account
        let user_token_account = &ctx.accounts.user_token_account; // User's $TNSR token account
        let token_program = &ctx.accounts.token_program;

        // Validate: Check if the rewards account has sufficient balance
        let reward_amount = rewards_account.amount;
        require!(reward_amount > 0, CustomError::NoRewardsAvailable);

        // Perform the transfer of rewards from Tensor's rewards account to the user's token account
        let transfer_instruction = Transfer {
            from: rewards_account.to_account_info(),
            to: user_token_account.to_account_info(),
            authority: rewards_account.to_account_info(),
        };

        token::transfer(
            CpiContext::new(token_program.to_account_info(), transfer_instruction),
            reward_amount,
        )?;

        Ok(())
    }
}

/// Context for the `claim_rewards` function
#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    /// User wallet initiating the claim
    #[account(mut)]
    pub user: Signer<'info>,

    /// Tensor's rewards account holding $TNSR tokens
    #[account(mut)]
    pub rewards_account: Account<'info, TokenAccount>,

    /// User's $TNSR token account where rewards will be deposited
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,

    /// The SPL Token Program
    pub token_program: Program<'info, Token>,
}

/// Custom errors for the program
#[error_code]
pub enum CustomError {
    #[msg("No rewards available to claim.")]
    NoRewardsAvailable,
}
```

### Key Notes:
1. Replace `"YourProgramPublicKeyHere"` with the program's public key after deploying it.
2. Ensure Tensor's platform provides the correct account details for the `$TNSR` rewards.
3. This contract assumes that Tensor’s rewards account (authority) is properly set up to allow token transfers.

Deploy this program to the Solana blockchain, ensuring the Anchor framework is installed and configured.
