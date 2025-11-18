"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bongers-testnets-r8pj.vercel.app
Prompt: Create a smart contract in Rust for minting Bongers Origin NFTs on the Solana blockchain, ensuring the total supply does not exceed 1000.
Generated: DETERMINISTIC_396ef8ff7f1f90ba
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use anchor_lang::prelude::*;
use anchor_lang::solana_program::program_error::ProgramError;

declare_id!("YourProgramIDHere"); // Replace with your program ID

#[program]
pub mod bongers_origin_nft {
    use super::*;

    // Initialize the minting setup
    pub fn initialize(ctx: Context<Initialize>, max_supply: u64) -> Result<()> {
        let state = &mut ctx.accounts.state;
        state.max_supply = max_supply;
        state.total_minted = 0;
        Ok(())
    }

    // Mint a new NFT
    pub fn mint(ctx: Context<Mint>, metadata: String) -> Result<()> {
        let state = &mut ctx.accounts.state;

        // Check if the max supply has been reached
        if state.total_minted >= state.max_supply {
            return Err(ProgramError::Custom(1000).into()); // Custom error code for supply exceeded
        }

        // Increment the total minted count
        state.total_minted += 1;

        // Logic to mint NFT metadata (dummy operation here for simplicity)
        msg!("Minting Bongers Origin NFT with metadata: {}", metadata);

        Ok(())
    }
}

#[account]
pub struct State {
    // Maximum number of NFTs that can be minted
    pub max_supply: u64,
    // Current number of minted NFTs
    pub total_minted: u64,
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8 + 8)] // Allocate space for State struct
    pub state: Account<'info, State>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Mint<'info> {
    #[account(mut)]
    pub state: Account<'info, State>,
    pub user: Signer<'info>,
}
```
