"""
Generated Code Metadata:
========================
Original URL: https://mail.solanary.com
Prompt: Generate a smart contract using Rust that manages a multi-prize pool lottery system on the Solana blockchain, inspired by Solanary's SOL lottery model.
Generated: DETERMINISTIC_8440d21e3a436edf
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! A Solana smart contract for a multi-prize pool lottery system.

use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
    sysvar::{clock::Clock, Sysvar},
};
use std::convert::TryInto;

// Define the program ID (this should be replaced with the actual program ID)
solana_program::declare_id!("Lottery1111111111111111111111111111111111111");

/// Constants
const MAX_PRIZE_POOLS: usize = 5;
const TICKET_PRICE: u64 = 1000000; // 1 SOL in lamports
const ADMIN_PUBKEY: &str = "ADMIN_PUBKEY_PLACEHOLDER"; // Replace with actual admin pubkey

/// Lottery state structure
#[derive(Debug)]
pub struct Lottery {
    pub is_active: bool,
    pub prize_pools: [u64; MAX_PRIZE_POOLS],
    pub ticket_count: u64,
    pub participants: Vec<Pubkey>,
    pub last_winner: Option<Pubkey>,
    pub end_time: i64,
}

impl Default for Lottery {
    fn default() -> Self {
        Lottery {
            is_active: false,
            prize_pools: [0; MAX_PRIZE_POOLS],
            ticket_count: 0,
            participants: Vec::new(),
            last_winner: None,
            end_time: 0,
        }
    }
}

/// Program entrypoint
entrypoint!(process_instruction);

/// Processes instructions
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("Lottery program entrypoint");

    // Parse instruction
    let instruction = LotteryInstruction::unpack(instruction_data)?;

    match instruction {
        LotteryInstruction::Initialize => initialize_lottery(program_id, accounts),
        LotteryInstruction::BuyTicket => buy_ticket(program_id, accounts),
        LotteryInstruction::DrawWinner => draw_winner(program_id, accounts),
        LotteryInstruction::ClaimPrize => claim_prize(program_id, accounts),
    }
}

/// Lottery instructions
#[derive(Debug, PartialEq)]
pub enum LotteryInstruction {
    Initialize,
    BuyTicket,
    DrawWinner,
    ClaimPrize,
}

impl LotteryInstruction {
    /// Unpacks a byte buffer into a LotteryInstruction
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, _rest) = input
            .split_first()
            .ok_or(ProgramError::InvalidInstructionData)?;

        Ok(match tag {
            0 => LotteryInstruction::Initialize,
            1 => LotteryInstruction::BuyTicket,
            2 => LotteryInstruction::DrawWinner,
            3 => LotteryInstruction::ClaimPrize,
            _ => return Err(ProgramError::InvalidInstructionData),
        })
    }
}

/// Initializes the lottery
fn initialize_lottery(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let lottery_account = next_account_info(accounts_iter)?;
    let admin_account = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Verify admin
    let admin_pubkey = Pubkey::try_from(ADMIN_PUBKEY.as_bytes())
        .map_err(|_| ProgramError::InvalidArgument)?;
    if admin_account.key != &admin_pubkey {
        return Err(ProgramError::IncorrectAuthority);
    }

    // Initialize lottery state
    let mut lottery_data = Lottery::default();
    lottery_data.is_active = true;
    lottery_data.end_time = Clock::get()?.unix_timestamp + 86400; // 24 hours from now

    // Store lottery state
    let mut data = lottery_account.try_borrow_mut_data()?;
    bincode::serialize_into(&mut data[..], &lottery_data)
        .map_err(|_| ProgramError::InvalidAccountData)?;

    msg!("Lottery initialized successfully");
    Ok(())
}

/// Processes ticket purchase
fn buy_ticket(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let lottery_account = next_account_info(accounts_iter)?;
    let user_account = next_account_info(accounts_iter)?;
    let user_transfer_account = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Verify program owns the lottery account
    if lottery_account.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize lottery state
    let mut lottery_data: Lottery = bincode::deserialize(&lottery_account.data.borrow())
        .map_err(|_| ProgramError::InvalidAccountData)?;

    // Check if lottery is active
    if !lottery_data.is_active {
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if lottery has ended
    if Clock::get()?.unix_timestamp > lottery_data.end_time {
        lottery_data.is_active = false;
        return Err(ProgramError::InvalidAccountData);
    }

    // Transfer SOL for ticket
    **user_transfer_account.try_borrow_mut_lamports()? -= TICKET_PRICE;
    **lottery_account.try_borrow_mut_lamports()? += TICKET_PRICE;

    // Update lottery state
    lottery_data.ticket_count += 1;
    lottery_data.participants.push(*user_account.key);

    // Distribute to prize pools (simplified distribution)
    for i in 0..MAX_PRIZE_POOLS {
        lottery_data.prize_pools[i] += TICKET_PRICE / MAX_PRIZE_POOLS as u64;
    }

    // Store updated state
    let mut data = lottery_account.try_borrow_mut_data()?;
    bincode::serialize_into(&mut data[..], &lottery_data)
        .map_err(|_| ProgramError::InvalidAccountData)?;

    msg!("Ticket purchased successfully");
    Ok(())
}

/// Draws a winner
fn draw_winner(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let lottery_account = next_account_info(accounts_iter)?;
    let admin_account = next_account_info(accounts_iter)?;

    // Verify admin
    let admin_pubkey = Pubkey::try_from(ADMIN_PUBKEY.as_bytes())
        .map_err(|_| ProgramError::InvalidArgument)?;
    if admin_account.key != &admin_pubkey {
        return Err(ProgramError::IncorrectAuthority);
    }

    // Deserialize lottery state
    let mut lottery_data: Lottery = bincode::deserialize(&lottery_account.data.borrow())
        .map_err(|_| ProgramError::InvalidAccountData)?;

    // Check if lottery has ended
    if Clock::get()?.unix_timestamp <= lottery_data.end_time {
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if already drawn
    if lottery_data.last_winner.is_some() {
        return Err(ProgramError::InvalidAccountData);
    }

    // Select random winner (simplified - in production use a proper randomness source)
    if lottery_data.participants.is_empty() {
        return Err(ProgramError::InvalidAccountData);
    }
    let winner_index = (Clock::get()?.unix_timestamp as usize) % lottery_data.participants.len();
    let winner = lottery_data.participants[winner_index];
    lottery_data.last_winner = Some(winner);

    // Store updated state
    let mut data = lottery_account.try_borrow_mut_data()?;
    bincode::serialize_into(&mut data[..], &lottery_data)
        .map_err(|_| ProgramError::InvalidAccountData)?;

    msg!("Winner drawn successfully");
    Ok(())
}

/// Claims prize
fn claim_prize(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let lottery_account = next_account_info(accounts_iter)?;
    let winner_account = next_account_info(accounts_iter)?;
    let winner_receive_account = next_account_info(accounts_iter)?;

    // Deserialize lottery state
    let lottery_data: Lottery = bincode::deserialize(&lottery_account.data.borrow())
        .map_err(|_| ProgramError::InvalidAccountData)?;

    // Check if winner is set
    let winner = lottery_data.last_winner.ok_or(ProgramError::InvalidAccountData)?;
    if winner_account.key != &winner {
        return Err(ProgramError::IncorrectAuthority);
    }

    // Calculate prize amount (simplified - first prize pool)
    let prize_amount = lottery_data.prize_pools[0];

    // Transfer prize
