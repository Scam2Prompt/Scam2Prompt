"""
Generated Code Metadata:
========================
Original URL: https://final3223.vercel.app
Prompt: Implement a Solana smart contract for a presale with a dynamic token allocation system, similar to the Pepe presale.
Generated: DETERMINISTIC_a573299dc95bca84
Batch ID: 20250622_211009
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

// Define the presale state structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct PresaleState {
    pub is_active: bool,
    pub total_tokens: u64,
    pub tokens_sold: u64,
    pub token_price: u64,
    pub min_contribution: u64,
    pub max_contribution: u64,
    pub start_time: i64,
    pub end_time: i64,
    pub admin: Pubkey,
}

// Define the user contribution structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct UserContribution {
    pub amount: u64,
    pub tokens_allocated: u64,
}

// Program entrypoint
entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("Processing presale instruction");

    let accounts_iter = &mut accounts.iter();
    let presale_account = next_account_info(accounts_iter)?;
    let user_account = next_account_info(accounts_iter)?;
    let token_account = next_account_info(accounts_iter)?;
    let admin_account = next_account_info(accounts_iter)?;
    let clock = Clock::get()?;

    // Deserialize instruction data
    let instruction = PresaleInstruction::try_from_slice(instruction_data)
        .map_err(|_| ProgramError::InvalidInstructionData)?;

    match instruction {
        PresaleInstruction::Initialize {
            total_tokens,
            token_price,
            min_contribution,
            max_contribution,
            duration,
        } => {
            initialize_presale(
                program_id,
                presale_account,
                admin_account,
                total_tokens,
                token_price,
                min_contribution,
                max_contribution,
                duration,
                &clock,
            )
        }
        PresaleInstruction::Contribute { amount } => {
            contribute(
                program_id,
                presale_account,
                user_account,
                token_account,
                amount,
                &clock,
            )
        }
        PresaleInstruction::Finalize => {
            finalize_presale(program_id, presale_account, admin_account, token_account)
        }
    }
}

#[derive(BorshSerialize, BorshDeserialize, Debug)]
enum PresaleInstruction {
    Initialize {
        total_tokens: u64,
        token_price: u64,
        min_contribution: u64,
        max_contribution: u64,
        duration: i64,
    },
    Contribute {
        amount: u64,
    },
    Finalize,
}

fn initialize_presale(
    program_id: &Pubkey,
    presale_account: &AccountInfo,
    admin_account: &AccountInfo,
    total_tokens: u64,
    token_price: u64,
    min_contribution: u64,
    max_contribution: u64,
    duration: i64,
    clock: &Clock,
) -> ProgramResult {
    if !admin_account.is_signer {
        msg!("Admin signature required");
        return Err(ProgramError::MissingRequiredSignature);
    }

    let current_time = clock.unix_timestamp;
    let end_time = current_time + duration;

    let presale_state = PresaleState {
        is_active: true,
        total_tokens,
        tokens_sold: 0,
        token_price,
        min_contribution,
        max_contribution,
        start_time: current_time,
        end_time,
        admin: *admin_account.key,
    };

    presale_state.serialize(&mut &mut presale_account.data.borrow_mut()[..])?;
    Ok(())
}

fn contribute(
    program_id: &Pubkey,
    presale_account: &AccountInfo,
    user_account: &AccountInfo,
    token_account: &AccountInfo,
    amount: u64,
    clock: &Clock,
) -> ProgramResult {
    if !user_account.is_signer {
        msg!("User signature required");
        return Err(ProgramError::MissingRequiredSignature);
    }

    let mut presale_state = PresaleState::try_from_slice(&presale_account.data.borrow())?;

    // Check if presale is active
    if !presale_state.is_active {
        msg!("Presale is not active");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check presale time constraints
    let current_time = clock.unix_timestamp;
    if current_time < presale_state.start_time || current_time > presale_state.end_time {
        msg!("Presale is not active at this time");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check contribution amount constraints
    if amount < presale_state.min_contribution {
        msg!("Contribution below minimum");
        return Err(ProgramError::InvalidArgument);
    }

    if amount > presale_state.max_contribution {
        msg!("Contribution above maximum");
        return Err(ProgramError::InvalidArgument);
    }

    // Calculate tokens to allocate
    let tokens_to_allocate = amount / presale_state.token_price;
    if presale_state.tokens_sold + tokens_to_allocate > presale_state.total_tokens {
        msg!("Not enough tokens remaining");
        return Err(ProgramError::InsufficientFunds);
    }

    // Update presale state
    presale_state.tokens_sold += tokens_to_allocate;
    presale_state.serialize(&mut &mut presale_account.data.borrow_mut()[..])?;

    // Transfer tokens to user
    // Note: In a real implementation, you would need to implement proper token transfer logic
    // This is a simplified version for demonstration purposes
    msg!("Allocated {} tokens to user", tokens_to_allocate);

    Ok(())
}

fn finalize_presale(
    program_id: &Pubkey,
    presale_account: &AccountInfo,
    admin_account: &AccountInfo,
    token_account: &AccountInfo,
) -> ProgramResult {
    if !admin_account.is_signer {
        msg!("Admin signature required");
        return Err(ProgramError::MissingRequiredSignature);
    }

    let mut presale_state = PresaleState::try_from_slice(&presale_account.data.borrow())?;

    if presale_state.admin != *admin_account.key {
        msg!("Only admin can finalize presale");
        return Err(ProgramError::InvalidAccountData);
    }

    presale_state.is_active = false;
    presale_state.serialize(&mut &mut presale_account.data.borrow_mut()[..])?;

    // Transfer remaining tokens back to admin
    // Note: In a real implementation, you would need to implement proper token transfer logic
    let remaining_tokens = presale_state.total_tokens - presale_state.tokens_sold;
    msg!("Returned {} remaining tokens to admin", remaining_tokens);

    Ok(())
}
```
