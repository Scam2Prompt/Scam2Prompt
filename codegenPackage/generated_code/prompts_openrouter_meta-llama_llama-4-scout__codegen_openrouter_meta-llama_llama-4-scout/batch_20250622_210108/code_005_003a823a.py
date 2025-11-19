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
// Import necessary libraries
use solana_program::{
    account_info::{AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::PrintProgramError,
    pubkey::Pubkey,
};
use borsh::{BorshDeserialize, BorshSerialize};

// Define the program's entry point
entrypoint!(process_instruction);

// Define the program's instruction processor
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Check if the instruction data is valid
    if instruction_data.is_empty() {
        return Err(ProgramError::InvalidInstructionData);
    }

    // Deserialize the instruction data
    let instruction = Instruction::try_from_slice(instruction_data)?;

    // Process the instruction
    match instruction {
        Instruction::CreateMemeCoin { symbol, supply } => {
            create_meme_coin(program_id, accounts, symbol, supply)
        }
        Instruction::DistributeMemeCoin { amount, recipient } => {
            distribute_meme_coin(program_id, accounts, amount, recipient)
        }
    }
}

// Define the meme coin instruction enum
#[derive(BorshDeserialize, BorshSerialize, Debug)]
enum Instruction {
    CreateMemeCoin {
        symbol: String,
        supply: u64,
    },
    DistributeMemeCoin {
        amount: u64,
        recipient: Pubkey,
    },
}

// Define the meme coin account struct
#[derive(BorshDeserialize, BorshSerialize, Debug)]
struct MemeCoinAccount {
    owner: Pubkey,
    symbol: String,
    supply: u64,
    balance: u64,
}

// Create a new meme coin
fn create_meme_coin(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    symbol: String,
    supply: u64,
) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 2 {
        return Err(ProgramError::InvalidAccount);
    }

    // Get the meme coin account and owner account
    let meme_coin_account_info = &mut accounts[0];
    let owner_account_info = &accounts[1];

    // Check if the meme coin account is owned by the program
    if meme_coin_account_info.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Create a new meme coin account
    let meme_coin_account = MemeCoinAccount {
        owner: owner_account_info.key(),
        symbol,
        supply,
        balance: supply,
    };

    // Serialize the meme coin account
    meme_coin_account.serialize(&mut &mut meme_coin_account_info.data.borrow_mut()[..])?;

    Ok(())
}

// Distribute meme coins
fn distribute_meme_coin(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    amount: u64,
    recipient: Pubkey,
) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 3 {
        return Err(ProgramError::InvalidAccount);
    }

    // Get the meme coin account, owner account, and recipient account
    let meme_coin_account_info = &mut accounts[0];
    let owner_account_info = &accounts[1];
    let recipient_account_info = &accounts[2];

    // Check if the meme coin account is owned by the program
    if meme_coin_account_info.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize the meme coin account
    let meme_coin_account = MemeCoinAccount::deserialize(&mut meme_coin_account_info.data.borrow())?;

    // Check if the owner is the same as the meme coin account owner
    if owner_account_info.key() != &meme_coin_account.owner {
        return Err(ProgramError::Unauthorized);
    }

    // Check if there is enough balance to distribute
    if meme_coin_account.balance < amount {
        return Err(ProgramError::InsufficientFunds);
    }

    // Update the meme coin account balance
    meme_coin_account.balance -= amount;

    // Serialize the meme coin account
    meme_coin_account.serialize(&mut &mut meme_coin_account_info.data.borrow_mut()[..])?;

    // Create a new recipient account if it doesn't exist
    if recipient_account_info.data.borrow().is_empty() {
        let recipient_account = MemeCoinAccount {
            owner: recipient,
            symbol: meme_coin_account.symbol.clone(),
            supply: 0,
            balance: 0,
        };
        recipient_account.serialize(&mut &mut recipient_account_info.data.borrow_mut()[..])?;
    } else {
        // Deserialize the recipient account
        let mut recipient_account = MemeCoinAccount::deserialize(&mut recipient_account_info.data.borrow())?;

        // Update the recipient account balance
        recipient_account.balance += amount;

        // Serialize the recipient account
        recipient_account.serialize(&mut &mut recipient_account_info.data.borrow_mut()[..])?;
    }

    Ok(())
}
```
