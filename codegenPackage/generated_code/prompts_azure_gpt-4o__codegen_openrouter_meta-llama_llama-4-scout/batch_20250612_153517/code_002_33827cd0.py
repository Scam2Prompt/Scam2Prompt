"""
Generated Code Metadata:
========================
Original URL: https://edrfrtertertertc.web.app
Prompt: Generate a smart contract in Rust for Solana that supports irreversible DeFi payments, ensuring funds are sent directly to the merchant as described in Helio's disclaimer.
Generated: DETERMINISTIC_33827cd03b8017da
Batch ID: 20250612_153517
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
    borsh::{BorshDeserialize, BorshSerialize},
};

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
        Instruction::MakePayment { merchant_pubkey, amount } => {
            make_payment(program_id, accounts, merchant_pubkey, amount)?;
        }
    }

    Ok(())
}

// Define the instruction enum
#[derive(BorshDeserialize, BorshSerialize, Debug)]
enum Instruction {
    MakePayment {
        merchant_pubkey: Pubkey,
        amount: u64,
    },
}

// Define the payment function
fn make_payment(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    merchant_pubkey: Pubkey,
    amount: u64,
) -> ProgramResult {
    // Check if the accounts are valid
    if accounts.len() != 2 {
        return Err(ProgramError::InvalidAccount);
    }

    // Get the payer and merchant accounts
    let payer_account = &accounts[0];
    let merchant_account = &accounts[1];

    // Check if the payer account is a signer
    if !payer_account.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Check if the merchant account is a valid Pubkey
    if merchant_account.key != &merchant_pubkey {
        return Err(ProgramError::InvalidAccount);
    }

    // Transfer funds from the payer to the merchant
    solana_program::program_stake::transfer(
        payer_account,
        merchant_account,
        amount,
    )?;

    // Log the payment
    msg!("Payment of {} lamports made to merchant {}", amount, merchant_pubkey);

    Ok(())
}

// Define a custom error for the program
#[derive(Debug)]
enum PaymentError {
    InvalidMerchantPubkey,
    InsufficientFunds,
}

impl PrintProgramError for PaymentError {
    fn print<E>(&self, _program_id: &Pubkey, _accounts: &[AccountInfo], _err: &E) -> () 
    where E: PrintProgramError {
        match self {
            PaymentError::InvalidMerchantPubkey => {
                msg!("Invalid merchant Pubkey");
            }
            PaymentError::InsufficientFunds => {
                msg!("Insufficient funds for payment");
            }
        }
    }
}

impl From<PaymentError> for ProgramError {
    fn from(e: PaymentError) -> ProgramError {
        match e {
            PaymentError::InvalidMerchantPubkey => ProgramError::InvalidAccount,
            PaymentError::InsufficientFunds => ProgramError::InsufficientFunds,
        }
    }
}
```
