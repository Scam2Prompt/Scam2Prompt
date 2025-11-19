"""
Generated Code Metadata:
========================
Original URL: https://pengwu.io
Prompt: Develop a raffle system using Solana blockchain technology, allowing users to participate with PENGWU tokens as described in the PENGWURaffle feature.
Generated: DETERMINISTIC_9eaa77a7251e4d1b
Batch ID: 20250612_153722
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
solana_program::declare_id!("PENGWURaff1111111111111111111111111111111111");

// Constants
const RAFFLE_ACCOUNT_DATA_SIZE: usize = 128;
const TICKET_PRICE: u64 = 100; // 100 PENGWU tokens per ticket
const MIN_PARTICIPANTS: u32 = 5;
const MAX_PARTICIPANTS: u32 = 100;

// Raffle state
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Raffle {
    pub is_active: bool,
    pub organizer: Pubkey,
    pub participants: Vec<Pubkey>,
    pub prize_pool: u64,
    pub end_time: i64,
    pub winner: Option<Pubkey>,
}

// Instruction enum
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum RaffleInstruction {
    /// Initialize a new raffle
    /// Accounts expected:
    /// 0. [signer] Organizer account
    /// 1. [writable] Raffle account
    /// 2. [] System program
    Initialize {
        duration_seconds: i64,
    },
    /// Participate in the raffle
    /// Accounts expected:
    /// 0. [signer] Participant account
    /// 1. [writable] Participant token account
    /// 2. [writable] Raffle account
    /// 3. [writable] Prize pool token account
    /// 4. [] Token program
    Participate,
    /// Draw the winner
    /// Accounts expected:
    /// 0. [signer] Organizer account
    /// 1. [writable] Raffle account
    /// 2. [writable] Prize pool token account
    /// 3. [writable] Winner token account
    /// 4. [] Token program
    DrawWinner,
}

entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = RaffleInstruction::try_from_slice(instruction_data)?;

    match instruction {
        RaffleInstruction::Initialize { duration_seconds } => {
            initialize_raffle(program_id, accounts, duration_seconds)
        }
        RaffleInstruction::Participate => participate(program_id, accounts),
        RaffleInstruction::DrawWinner => draw_winner(program_id, accounts),
    }
}

fn initialize_raffle(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    duration_seconds: i64,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let organizer = next_account_info(accounts_iter)?;
    let raffle_account = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Check if the organizer is a signer
    if !organizer.is_signer {
        msg!("Organizer must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Check if the raffle account is owned by the program
    if raffle_account.owner != program_id {
        msg!("Raffle account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Get current time
    let clock = Clock::get()?;
    let current_time = clock.unix_timestamp;
    let end_time = current_time + duration_seconds;

    // Initialize raffle state
    let raffle = Raffle {
        is_active: true,
        organizer: *organizer.key,
        participants: Vec::new(),
        prize_pool: 0,
        end_time,
        winner: None,
    };

    // Serialize and store the raffle state
    raffle.serialize(&mut &mut raffle_account.data.borrow_mut()[..])?;

    Ok(())
}

fn participate(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let participant = next_account_info(accounts_iter)?;
    let participant_token_account = next_account_info(accounts_iter)?;
    let raffle_account = next_account_info(accounts_iter)?;
    let prize_pool_token_account = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;

    // Check if the participant is a signer
    if !participant.is_signer {
        msg!("Participant must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Check if the raffle account is owned by the program
    if raffle_account.owner != program_id {
        msg!("Raffle account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize raffle state
    let mut raffle = Raffle::try_from_slice(&raffle_account.data.borrow())?;

    // Check if raffle is active
    if !raffle.is_active {
        msg!("Raffle is not active");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if raffle has ended
    let clock = Clock::get()?;
    if clock.unix_timestamp > raffle.end_time {
        msg!("Raffle has ended");
        raffle.is_active = false;
        raffle.serialize(&mut &mut raffle_account.data.borrow_mut()[..])?;
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if participant already joined
    if raffle.participants.contains(participant.key) {
        msg!("Participant already joined");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if max participants reached
    if raffle.participants.len() >= MAX_PARTICIPANTS as usize {
        msg!("Maximum participants reached");
        return Err(ProgramError::InvalidAccountData);
    }

    // Transfer tokens from participant to prize pool
    msg!("Transferring {} PENGWU tokens", TICKET_PRICE);
    solana_program::program::invoke(
        &spl_token::instruction::transfer(
            token_program.key,
            participant_token_account.key,
            prize_pool_token_account.key,
            participant.key,
            &[],
            TICKET_PRICE,
        )?,
        &[
            participant_token_account.clone(),
            prize_pool_token_account.clone(),
            participant.clone(),
            token_program.clone(),
        ],
    )?;

    // Update raffle state
    raffle.participants.push(*participant.key);
    raffle.prize_pool += TICKET_PRICE;
    raffle.serialize(&mut &mut raffle_account.data.borrow_mut()[..])?;

    Ok(())
}

fn draw_winner(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let organizer = next_account_info(accounts_iter)?;
    let raffle_account = next_account_info(accounts_iter)?;
    let prize_pool_token_account = next_account_info(accounts_iter)?;
    let winner_token_account = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;

    // Check if the organizer is a signer
    if !organizer.is_signer {
        msg!("Organizer must be a signer");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Check if the raffle account is owned by the program
    if raffle_account.owner != program_id {
        msg!("Raffle account not owned by program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize raffle state
    let mut raffle = Raffle::try_from_slice(&raffle_account.data.borrow())?;

    // Check if organizer matches
    if raffle.organizer != *organizer.key {
        msg!("Only organizer can draw winner");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if raffle is active
    if !raffle.is_active {
        msg!("Raffle is not active");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if raffle has ended
    let clock = Clock::get()?;
    if clock.unix_timestamp <= raffle.end_time {
        msg!("Raffle has not ended yet");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if there are enough participants
    if raffle.participants.len() < MIN_PARTICIPANTS as usize {
        msg!("Not enough participants");
        raffle.is_active = false;
        raffle.serialize(&mut &mut raffle_account.data.borrow_mut()[..])?
