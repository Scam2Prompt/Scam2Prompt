"""
Generated Code Metadata:
========================
Original URL: https://wl-bread.web.app
Prompt: Create a Solana-based smart contract that enforces whitelist minting rights for token holders, inspired by the Bread Whitelist Mint process.
Generated: DETERMINISTIC_2853b0778234d833
Batch ID: 20250612_152358
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

// Whitelist mint program
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    // Get account iterator
    let accounts_iter = &mut accounts.iter();

    // Get required accounts
    let whitelist_token_account = next_account_info(accounts_iter)?;
    let user_token_account = next_account_info(accounts_iter)?;
    let user = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;
    let clock = Clock::get()?;

    // Verify accounts
    if !user.is_signer {
        msg!("User must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Deserialize token accounts
    let whitelist_token_data = TokenAccount::unpack(&whitelist_token_account.data.borrow())?;
    let user_token_data = TokenAccount::unpack(&user_token_account.data.borrow())?;

    // Check if user holds the whitelist token
    if whitelist_token_data.mint != user_token_data.mint {
        msg!("User does not hold the required whitelist token");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if user owns the token account
    if user_token_data.owner != *user.key {
        msg!("User does not own the token account");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if token account has sufficient balance (at least 1 token)
    if user_token_data.amount < 1 {
        msg!("User does not have sufficient token balance");
        return Err(ProgramError::InsufficientFunds);
    }

    // Check if minting period is active (example: between Unix timestamps)
    let current_timestamp = clock.unix_timestamp;
    let mint_start_timestamp = 1635724800; // Nov 1, 2021 00:00:00 UTC
    let mint_end_timestamp = 1638316800;   // Dec 1, 2021 00:00:00 UTC

    if current_timestamp < mint_start_timestamp {
        msg!("Minting has not started yet");
        return Err(ProgramError::InvalidInstructionData);
    }

    if current_timestamp > mint_end_timestamp {
        msg!("Minting period has ended");
        return Err(ProgramError::InvalidInstructionData);
    }

    // If all checks pass, allow minting
    msg!("User is whitelisted and can mint");
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
    use spl_token::state::{Account, Mint};

    #[tokio::test]
    async fn test_whitelist_mint() {
        let program_id = Pubkey::new_unique();
        let mut program_test = ProgramTest::new(
            "whitelist_mint",
            program_id,
            processor!(process_instruction),
        );

        // Setup test accounts
        let (mut banks_client, payer, recent_blockhash) = program_test.start().await;

        // Create test token mint
        let token_mint = Pubkey::new_unique();
        let mint_account = Account {
            lamports: 1000000000,
            data: Mint {
                mint_authority: Some(payer.pubkey()).into(),
                supply: 1000,
                decimals: 0,
                is_initialized: true,
                freeze_authority: Some(payer.pubkey()).into(),
            }
            .pack(),
            owner: spl_token::id(),
            executable: false,
            rent_epoch: Epoch::default(),
        };

        // Create whitelist token account
        let whitelist_token_account = Pubkey::new_unique();
        let whitelist_account = Account {
            lamports: 1000000000,
            data: Account {
                mint: token_mint,
                owner: payer.pubkey(),
                amount: 1,
                delegate: None,
                state: spl_token::state::AccountState::Initialized,
                is_native: None,
                delegated_amount: 0,
                close_authority: None,
            }
            .pack(),
            owner: spl_token::id(),
            executable: false,
            rent_epoch: Epoch::default(),
        };

        // Create user token account
        let user_token_account = Pubkey::new_unique();
        let user_account = Account {
            lamports: 1000000000,
            data: Account {
                mint: token_mint,
                owner: payer.pubkey(),
                amount: 1,
                delegate: None,
                state: spl_token::state::AccountState::Initialized,
                is_native: None,
                delegated_amount: 0,
                close_authority: None,
            }
            .pack(),
            owner: spl_token::id(),
            executable: false,
            rent_epoch: Epoch::default(),
        };

        // Add accounts to program test
        program_test.add_account(token_mint, mint_account);
        program_test.add_account(whitelist_token_account, whitelist_account);
        program_test.add_account(user_token_account, user_account);

        // Create transaction
        let mut transaction = Transaction::new_with_payer(
            &[solana_program::instruction::Instruction {
                program_id,
                accounts: vec![
                    solana_sdk::instruction::AccountMeta::new(whitelist_token_account, false),
                    solana_sdk::instruction::AccountMeta::new(user_token_account, false),
                    solana_sdk::instruction::AccountMeta::new(payer.pubkey(), true),
                    solana_sdk::instruction::AccountMeta::new_readonly(spl_token::id(), false),
                ],
                data: vec![],
            }],
            Some(&payer.pubkey()),
        );

        transaction.sign(&[&payer], recent_blockhash);

        // Process transaction
        banks_client.process_transaction(transaction).await.unwrap();
    }
}
```
