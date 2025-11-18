"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengwu.io
Prompt: Design a mini-game on Solana where players can earn PENGWU tokens as rewards, inspired by the Mini Games feature on the website.
Generated: DETERMINISTIC_dc8ea8350e4eaed9
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready Rust code that implements a mini-game smart contract on Solana. Players interact with the program and earn "PENGWU" tokens based on their performance.

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount, Token, Transfer};

declare_id!("YourProgramIdHere123456789");

#[program]
pub mod pengwu_mini_game {
    use super::*;

    // Initializes the game and creates a reward pool
    pub fn initialize_game(ctx: Context<InitializeGame>, reward_pool_amount: u64) -> Result<()> {
        let game_state = &mut ctx.accounts.game_state;
        game_state.authority = ctx.accounts.authority.key();
        game_state.reward_pool = ctx.accounts.reward_pool.key();
        game_state.reward_pool_amount = reward_pool_amount;

        // Transfer tokens from the authority to the reward pool
        let transfer_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            token::Transfer {
                from: ctx.accounts.authority_token_account.to_account_info(),
                to: ctx.accounts.reward_pool.to_account_info(),
                authority: ctx.accounts.authority.to_account_info(),
            },
        );
        token::transfer(transfer_ctx, reward_pool_amount)?;

        Ok(())
    }

    // Allows players to play the mini-game and win tokens
    pub fn play_game(ctx: Context<PlayGame>, score: u8) -> Result<()> {
        let game_state = &mut ctx.accounts.game_state;

        // Ensure the reward pool has enough tokens
        if game_state.reward_pool_amount < score.into() {
            return err!(ErrorCode::InsufficientRewardPool);
        }

        // Calculate reward based on the player's score
        let reward = score as u64;

        // Transfer reward tokens to the player's account
        let transfer_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            token::Transfer {
                from: ctx.accounts.reward_pool.to_account_info(),
                to: ctx.accounts.player_token_account.to_account_info(),
                authority: ctx.accounts.authority.to_account_info(),
            },
        );
        token::transfer(transfer_ctx, reward)?;

        // Update reward pool amount
        game_state.reward_pool_amount -= reward;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeGame<'info> {
    #[account(mut)]
    pub authority: Signer<'info>, // Owner of the game
    #[account(mut)]
    pub authority_token_account: Account<'info, TokenAccount>, // Token account of the authority
    #[account(mut)]
    pub reward_pool: Account<'info, TokenAccount>, // Reward pool for the game
    #[account(init, payer = authority, space = 8 + 32 + 32 + 8)]
    pub game_state: Account<'info, GameState>, // Game state account
    pub token_program: Program<'info, Token>, // Token program
    pub system_program: Program<'info, System>, // System program
    pub rent: Sysvar<'info, Rent>, // Rent system account
}

#[derive(Accounts)]
pub struct PlayGame<'info> {
    #[account(mut)]
    pub game_state: Account<'info, GameState>, // Game state account
    #[account(mut)]
    pub reward_pool: Account<'info, TokenAccount>, // Reward pool for the game
    #[account(mut)]
    pub player_token_account: Account<'info, TokenAccount>, // Player's token account
    #[account(mut)]
    pub authority: Signer<'info>, // Owner of the game
    pub token_program: Program<'info, Token>, // Token program
}

#[account]
pub struct GameState {
    pub authority: Pubkey, // Owner of the game
    pub reward_pool: Pubkey, // Reward pool for the game
    pub reward_pool_amount: u64, // Amount of tokens in the reward pool
}

#[error_code]
pub enum ErrorCode {
    #[msg("Insufficient tokens in the reward pool.")]
    InsufficientRewardPool,
    #[msg("Invalid game action.")]
    InvalidAction,
}
```

This code implements a basic Solana program for a mini-game where players can earn tokens. Replace `YourProgramIdHere123456789` with your actual program ID and deploy it using the Anchor framework.
