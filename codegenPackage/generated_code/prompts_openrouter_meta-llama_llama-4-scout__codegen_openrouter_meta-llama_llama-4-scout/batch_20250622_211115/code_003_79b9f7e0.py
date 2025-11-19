"""
Generated Code Metadata:
========================
Original URL: https://atlasorng.web.app
Prompt: Design a blockchain-based raffle system on Solana with entry requirements and winner selection using the $ORANGE token.
Generated: DETERMINISTIC_79b9f7e009b2bd55
Batch ID: 20250622_211115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import required libraries
use solana_program::{
    account_info::{AccountInfo, next_account_info},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::PrintProgramError,
    program_error::ProgramError,
    pubkey::Pubkey,
};
use solana_program::program_pack::{Pack, Sealed};
use spl_token::instruction::{transfer, Transfer};
use spl_token::state::Mint;

// Define the program's entry point
entrypoint!(process_instruction);

// Define the program's instruction processor
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Check if the instruction data is valid
    if instruction_data.is_empty() {
        return Err(ProgramError::InvalidInstructionData);
    }

    // Unpack the instruction data
    let instruction = instruction_data[0];
    match instruction {
        1 => process_enter_raffle(program_id, accounts),
        2 => process_select_winner(program_id, accounts),
        _ => Err(ProgramError::InvalidInstructionData),
    }
}

// Define the Enter Raffle instruction processor
fn process_enter_raffle(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    // Get the accounts
    let accounts_iter = &mut accounts.iter();
    let raffle_account = next_account_info(accounts_iter)?;
    let user_account = next_account_info(accounts_iter)?;
    let token_account = next_account_info(accounts_iter)?;
    let mint_account = next_account_info(accounts_iter)?;

    // Check if the accounts are valid
    if raffle_account.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }
    if token_account.owner != spl_token::id() {
        return Err(ProgramError::IncorrectProgramId);
    }
    if mint_account.owner != spl_token::id() {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Check if the user has the required $ORANGE tokens
    let token_amount = 10; // 10 $ORANGE tokens required to enter the raffle
    let user_token_balance = spl_token::state::Account::unpack_from_slice(token_account.data.borrow())?.amount;
    if user_token_balance < token_amount {
        return Err(ProgramError::InsufficientFunds);
    }

    // Transfer the $ORANGE tokens to the raffle account
    let transfer_instruction = transfer(
        &spl_token::id(),
        token_account.key,
        raffle_account.key,
        user_account.key,
        &[],
        token_amount,
    )?;
    solana_program::program_stubs::solana_transfer(transfer_instruction)?;

    // Update the raffle account
    let mut raffle_data = RaffleData::unpack_from_slice(raffle_account.data.borrow_mut())?;
    raffle_data.entries += 1;
    raffle_data.pack_into_slice(raffle_account.data.borrow_mut())?;

    Ok(())
}

// Define the Select Winner instruction processor
fn process_select_winner(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    // Get the accounts
    let accounts_iter = &mut accounts.iter();
    let raffle_account = next_account_info(accounts_iter)?;
    let winner_account = next_account_info(accounts_iter)?;

    // Check if the accounts are valid
    if raffle_account.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Check if the raffle has enough entries
    let raffle_data = RaffleData::unpack_from_slice(raffle_account.data.borrow())?;
    if raffle_data.entries < 2 {
        return Err(ProgramError::InvalidAccountState);
    }

    // Select a random winner
    let winner_seed = solana_program::hash::hashv(&[raffle_account.data.borrow()]);
    let winner_pubkey = Pubkey::new_unique(winner_seed.as_ref())?;

    // Update the winner account
    let mut winner_data = WinnerData::unpack_from_slice(winner_account.data.borrow_mut())?;
    winner_data.winner_pubkey = winner_pubkey;
    winner_data.pack_into_slice(winner_account.data.borrow_mut())?;

    // Transfer the $ORANGE tokens to the winner
    let token_amount = raffle_data.entries * 10; // 10 $ORANGE tokens per entry
    let transfer_instruction = transfer(
        &spl_token::id(),
        raffle_account.key,
        winner_account.key,
        raffle_account.key,
        &[],
        token_amount,
    )?;
    solana_program::program_stubs::solana_transfer(transfer_instruction)?;

    Ok(())
}

// Define the RaffleData struct
#[derive(Sealed, Debug, Default, PartialEq)]
pub struct RaffleData {
    pub entries: u32,
}

impl Pack for RaffleData {
    const LEN: usize = 4;

    fn pack_into_slice(&self, dst: &mut [u8]) -> Result<usize, ProgramError> {
        let mut bytes = [0; Self::LEN];
        bytes[..4].copy_from_slice(&self.entries.to_le_bytes());
        Ok(Self::LEN)
    }

    fn unpack_from_slice(src: &[u8]) -> Result<Self, ProgramError> {
        let entries = u32::from_le_bytes([src[0], src[1], src[2], src[3]]);
        Ok(RaffleData { entries })
    }
}

// Define the WinnerData struct
#[derive(Sealed, Debug, Default, PartialEq)]
pub struct WinnerData {
    pub winner_pubkey: Pubkey,
}

impl Pack for WinnerData {
    const LEN: usize = 32;

    fn pack_into_slice(&self, dst: &mut [u8]) -> Result<usize, ProgramError> {
        let mut bytes = [0; Self::LEN];
        bytes[..32].copy_from_slice(self.winner_pubkey.as_ref());
        Ok(Self::LEN)
    }

    fn unpack_from_slice(src: &[u8]) -> Result<Self, ProgramError> {
        let winner_pubkey = Pubkey::new_from_bytes([src[0], src[1], src[2], src[3], src[4], src[5], src[6], src[7], src[8], src[9], src[10], src[11], src[12], src[13], src[14], src[15], src[16], src[17], src[18], src[19], src[20], src[21], src[22], src[23], src[24], src[25], src[26], src[27], src[28], src[29], src[30], src[31]])?;
        Ok(WinnerData { winner_pubkey })
    }
}
```
