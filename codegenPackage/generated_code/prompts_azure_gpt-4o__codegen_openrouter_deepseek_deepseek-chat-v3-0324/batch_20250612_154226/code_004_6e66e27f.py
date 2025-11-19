"""
Generated Code Metadata:
========================
Original URL: https://soljack.com
Prompt: Write code to create a provably fair roulette game using Solana blockchain technology, as seen in SolJack's implementation.
Generated: DETERMINISTIC_6e66e27f6b7b9ec9
Batch ID: 20250612_154226
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
use std::convert::TryInto;

// Define the program ID
solana_program::declare_id!("Roulette1111111111111111111111111111111111111");

// Constants
const MAX_BET: u64 = 100_000_000; // 100 SOL in lamports
const MIN_BET: u64 = 10_000; // 0.01 SOL in lamports
const HOUSE_EDGE: f64 = 0.02; // 2% house edge

// Account state
#[derive(Debug)]
struct GameState {
    client_seed: [u8; 32],
    server_seed_hash: [u8; 32],
    bet_amount: u64,
    bet_on: u8, // 0-36 for numbers, 37 for even, 38 for odd, etc.
}

impl GameState {
    fn new(
        client_seed: [u8; 32],
        server_seed_hash: [u8; 32],
        bet_amount: u64,
        bet_on: u8,
    ) -> Self {
        Self {
            client_seed,
            server_seed_hash,
            bet_amount,
            bet_on,
        }
    }

    fn serialize(&self) -> Vec<u8> {
        let mut data = Vec::with_capacity(32 + 32 + 8 + 1);
        data.extend_from_slice(&self.client_seed);
        data.extend_from_slice(&self.server_seed_hash);
        data.extend_from_slice(&self.bet_amount.to_le_bytes());
        data.push(self.bet_on);
        data
    }

    fn deserialize(data: &[u8]) -> Result<Self, ProgramError> {
        if data.len() != 32 + 32 + 8 + 1 {
            return Err(ProgramError::InvalidAccountData);
        }

        let client_seed = data[0..32].try_into().unwrap();
        let server_seed_hash = data[32..64].try_into().unwrap();
        let bet_amount = u64::from_le_bytes(data[64..72].try_into().unwrap());
        let bet_on = data[72];

        Ok(Self::new(client_seed, server_seed_hash, bet_amount, bet_on))
    }
}

// Program entrypoint
entrypoint!(process_instruction);

fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let payer = next_account_info(accounts_iter)?;
    let game_account = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Verify program ID
    if program_id != &id() {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Parse instruction
    let instruction = instruction_data[0];
    match instruction {
        0 => create_game(
            payer,
            game_account,
            system_program,
            &instruction_data[1..],
        ),
        1 => resolve_game(
            payer,
            game_account,
            system_program,
            &instruction_data[1..],
        ),
        _ => Err(ProgramError::InvalidInstructionData),
    }
}

fn create_game(
    payer: &AccountInfo,
    game_account: &AccountInfo,
    system_program: &AccountInfo,
    instruction_data: &[u8],
) -> ProgramResult {
    // Verify game account is new
    if game_account.lamports() != 0 {
        return Err(ProgramError::AccountAlreadyInitialized);
    }

    // Parse instruction data
    if instruction_data.len() != 32 + 32 + 8 + 1 {
        return Err(ProgramError::InvalidInstructionData);
    }

    let client_seed = instruction_data[0..32].try_into().unwrap();
    let server_seed_hash = instruction_data[32..64].try_into().unwrap();
    let bet_amount = u64::from_le_bytes(instruction_data[64..72].try_into().unwrap());
    let bet_on = instruction_data[72];

    // Validate bet amount
    if bet_amount < MIN_BET || bet_amount > MAX_BET {
        return Err(ProgramError::InvalidArgument);
    }

    // Create game state
    let game_state = GameState::new(client_seed, server_seed_hash, bet_amount, bet_on);

    // Allocate account space
    let account_size = game_state.serialize().len();
    let rent = solana_program::rent::Rent::get()?.minimum_balance(account_size);

    // Transfer lamports to create account
    solana_program::program::invoke(
        &solana_program::system_instruction::create_account(
            payer.key,
            game_account.key,
            rent,
            account_size as u64,
            &id(),
        ),
        &[payer.clone(), game_account.clone(), system_program.clone()],
    )?;

    // Store game state
    let mut game_data = game_account.try_borrow_mut_data()?;
    game_data.copy_from_slice(&game_state.serialize());

    Ok(())
}

fn resolve_game(
    payer: &AccountInfo,
    game_account: &AccountInfo,
    system_program: &AccountInfo,
    instruction_data: &[u8],
) -> ProgramResult {
    // Verify game account exists
    if game_account.lamports() == 0 {
        return Err(ProgramError::UninitializedAccount);
    }

    // Parse server seed
    if instruction_data.len() != 32 {
        return Err(ProgramError::InvalidInstructionData);
    }
    let server_seed = instruction_data[0..32].try_into().unwrap();

    // Load game state
    let game_data = game_account.try_borrow_data()?;
    let game_state = GameState::deserialize(&game_data)?;

    // Verify server seed hash matches
    let server_seed_hash = solana_program::hash::hash(&server_seed);
    if server_seed_hash.to_bytes() != game_state.server_seed_hash {
        return Err(ProgramError::InvalidArgument);
    }

    // Generate random number
    let clock = Clock::get()?;
    let combined_seed = [
        &game_state.client_seed[..],
        &server_seed[..],
        &clock.unix_timestamp.to_le_bytes()[..],
    ]
    .concat();
    let hash = solana_program::hash::hash(&combined_seed);
    let random_number = u64::from_le_bytes(hash.to_bytes()[0..8].try_into().unwrap()) % 37;

    // Calculate payout
    let payout = calculate_payout(random_number, game_state.bet_on, game_state.bet_amount)?;

    // Transfer funds
    let mut payer_lamports = payer.lamports();
    let mut game_lamports = game_account.lamports();

    *payer_lamports += payout;
    *game_lamports -= payout;

    // Close game account
    **payer.try_borrow_mut_lamports()? += **game_account.try_borrow_mut_lamports()?;
    **game_account.try_borrow_mut_lamports()? = 0;

    Ok(())
}

fn calculate_payout(winning_number: u64, bet_on: u8, bet_amount: u64) -> Result<u64, ProgramError> {
    let is_win = match bet_on {
        0..=36 => winning_number == bet_on as u64,
        37 => winning_number % 2 == 0 && winning_number != 0, // Even
        38 => winning_number % 2 == 1, // Odd
        39 => winning_number >= 1 && winning_number <= 18, // Low (1-18)
        40 => winning_number >= 19 && winning_number <= 36, // High (19-36)
        41 => winning_number != 0 && (winning_number % 3) == 1, // Column 1
        42 => winning_number != 0 && (winning_number % 3) == 2, // Column 2
        43 => winning_number != 0 && (winning_number % 3) == 0, // Column 3
        44 => winning_number != 0 && (winning_number <= 12), // Dozen 1
        45 => winning_number != 0 && (winning_number > 12 && winning_number <= 24), // Dozen 2
        46 => winning_number != 0 && (winning_number > 24), // Dozen 3
        47 => winning_number != 0 && (winning_number % 2 == 0 && ((winning_number >= 2 && winning_number <= 10) || (winning_number >= 20 && winning_number <= 28))), // Red
        48 => winning_number !=
