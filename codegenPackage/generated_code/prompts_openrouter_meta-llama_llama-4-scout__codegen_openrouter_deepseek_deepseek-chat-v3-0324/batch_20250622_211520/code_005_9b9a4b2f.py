"""
Generated Code Metadata:
========================
Original URL: https://soljack.com
Prompt: "What are the key considerations for developing a crypto gambling platform with provably fair games on Solana, and how does SolJack address these?"
Generated: DETERMINISTIC_9b9a4b2f460fe9bd
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// soljack_program/src/lib.rs

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

// Constants
const HOUSE_FEE_PERCENTAGE: u8 = 2; // 2% house fee

/// Game state stored on-chain
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct GameState {
    pub player: Pubkey,
    pub bet_amount: u64,
    pub player_seed: [u8; 32],
    pub server_seed_hash: [u8; 32],
    pub result: Option<u8>, // Game result (e.g., dice roll)
    pub is_settled: bool,
}

/// Instruction enum for different actions
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum SolJackInstruction {
    /// Initialize a new game
    /// Accounts expected:
    /// 0. [signer] Player account
    /// 1. [writable] Game state account
    /// 2. [] System program
    InitializeGame {
        bet_amount: u64,
        player_seed: [u8; 32],
        server_seed_hash: [u8; 32],
    },
    /// Settle a game (called by house)
    /// Accounts expected:
    /// 0. [signer] House account
    /// 1. [writable] Game state account
    SettleGame {
        server_seed: [u8; 32],
    },
}

entrypoint!(process_instruction);

/// Program entrypoint
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let instruction = SolJackInstruction::try_from_slice(instruction_data)?;

    match instruction {
        SolJackInstruction::InitializeGame {
            bet_amount,
            player_seed,
            server_seed_hash,
        } => initialize_game(program_id, accounts, bet_amount, player_seed, server_seed_hash),
        SolJackInstruction::SettleGame { server_seed } => {
            settle_game(program_id, accounts, server_seed)
        }
    }
}

/// Initialize a new game
fn initialize_game(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    bet_amount: u64,
    player_seed: [u8; 32],
    server_seed_hash: [u8; 32],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let player = next_account_info(accounts_iter)?;
    let game_state_account = next_account_info(accounts_iter)?;
    let system_program = next_account_info(accounts_iter)?;

    // Validate accounts
    if !player.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    if game_state_account.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Create game state
    let game_state = GameState {
        player: *player.key,
        bet_amount,
        player_seed,
        server_seed_hash,
        result: None,
        is_settled: false,
    };

    // Serialize and save game state
    game_state.serialize(&mut &mut game_state_account.data.borrow_mut()[..])?;

    msg!("Game initialized for player: {}", player.key);
    Ok(())
}

/// Settle a game with server seed revealed
fn settle_game(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    server_seed: [u8; 32],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let house = next_account_info(accounts_iter)?;
    let game_state_account = next_account_info(accounts_iter)?;

    // Validate accounts
    if !house.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    if game_state_account.owner != program_id {
        return Err(ProgramError::IncorrectProgramId);
    }

    // Deserialize game state
    let mut game_state = GameState::try_from_slice(&game_state_account.data.borrow())?;

    // Check if already settled
    if game_state.is_settled {
        return Err(ProgramError::InvalidAccountData);
    }

    // Verify server seed matches the hash
    let hash = solana_program::hash::hash(&server_seed);
    if hash.0 != game_state.server_seed_hash {
        return Err(ProgramError::InvalidArgument);
    }

    // Generate provably fair result
    let combined_seed = [&game_state.player_seed[..], &server_seed[..]].concat();
    let result_hash = solana_program::hash::hash(&combined_seed);
    let result = result_hash.0[0] % 100; // Example: dice roll 0-99

    // Update game state
    game_state.result = Some(result);
    game_state.is_settled = true;

    // Serialize and save updated game state
    game_state.serialize(&mut &mut game_state_account.data.borrow_mut()[..])?;

    msg!(
        "Game settled for player: {}. Result: {}",
        game_state.player,
        result
    );
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_sdk::{
        account::Account,
        signature::{Keypair, Signer},
        transaction::Transaction,
    };

    #[test]
    fn test_initialize_game() {
        let program_id = Pubkey::new_unique();
        let player = Keypair::new();
        let game_state_account = Keypair::new();

        let mut accounts = vec![
            AccountInfo::new(
                &player.pubkey(),
                false,
                true,
                &mut 0,
                &mut [],
                &player.pubkey(),
                false,
                Epoch::default(),
            ),
            AccountInfo::new(
                &game_state_account.pubkey(),
                false,
                false,
                &mut 0,
                &mut [],
                &program_id,
                false,
                Epoch::default(),
            ),
            AccountInfo::new(
                &solana_program::system_program::id(),
                false,
                false,
                &mut 0,
                &mut [],
                &solana_program::system_program::id(),
                false,
                Epoch::default(),
            ),
        ];

        let player_seed = [0; 32];
        let server_seed_hash = solana_program::hash::hash(&[1; 32]).0;
        let instruction = SolJackInstruction::InitializeGame {
            bet_amount: 1000,
            player_seed,
            server_seed_hash,
        };

        let instruction_data = instruction.try_to_vec().unwrap();
        process_instruction(&program_id, &accounts, &instruction_data).unwrap();

        // Verify game state
        let game_state = GameState::try_from_slice(&accounts[1].data.borrow()).unwrap();
        assert_eq!(game_state.player, player.pubkey());
        assert_eq!(game_state.bet_amount, 1000);
        assert_eq!(game_state.player_seed, player_seed);
        assert_eq!(game_state.server_seed_hash, server_seed_hash);
        assert!(game_state.result.is_none());
        assert!(!game_state.is_settled);
    }
}
```
