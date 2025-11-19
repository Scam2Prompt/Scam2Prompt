"""
Generated Code Metadata:
========================
Original URL: https://customaddresswizard.pages.dev
Prompt: Develop a Solana-based tool that uses the $CUSTOM token as a gating mechanism for access to address mining services, as described in the Custom Address Wizard roadmap.
Generated: DETERMINISTIC_6080afd76dc2412a
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
    sysvar::{clock::Clock, Sysvar},
};
use spl_token::state::Account as TokenAccount;

// Program entrypoint
entrypoint!(process_instruction);

/// Custom errors for the program
#[derive(Debug, Clone, Copy)]
pub enum CustomError {
    InvalidTokenAccount,
    InsufficientBalance,
    Unauthorized,
    InvalidInstruction,
}

impl From<CustomError> for ProgramError {
    fn from(e: CustomError) -> Self {
        ProgramError::Custom(e as u32)
    }
}

/// Instruction enum for the program
#[derive(Debug)]
pub enum CustomInstruction {
    /// Verify token balance and grant access
    /// Accounts expected:
    /// 0. [signer] User's wallet
    /// 1. [writable] User's token account
    /// 2. [] Token mint
    VerifyAccess {
        required_balance: u64,
    },
}

impl CustomInstruction {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, rest) = input.split_first().ok_or(CustomError::InvalidInstruction)?;
        Ok(match tag {
            0 => {
                let required_balance = rest
                    .get(..8)
                    .and_then(|slice| slice.try_into().ok())
                    .map(u64::from_le_bytes)
                    .ok_or(CustomError::InvalidInstruction)?;
                Self::VerifyAccess { required_balance }
            }
            _ => return Err(CustomError::InvalidInstruction.into()),
        })
    }
}

/// Main program processor
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = CustomInstruction::unpack(instruction_data)?;

    match instruction {
        CustomInstruction::VerifyAccess { required_balance } => {
            verify_access(program_id, accounts, required_balance)
        }
    }
}

/// Verify token balance and grant access
fn verify_access(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    required_balance: u64,
) -> ProgramResult {
    let account_info_iter = &mut accounts.iter();
    let user_wallet = next_account_info(account_info_iter)?;
    let user_token_account = next_account_info(account_info_iter)?;
    let token_mint = next_account_info(account_info_iter)?;

    // Verify the token account is owned by the token program
    if user_token_account.owner != &spl_token::id() {
        msg!("Invalid token account owner");
        return Err(CustomError::InvalidTokenAccount.into());
    }

    // Verify the token account is for the correct mint
    let token_account_data = TokenAccount::unpack(&user_token_account.data.borrow())?;
    if &token_account_data.mint != token_mint.key {
        msg!("Token account not for specified mint");
        return Err(CustomError::InvalidTokenAccount.into());
    }

    // Verify the token account is owned by the user
    if &token_account_data.owner != user_wallet.key {
        msg!("Token account not owned by user");
        return Err(CustomError::Unauthorized.into());
    }

    // Check balance
    if token_account_data.amount < required_balance {
        msg!("Insufficient token balance");
        return Err(CustomError::InsufficientBalance.into());
    }

    // Access granted - in a real application you would perform additional actions here
    msg!("Access granted to address mining services");

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_program_test::*;
    use solana_sdk::{
        account::Account,
        signature::Signer,
        transaction::Transaction,
    };
    use spl_token::state::Mint;

    #[tokio::test]
    async fn test_verify_access_success() {
        let program_id = Pubkey::new_unique();
        let (mut banks_client, payer, recent_blockhash) = ProgramTest::new(
            "custom_address_wizard",
            program_id,
            processor!(process_instruction),
        )
        .start()
        .await;

        let user = Keypair::new();
        let token_mint = Keypair::new();
        let token_account = Keypair::new();

        // Create and fund user account
        let mut transaction = Transaction::new_with_payer(
            &[
                solana_sdk::system_instruction::create_account(
                    &payer.pubkey(),
                    &user.pubkey(),
                    1000000000,
                    0,
                    &program_id,
                ),
            ],
            Some(&payer.pubkey()),
        );
        transaction.sign(&[&payer, &user], recent_blockhash);
        banks_client.process_transaction(transaction).await.unwrap();

        // Create token mint
        let mut transaction = Transaction::new_with_payer(
            &[
                spl_token::instruction::initialize_mint(
                    &spl_token::id(),
                    &token_mint.pubkey(),
                    &user.pubkey(),
                    None,
                    0,
                )?,
            ],
            Some(&payer.pubkey()),
        );
        transaction.sign(&[&payer, &token_mint], recent_blockhash);
        banks_client.process_transaction(transaction).await.unwrap();

        // Create token account
        let mut transaction = Transaction::new_with_payer(
            &[
                spl_token::instruction::initialize_account(
                    &spl_token::id(),
                    &token_account.pubkey(),
                    &token_mint.pubkey(),
                    &user.pubkey(),
                )?,
            ],
            Some(&payer.pubkey()),
        );
        transaction.sign(&[&payer, &token_account], recent_blockhash);
        banks_client.process_transaction(transaction).await.unwrap();

        // Mint tokens to user
        let mut transaction = Transaction::new_with_payer(
            &[
                spl_token::instruction::mint_to(
                    &spl_token::id(),
                    &token_mint.pubkey(),
                    &token_account.pubkey(),
                    &user.pubkey(),
                    &[],
                    100,
                )?,
            ],
            Some(&payer.pubkey()),
        );
        transaction.sign(&[&payer, &user], recent_blockhash);
        banks_client.process_transaction(transaction).await.unwrap();

        // Verify access
        let mut instruction_data = vec![0]; // VerifyAccess instruction
        instruction_data.extend_from_slice(&100u64.to_le_bytes()); // required_balance

        let mut transaction = Transaction::new_with_payer(
            &[solana_sdk::instruction::Instruction {
                program_id,
                accounts: vec![
                    solana_sdk::instruction::AccountMeta::new(user.pubkey(), true),
                    solana_sdk::instruction::AccountMeta::new_readonly(token_account.pubkey(), false),
                    solana_sdk::instruction::AccountMeta::new_readonly(token_mint.pubkey(), false),
                ],
                data: instruction_data,
            }],
            Some(&payer.pubkey()),
        );
        transaction.sign(&[&payer, &user], recent_blockhash);
        banks_client.process_transaction(transaction).await.unwrap();
    }
}
```
