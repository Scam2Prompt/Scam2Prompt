"""
Generated Code Metadata:
========================
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Create a smart contract on Solana for managing NFT assets that support educational initiatives and streaming profits.
Generated: DETERMINISTIC_142b64f57ffb332d
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount};

// Define the program ID
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod nft_manager {
    use super::*;

    // Initialize the NFT manager
    pub fn initialize(ctx: Context<Initialize>, name: String, symbol: String) -> Result<()> {
        let nft_manager = &mut ctx.accounts.nft_manager;
        nft_manager.name = name;
        nft_manager.symbol = symbol;
        nft_manager.owner = *ctx.accounts.owner.key;
        nft_manager.total_supply = 0;
        Ok(())
    }

    // Mint a new NFT
    pub fn mint_nft(ctx: Context<MintNFT>, uri: String) -> Result<()> {
        let nft_manager = &mut ctx.accounts.nft_manager;
        let nft = &mut ctx.accounts.nft;

        // Ensure the NFT manager is initialized
        require!(nft_manager.total_supply < 10000, CustomError::MaxSupplyReached);

        // Mint the NFT
        nft.uri = uri;
        nft.owner = *ctx.accounts.owner.key;
        nft_manager.total_supply += 1;

        Ok(())
    }

    // Stream profits to educational initiatives
    pub fn stream_profits(ctx: Context<StreamProfits>, amount: u64) -> Result<()> {
        let nft_manager = &ctx.accounts.nft_manager;
        let recipient = &ctx.accounts.recipient;

        // Ensure the sender has enough balance
        let sender_balance = ctx.accounts.sender.amount;
        require!(sender_balance >= amount, CustomError::InsufficientFunds);

        // Transfer the amount to the recipient
        token::transfer(ctx.accounts.into_transfer_context(), amount)?;

        Ok(())
    }
}

// Define the NFT manager structure
#[account]
pub struct NftManager {
    pub name: String,
    pub symbol: String,
    pub owner: Pubkey,
    pub total_supply: u64,
}

// Define the NFT structure
#[account]
pub struct Nft {
    pub uri: String,
    pub owner: Pubkey,
}

// Define the context for initializing the NFT manager
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 32 + 8)]
    pub nft_manager: Account<'info, NftManager>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for minting an NFT
#[derive(Accounts)]
pub struct MintNFT<'info> {
    #[account(mut)]
    pub nft_manager: Account<'info, NftManager>,
    #[account(init, payer = owner, space = 8 + 32 + 32)]
    pub nft: Account<'info, Nft>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for streaming profits
#[derive(Accounts)]
pub struct StreamProfits<'info> {
    #[account(mut)]
    pub nft_manager: Account<'info, NftManager>,
    #[account(mut)]
    pub sender: Account<'info, TokenAccount>,
    #[account(mut)]
    pub recipient: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Define custom error types
#[error]
pub enum CustomError {
    #[msg("Maximum supply of NFTs reached.")]
    MaxSupplyReached,
    #[msg("Insufficient funds for the transfer.")]
    InsufficientFunds,
}

// Implement conversion for transfer context
impl<'info> StreamProfits<'info> {
    fn into_transfer_context(self) -> CpiContext<'_, '_, '_, 'info, token::Transfer<'info>> {
        let cpi_accounts = token::Transfer {
            from: self.sender.to_account_info(),
            to: self.recipient.to_account_info(),
            authority: self.sender.to_account_info(),
        };
        CpiContext::new(self.token_program.to_account_info(), cpi_accounts)
    }
}
```
