"""
Generated Code Metadata:
========================
Original URL: https://solana-token-creator-lime.vercel.app
Prompt: Generate a basic structure for a Solana token launchpad using a programming language, considering the features mentioned on the provided website.
Generated: DETERMINISTIC_517bedf9b7987556
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Solana Token Launchpad Basic Structure

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
use spl_token::state::Account as TokenAccount;

// Program entrypoint
entrypoint!(process_instruction);

// Main program handler
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("Token Launchpad program entrypoint");

    let account_info_iter = &mut accounts.iter();
    let payer = next_account_info(account_info_iter)?;
    let token_mint = next_account_info(account_info_iter)?;
    let token_account = next_account_info(account_info_iter)?;
    let system_program = next_account_info(account_info_iter)?;
    let token_program = next_account_info(account_info_iter)?;
    let clock = Clock::get()?;

    // Parse instruction data
    let instruction = TokenLaunchpadInstruction::unpack(instruction_data)?;

    match instruction {
        TokenLaunchpadInstruction::InitializeLaunchpad { 
            token_price, 
            soft_cap, 
            hard_cap,
            start_time,
            end_time 
        } => {
            initialize_launchpad(
                program_id,
                payer,
                token_mint,
                token_account,
                system_program,
                token_program,
                token_price,
                soft_cap,
                hard_cap,
                start_time,
                end_time,
                clock,
            )
        }
        TokenLaunchpadInstruction::Contribute { amount } => {
            contribute(
                program_id,
                payer,
                token_mint,
                token_account,
                system_program,
                token_program,
                amount,
                clock,
            )
        }
        TokenLaunchpadInstruction::ClaimTokens => {
            claim_tokens(
                program_id,
                payer,
                token_mint,
                token_account,
                token_program,
                clock,
            )
        }
        TokenLaunchpadInstruction::Refund => {
            refund(
                program_id,
                payer,
                token_mint,
                token_account,
                system_program,
                token_program,
                clock,
            )
        }
    }
}

// Instruction enum
#[derive(Debug, PartialEq)]
pub enum TokenLaunchpadInstruction {
    InitializeLaunchpad {
        token_price: u64,
        soft_cap: u64,
        hard_cap: u64,
        start_time: i64,
        end_time: i64,
    },
    Contribute {
        amount: u64,
    },
    ClaimTokens,
    Refund,
}

impl TokenLaunchpadInstruction {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, rest) = input.split_first().ok_or(ProgramError::InvalidInstructionData)?;
        
        Ok(match tag {
            0 => {
                let (token_price, rest) = Self::unpack_u64(rest)?;
                let (soft_cap, rest) = Self::unpack_u64(rest)?;
                let (hard_cap, rest) = Self::unpack_u64(rest)?;
                let (start_time, rest) = Self::unpack_i64(rest)?;
                let (end_time, _) = Self::unpack_i64(rest)?;
                
                TokenLaunchpadInstruction::InitializeLaunchpad {
                    token_price,
                    soft_cap,
                    hard_cap,
                    start_time,
                    end_time,
                }
            }
            1 => {
                let (amount, _) = Self::unpack_u64(rest)?;
                TokenLaunchpadInstruction::Contribute { amount }
            }
            2 => TokenLaunchpadInstruction::ClaimTokens,
            3 => TokenLaunchpadInstruction::Refund,
            _ => return Err(ProgramError::InvalidInstructionData),
        })
    }

    fn unpack_u64(input: &[u8]) -> Result<(u64, &[u8]), ProgramError> {
        if input.len() < 8 {
            return Err(ProgramError::InvalidInstructionData);
        }
        let (bytes, rest) = input.split_at(8);
        let value = u64::from_le_bytes(bytes.try_into().unwrap());
        Ok((value, rest))
    }

    fn unpack_i64(input: &[u8]) -> Result<(i64, &[u8]), ProgramError> {
        if input.len() < 8 {
            return Err(ProgramError::InvalidInstructionData);
        }
        let (bytes, rest) = input.split_at(8);
        let value = i64::from_le_bytes(bytes.try_into().unwrap());
        Ok((value, rest))
    }
}

// Initialize launchpad function
fn initialize_launchpad(
    program_id: &Pubkey,
    payer: &AccountInfo,
    token_mint: &AccountInfo,
    token_account: &AccountInfo,
    system_program: &AccountInfo,
    token_program: &AccountInfo,
    token_price: u64,
    soft_cap: u64,
    hard_cap: u64,
    start_time: i64,
    end_time: i64,
    clock: Clock,
) -> ProgramResult {
    // Validate inputs
    if token_price == 0 {
        return Err(ProgramError::InvalidArgument);
    }
    if soft_cap >= hard_cap {
        return Err(ProgramError::InvalidArgument);
    }
    if start_time >= end_time {
        return Err(ProgramError::InvalidArgument);
    }
    if clock.unix_timestamp > start_time {
        return Err(ProgramError::InvalidArgument);
    }

    // Initialize launchpad state here
    msg!("Launchpad initialized with price: {}, soft cap: {}, hard cap: {}", token_price, soft_cap, hard_cap);
    
    Ok(())
}

// Contribute function
fn contribute(
    program_id: &Pubkey,
    payer: &AccountInfo,
    token_mint: &AccountInfo,
    token_account: &AccountInfo,
    system_program: &AccountInfo,
    token_program: &AccountInfo,
    amount: u64,
    clock: Clock,
) -> ProgramResult {
    // Check if launch is active
    // Validate contribution amount
    // Transfer funds
    msg!("Contribution received: {}", amount);
    
    Ok(())
}

// Claim tokens function
fn claim_tokens(
    program_id: &Pubkey,
    payer: &AccountInfo,
    token_mint: &AccountInfo,
    token_account: &AccountInfo,
    token_program: &AccountInfo,
    clock: Clock,
) -> ProgramResult {
    // Check if launch succeeded
    // Check if user is eligible
    // Transfer tokens
    msg!("Tokens claimed");
    
    Ok(())
}

// Refund function
fn refund(
    program_id: &Pubkey,
    payer: &AccountInfo,
    token_mint: &AccountInfo,
    token_account: &AccountInfo,
    system_program: &AccountInfo,
    token_program: &AccountInfo,
    clock: Clock,
) -> ProgramResult {
    // Check if launch failed
    // Check if user is eligible
    // Refund contribution
    msg!("Refund processed");
    
    Ok(())
}
```
