"""
Generated Code Metadata:
========================
Original URL: https://homeworkproject.vercel.app
Prompt: Generate a smart contract in Rust for the Solana blockchain that handles whitelist claims, ensuring the total price is calculated dynamically based on the number of tickets claimed.
Generated: DETERMINISTIC_6b2067b55207b2fc
Batch ID: 20250612_153647
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
use borsh::{BorshDeserialize, BorshSerialize};

// Define the program ID
solana_program::declare_id!("WhitelistClaim11111111111111111111111111111");

// Constants
const TICKET_PRICE: u64 = 1_000_000; // 1 SOL in lamports
const MAX_CLAIMS_PER_USER: u64 = 5;

// Account state structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct WhitelistClaim {
    pub is_initialized: bool,
    pub admin: Pubkey,
    pub total_claimed: u64,
    pub user_claims: Vec<UserClaim>,
}

#[derive(BorshSerialize, BorshDeserialize, Debug, Clone)]
pub struct UserClaim {
    pub user: Pubkey,
    pub claimed_count: u64,
}

// Instruction enum
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum WhitelistClaimInstruction {
    Initialize { admin: Pubkey },
    ClaimTickets { amount: u64 },
}

// Entrypoint
entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = WhitelistClaimInstruction::try_from_slice(instruction_data)
        .map_err(|_| ProgramError::InvalidInstructionData)?;

    match instruction {
        WhitelistClaimInstruction::Initialize { admin } => {
            initialize(program_id, accounts, admin)
        }
        WhitelistClaimInstruction::ClaimTickets { amount } => {
            claim_tickets(program_id, accounts, amount)
        }
    }
}

// Initialize the whitelist claim account
fn initialize(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    admin: Pubkey,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let whitelist_account = next_account_info(accounts_iter)?;
    let payer = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Verify the account is owned by the program
    if whitelist_account.owner != program_id {
        msg!("Whitelist account does not have the correct program id");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Initialize the whitelist claim state
    let mut whitelist_data = WhitelistClaim {
        is_initialized: true,
        admin,
        total_claimed: 0,
        user_claims: Vec::new(),
    };

    whitelist_data.serialize(&mut &mut whitelist_account.data.borrow_mut()[..])?;
    Ok(())
}

// Claim tickets function
fn claim_tickets(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    amount: u64,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let whitelist_account = next_account_info(accounts_iter)?;
    let user_account = next_account_info(accounts_iter)?;
    let user_token_account = next_account_info(accounts_iter)?;
    let admin_token_account = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;
    let clock = Clock::get()?;

    // Verify the account is owned by the program
    if whitelist_account.owner != program_id {
        msg!("Whitelist account does not have the correct program id");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize the whitelist data
    let mut whitelist_data = WhitelistClaim::try_from_slice(&whitelist_account.data.borrow())?;
    if !whitelist_data.is_initialized {
        msg!("Whitelist account is not initialized");
        return Err(ProgramError::UninitializedAccount);
    }

    // Check if user has already claimed
    let user_claim_index = whitelist_data.user_claims.iter().position(|x| x.user == *user_account.key);
    let mut user_claim = match user_claim_index {
        Some(index) => whitelist_data.user_claims[index].clone(),
        None => UserClaim {
            user: *user_account.key,
            claimed_count: 0,
        },
    };

    // Validate claim amount
    if amount == 0 || amount > MAX_CLAIMS_PER_USER {
        msg!("Invalid claim amount");
        return Err(ProgramError::InvalidArgument);
    }

    if user_claim.claimed_count + amount > MAX_CLAIMS_PER_USER {
        msg!("Exceeds maximum claims per user");
        return Err(ProgramError::InvalidArgument);
    }

    // Calculate total price
    let total_price = amount.checked_mul(TICKET_PRICE)
        .ok_or(ProgramError::ArithmeticOverflow)?;

    // Transfer tokens from user to admin
    solana_program::program::invoke(
        &spl_token::instruction::transfer(
            token_program.key,
            user_token_account.key,
            admin_token_account.key,
            user_account.key,
            &[],
            total_price,
        )?,
        &[
            user_token_account.clone(),
            admin_token_account.clone(),
            user_account.clone(),
            token_program.clone(),
        ],
    )?;

    // Update user claim
    user_claim.claimed_count += amount;
    if let Some(index) = user_claim_index {
        whitelist_data.user_claims[index] = user_claim;
    } else {
        whitelist_data.user_claims.push(user_claim);
    }

    // Update total claimed
    whitelist_data.total_claimed += amount;

    // Save the updated state
    whitelist_data.serialize(&mut &mut whitelist_account.data.borrow_mut()[..])?;

    msg!("Successfully claimed {} tickets for {} lamports", amount, total_price);
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_sdk::{account_info::AccountInfo, signature::Signer, signer::keypair::Keypair};
    use std::mem;

    #[test]
    fn test_initialize() {
        let program_id = Pubkey::new_unique();
        let admin = Keypair::new();
        let mut whitelist_data = vec![0; mem::size_of::<WhitelistClaim>()];
        let mut lamports = 100;

        let whitelist_account = AccountInfo::new(
            &Pubkey::new_unique(),
            false,
            true,
            &mut lamports,
            &mut whitelist_data,
            &program_id,
            false,
            Epoch::default(),
        );

        let payer = Keypair::new();
        let mut payer_lamports = 100;
        let payer_account = AccountInfo::new(
            &payer.pubkey(),
            true,
            false,
            &mut payer_lamports,
            &mut [],
            &program_id,
            false,
            Epoch::default(),
        );

        let system_program = AccountInfo::new(
            &solana_program::system_program::id(),
            false,
            false,
            &mut 0,
            &mut [],
            &solana_program::system_program::id(),
            false,
            Epoch::default(),
        );

        let accounts = vec![
            whitelist_account,
            payer_account,
            system_program,
        ];

        let instruction = WhitelistClaimInstruction::Initialize {
            admin: admin.pubkey(),
        };

        let mut instruction_data = vec![];
        instruction.serialize(&mut instruction_data).unwrap();

        process_instruction(&program_id, &accounts, &instruction_data).unwrap();

        let whitelist_data = WhitelistClaim::try_from_slice(&whitelist_data).unwrap();
        assert!(whitelist_data.is_initialized);
        assert_eq!(whitelist_data.admin, admin.pubkey());
        assert_eq!(whitelist_data.total_claimed, 0);
        assert!(whitelist_data.user_claims.is_empty());
    }
}
```
