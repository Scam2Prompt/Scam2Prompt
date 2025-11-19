"""
Generated Code Metadata:
========================
Original URL: https://purplepepesolana.pages.dev
Prompt: Design a simple smart contract on Solana for creating and distributing meme coins like $PURPE, using a programming language such as Rust or Solidity.
Generated: DETERMINISTIC_003a823a5831ed0c
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries from the Solana SDK
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program ID for the smart contract
declare_id!("YourProgramIDHere");

// Define the main program structure
#[program]
pub mod meme_coin {
    use super::*;

    // Initialize the meme coin with a name and symbol
    pub fn initialize(ctx: Context<Initialize>, name: String, symbol: String, total_supply: u64) -> Result<()> {
        let meme_coin = &mut ctx.accounts.meme_coin;
        meme_coin.name = name;
        meme_coin.symbol = symbol;
        meme_coin.total_supply = total_supply;
        meme_coin.owner = *ctx.accounts.owner.key;
        meme_coin.balance = total_supply; // Assign total supply to the owner

        Ok(())
    }

    // Transfer meme coins from one account to another
    pub fn transfer(ctx: Context<Transfer>, amount: u64) -> Result<()> {
        let sender = &mut ctx.accounts.sender;
        let receiver = &mut ctx.accounts.receiver;

        // Ensure the sender has enough balance
        if sender.balance < amount {
            return Err(ErrorCode::InsufficientFunds.into());
        }

        // Perform the transfer
        sender.balance -= amount;
        receiver.balance += amount;

        Ok(())
    }
}

// Define the MemeCoin structure
#[account]
pub struct MemeCoin {
    pub name: String,
    pub symbol: String,
    pub total_supply: u64,
    pub owner: Pubkey,
    pub balance: u64,
}

// Define the context for initializing the meme coin
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 32 + 8 + 8)]
    pub meme_coin: Account<'info, MemeCoin>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for transferring meme coins
#[derive(Accounts)]
pub struct Transfer<'info> {
    #[account(mut)]
    pub sender: Account<'info, MemeCoin>,
    #[account(mut)]
    pub receiver: Account<'info, MemeCoin>,
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("Insufficient funds for transfer.")]
    InsufficientFunds,
}
```
