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

```rust
// Import necessary libraries and modules
use anchor_lang::prelude::*;
use anchor_spl::token::{Mint, TokenAccount, Token};
use anchor_lang::solana_program::program::invoke_signed;

declare_id!("YourProgramIDHere");

#[program]
pub mod pengwu_game {
    use super::*;

    // Initialize the game state
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let game_state = &mut ctx.accounts.game_state;
        game_state.owner = *ctx.accounts.user.key;
        game_state.total_players = 0;
        game_state.total_rewards = 0;
        Ok(())
    }

    // Function to allow players to participate in the game
    pub fn play_game(ctx: Context<PlayGame>) -> Result<()> {
        let game_state = &mut ctx.accounts.game_state;
        
        // Ensure the player hasn't already played
        if game_state.players.contains(&ctx.accounts.player.key) {
            return Err(ErrorCode::AlreadyPlayed.into());
        }
        
        // Simulate game logic (e.g., random win/lose)
        let win = rand::random::<u8>() % 2 == 0; // Simple winning condition
        
        // Update the game state
        game_state.players.push(*ctx.accounts.player.key);
        game_state.total_players += 1;

        // Reward the player if they win
        if win {
            let reward_amount = 10; // Fixed reward amount
            game_state.total_rewards += reward_amount;

            // Transfer tokens to the player
            let cpi_accounts = Transfer {
                from: ctx.accounts.reward_pool.to_account_info(),
                to: ctx.accounts.player_token_account.to_account_info(),
                authority: ctx.accounts.owner.to_account_info(),
            };
            let cpi_program = ctx.accounts.token_program.clone();
            let seeds = &[ctx.accounts.owner.key.as_ref(), &[ctx.bumps.get("owner").unwrap()]];
            invoke_signed(
                &cpi_accounts,
                cpi_program,
                &[&seeds[..]],
            )?;
        }
        Ok(())
    }
}

// Contexts
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 32 + 4 + 8)]
    pub game_state: Account<'info, GameState>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct PlayGame<'info> {
    #[account(mut)]
    pub game_state: Account<'info, GameState>,
    #[account(mut)]
    pub player: Signer<'info>,
    #[account(mut)]
    pub reward_pool: Account<'info, TokenAccount>,
    #[account(mut)]
    pub player_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
    #[account(mut)]
    pub owner: Signer<'info>,
}

// Game state structure
#[account]
pub struct GameState {
    pub owner: Pubkey,
    pub total_players: u32,
    pub total_rewards: u64,
    pub players: Vec<Pubkey>, // Store players who have participated
}

// Error handling
#[error]
pub enum ErrorCode {
    #[msg("Player has already played the game.")]
    AlreadyPlayed,
}

// Note: This is a basic representation of a Solana program. 
// Ensure you install the proper dependencies and set up Anchor on your local environment to run and test this code.
```
