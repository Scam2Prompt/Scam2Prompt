"""
Generated Code Metadata:
========================
Original URL: https://v0-solana-meme-coin-site.vercel.app
Prompt: How can I create my own meme coin on the Solana blockchain using the guidelines provided by Sol Hub?
Generated: DETERMINISTIC_a3bc95047f2b5418
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Solana Meme Coin Creation Code**
```rust
// Import required libraries
use solana_program::{
    account_info::{AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::PrintProgramError,
    pubkey::Pubkey,
};
use solana_program::instruction::Instruction;
use borsh::{BorshDeserialize, BorshSerialize};

// Define the meme coin struct
#[derive(BorshDeserialize, BorshSerialize, Debug)]
pub struct MemeCoin {
    pub name: String,
    pub symbol: String,
    pub total_supply: u64,
    pub mint_authority: Pubkey,
}

// Define the program's entry point
entrypoint!(process_instruction);

// Process instructions
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Check if the instruction data is not empty
    if instruction_data.is_empty() {
        return Err(MemeCoinError::InvalidInstructionData.into());
    }

    // Deserialize the instruction data
    let instruction = MemeCoinInstruction::try_from_slice(instruction_data)?;

    // Process the instruction
    match instruction {
        MemeCoinInstruction::CreateMemeCoin {
            name,
            symbol,
            total_supply,
        } => create_meme_coin(program_id, accounts, name, symbol, total_supply),
        MemeCoinInstruction::Mint {
            amount,
        } => mint_meme_coin(program_id, accounts, amount),
    }
}

// Define the meme coin instructions
#[derive(BorshDeserialize, BorshSerialize, Debug)]
enum MemeCoinInstruction {
    CreateMemeCoin {
        name: String,
        symbol: String,
        total_supply: u64,
    },
    Mint {
        amount: u64,
    },
}

// Create a new meme coin
fn create_meme_coin(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    name: String,
    symbol: String,
    total_supply: u64,
) -> ProgramResult {
    // Check if the accounts array has at least one account
    if accounts.len() < 1 {
        return Err(MemeCoinError::InvalidAccounts.into());
    }

    // Get the meme coin account
    let meme_coin_account = &mut accounts[0];

    // Check if the meme coin account is owned by the program
    if meme_coin_account.owner != program_id {
        return Err(MemeCoinError::InvalidAccountOwner.into());
    }

    // Create a new meme coin
    let meme_coin = MemeCoin {
        name,
        symbol,
        total_supply,
        mint_authority: *program_id,
    };

    // Serialize the meme coin and store it in the account
    meme_coin.serialize(&mut &mut meme_coin_account.data.borrow_mut()[..])?;

    msg!("Meme coin created successfully!");

    Ok(())
}

// Mint meme coins
fn mint_meme_coin(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    amount: u64,
) -> ProgramResult {
    // Check if the accounts array has at least one account
    if accounts.len() < 1 {
        return Err(MemeCoinError::InvalidAccounts.into());
    }

    // Get the meme coin account
    let meme_coin_account = &mut accounts[0];

    // Check if the meme coin account is owned by the program
    if meme_coin_account.owner != program_id {
        return Err(MemeCoinError::InvalidAccountOwner.into());
    }

    // Deserialize the meme coin
    let meme_coin = MemeCoin::deserialize(&mut meme_coin_account.data.borrow())?;

    // Check if the mint authority is the program
    if meme_coin.mint_authority != *program_id {
        return Err(MemeCoinError::InvalidMintAuthority.into());
    }

    // Mint meme coins
    meme_coin.total_supply += amount;

    // Serialize the meme coin and store it in the account
    meme_coin.serialize(&mut &mut meme_coin_account.data.borrow_mut()[..])?;

    msg!("Meme coins minted successfully!");

    Ok(())
}

// Define meme coin errors
#[derive(Debug, PartialEq, Eq)]
enum MemeCoinError {
    InvalidInstructionData,
    InvalidAccounts,
    InvalidAccountOwner,
    InvalidMintAuthority,
}

impl PrintProgramError for MemeCoinError {
    fn print<E: std::fmt::Write>(&self, _program_id: &Pubkey, writer: &mut E) -> std::fmt::Result {
        match self {
            MemeCoinError::InvalidInstructionData => {
                write!(writer, "Invalid instruction data")
            }
            MemeCoinError::InvalidAccounts => {
                write!(writer, "Invalid accounts")
            }
            MemeCoinError::InvalidAccountOwner => {
                write!(writer, "Invalid account owner")
            }
            MemeCoinError::InvalidMintAuthority => {
                write!(writer, "Invalid mint authority")
            }
        }
    }
}
```
**Cargo.toml**
```toml
[package]
name = "meme_coin"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["cdylib"]

[dependencies]
solana-program = "1.10.20"
borsh = "0.7.1"
```
