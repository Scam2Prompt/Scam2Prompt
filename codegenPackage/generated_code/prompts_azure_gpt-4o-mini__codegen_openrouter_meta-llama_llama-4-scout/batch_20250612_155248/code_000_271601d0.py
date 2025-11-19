"""
Generated Code Metadata:
========================
Original URL: https://doggodao.web.app
Prompt: Generate a code snippet for integrating $DOGGO token into a Solana NFT project for staking rewards.
Generated: DETERMINISTIC_271601d0d7d5c589
Batch ID: 20250612_155248
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
use anchor_spl::token::{Token, TokenAccount};

// Define the program ID
declare_id!("");

// Define the staking program
#[program]
pub mod doggo_staking {
    use super::*;

    // Initialize the staking program
    pub fn initialize(ctx: Context<Initialize>, reward_amount: u64) -> Result<()> {
        // Get the staking account
        let staking_account = &mut ctx.accounts.staking_account;

        // Initialize the staking account
        staking_account.authority = ctx.accounts.authority.key();
        staking_account.reward_amount = reward_amount;
        staking_account.stakers = 0;

        Ok(())
    }

    // Stake an NFT
    pub fn stake(ctx: Context<Stake>, nft_token_account: Pubkey) -> Result<()> {
        // Get the staking account and NFT token account
        let staking_account = &mut ctx.accounts.staking_account;
        let nft_token_account = &ctx.accounts.nft_token_account;

        // Check if the NFT is already staked
        if staking_account.stakers > 0 {
            // Check if the staker is the same as the authority
            if staking_account.authority != ctx.accounts.staker.key() {
                return Err(ProgramError::InvalidArgument);
            }
        }

        // Add the staker and NFT to the staking account
        staking_account.stakers += 1;
        staking_account.nfts.push(nft_token_account.key());

        Ok(())
    }

    // Unstake an NFT
    pub fn unstake(ctx: Context<Unstake>, nft_token_account: Pubkey) -> Result<()> {
        // Get the staking account and NFT token account
        let staking_account = &mut ctx.accounts.staking_account;
        let nft_token_account = &ctx.accounts.nft_token_account;

        // Check if the NFT is staked
        if !staking_account.nfts.contains(&nft_token_account.key()) {
            return Err(ProgramError::InvalidArgument);
        }

        // Remove the staker and NFT from the staking account
        staking_account.stakers -= 1;
        staking_account.nfts.retain(|x| *x != nft_token_account.key());

        Ok(())
    }

    // Claim rewards
    pub fn claim(ctx: Context<Claim>) -> Result<()> {
        // Get the staking account and reward token account
        let staking_account = &ctx.accounts.staking_account;
        let reward_token_account = &ctx.accounts.reward_token_account;

        // Calculate the reward
        let reward = staking_account.reward_amount * staking_account.stakers;

        // Transfer the reward to the staker
        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.key(),
            anchor_spl::token::Transfer {
                from: ctx.accounts.reward_token_mint.key(),
                to: reward_token_account.key(),
                authority: ctx.accounts.authority.key(),
            },
        );
        anchor_spl::token::transfer(cpi_ctx, reward)?;

        Ok(())
    }
}

// Define the staking account
#[account]
pub struct StakingAccount {
    pub authority: Pubkey,
    pub reward_amount: u64,
    pub stakers: u64,
    pub nfts: Vec<Pubkey>,
}

// Define the Initialize instruction
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 1024)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the Stake instruction
#[derive(Accounts)]
pub struct Stake<'info> {
    #[account(mut)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub staker: Signer<'info>,
    #[account(mut)]
    pub nft_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define the Unstake instruction
#[derive(Accounts)]
pub struct Unstake<'info> {
    #[account(mut)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub staker: Signer<'info>,
    #[account(mut)]
    pub nft_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define the Claim instruction
#[derive(Accounts)]
pub struct Claim<'info> {
    #[account(mut)]
    pub staking_account: Account<'info, StakingAccount>,
    #[account(mut)]
    pub reward_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub reward_token_mint: Account<'info, TokenAccount>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}
```
