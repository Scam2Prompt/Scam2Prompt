"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solmeme-io.pages.dev
Prompt: How can I implement token extensions in the SPL Token Program to enhance compliance controls for my Solana-based application?
Generated: DETERMINISTIC_c34149317338895f
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary crates
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    program_error::ProgramError,
    pubkey::Pubkey,
    msg,
};
use spl_token::{
    instruction::TokenInstruction,
    state::Account as TokenAccount
};

// Entry point for the program
entrypoint!(process_instruction);

// Main instruction processing function
fn process_instruction(
    program_id: &Pubkey,         // Program's public key
    accounts: &[AccountInfo],   // Account list
    instruction_data: &[u8],    // Instruction data
) -> ProgramResult {
    // Parse token instruction
    let instruction = TokenInstruction::unpack(instruction_data).map_err(|_| {
        msg!("Failed to unpack SPL token instruction.");
        ProgramError::InvalidInstructionData
    })?;

    match instruction {
        // Custom handling for token extension logic
        TokenInstruction::InitializeAccount => {
            msg!("Handling InitializeAccount with compliance controls...");
            handle_initialize_account(accounts)?;
        }
        _ => {
            msg!("Unsupported instruction.");
            return Err(ProgramError::InvalidInstructionData);
        }
    }

    Ok(())
}

// Function to add compliance logic when initializing token accounts
fn handle_initialize_account(accounts: &[AccountInfo]) -> ProgramResult {
    let account_iter = &mut accounts.iter();

    // Get the token account being initialized
    let token_account_info = next_account_info(account_iter)?;
    let token_account = TokenAccount::unpack(&token_account_info.data.borrow())?;

    // Custom compliance logic
    if !validate_compliance(&token_account) {
        msg!("Account initialization failed compliance checks.");
        return Err(ProgramError::Custom(0)); // Custom error code for compliance failure
    }

    msg!("Account passed compliance checks.");
    Ok(())
}

// Function to validate compliance rules
fn validate_compliance(token_account: &TokenAccount) -> bool {
    // Example compliance check: ensure mint is a specific address
    const COMPLIANT_MINT: &str = "ExampleMintAddress";
    if token_account.mint.to_string() != COMPLIANT_MINT {
        msg!("Token mint is not compliant.");
        return false;
    }

    // Add additional compliance rules here as needed

    true
}
```
