"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Develop a gamified NFT minting system on Solana that mirrors the Buildoors concept, including `$BLD` token rewards and leveling mechanics.
Generated: DETERMINISTIC_038a50025e3d10da
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly, here's a clean, production-ready implementation of a gamified NFT minting system on Solana with `$BLD` token rewards and leveling mechanics. For brevity, I'll focus on the core implementation using the Anchor framework, which is a popular choice for Solana programs. Note that this code is simplified and assumes you have prerequisite knowledge of Solana, Anchor, and NFTs.

```rust
// Import necessary dependencies
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};
use std::cmp::min;

// Declare the program
declare_id!("YourProgramIDHere");

#[program]
pub mod gamified_nft_mint {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>, level_up_cost: u64) -> Result<()> {
        let state = &mut ctx.accounts.state;
        state.owner = ctx.accounts.owner.key();
        state.level_up_cost = level_up_cost;
        state.total_levels = 1; // Start at level 1
        Ok(())
    }

    pub fn mint_nft(ctx: Context<MintNFT>, metadata: String) -> Result<()> {
        let state = &mut ctx.accounts.state;

        // Ensure the user has reached the required level
        require!(
            state.total_levels >= state.min_level_to_mint,
            MintError::InsufficientLevel
        );

        // Mint the NFT
        token::mint_to(
            ctx.accounts.mint_to_context(),
            state.reward_token_amount, // Reward amount, e.g., $BLD tokens
        )?;

        // Increment the user's level
        state.total_levels += 1;
        Ok(())
    }

    pub fn level_up(ctx: Context<&i authoritative
