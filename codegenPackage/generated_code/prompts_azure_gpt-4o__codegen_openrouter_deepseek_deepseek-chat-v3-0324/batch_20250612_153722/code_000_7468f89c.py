"""
Generated Code Metadata:
========================
Original URL: https://pengwu.io
Prompt: Write a Solana-based smart contract for a meme token similar to PENGWU, including functionalities for staking rewards and airdrop distribution as described in PENGWU's tokenomics.
Generated: DETERMINISTIC_7468f89ccdf93b61
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};
use std::convert::Into;

declare_id!("YourProgramIDHere");

#[program]
pub mod pengwu_token {
    use super::*;

    // Initializes the meme token program
    pub fn initialize(ctx: Context<Initialize>, total_supply: u64) -> Result<()> {
        let mint = &mut ctx.accounts.mint;
        mint.mint_authority = COption::Some(ctx.accounts.authority.key());
        mint.freeze_authority = COption::Some(ctx.accounts.authority.key());
        mint.supply = total_supply;

        Ok(())
    }

    // Stakes tokens to earn rewards
    pub fn stake_tokens(ctx: Context<StakeTokens>, amount: u64) -> Result<()> {
        let stake_account = &mut ctx.accounts.stake_account;
        let clock = Clock::get()?;

        // Transfer tokens to staking account
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.user_token_account.to_account_info(),
                    to: ctx.accounts.stake_token_account.to_account_info(),
                    authority: ctx.accounts.user.to_account_info(),
                },
            ),
            amount,
        )?;

        // Update stake account
        stake_account.amount += amount;
        stake_account.stake_time = clock.unix_timestamp;
        stake_account.user = ctx.accounts.user.key();

        Ok(())
    }

    // Claims staking rewards
    pub fn claim_rewards(ctx: Context<ClaimRewards>) -> Result<()> {
        let stake_account = &mut ctx.accounts.stake_account;
        let reward_account = &mut ctx.accounts.reward_account;
        let clock = Clock::get()?;

        // Calculate rewards (simple linear reward for example)
        let staked_duration = (clock.unix_timestamp - stake_account.stake_time) as u64;
        let reward_amount = stake_account.amount * staked_duration / REWARD_RATE_DENOMINATOR;

        // Mint reward tokens
        token::mint_to(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                token::MintTo {
                    mint: ctx.accounts.mint.to_account_info(),
                    to: ctx.accounts.user_token_account.to_account_info(),
                    authority: ctx.accounts.reward_authority.to_account_info(),
                },
            ),
            reward_amount,
        )?;

        // Update stake account
        stake_account.stake_time = clock.unix_timestamp;
        reward_account.total_distributed += reward_amount;

        Ok(())
    }

    // Distributes airdrop to eligible users
    pub fn distribute_airdrop(ctx: Context<DistributeAirdrop>, amount: u64) -> Result<()> {
        let airdrop_account = &mut ctx.accounts.airdrop_account;
        let clock = Clock::get()?;

        // Check if user is eligible (simplified for example)
        if !airdrop_account.eligible_users.contains(&ctx.accounts.user.key()) {
            return Err(ErrorCode::UserNotEligible.into());
        }

        // Check if user has already claimed
        if airdrop_account.claimed_users.contains(&ctx.accounts.user.key()) {
            return Err(ErrorCode::AlreadyClaimed.into());
        }

        // Transfer airdrop tokens
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.airdrop_vault.to_account_info(),
                    to: ctx.accounts.user_token_account.to_account_info(),
                    authority: ctx.accounts.airdrop_authority.to_account_info(),
                },
            ),
            amount,
        )?;

        // Update airdrop account
        airdrop_account.claimed_users.push(ctx.accounts.user.key());
        airdrop_account.total_distributed += amount;
        airdrop_account.last_distribution = clock.unix_timestamp;

        Ok(())
    }
}

// Constants
const REWARD_RATE_DENOMINATOR: u64 = 31536000; // Rewards per second (simplified)

// Accounts
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 8 + 32 + 8 + 8)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
    pub rent: Sysvar<'info, Rent>,
}

#[derive(Accounts)]
pub struct StakeTokens<'info> {
    #[account(mut)]
    pub stake_account: Account<'info, StakeAccount>,
    #[account(mut)]
    pub stake_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub stake_account: Account<'info, StakeAccount>,
    #[account(mut)]
    pub reward_account: Account<'info, RewardAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub reward_authority: Signer<'info>,
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    pub token_program: Program<'info, Token>,
    pub clock: Sysvar<'info, Clock>,
}

#[derive(Accounts)]
pub struct DistributeAirdrop<'info> {
    #[account(mut)]
    pub airdrop_account: Account<'info, AirdropAccount>,
    #[account(mut)]
    pub airdrop_vault: Account<'info, TokenAccount>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub airdrop_authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
    pub clock: Sysvar<'info, Clock>,
}

// Account structures
#[account]
pub struct StakeAccount {
    pub amount: u64,
    pub stake_time: i64,
    pub user: Pubkey,
}

#[account]
pub struct RewardAccount {
    pub total_distributed: u64,
}

#[account]
pub struct AirdropAccount {
    pub eligible_users: Vec<Pubkey>,
    pub claimed_users: Vec<Pubkey>,
    pub total_distributed: u64,
    pub last_distribution: i64,
}

// Error codes
#[error_code]
pub enum ErrorCode {
    #[msg("User is not eligible for airdrop")]
    UserNotEligible,
    #[msg("User has already claimed airdrop")]
    AlreadyClaimed,
    #[msg("Insufficient funds in airdrop vault")]
    InsufficientFunds,
    #[msg("Staking amount must be greater than zero")]
    InvalidStakeAmount,
}
```
