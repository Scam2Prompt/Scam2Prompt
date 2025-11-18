"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimprize-17.web.app
Prompt: Develop a smart contract on Solana that automates the distribution of DUST tokens to eligible wallets during an airdrop.
Generated: DETERMINISTIC_d70b8136d15b62d1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// This is a smart contract for the Solana blockchain designed to automate the distribution of DUST tokens during an airdrop.
// The contract follows best practices and includes proper error handling.

use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    program::invoke,
    program_error::ProgramError,
    pubkey::Pubkey,
    system_instruction,
};
use spl_token::instruction as token_instruction;

entrypoint!(process_instruction);

/// Entry point for the smart contract.
fn process_instruction(
    program_id: &Pubkey, // The program ID of the contract.
    accounts: &[AccountInfo], // Accounts involved in the transaction.
    _instruction_data: &[u8], // Instruction data (not used in this implementation for simplicity).
) -> ProgramResult {
    let account_iter = &mut accounts.iter();

    // Extract and validate accounts.
    let distributor_wallet = next_account_info(account_iter)?; // Wallet distributing DUST tokens.
    if !distributor_wallet.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    let token_mint = next_account_info(account_iter)?; // Mint account for the DUST token.
    let recipient_wallet = next_account_info(account_iter)?; // The wallet receiving DUST tokens.
    let recipient_token_account = next_account_info(account_iter)?; // Token account of the recipient.

    let token_program = next_account_info(account_iter)?; // SPL Token program ID.
    if token_program.key != &spl_token::id() {
        return Err(ProgramError::InvalidAccountData);
    }

    let system_program = next_account_info(account_iter)?; // System program ID for creating associated accounts.

    // Define the amount of DUST tokens to be distributed in the airdrop.
    let airdrop_amount: u64 = 1000; // Example: 1000 DUST tokens.

    // Check if the recipient's token account exists; if not, create it.
    if recipient_token_account.lamports() == 0 {
        invoke(
            &system_instruction::create_account(
                distributor_wallet.key, // Funding the account from the distributor wallet.
                recipient_token_account.key, // Address of the recipient token account.
                system_program.key,          // System program for account creation.
                spl_token::state::Account::LEN as u64, // Minimum rent-exempt balance.
                spl_token::id(),             // SPL Token program ID.
            ),
            &[
                distributor_wallet.clone(),
                recipient_token_account.clone(),
                system_program.clone(),
            ],
        )?;
    }

    // Transfer DUST tokens from the distributor wallet to the recipient's token account.
    invoke(
        &token_instruction::transfer(
            token_program.key, // SPL Token program ID.
            distributor_wallet.key, // Source wallet (distributor).
            recipient_token_account.key, // Destination wallet (recipient).
            distributor_wallet.key, // Authority to transfer tokens.
            &[],                     // No multisignature required.
            airdrop_amount,          // Amount to transfer.
        )?,
        &[
            distributor_wallet.clone(),
            recipient_token_account.clone(),
            token_program.clone(),
        ],
    )?;

    Ok(())
}
```
