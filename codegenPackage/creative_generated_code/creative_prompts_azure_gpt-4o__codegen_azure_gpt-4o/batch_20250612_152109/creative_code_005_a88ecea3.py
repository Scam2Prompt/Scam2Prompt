"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnfts.web.app
Prompt: Create a smart contract on the Solana blockchain that implements the rules for the $LOYAL token airdrop, ensuring only active holders can claim rewards.
Generated: DETERMINISTIC_a88ecea37c1109fb
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Smart Contract for $LOYAL token airdrop on Solana blockchain
// Implements rules to ensure only active holders can claim rewards

use anchor_lang::prelude::*;
use anchor_spl::token::{self, TokenAccount, Token, Transfer};
use std::ops::Deref;

// Program ID for the smart contract
declare_id!("YourProgramIDHere");

#[program]
pub mod loyal_airdrop {
    use super::*;

    // Initialize the airdrop configuration
    pub fn initialize_airdrop(
        ctx: Context<InitializeAirdrop>,
        reward_amount: u64,
    ) -> Result<()> {
        let airdrop_config = &mut ctx.accounts.airdrop_config;
        airdrop_config.reward_amount = reward_amount;
        airdrop_config.authority = *ctx.accounts.authority.key;
        Ok(())
    }

    // Claim rewards for the $LOYAL token airdrop
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let airdrop_config = &ctx.accounts.airdrop_config;

        // Ensure the claimant is active (e.g., token balance > 0)
        let claimant_balance = ctx.accounts.claimant_token_account.amount;
        require!(
            claimant_balance > 0,
            AirdropError::InactiveHolder
        );

        // Transfer rewards to the claimant
        let transfer_instruction = Transfer {
            from: ctx.accounts.airdrop_token_account.to_account_info(),
            to: ctx.accounts.claimant_token_account.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };
        let signer_seeds = &[&airdrop_config.authority.to_bytes()[..]];
        token::transfer(
            ctx.accounts.into_transfer_context(transfer_instruction),
            airdrop_config.reward_amount,
        )?;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeAirdrop<'info> {
    #[account(mut)]
    pub authority: Signer<'info>,
    #[account(
        init,
        payer = authority,
        space = 8 + 8 + 32
    )]
    pub airdrop_config: Account<'info, AirdropConfig>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub authority: Signer<'info>,
    #[account(mut)]
    pub airdrop_config: Account<'info, AirdropConfig>,
    #[account(mut)]
    pub airdrop_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub claimant_token_account: Account<'info, TokenAccount>,
    #[account(address = token_program::ID)]
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct AirdropConfig {
    pub reward_amount: u64,  // Amount of tokens to reward
    pub authority: Pubkey,  // Authority who initializes the airdrop
}

impl<'info> ClaimRewards<'info> {
    fn into_transfer_context<'a>(
        &self,
        transfer: Transfer<'a>,
    ) -> CpiContext<'a, 'info, Transfer<'a>> {
        let accounts = transfer.deref();
        CpiContext::new(self.token_program.to_account_info(), accounts.clone())
    }
}

#[error_code]
pub enum AirdropError {
    #[msg("Claimant is not an active holder.")]
    InactiveHolder,
}
```
