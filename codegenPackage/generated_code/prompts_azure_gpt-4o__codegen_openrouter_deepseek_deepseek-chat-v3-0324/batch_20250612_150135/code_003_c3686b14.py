"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Create a smart contract in Rust for the Solana blockchain that facilitates decentralized funding for entrepreneurs, inspired by the Viva La Libertad Project's mission.
Generated: DETERMINISTIC_c3686b1444f13ffe
Batch ID: 20250612_150135
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
    system_instruction,
    sysvar::{clock::Clock, Sysvar},
};
use std::convert::TryInto;

// Define the program's state structure
#[derive(Debug)]
pub struct FundingProject {
    pub entrepreneur: Pubkey,
    pub target_amount: u64,
    pub raised_amount: u64,
    pub contributors: Vec<Pubkey>,
    pub is_active: bool,
    pub deadline: i64,
}

// Define program instructions
#[derive(Debug)]
pub enum FundingInstruction {
    /// Initialize a new funding project
    /// Accounts expected:
    /// 0. [signer] Entrepreneur account
    /// 1. [writable] Funding project account
    /// 2. [] System program
    Initialize {
        target_amount: u64,
        duration_days: u64,
    },
    /// Contribute to a funding project
    /// Accounts expected:
    /// 0. [signer] Contributor account
    /// 1. [writable] Funding project account
    /// 2. [writable] Contributor's funding account
    /// 3. [] System program
    Contribute {
        amount: u64,
    },
    /// Withdraw funds if target is met
    /// Accounts expected:
    /// 0. [signer] Entrepreneur account
    /// 1. [writable] Funding project account
    /// 2. [writable] Entrepreneur's funding account
    WithdrawFunds,
    /// Refund contributors if target not met
    /// Accounts expected:
    /// 0. [signer] Contributor account
    /// 1. [writable] Funding project account
    /// 2. [writable] Contributor's funding account
    ClaimRefund,
}

impl FundingInstruction {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, rest) = input.split_first().ok_or(ProgramError::InvalidInstructionData)?;
        Ok(match tag {
            0 => {
                let target_amount = rest
                    .get(..8)
                    .and_then(|slice| slice.try_into().ok())
                    .map(u64::from_le_bytes)
                    .ok_or(ProgramError::InvalidInstructionData)?;
                let duration_days = rest
                    .get(8..16)
                    .and_then(|slice| slice.try_into().ok())
                    .map(u64::from_le_bytes)
                    .ok_or(ProgramError::InvalidInstructionData)?;
                Self::Initialize {
                    target_amount,
                    duration_days,
                }
            }
            1 => {
                let amount = rest
                    .get(..8)
                    .and_then(|slice| slice.try_into().ok())
                    .map(u64::from_le_bytes)
                    .ok_or(ProgramError::InvalidInstructionData)?;
                Self::Contribute { amount }
            }
            2 => Self::WithdrawFunds,
            3 => Self::ClaimRefund,
            _ => return Err(ProgramError::InvalidInstructionData),
        })
    }
}

// Program entrypoint
entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = FundingInstruction::unpack(instruction_data)?;

    match instruction {
        FundingInstruction::Initialize {
            target_amount,
            duration_days,
        } => initialize_project(program_id, accounts, target_amount, duration_days),
        FundingInstruction::Contribute { amount } => contribute(program_id, accounts, amount),
        FundingInstruction::WithdrawFunds => withdraw_funds(program_id, accounts),
        FundingInstruction::ClaimRefund => claim_refund(program_id, accounts),
    }
}

// Initialize a new funding project
fn initialize_project(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    target_amount: u64,
    duration_days: u64,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let entrepreneur = next_account_info(accounts_iter)?;
    let funding_account = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Verify entrepreneur is signer
    if !entrepreneur.is_signer {
        msg!("Entrepreneur must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Verify funding account is owned by the program
    if funding_account.owner != program_id {
        msg!("Funding account must be owned by the program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Calculate deadline from current time
    let clock = Clock::get()?;
    let deadline = clock.unix_timestamp + (duration_days as i64 * 86400);

    // Initialize project data
    let project = FundingProject {
        entrepreneur: *entrepreneur.key,
        target_amount,
        raised_amount: 0,
        contributors: Vec::new(),
        is_active: true,
        deadline,
    };

    // Serialize and store project data
    let mut data = funding_account.try_borrow_mut_data()?;
    bincode::serialize_into(&mut data[..], &project)?;

    Ok(())
}

// Contribute to a funding project
fn contribute(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    amount: u64,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let contributor = next_account_info(accounts_iter)?;
    let funding_account = next_account_info(accounts_iter)?;
    let contributor_funding = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Verify contributor is signer
    if !contributor.is_signer {
        msg!("Contributor must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Verify funding account is owned by the program
    if funding_account.owner != program_id {
        msg!("Funding account must be owned by the program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize project data
    let mut data = funding_account.try_borrow_mut_data()?;
    let mut project: FundingProject = bincode::deserialize(&data)?;

    // Check if project is still active
    if !project.is_active {
        msg!("Project is no longer active");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if deadline has passed
    let clock = Clock::get()?;
    if clock.unix_timestamp > project.deadline {
        project.is_active = false;
        bincode::serialize_into(&mut data[..], &project)?;
        msg!("Project deadline has passed");
        return Err(ProgramError::InvalidAccountData);
    }

    // Transfer funds from contributor to project
    let transfer_ix = system_instruction::transfer(
        contributor.key,
        funding_account.key,
        amount,
    );
    solana_program::program::invoke(
        &transfer_ix,
        &[contributor.clone(), funding_account.clone(), system_program.clone()],
    )?;

    // Update project data
    project.raised_amount += amount;
    project.contributors.push(*contributor.key);
    bincode::serialize_into(&mut data[..], &project)?;

    Ok(())
}

// Withdraw funds if target is met
fn withdraw_funds(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let entrepreneur = next_account_info(accounts_iter)?;
    let funding_account = next_account_info(accounts_iter)?;
    let entrepreneur_funding = next_account_info(accounts_iter)?;

    // Verify entrepreneur is signer
    if !entrepreneur.is_signer {
        msg!("Entrepreneur must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Verify funding account is owned by the program
    if funding_account.owner != program_id {
        msg!("Funding account must be owned by the program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize project data
    let mut data = funding_account.try_borrow_mut_data()?;
    let mut project: FundingProject = bincode::deserialize(&data)?;

    // Verify entrepreneur matches project
    if *entrepreneur.key != project.entrepreneur {
        msg!("Only the project entrepreneur can withdraw funds");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if target is met
    if project.raised_amount < project.target_amount {
        msg!("Target amount not reached");
        return Err(ProgramError::InsufficientFunds);
    }

    // Check if project is still active
    if !project.is_active {
        msg!("Project is no longer active");
        return Err(ProgramError::InvalidAccountData);
    }

    // Transfer funds
