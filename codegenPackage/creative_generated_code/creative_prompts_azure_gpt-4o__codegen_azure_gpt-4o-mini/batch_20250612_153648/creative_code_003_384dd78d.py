"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immortals-nft.web.app
Prompt: Create a smart contract for managing a whitelist and free minting process for 3333 NFTs on the Solana blockchain, inspired by the Immortals NFT project.
Generated: DETERMINISTIC_384dd78d1abdb2e3
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;
use anchor_lang::solana_program::system_program;
use anchor_spl::token::{self, Mint, Token, TokenAccount};

declare_id!("YourProgramIdHere"); // Replace with your program ID

#[program]
pub mod nft_whitelist {
    use super::*;

    // Struct to hold the state of the NFT minting process
    #[state]
    pub struct NftMintState {
        pub total_minted: u32,
        pub max_supply: u32,
        pub whitelist: Vec<Pubkey>, // Store whitelisted addresses
    }

    impl NftMintState {
        // Initialize the mint state with a maximum of 3333 NFTs
        pub fn new(ctx: Context<Initialize>) -> Result<Self> {
            Ok(NftMintState {
                total_minted: 0,
                max_supply: 3333,
                whitelist: Vec::new(),
            })
        }

        // Function to add addresses to the whitelist
        pub fn add_to_whitelist(&mut self, ctx: Context<ModifyWhitelist>, user: Pubkey) -> Result<()> {
            // Check if user is already whitelisted
            if self.whitelist.contains(&user) {
                return Err(ErrorCode::AlreadyWhitelisted.into());
            }
            self.whitelist.push(user);
            Ok(())
        }

        // Function to mint NFTs for whitelisted users
        pub fn mint_nft(&mut self, ctx: Context<MintNft>, user: Pubkey) -> Result<()> {
            // Check if the user is whitelisted
            if !self.whitelist.contains(&user) {
                return Err(ErrorCode::NotWhitelisted.into());
            }
            // Ensure the total minted count does not exceed max supply
            require!(self.total_minted < self.max_supply, ErrorCode::MaxSupplyReached);
            self.total_minted += 1;

            // Logic for minting NFT would go here
            // For example, interacting with token minting functions

            Ok(())
        }
    }

    // Context for initializing the NFT mint state
    #[derive(Accounts)]
    pub struct Initialize<'info> {
        #[account(init, payer = user, space = 8 + 32 + 4 + 4)] // Space for state
        pub nft_mint_state: Account<'info, NftMintState>,
        #[account(mut)]
        pub user: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    // Context for modifying the whitelist
    #[derive(Accounts)]
    pub struct ModifyWhitelist<'info> {
        #[account(mut)]
        pub nft_mint_state: Account<'info, NftMintState>,
        #[account(mut)]
        pub user: Signer<'info>,
    }

    // Context for minting NFT
    #[derive(Accounts)]
    pub struct MintNft<'info> {
        #[account(mut)]
        pub nft_mint_state: Account<'info, NftMintState>,
        #[account(mut)]
        pub user: Signer<'info>,
        // Additional accounts needed for minting can be added here
    }
}

// Custom error codes for specific error cases
#[error_code]
pub enum ErrorCode {
    #[msg("The user is already whitelisted.")]
    AlreadyWhitelisted,
    #[msg("The user is not whitelisted.")]
    NotWhitelisted,
    #[msg("The maximum supply of NFTs has been reached.")]
    MaxSupplyReached,
}
```
