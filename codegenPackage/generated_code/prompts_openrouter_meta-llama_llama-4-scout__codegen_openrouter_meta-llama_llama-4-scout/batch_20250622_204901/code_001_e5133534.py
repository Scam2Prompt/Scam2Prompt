"""
Generated Code Metadata:
========================
Original URL: https://jupiter-git-temporarily-hardcode-usdt-as-short-token-wowcats.vercel.app
Prompt: Recommend a suitable library for building a perpetual trade station on Solana, considering the features offered by Jupiter Trade Perpetual Trade Station.
Generated: DETERMINISTIC_e5133534001014ce
Batch ID: 20250622_204901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import required libraries
use std::error::Error;
use solana_program::{
    account_info::{AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::PrintProgramError,
    pubkey::Pubkey,
};
use jupiter_perpetual_trade_station::{
    instructions::{Initialize, Trade},
    state::TradeStation,
};

// Define the entry point for the program
entrypoint!(process_instruction);

// Define the process instruction function
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Check if the instruction data is valid
    if instruction_data.is_empty() {
        return Err(solana_program::program_error::ProgramError::InvalidInstructionData);
    }

    // Parse the instruction data
    let instruction = match bincode::deserialize(instruction_data) {
        Ok(instruction) => instruction,
        Err(err) => {
            msg!("Failed to deserialize instruction: {}", err);
            return Err(solana_program::program_error::ProgramError::InvalidInstructionData);
        }
    };

    // Process the instruction
    match instruction {
        JupiterInstruction::Initialize => {
            // Initialize the trade station
            initialize_trade_station(program_id, accounts)
        }
        JupiterInstruction::Trade { .. } => {
            // Process a trade
            trade(program_id, accounts, instruction)
        }
    }
}

// Define the initialize trade station function
fn initialize_trade_station(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 2 {
        return Err(solana_program::program_error::ProgramError::InvalidAccount);
    }

    // Get the trade station account
    let trade_station_account = &accounts[0];

    // Check if the trade station account is owned by the program
    if trade_station_account.owner != program_id {
        return Err(solana_program::program_error::ProgramError::IncorrectProgramId);
    }

    // Initialize the trade station
    let trade_station = TradeStation::new();
    trade_station.serialize(&mut &mut trade_station_account.data.borrow_mut()[..])?;

    Ok(())
}

// Define the trade function
fn trade(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction: JupiterInstruction,
) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 3 {
        return Err(solana_program::program_error::ProgramError::InvalidAccount);
    }

    // Get the trade station account
    let trade_station_account = &accounts[0];

    // Check if the trade station account is owned by the program
    if trade_station_account.owner != program_id {
        return Err(solana_program::program_error::ProgramError::IncorrectProgramId);
    }

    // Deserialize the trade station
    let trade_station = TradeStation::deserialize(&mut &trade_station_account.data.borrow()[..])?;

    // Process the trade
    match instruction {
        JupiterInstruction::Trade { side, amount, price } => {
            // Validate the trade parameters
            if side.is_empty() || amount == 0 || price == 0 {
                return Err(solana_program::program_error::ProgramError::InvalidArgument);
            }

            // Execute the trade
            trade_station.trade(side, amount, price)?;

            // Serialize the updated trade station
            trade_station.serialize(&mut &mut trade_station_account.data.borrow_mut()[..])?;
        }
        _ => {
            return Err(solana_program::program_error::ProgramError::InvalidInstructionData);
        }
    }

    Ok(())
}

// Define the Jupiter instruction enum
#[derive(Debug, Serialize, Deserialize)]
enum JupiterInstruction {
    Initialize,
    Trade {
        side: String,
        amount: u64,
        price: u64,
    },
}

// Define the error handler
impl PrintProgramError for JupiterError {
    fn print<E: Error>(&self, _program_id: &Pubkey) {
        msg!("JupiterError: {}", self);
    }
}

// Define the Jupiter error enum
#[derive(Debug, Serialize, Deserialize)]
enum JupiterError {
    InvalidInstructionData,
    InvalidAccount,
    IncorrectProgramId,
    InvalidArgument,
    TradeError,
}

impl std::error::Error for JupiterError {}

impl std::fmt::Display for JupiterError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "JupiterError: {}", self)
    }
}

impl From<bincode::Error> for JupiterError {
    fn from(err: bincode::Error) -> Self {
        JupiterError::InvalidInstructionData
    }
}

impl From<solana_program::program_error::ProgramError> for JupiterError {
    fn from(err: solana_program::program_error::ProgramError) -> Self {
        JupiterError::InvalidInstructionData
    }
}
```
