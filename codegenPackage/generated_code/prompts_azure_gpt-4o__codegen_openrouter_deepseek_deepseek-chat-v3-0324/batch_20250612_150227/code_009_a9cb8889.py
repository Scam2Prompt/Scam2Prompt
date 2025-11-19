"""
Generated Code Metadata:
========================
Original URL: https://cpanel.solanaaihackathon.com
Prompt: Generate a smart contract on Solana for an AI agent that facilitates fair token launches and liquidity provision, as outlined in the "Agent Token Tooling" track.
Generated: DETERMINISTIC_a9cb8889c7bb2c37
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
    sysvar::{clock::Clock, Sysvar},
};

// Program ID will be replaced during deployment
declare_id!("YourProgramIDHere");

#[derive(Debug)]
pub struct LaunchConfig {
    pub token_mint: Pubkey,
    pub launch_price: u64,
    pub min_liquidity: u64,
    pub max_allocation_per_user: u64,
    pub start_time: i64,
    pub end_time: i64,
    pub is_fair_launch: bool,
}

#[derive(Debug)]
pub struct UserAllocation {
    pub user: Pubkey,
    pub amount: u64,
    pub claimed: bool,
}

#[derive(Debug)]
pub struct LiquidityPool {
    pub token_amount: u64,
    pub sol_amount: u64,
    pub lp_token_mint: Pubkey,
}

#[account]
pub struct LaunchState {
    pub config: LaunchConfig,
    pub allocations: Vec<UserAllocation>,
    pub liquidity_pool: LiquidityPool,
    pub admin: Pubkey,
    pub total_raised: u64,
    pub is_initialized: bool,
}

impl LaunchState {
    pub const LEN: usize = 5000; // Sufficient space for allocations
}

#[derive(Debug)]
pub enum LaunchError {
    NotInitialized,
    AlreadyInitialized,
    InvalidAdmin,
    InvalidTime,
    AllocationExceeded,
    NotEnoughLiquidity,
    LaunchNotStarted,
    LaunchEnded,
    InvalidUser,
    AlreadyClaimed,
}

impl From<LaunchError> for ProgramError {
    fn from(e: LaunchError) -> Self {
        ProgramError::Custom(e as u32)
    }
}

#[derive(Debug)]
pub enum LaunchInstruction {
    Initialize {
        config: LaunchConfig,
    },
    Participate {
        amount: u64,
    },
    ClaimTokens,
    AddLiquidity {
        token_amount: u64,
        sol_amount: u64,
    },
    FinalizeLaunch,
}

impl LaunchInstruction {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, rest) = input.split_first().ok_or(ProgramError::InvalidInstructionData)?;
        Ok(match tag {
            0 => {
                let config = LaunchConfig::try_from_slice(rest)?;
                Self::Initialize { config }
            }
            1 => {
                let amount = u64::from_le_bytes(rest[..8].try_into().unwrap());
                Self::Participate { amount }
            }
            2 => Self::ClaimTokens,
            3 => {
                let token_amount = u64::from_le_bytes(rest[..8].try_into().unwrap());
                let sol_amount = u64::from_le_bytes(rest[8..16].try_into().unwrap());
                Self::AddLiquidity {
                    token_amount,
                    sol_amount,
                }
            }
            4 => Self::FinalizeLaunch,
            _ => return Err(ProgramError::InvalidInstructionData),
        })
    }
}

entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = LaunchInstruction::unpack(instruction_data)?;
    match instruction {
        LaunchInstruction::Initialize { config } => {
            initialize_launch(program_id, accounts, config)
        }
        LaunchInstruction::Participate { amount } => {
            participate(program_id, accounts, amount)
        }
        LaunchInstruction::ClaimTokens => claim_tokens(program_id, accounts),
        LaunchInstruction::AddLiquidity {
            token_amount,
            sol_amount,
        } => add_liquidity(program_id, accounts, token_amount, sol_amount),
        LaunchInstruction::FinalizeLaunch => finalize_launch(program_id, accounts),
    }
}

fn initialize_launch(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    config: LaunchConfig,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let launch_state_account = next_account_info(accounts_iter)?;
    let admin = next_account_info(accounts_iter)?;
    let payer = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Verify admin is signer
    if !admin.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Initialize launch state
    let mut launch_state = LaunchState {
        config,
        allocations: Vec::new(),
        liquidity_pool: LiquidityPool {
            token_amount: 0,
            sol_amount: 0,
            lp_token_mint: Pubkey::default(),
        },
        admin: *admin.key,
        total_raised: 0,
        is_initialized: true,
    };

    launch_state.serialize(&mut &mut launch_state_account.data.borrow_mut()[..])?;

    Ok(())
}

fn participate(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    amount: u64,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let launch_state_account = next_account_info(accounts_iter)?;
    let user = next_account_info(accounts_iter)?;
    let user_token_account = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;

    // Verify user is signer
    if !user.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Load launch state
    let mut launch_state = LaunchState::try_from_slice(&launch_state_account.data.borrow())?;
    
    // Check if launch is initialized
    if !launch_state.is_initialized {
        return Err(LaunchError::NotInitialized.into());
    }

    // Check launch time
    let clock = Clock::get()?;
    if clock.unix_timestamp < launch_state.config.start_time {
        return Err(LaunchError::LaunchNotStarted.into());
    }
    if clock.unix_timestamp > launch_state.config.end_time {
        return Err(LaunchError::LaunchEnded.into());
    }

    // Check allocation limits
    let user_allocation = launch_state.allocations.iter_mut()
        .find(|a| a.user == *user.key)
        .ok_or(LaunchError::InvalidUser)?;

    if user_allocation.amount + amount > launch_state.config.max_allocation_per_user {
        return Err(LaunchError::AllocationExceeded.into());
    }

    // Update allocation
    user_allocation.amount += amount;
    launch_state.total_raised += amount;

    // Transfer SOL from user to launch pool
    // (In a real implementation, this would involve actual token transfers)

    launch_state.serialize(&mut &mut launch_state_account.data.borrow_mut()[..])?;

    Ok(())
}

fn claim_tokens(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let launch_state_account = next_account_info(accounts_iter)?;
    let user = next_account_info(accounts_iter)?;
    let user_token_account = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;

    // Load launch state
    let mut launch_state = LaunchState::try_from_slice(&launch_state_account.data.borrow())?;
    
    // Find user allocation
    let user_allocation = launch_state.allocations.iter_mut()
        .find(|a| a.user == *user.key)
        .ok_or(LaunchError::InvalidUser)?;

    // Check if already claimed
    if user_allocation.claimed {
        return Err(LaunchError::AlreadyClaimed.into());
    }

    // Mark as claimed
    user_allocation.claimed = true;

    // Transfer tokens to user
    // (In a real implementation, this would involve actual token transfers)

    launch_state.serialize(&mut &mut launch_state_account.data.borrow_mut()[..])?;

    Ok(())
}

fn add_liquidity(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    token_amount: u64,
    sol_amount: u64,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let launch_state_account = next_account_info(accounts_iter)?;
    let admin = next_account_info(accounts_iter)?;
    let token_account = next_account_info(accounts_iter)?;
    let token_program = next_account_info(accounts_iter)?;

    // Verify admin is signer
    if !admin.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Load launch state
    let mut launch_state = LaunchState::try_from_slice(&launch_state_account.data.borrow())?;
    
    // Verify admin
    if launch_state.admin != *admin.key {
        return Err(LaunchError::InvalidAdmin.into());
    }

    // Update liquidity pool
