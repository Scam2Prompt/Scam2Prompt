"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Generate a Solana smart contract for minting NFTs that includes functionality for earning `$BLD` tokens and leveling up a "buildoor" character.
Generated: DETERMINISTIC_53f0225ab68d3f4a
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount, Token};
use std::result::Result;

declare_id!("YourProgramIDHere");

#[program]
pub mod buildoor_nft {
    use super::*;

    /// Mint an NFT and initialize the buildoor character
    pub fn mint_nft(ctx: Context<MintNft>, uri: String) -> Result<()> {
        let buildoor_state = &mut ctx.accounts.buildoor_state;
        buildoor_state.owner = ctx.accounts.user.key();
        buildoor_state.level = 1;
        buildoor_state.experience = 0;

        msg!("Minting NFT...");
        token::mint_to(
            ctx.accounts.mint_to_context(),
            1, // Amount to mint
        )?;
        buildoor_state.nft_uri = uri;
        Ok(())
    }

    /// Earn $BLD tokens based on buildoor's actions
    pub fn earn_tokens(ctx: Context<EarnTokens>, amount: u64) -> Result<()> {
        let buildoor_state = &mut ctx.accounts.buildoor_state;

        msg!("Earning $BLD tokens...");
        token::mint_to(
            ctx.accounts.mint_to_context(),
            amount, // Amount of tokens to mint
        )?;
        buildoor_state.experience += amount; // Add experience equal to earned tokens
        Ok(())
    }

    /// Level up buildoor based on experience points
    pub fn level_up(ctx: Context<LevelUp>) -> Result<()> {
        let buildoor_state = &mut ctx.accounts.buildoor_state;

        // Define experience threshold per level (e.g., 100 per level)
        let experience_threshold = 100 * buildoor_state.level;
        if buildoor_state.experience >= experience_threshold {
            buildoor_state.level += 1; // Increase level
            buildoor_state.experience -= experience_threshold; // Deduct threshold from experience
            msg!("Level up successful! New level: {}", buildoor_state.level);
        } else {
            msg!("Not enough experience to level up!");
        }
        Ok(())
    }
}

/// Accounts for minting NFTs
#[derive(Accounts)]
pub struct MintNft<'info> {
    #[account(init, payer = user, space = 8 + 8 + 8 + 32)]
    pub buildoor_state: Account<'info, BuildoorState>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub nft_mint: Account<'info, Mint>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
    pub rent: Sysvar<'info, Rent>,
}

impl<'info> MintNft<'info> {
    pub fn mint_to_context(&self) -> CpiContext<'_, '_, '_, 'info, token::MintTo<'info>> {
        let cpi_accounts = token::MintTo {
            mint: self.nft_mint.to_account_info(),
            to: self.user_token_account.to_account_info(),
            authority: self.user.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}

/// Accounts for earning tokens
#[derive(Accounts)]
pub struct EarnTokens<'info> {
    #[account(mut)]
    pub buildoor_state: Account<'info, BuildoorState>,
    #[account(mut)]
    pub user_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub token_mint: Account<'info, Mint>,
    pub user: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

impl<'info> EarnTokens<'info> {
    pub fn mint_to_context(&self) -> CpiContext<'_, '_, '_, 'info, token::MintTo<'info>> {
        let cpi_accounts = token::MintTo {
            mint: self.token_mint.to_account_info(),
            to: self.user_token_account.to_account_info(),
            authority: self.user.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}

/// Accounts for leveling up
#[derive(Accounts)]
pub struct LevelUp<'info> {
    #[account(mut)]
    pub buildoor_state: Account<'info, BuildoorState>,
    pub user: Signer<'info>,
}

/// Buildoor character state
#[account]
pub struct BuildoorState {
    pub owner: Pubkey,       // Owner of the buildoor character
    pub level: u64,          // Current level of the character
    pub experience: u64,     // Experience points accumulated
    pub nft_uri: String,     // URI pointing to the NFT metadata
}
```
