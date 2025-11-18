"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helioxdrop.web.app
Prompt: Develop a smart contract to facilitate token swaps and payments on the Solana network, incorporating Helio's merchant-first approach.
Generated: DETERMINISTIC_9c5aa87ef11907d5
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Smart Contract for Token Swaps and Payments on the Solana Network
// This contract is designed with Helio's merchant-first approach.

// Import necessary Solana libraries and dependencies
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program::{invoke, invoke_signed},
    program_error::ProgramError,
    program_pack::{IsInitialized, Pack},
    pubkey::Pubkey,
    system_instruction,
};
use spl_token::state::Account as TokenAccount;

// Declare the entrypoint of the smart contract
entrypoint!(process_instruction);

// Main processing function for the smart contract
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("Starting token swap or payment...");

    // Parse incoming accounts
    let accounts_iter = &mut accounts.iter();
    let payer_account = next_account_info(accounts_iter)?; // Account initiating the transaction
    let merchant_account = next_account_info(accounts_iter)?; // Merchant receiving payment
    let payer_token_account = next_account_info(accounts_iter)?; // Payer's token account
    let merchant_token_account = next_account_info(accounts_iter)?; // Merchant's token account
    let token_program_account = next_account_info(accounts_iter)?; // SPL Token Program

    // Ensure all accounts are valid and have required permissions
    if !payer_account.is_signer {
        msg!("Payer account must be a signer.");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Decode instruction data (amount and token type)
    let (amount, token_type) = decode_instruction_data(instruction_data)?;

    // Perform a token transfer (swap or payment)
    invoke(
        &spl_token::instruction::transfer(
            token_program_account.key,
            payer_token_account.key,
            merchant_token_account.key,
            payer_account.key,
            &[payer_account.key],
            amount,
        )?,
        &[
            payer_account.clone(),
            payer_token_account.clone(),
            merchant_token_account.clone(),
            token_program_account.clone(),
        ],
    )?;

    msg!(
        "Successfully transferred {} units of token type {} from {} to {}.",
        amount,
        token_type,
        payer_account.key,
        merchant_account.key
    );

    Ok(())
}

// Helper function to decode instruction data
fn decode_instruction_data(data: &[u8]) -> Result<(u64, String), ProgramError> {
    if data.len() < 8 {
        msg!("Invalid instruction data length.");
        return Err(ProgramError::InvalidInstructionData);
    }

    // Extract amount (u64) and token type (UTF-8 string)
    let amount = u64::from_le_bytes(data[0..8].try_into().unwrap()); // First 8 bytes: amount
    let token_type = String::from_utf8(data[8..].to_vec()).map_err(|_| ProgramError::InvalidInstructionData)?; // Remaining bytes: token type

    Ok((amount, token_type))
}
```
