"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scream-buy.pages.dev
Prompt: Write a smart contract on Solana that supports staking $SCREAM tokens and implements a voting utility for stakers as described in the roadmap.
Generated: DETERMINISTIC_f58641a92b89754d
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Solana smart contract for staking $SCREAM tokens and implementing voting utility for stakers.
// Written in Rust using the Anchor framework.

use anchor_lang::prelude::*;
use anchor_spl::token::{Token, TokenAccount, Mint, Transfer};
use std::collections::HashMap;

declare_id!("YourProgramIDHere1234567890abcdef");

#[program]
pub mod scream_staking_voting {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>, stake_duration: u64) -> Result<()> {
        let state = &mut ctx.accounts.state;
        state.admin = ctx.accounts.admin.key();
        state.stake_duration = stake_duration;
        state.total_staked = 0;
        state.voting_power = HashMap::new();
        Ok(())
    }

    pub fn stake_tokens(ctx: Context<StakeTokens>, amount: u64) -> Result<()> {
        let user = &mut ctx.accounts.user;
        let state = &mut ctx.accounts.state;

        // Ensure valid staking amount
        if amount == 0 {
            return Err(ErrorCode::InvalidAmount.into());
        }

        // Transfer tokens from user to the staking pool
        let transfer_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            Transfer {
                from: ctx.accounts.user_token_account.to_account_info(),
                to: ctx.accounts.pool_token_account.to_account_info(),
                authority: ctx.accounts.user.to_account_info(),
            },
        );
        anchor_spl::token::transfer(transfer_ctx, amount)?;

        // Update staking state
        user.staked_amount += amount;
        state.total_staked += amount;
        state.voting_power.insert(user.key(), user.staked_amount);

        Ok(())
    }

    pub fn unstake_tokens(ctx: Context<UnstakeTokens>) -> Result<()> {
        let user = &mut ctx.accounts.user;
        let state = &mut ctx.accounts.state;

        // Ensure user has staked tokens
        if user.staked_amount == 0 {
            return Err(ErrorCode::NoTokensStaked.into());
        }

        // Transfer tokens back to user
        let transfer_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            Transfer {
                from: ctx.accounts.pool_token_account.to_account_info(),
                to: ctx.accounts.user_token_account.to_account_info(),
                authority: ctx.accounts.state.to_account_info(),
            },
        );
        anchor_spl::token::transfer(transfer_ctx, user.staked_amount)?;

        // Update staking state
        state.total_staked -= user.staked_amount;
        state.voting_power.remove(&user.key());
        user.staked_amount = 0;

        Ok(())
    }

    pub fn cast_vote(ctx: Context<CastVote>, proposal_id: u64, approve: bool) -> Result<()> {
        let user = &ctx.accounts.user;
        let state = &ctx.accounts.state;

        // Ensure user has voting power
        if !state.voting_power.contains_key(&user.key()) {
            return Err(ErrorCode::NoVotingPower.into());
        }

        let voting_power = state.voting_power.get(&user.key()).unwrap_or(&0);

        // Record the vote (this is a simplified representation)
        state.votes.insert(proposal_id, (*voting_power, approve));

        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(mut)]
    pub admin: Signer<'info>,
    #[account(init, payer = admin, space = 8 + 32 + 8 + 8 + 1024)]
    pub state: Account<'info, State>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct StakeTokens<'info> {
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub state: Account<'info, State>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct UnstakeTokens<'info> {
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub pool_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub state: Account<'info, State>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct CastVote<'info> {
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub state: Account<'info, State>,
}

#[account]
pub struct State {
    pub admin: Pubkey,
    pub stake_duration: u64,
    pub total_staked: u64,
    pub voting_power: HashMap<Pubkey, u64>,
    pub votes: HashMap<u64, (u64, bool)>, // proposal_id -> (voting_power, approve)
}

#[account]
pub struct User {
    pub staked_amount: u64,
}

#[error_code]
pub enum ErrorCode {
    #[msg("Invalid staking amount.")]
    InvalidAmount,
    #[msg("No tokens staked.")]
    NoTokensStaked,
    #[msg("You have no voting power.")]
    NoVotingPower,
}
```
