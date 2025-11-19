"""
Generated Code Metadata:
========================
Original URL: https://solex-whitelisting.pages.dev
Prompt: How can I implement a whitelisting feature for an AI decentralized launchpad on Solana using Solex's guidelines?
Generated: DETERMINISTIC_a30fd399300e56c2
Batch ID: 20250612_163659
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
use solana_program::borsh::{BorshDeserialize, BorshSerialize};

// Define a struct to represent the whitelisted user
#[derive(BorshDeserialize, BorshSerialize, Debug)]
pub struct WhitelistedUser {
    pub user_pubkey: Pubkey,
}

// Define the program's state
#[derive(BorshDeserialize, BorshSerialize, Debug)]
pub struct WhitelistProgramState {
    pub whitelisted_users: Vec<WhitelistedUser>,
}

// Define the program's entry point
entrypoint!(process_instruction);

// Process a single instruction
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Check if the instruction data is valid
    if instruction_data.is_empty() {
        return Err(WhitelistError::InvalidInstructionData.into());
    }

    // Deserialize the instruction data
    let instruction = instruction_data[0];

    // Handle the instruction
    match instruction {
        1 => add_user_to_whitelist(program_id, accounts),
        2 => remove_user_from_whitelist(program_id, accounts),
        3 => check_if_user_is_whitelisted(program_id, accounts),
        _ => Err(WhitelistError::InvalidInstruction.into()),
    }
}

// Add a user to the whitelist
fn add_user_to_whitelist(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 2 {
        return Err(WhitelistError::InvalidAccounts.into());
    }

    // Get the program state account
    let program_state_account = &accounts[0];

    // Check if the program state account is owned by the program
    if program_state_account.owner != program_id {
        return Err(WhitelistError::InvalidProgramStateAccount.into());
    }

    // Get the user account
    let user_account = &accounts[1];

    // Check if the user account is a valid Pubkey
    if user_account.data.borrow().is_empty() {
        return Err(WhitelistError::InvalidUserAccount.into());
    }

    // Deserialize the program state
    let mut program_state = WhitelistProgramState::try_from_slice(&program_state_account.data.borrow())?;

    // Check if the user is already whitelisted
    for user in &program_state.whitelisted_users {
        if user.user_pubkey == *user_account.key {
            return Err(WhitelistError::UserAlreadyWhitelisted.into());
        }
    }

    // Add the user to the whitelist
    program_state.whitelisted_users.push(WhitelistedUser {
        user_pubkey: *user_account.key,
    });

    // Serialize the program state
    program_state.serialize(&mut &mut program_state_account.data.borrow_mut()[..])?;

    Ok(())
}

// Remove a user from the whitelist
fn remove_user_from_whitelist(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 2 {
        return Err(WhitelistError::InvalidAccounts.into());
    }

    // Get the program state account
    let program_state_account = &accounts[0];

    // Check if the program state account is owned by the program
    if program_state_account.owner != program_id {
        return Err(WhitelistError::InvalidProgramStateAccount.into());
    }

    // Get the user account
    let user_account = &accounts[1];

    // Deserialize the program state
    let mut program_state = WhitelistProgramState::try_from_slice(&program_state_account.data.borrow())?;

    // Check if the user is whitelisted
    let mut whitelisted = false;
    for i in 0..program_state.whitelisted_users.len() {
        if program_state.whitelisted_users[i].user_pubkey == *user_account.key {
            program_state.whitelisted_users.remove(i);
            whitelisted = true;
            break;
        }
    }

    // Check if the user was whitelisted
    if !whitelisted {
        return Err(WhitelistError::UserNotWhitelisted.into());
    }

    // Serialize the program state
    program_state.serialize(&mut &mut program_state_account.data.borrow_mut()[..])?;

    Ok(())
}

// Check if a user is whitelisted
fn check_if_user_is_whitelisted(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 2 {
        return Err(WhitelistError::InvalidAccounts.into());
    }

    // Get the program state account
    let program_state_account = &accounts[0];

    // Check if the program state account is owned by the program
    if program_state_account.owner != program_id {
        return Err(WhitelistError::InvalidProgramStateAccount.into());
    }

    // Get the user account
    let user_account = &accounts[1];

    // Deserialize the program state
    let program_state = WhitelistProgramState::try_from_slice(&program_state_account.data.borrow())?;

    // Check if the user is whitelisted
    for user in &program_state.whitelisted_users {
        if user.user_pubkey == *user_account.key {
            msg!("User is whitelisted");
            return Ok(());
        }
    }

    msg!("User is not whitelisted");
    Err(WhitelistError::UserNotWhitelisted.into())
}

// Define the program's custom errors
#[derive(Debug, PartialEq, Eq)]
pub enum WhitelistError {
    InvalidInstruction,
    InvalidInstructionData,
    InvalidAccounts,
    InvalidProgramStateAccount,
    InvalidUserAccount,
    UserAlreadyWhitelisted,
    UserNotWhitelisted,
}

impl std::error::Error for WhitelistError {}

impl solana_program::program_error::ProgramError for WhitelistError {
    fn code(&self) -> i32 {
        match self {
            WhitelistError::InvalidInstruction => 1,
            WhitelistError::InvalidInstructionData => 2,
            WhitelistError::InvalidAccounts => 3,
            WhitelistError::InvalidProgramStateAccount => 4,
            WhitelistError::InvalidUserAccount => 5,
            WhitelistError::UserAlreadyWhitelisted => 6,
            WhitelistError::UserNotWhitelisted => 7,
        }
    }

    fn to_string(&self) -> String {
        match self {
            WhitelistError::InvalidInstruction => "Invalid instruction".to_string(),
            WhitelistError::InvalidInstructionData => "Invalid instruction data".to_string(),
            WhitelistError::InvalidAccounts => "Invalid accounts".to_string(),
            WhitelistError::InvalidProgramStateAccount => "Invalid program state account".to_string(),
            WhitelistError::InvalidUserAccount => "Invalid user account".to_string(),
            WhitelistError::UserAlreadyWhitelisted => "User already whitelisted".to_string(),
            WhitelistError::UserNotWhitelisted => "User not whitelisted".to_string(),
        }
    }
}
```
