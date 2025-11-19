"""
Generated Code Metadata:
========================
Original URL: https://solanaclaims.web.app
Prompt: Develop a smart contract on Solana for gaming and entertainment use cases, optimized for scalability and user engagement as highlighted in the hackathon tracks.
Generated: DETERMINISTIC_f19db72aaf220fac
Batch ID: 20250612_151847
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

// Define the game state structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct GameState {
    pub players: Vec<Pubkey>,
    pub scores: Vec<u64>,
    pub game_start_time: i64,
    pub game_end_time: i64,
    pub is_active: bool,
    pub prize_pool: u64,
}

// Define the player state structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct PlayerState {
    pub player: Pubkey,
    pub score: u64,
    pub last_played: i64,
    pub games_played: u64,
}

// Define the program instructions
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum GameInstruction {
    InitializeGame {
        duration: i64,
        prize_pool: u64,
    },
    JoinGame,
    SubmitScore {
        score: u64,
    },
    EndGame,
    ClaimPrize,
}

// Entry point for the program
entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // Parse the instruction
    let instruction = GameInstruction::try_from_slice(instruction_data)?;

    match instruction {
        GameInstruction::InitializeGame { duration, prize_pool } => {
            initialize_game(program_id, accounts, duration, prize_pool)
        }
        GameInstruction::JoinGame => join_game(program_id, accounts),
        GameInstruction::SubmitScore { score } => submit_score(program_id, accounts, score),
        GameInstruction::EndGame => end_game(program_id, accounts),
        GameInstruction::ClaimPrize => claim_prize(program_id, accounts),
    }
}

// Initialize a new game
fn initialize_game(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    duration: i64,
    prize_pool: u64,
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let game_account = next_account_info(accounts_iter)?;
    let payer = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Verify the game account is owned by the program
    if game_account.owner != program_id {
        msg!("Game account does not have the correct program id");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Get current clock time
    let clock = Clock::get()?;
    let current_time = clock.unix_timestamp;

    // Initialize game state
    let game_state = GameState {
        players: Vec::new(),
        scores: Vec::new(),
        game_start_time: current_time,
        game_end_time: current_time + duration,
        is_active: true,
        prize_pool,
    };

    // Serialize and save the game state
    game_state.serialize(&mut &mut game_account.data.borrow_mut()[..])?;

    Ok(())
}

// Join an existing game
fn join_game(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let game_account = next_account_info(accounts_iter)?;
    let player_account = next_account_info(accounts_iter)?;
    let player_state_account = next_account_info(accounts_iter)?;

    // Verify ownership
    if game_account.owner != program_id {
        msg!("Game account does not have the correct program id");
        return Err(ProgramError::IncorrectProgramId);
    }

    if player_state_account.owner != program_id {
        msg!("Player state account does not have the correct program id");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize game state
    let mut game_state = GameState::try_from_slice(&game_account.data.borrow())?;

    // Check if game is active
    if !game_state.is_active {
        msg!("Game is not active");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if game has ended
    let clock = Clock::get()?;
    if clock.unix_timestamp > game_state.game_end_time {
        msg!("Game has ended");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if player already joined
    if game_state.players.contains(&player_account.key) {
        msg!("Player already joined the game");
        return Err(ProgramError::AccountAlreadyInitialized);
    }

    // Add player to the game
    game_state.players.push(*player_account.key);
    game_state.scores.push(0);

    // Initialize player state
    let player_state = PlayerState {
        player: *player_account.key,
        score: 0,
        last_played: clock.unix_timestamp,
        games_played: 1,
    };

    // Save states
    game_state.serialize(&mut &mut game_account.data.borrow_mut()[..])?;
    player_state.serialize(&mut &mut player_state_account.data.borrow_mut()[..])?;

    Ok(())
}

// Submit a score to the game
fn submit_score(program_id: &Pubkey, accounts: &[AccountInfo], score: u64) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let game_account = next_account_info(accounts_iter)?;
    let player_account = next_account_info(accounts_iter)?;
    let player_state_account = next_account_info(accounts_iter)?;

    // Verify ownership
    if game_account.owner != program_id {
        msg!("Game account does not have the correct program id");
        return Err(ProgramError::IncorrectProgramId);
    }

    if player_state_account.owner != program_id {
        msg!("Player state account does not have the correct program id");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize states
    let mut game_state = GameState::try_from_slice(&game_account.data.borrow())?;
    let mut player_state = PlayerState::try_from_slice(&player_state_account.data.borrow())?;

    // Check if game is active
    if !game_state.is_active {
        msg!("Game is not active");
        return Err(ProgramError::InvalidAccountData);
    }

    // Check if game has ended
    let clock = Clock::get()?;
    if clock.unix_timestamp > game_state.game_end_time {
        msg!("Game has ended");
        return Err(ProgramError::InvalidAccountData);
    }

    // Find player index
    let player_index = match game_state.players.iter().position(|&x| x == *player_account.key) {
        Some(index) => index,
        None => {
            msg!("Player not found in game");
            return Err(ProgramError::InvalidAccountData);
        }
    };

    // Update scores
    if score > game_state.scores[player_index] {
        game_state.scores[player_index] = score;
        player_state.score = score;
    }

    // Update last played time
    player_state.last_played = clock.unix_timestamp;

    // Save states
    game_state.serialize(&mut &mut game_account.data.borrow_mut()[..])?;
    player_state.serialize(&mut &mut player_state_account.data.borrow_mut()[..])?;

    Ok(())
}

// End the game and determine winners
fn end_game(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let game_account = next_account_info(accounts_iter)?;
    let authority = next_account_info(accounts_iter)?;

    // Verify authority
    if !authority.is_signer {
        msg!("Authority did not sign the transaction");
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Deserialize game state
    let mut game_state = GameState::try_from_slice(&game_account.data.borrow())?;

    // Check if game is already ended
    if !game_state.is_active {
        msg!("Game is already ended");
        return Err(ProgramError::InvalidAccountData);
    }

    // End the game
    game_state.is_active = false;
    game_state.serialize(&mut &mut game_account.data.borrow_mut()[..])?;

    Ok(())
}

// Claim prize for winning players
fn claim_prize(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let game_account = next_account_info(accounts_iter)?;
    let player_account = next_account_info(accounts_iter)?;
    let player_state_account = next_account_info(accounts_iter)?;
    let prize_vault = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Verify ownership
    if game_account.owner != program
