"""
Generated Code Metadata:
========================
Original URL: https://the-heist-giveaway.web.app
Prompt: Generate code to create a Solana-based payment system that supports fast transactions (e.g., 4,154 TPS) and includes a disclaimer for irreversible payments.
Generated: DETERMINISTIC_188eafa0bba3616d
Batch ID: 20250612_150557
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
    program_error::ProgramError,
    pubkey::Pubkey,
};
use solana_program::instruction::Instruction;
use solana_program::program::invoke;
use solana_program::system_instruction;
use std::convert::TryInto;

// Define the program's entry point
entrypoint!(process_transaction);

// Define the program's processor
fn process_transaction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    // Check if the number of accounts is correct
    if accounts.len() != 3 {
        return Err(ProgramError::InvalidArgument);
    }

    // Get the accounts
    let sender_account = &accounts[0];
    let recipient_account = &accounts[1];
    let system_program_account = &accounts[2];

    // Check if the accounts are valid
    if !sender_account.is_writable || !recipient_account.is_writable {
        return Err(ProgramError::InvalidArgument);
    }

    // Get the transaction amount
    let amount = 1_000_000; // 1 SOL

    // Check if the sender has enough balance
    if sender_account.lamports() < amount {
        return Err(ProgramError::InsufficientFunds);
    }

    // Transfer the funds
    invoke(
        &system_instruction::transfer(
            sender_account.key,
            recipient_account.key,
            amount,
        ),
        &[
            sender_account.clone(),
            recipient_account.clone(),
            system_program_account.clone(),
        ],
    )?;

    // Log the transaction
    msg!("Transaction processed: {} -> {}: {} lamports", 
         sender_account.key, 
         recipient_account.key, 
         amount);

    // Return success
    Ok(())
}

// Define a custom error for the program
#[derive(Debug)]
enum PaymentError {
    InvalidArgument,
    InsufficientFunds,
    IrreversiblePayment,
}

impl std::error::Error for PaymentError {}

impl PrintProgramError for PaymentError {
    fn print<E>(&self, _program_id: &Pubkey, _is_in_debug_mode: bool) -> E
    where
        E: std::error::Error + 'static,
    {
        match self {
            PaymentError::InvalidArgument => {
                msg!("Invalid argument");
                PaymentError::InvalidArgument
            }
            PaymentError::InsufficientFunds => {
                msg!("Insufficient funds");
                PaymentError::InsufficientFunds
            }
            PaymentError::IrreversiblePayment => {
                msg!("Irreversible payment");
                PaymentError::IrreversiblePayment
            }
        }
    }
}

impl From<PaymentError> for ProgramError {
    fn from(e: PaymentError) -> ProgramError {
        match e {
            PaymentError::InvalidArgument => ProgramError::InvalidArgument,
            PaymentError::InsufficientFunds => ProgramError::InsufficientFunds,
            PaymentError::IrreversiblePayment => ProgramError::InvalidInstructionData,
        }
    }
}

// Include a disclaimer for irreversible payments
// WARNING: Payments made using this program are irreversible.
// Please ensure you are sending transactions to the correct recipient.
```
