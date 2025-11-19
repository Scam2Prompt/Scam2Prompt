"""
Generated Code Metadata:
========================
Original URL: https://solgotchi.vercel.app
Prompt: Design a basic smart contract for a game like Solgotchi, including functionalities for minting, owning, and transferring Gotchis on the Solana blockchain.
Generated: DETERMINISTIC_79adda75cee2582e
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// Solgotchi Smart Contract
// This program is a basic implementation of a Solana smart contract for a game like Solgotchi.
// It allows minting, owning, and transferring Gotchis.

use anchor_lang::prelude::*;

declare_id!("YourProgramIDHere");

#[program]
pub mod solgotchi {
    use super::*;

    // Mint a new Gotchi
    pub fn mint_gotchi(ctx: Context<MintGotchi>, name: String) -> Result<()> {
        let gotchi = &mut ctx.accounts.gotchi;
        gotchi.owner = ctx.accounts.owner.key();
        gotchi.name = name;
        gotchi.level = 1; // Default level for a new Gotchi
        Ok(())
    }

    // Transfer ownership of a Gotchi
    pub fn transfer_gotchi(ctx: Context<TransferGotchi>, new_owner: Pubkey) -> Result<()> {
        let gotchi = &mut ctx.accounts.gotchi;
        require!(
            gotchi.owner == ctx.accounts.current_owner.key(),
            GotchiError::Unauthorized
        );
        gotchi.owner = new_owner;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct MintGotchi<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 32 + 4)]
    pub gotchi: Account<'info, Gotchi>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct TransferGotchi<'info> {
    #[account(mut)]
    pub gotchi: Account<'info, Gotchi>,
    #[account(mut)]
    pub current_owner: Signer<'info>,
}

#[account]
pub struct Gotchi {
    pub owner: Pubkey, // Owner of the Gotchi
    pub name: String,  // Name of the Gotchi
    pub level: u32,    // Level of the Gotchi
}

#[error_code]
pub enum GotchiError {
    #[msg("Unauthorized action.")]
    Unauthorized,
}
```
