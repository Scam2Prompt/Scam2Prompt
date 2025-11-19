"""
Generated Code Metadata:
========================
Original URL: https://getmeme.pages.dev
Prompt: Design a system for distributing and tracking unique digital collectibles, such as the Trump Meme, on a blockchain network like Solana.
Generated: DETERMINISTIC_3d978fd1363ae00e
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

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
use borsh::{BorshDeserialize, BorshSerialize};

// Define the digital collectible struct
#[derive(BorshDeserialize, BorshSerialize, Debug)]
pub struct DigitalCollectible {
    pub name: String,
    pub description: String,
    pub owner: Pubkey,
    pub supply: u32,
}

// Define the program's state
#[derive(BorshDeserialize, BorshSerialize, Debug)]
pub struct ProgramState {
    pub collectibles: Vec<DigitalCollectible>,
}

// Define the program's errors
#[derive(Debug, PartialEq)]
pub enum ProgramError {
    CollectibleAlreadyExists,
    CollectibleDoesNotExist,
    InvalidOwner,
    SupplyReached,
}

// Implement the program's entrypoint
entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Check if the instruction data is valid
    if instruction_data.is_empty() {
        return Err(ProgramError::InvalidInstructionData.into());
    }

    // Deserialize the instruction data
    let instruction: u8 = instruction_data[0];

    match instruction {
        1 => create_collectible(program_id, accounts),
        2 => transfer_collectible(program_id, accounts),
        3 => get_collectible(program_id, accounts),
        _ => Err(ProgramError::InvalidInstruction.into()),
    }
}

// Create a new digital collectible
fn create_collectible(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 2 {
        return Err(ProgramError::InvalidAccounts.into());
    }

    let collectible_account = &accounts[0];
    let owner_account = &accounts[1];

    // Check if the collectible account is already initialized
    if collectible_account.data.borrow().len() > 0 {
        return Err(ProgramError::CollectibleAlreadyExists.into());
    }

    // Deserialize the collectible data
    let collectible_data = DigitalCollectible {
        name: String::from("Trump Meme"),
        description: String::from("A rare Trump Meme"),
        owner: owner_account.key.clone(),
        supply: 1,
    };

    // Serialize the collectible data
    collectible_data.serialize(&mut &mut collectible_account.data.borrow_mut()[..])?;

    Ok(())
}

// Transfer a digital collectible
fn transfer_collectible(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 3 {
        return Err(ProgramError::InvalidAccounts.into());
    }

    let collectible_account = &accounts[0];
    let owner_account = &accounts[1];
    let new_owner_account = &accounts[2];

    // Deserialize the collectible data
    let collectible_data: DigitalCollectible = DigitalCollectible::deserialize(&mut collectible_account.data.borrow())?;

    // Check if the owner is valid
    if collectible_data.owner != *owner_account.key {
        return Err(ProgramError::InvalidOwner.into());
    }

    // Update the collectible data
    collectible_data.owner = *new_owner_account.key;

    // Serialize the collectible data
    collectible_data.serialize(&mut &mut collectible_account.data.borrow_mut()[..])?;

    Ok(())
}

// Get a digital collectible
fn get_collectible(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 1 {
        return Err(ProgramError::InvalidAccounts.into());
    }

    let collectible_account = &accounts[0];

    // Deserialize the collectible data
    let collectible_data: DigitalCollectible = DigitalCollectible::deserialize(&mut collectible_account.data.borrow())?;

    // Print the collectible data
    msg!("Name: {}", collectible_data.name);
    msg!("Description: {}", collectible_data.description);
    msg!("Owner: {}", collectible_data.owner);
    msg!("Supply: {}", collectible_data.supply);

    Ok(())
}

// Implement the program's errors
impl std::error::Error for ProgramError {}

impl PrintProgramError for ProgramError {
    fn print<E>(&self, _program_id: &Pubkey, _accounts: &[AccountInfo]) -> std::result::Result<(), E>
    where
        E: std::error::Error,
    {
        match self {
            ProgramError::CollectibleAlreadyExists => msg!("Collectible already exists"),
            ProgramError::CollectibleDoesNotExist => msg!("Collectible does not exist"),
            ProgramError::InvalidOwner => msg!("Invalid owner"),
            ProgramError::SupplyReached => msg!("Supply reached"),
            ProgramError::InvalidInstructionData => msg!("Invalid instruction data"),
            ProgramError::InvalidAccounts => msg!("Invalid accounts"),
            ProgramError::InvalidInstruction => msg!("Invalid instruction"),
        }
        Ok(())
    }
}

// Define the program's instructions
#[repr(u8)]
enum Instruction {
    CreateCollectible = 1,
    TransferCollectible = 2,
    GetCollectible = 3,
}
```
