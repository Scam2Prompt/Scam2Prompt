"""
Generated Code Metadata:
========================
Original URL: https://timcheese.pages.dev
Prompt: Develop a smart contract in Solana's Anchor framework to enforce the 5 NFT max per transaction rule for Tim Cheese minting.
Generated: DETERMINISTIC_3c261decad87530a
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import required libraries
use anchor_lang::prelude::*;

// Define the program ID
declare_id!("");

// Define the TimCheeseNFT struct
#[account]
struct TimCheeseNFT {
    authority: Pubkey,
    nft_count: u8,
}

// Define the program interface
#[program]
pub mod tim_cheese_nft {
    use super::*;

    // Initialize the Tim Cheese NFT account
    pub fn initialize(ctx: Context<Initialize>, authority: Pubkey) -> Result<()> {
        let tim_cheese_nft_account = &mut ctx.accounts.tim_cheese_nft_account;
        tim_cheese_nft_account.authority = authority;
        tim_cheese_nft_account.nft_count = 0;
        Ok(())
    }

    // Mint a new NFT
    pub fn mint_nft(ctx: Context<MintNFT>, authority: Pubkey) -> Result<()> {
        let tim_cheese_nft_account = &mut ctx.accounts.tim_cheese_nft_account;

        // Check if the authority is the same as the one in the account
        require!(tim_cheese_nft_account.authority == authority, TimCheeseError::InvalidAuthority);

        // Check if the NFT count has reached the maximum of 5
        require!(tim_cheese_nft_account.nft_count < 5, TimCheeseError::NFTMaxLimitReached);

        // Increment the NFT count
        tim_cheese_nft_account.nft_count += 1;

        Ok(())
    }
}

// Define the accounts for the Initialize instruction
#[account]
struct InitializeAccounts {
    #[account(init, payer = authority, space = 8 + 32)]
    tim_cheese_nft_account: Account<TimCheeseNFT>,
    authority: Signer<'info>,
    system_program: Program<'info, System>,
}

// Define the accounts for the MintNFT instruction
#[account]
struct MintNFTAccounts {
    #[account(mut, has_one = authority)]
    tim_cheese_nft_account: Account<TimCheeseNFT>,
    authority: Signer<'info>,
}

// Define custom errors
#[error]
pub enum TimCheeseError {
    #[msg("Invalid authority")]
    InvalidAuthority,
    #[msg("NFT max limit reached")]
    NFTMaxLimitReached,
}
```
