"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helio-nine.web.app
Prompt: Write a smart contract for processing payments directly to merchants on the Solana network, referencing the Helio platform's payment flow.
Generated: DETERMINISTIC_c107222534de5d40
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Smart Contract for processing payments directly to merchants on the Solana network using the Helio platform's payment flow.
// This contract is written in Rust using the Solana Program Library.

use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    pubkey::Pubkey,
    program_error::ProgramError,
    program_pack::{IsInitialized, Pack},
    system_instruction,
    sysvar::{rent::Rent, Sysvar},
};

// Define the entry point of the program.
entrypoint!(process_instruction);

/// Main function that handles incoming instructions
///
/// # Arguments:
/// * `program_id` - The program ID of this smart contract.
/// * `accounts` - The accounts involved in the transaction.
/// * `instruction_data` - Data sent along with the instruction.
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("Processing payment...");

    // Ensure instruction data is not empty
    if instruction_data.is_empty() {
        msg!("Instruction data is empty!");
        return Err(ProgramError::InvalidInstructionData);
    }

    // Determine the payment amount
    let payment_amount = parse_payment_amount(instruction_data)?;

    // Validate accounts and extract payer and merchant accounts
    let accounts_iter = &mut accounts.iter();
    let payer_account = next_account_info(accounts_iter)?;
    let merchant_account = next_account_info(accounts_iter)?;

    // Check if payer has enough balance
    if **payer_account.lamports.borrow() < payment_amount {
        msg!("Payer does not have enough balance.");
        return Err(ProgramError::InsufficientFunds);
    }

    // Transfer funds from payer to merchant
    msg!("Initiating fund transfer...");
    transfer_funds(payer_account, merchant_account, payment_amount)?;

    msg!("Payment processed successfully.");
    Ok(())
}

/// Parses the payment amount from instruction data.
///
/// # Arguments:
/// * `instruction_data` - Data sent along with the instruction.
///
/// # Returns:
/// * `Result<u64, ProgramError>` - The payment amount or an error.
fn parse_payment_amount(instruction_data: &[u8]) -> Result<u64, ProgramError> {
    if instruction_data.len() != 8 {
        msg!("Instruction data should be exactly 8 bytes for payment amount.");
        return Err(ProgramError::InvalidInstructionData);
    }

    let amount_array: [u8; 8] = instruction_data.try_into().map_err(|_| ProgramError::InvalidInstructionData)?;
    Ok(u64::from_le_bytes(amount_array))
}

/// Transfers funds from one account to another.
///
/// # Arguments:
/// * `payer` - Account of the payer.
/// * `merchant` - Account of the merchant.
/// * `amount` - Amount to transfer.
///
/// # Returns:
/// * `ProgramResult` - Result of the transfer.
fn transfer_funds(
    payer: &AccountInfo,
    merchant: &AccountInfo,
    amount: u64,
) -> ProgramResult {
    let rent = Rent::get()?;
    if !rent.is_exempt(merchant.lamports(), merchant.data_len()) {
        msg!("Merchant account is not rent exempt!");
        return Err(ProgramError::InvalidAccountData);
    }

    let payer_starting_balance = **payer.lamports.borrow();
    let merchant_starting_balance = **merchant.lamports.borrow();

    **payer.lamports.borrow_mut() = payer_starting_balance.checked_sub(amount).ok_or(ProgramError::InsufficientFunds)?;
    **merchant.lamports.borrow_mut() = merchant_starting_balance.checked_add(amount).ok_or(ProgramError::InvalidInstructionData)?;

    Ok(())
}
```

This code defines a Solana smart contract that processes payments directly from a payer to a merchant. It includes error handling, validates inputs, checks for sufficient funds, and ensures the merchant's account is rent-exempt. Follow deployment guidelines for Solana programs to deploy this code.
