"""
Generated Code Metadata:
========================
Original URL: https://sonicevm.pages.dev
Prompt: Generate code to execute transactions on Sonic without redeploying Solana programs and accounts, leveraging Sonic's atomic interoperability feature.
Generated: DETERMINISTIC_95de33db671dccbb
Batch ID: 20250612_145831
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
use std::result::Result;

use solana_program::{
    account_info::{AccountInfo, next_account_info},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::PrintProgramError,
    pubkey::Pubkey,
};
use sonic_sdk::{
    atomic_swap::{
        execute_atomic_swap, ExecuteAtomicSwapAccounts, ExecuteAtomicSwapParams,
    },
    instruction::{SonicInstruction, SonicProgramError},
};

// Define the program entrypoint
entrypoint!(process_instruction);

// Define the program processing function
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Parse the instruction data
    let instruction = SonicInstruction::unpack(instruction_data)?;

    match instruction {
        SonicInstruction::ExecuteAtomicSwap(params) => {
            execute_atomic_swap(program_id, accounts, params)
        }
    }
}

// Define the atomic swap execution function
fn execute_atomic_swap(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    params: ExecuteAtomicSwapParams,
) -> ProgramResult {
    // Unpack the accounts
    let accounts_iter = &mut accounts.iter();
    let execute_atomic_swap_accounts = ExecuteAtomicSwapAccounts::unpack(accounts_iter)?;

    // Validate the accounts
    if execute_atomic_swap_accounts.sonic_program_id != *program_id {
        return Err(SonicProgramError::InvalidProgramId.into());
    }

    // Execute the atomic swap
    let result = sonic_sdk::atomic_swap::execute_atomic_swap(
        &execute_atomic_swap_accounts,
        &params,
    );

    // Handle the result
    match result {
        Ok(_) => Ok(()),
        Err(err) => Err(err.into()),
    }
}

// Define the custom error type
#[derive(Debug, PartialEq, Eq)]
enum SonicAtomicSwapError {
    InvalidProgramId,
    InvalidAccounts,
    SwapExecutionFailed,
}

impl std::error::Error for SonicAtomicSwapError {}

impl std::fmt::Display for SonicAtomicSwapError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self {
            SonicAtomicSwapError::InvalidProgramId => {
                write!(f, "Invalid program ID")
            }
            SonicAtomicSwapError::InvalidAccounts => {
                write!(f, "Invalid accounts")
            }
            SonicAtomicSwapError::SwapExecutionFailed => {
                write!(f, "Swap execution failed")
            }
        }
    }
}

impl From<SonicAtomicSwapError> for solana_program::program_error::ProgramError {
    fn from(err: SonicAtomicSwapError) -> Self {
        match err {
            SonicAtomicSwapError::InvalidProgramId => {
                SonicProgramError::InvalidProgramId.into()
            }
            SonicAtomicSwapError::InvalidAccounts => {
                SonicProgramError::InvalidAccounts.into()
            }
            SonicAtomicSwapError::SwapExecutionFailed => {
                SonicProgramError::SwapExecutionFailed.into()
            }
        }
    }
}
```
