"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Develop a gamified NFT minting system on Solana that mirrors the Buildoors concept, including `$BLD` token rewards and leveling mechanics.
Generated: DETERMINISTIC_038a50025e3d10da
Batch ID: 20250612_151550
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

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod buildoors {
    use super::*;

    // Initialize the game state
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let game_state = &mut ctx.accounts.game_state;
        game_state.authority = *ctx.accounts.authority.key;
        game_state.total_players = 0;
        game_state.total_bld_minted = 0;
        Ok(())
    }

    // Register a new player
    pub fn register_player(ctx: Context<RegisterPlayer>) -> Result<()> {
        let player = &mut ctx.accounts.player;
        let game_state = &mut ctx.accounts.game_state;

        player.authority = *ctx.accounts.authority.key;
        player.level = 1;
        player.experience = 0;
        player.bld_balance = 0;
        player.last_mint_timestamp = 0;

        game_state.total_players += 1;

        Ok(())
    }

    // Mint an NFT and reward BLD tokens
    pub fn mint_nft(ctx: Context<MintNFT>, metadata_uri: String) -> Result<()> {
        let player = &mut ctx.accounts.player;
        let game_state = &mut ctx.accounts.game_state;

        // Check cooldown period (24 hours)
        let current_timestamp = Clock::get()?.unix_timestamp;
        if current_timestamp - player.last_mint_timestamp < 86400 {
            return Err(ErrorCode::MintCooldown.into());
        }

        // Update player state
        player.last_mint_timestamp = current_timestamp;
        player.experience += 100;

        // Check for level up
        if player.experience >= player.level * 500 {
            player.level += 1;
        }

        // Reward BLD tokens based on level
        let reward_amount = player.level * 10;
        player.bld_balance += reward_amount;
        game_state.total_bld_minted += reward_amount;

        // Mint NFT logic would go here (omitted for brevity)
        // Typically would involve creating metadata account and minting the NFT

        Ok(())
    }

    // Claim BLD tokens
    pub fn claim_bld(ctx: Context<ClaimBLD>, amount: u64) -> Result<()> {
        let player = &mut ctx.accounts.player;
        let game_state = &mut ctx.accounts.game_state;

        if player.bld_balance < amount {
            return Err(ErrorCode::InsufficientBalance.into());
        }

        // Transfer BLD tokens from game vault to player
        let cpi_accounts = Transfer {
            from: ctx.accounts.game_vault.to_account_info(),
            to: ctx.accounts.player_token_account.to_account_info(),
            authority: ctx.accounts.game_state.to_account_info(),
        };

        let cpi_ctx = CpiContext::new(ctx.accounts.token_program.to_account_info(), cpi_accounts);
        token::transfer(cpi_ctx, amount)?;

        // Update balances
        player.bld_balance -= amount;
        game_state.total_bld_minted -= amount;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 8 + 32 + 8 + 8)]
    pub game_state: Account<'info, GameState>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct RegisterPlayer<'info> {
    #[account(init, payer = authority, space = 8 + 32 + 8 + 8 + 8 + 8)]
    pub player: Account<'info, Player>,
    #[account(mut)]
    pub game_state: Account<'info, GameState>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct MintNFT<'info> {
    #[account(mut, has_one = authority)]
    pub player: Account<'info, Player>,
    #[account(mut)]
    pub game_state: Account<'info, GameState>,
    pub authority: Signer<'info>,
    // NFT mint and metadata accounts would be included here
}

#[derive(Accounts)]
pub struct ClaimBLD<'info> {
    #[account(mut, has_one = authority)]
    pub player: Account<'info, Player>,
    #[account(mut)]
    pub game_state: Account<'info, GameState>,
    #[account(mut)]
    pub game_vault: Account<'info, TokenAccount>,
    #[account(mut)]
    pub player_token_account: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct GameState {
    pub authority: Pubkey,
    pub total_players: u64,
    pub total_bld_minted: u64,
}

#[account]
pub struct Player {
    pub authority: Pubkey,
    pub level: u64,
    pub experience: u64,
    pub bld_balance: u64,
    pub last_mint_timestamp: i64,
}

#[error_code]
pub enum ErrorCode {
    #[msg("Minting is on cooldown. Wait 24 hours between mints.")]
    MintCooldown,
    #[msg("Insufficient BLD balance.")]
    InsufficientBalance,
}
```
