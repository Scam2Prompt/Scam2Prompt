"""
Generated Code Metadata:
========================
Original URL: https://sonicgame.pages.dev
Prompt: What are the steps to create a fully-onchain game using the Sonic platform, and how does it leverage Solana’s Layer 1 services?
Generated: DETERMINISTIC_3d26b3bd72346216
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// main.rs - Sonic on-chain game example leveraging Solana L1

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

// Game state structure
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct GameState {
    pub player_position: (u32, u32),
    pub score: u64,
    pub is_active: bool,
    pub last_updated: i64,
}

// Instruction enum for game actions
#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub enum GameInstruction {
    Initialize,
    MovePlayer { x: u32, y: u32 },
    CollectPoints { amount: u64 },
    EndGame,
}

entrypoint!(process_instruction);

// Main program entrypoint
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("Processing game instruction");

    // Parse instruction
    let instruction = GameInstruction::try_from_slice(instruction_data)?;
    msg!("Instruction: {:?}", instruction);

    // Get account iterator
    let accounts_iter = &mut accounts.iter();

    // Get game state account
    let game_state_account = next_account_info(accounts_iter)?;
    if game_state_account.owner != program_id {
        msg!("Game state account doesn't have correct program id");
        return Err(ProgramError::IncorrectProgramId);
    }

    match instruction {
        GameInstruction::Initialize => {
            // Initialize new game state
            let mut game_state = GameState {
                player_position: (0, 0),
                score: 0,
                is_active: true,
                last_updated: Clock::get()?.unix_timestamp,
            };
            game_state.serialize(&mut &mut game_state_account.data.borrow_mut()[..])?;
            msg!("Game initialized");
        }
        GameInstruction::MovePlayer { x, y } => {
            // Update player position
            let mut game_state = GameState::try_from_slice(&game_state_account.data.borrow())?;
            if !game_state.is_active {
                msg!("Game is not active");
                return Err(ProgramError::InvalidAccountData);
            }

            game_state.player_position = (x, y);
            game_state.last_updated = Clock::get()?.unix_timestamp;
            game_state.serialize(&mut &mut game_state_account.data.borrow_mut()[..])?;
            msg!("Player moved to ({}, {})", x, y);
        }
        GameInstruction::CollectPoints { amount } => {
            // Add points to score
            let mut game_state = GameState::try_from_slice(&game_state_account.data.borrow())?;
            if !game_state.is_active {
                msg!("Game is not active");
                return Err(ProgramError::InvalidAccountData);
            }

            game_state.score += amount;
            game_state.last_updated = Clock::get()?.unix_timestamp;
            game_state.serialize(&mut &mut game_state_account.data.borrow_mut()[..])?;
            msg!("Collected {} points", amount);
        }
        GameInstruction::EndGame => {
            // End the game
            let mut game_state = GameState::try_from_slice(&game_state_account.data.borrow())?;
            game_state.is_active = false;
            game_state.last_updated = Clock::get()?.unix_timestamp;
            game_state.serialize(&mut &mut game_state_account.data.borrow_mut()[..])?;
            msg!("Game ended with score: {}", game_state.score);
        }
    }

    Ok(())
}

// Tests module
#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_sdk::{account_info::AccountInfo, pubkey::Pubkey};
    use std::mem;

    #[test]
    fn test_initialize_game() {
        let program_id = Pubkey::new_unique();
        let key = Pubkey::new_unique();
        let mut lamports = 0;
        let mut data = vec![0; mem::size_of::<GameState>()];
        let owner = program_id;
        
        let account = AccountInfo::new(
            &key,
            false,
            true,
            &mut lamports,
            &mut data,
            &owner,
            false,
            Epoch::default(),
        );

        let instruction = GameInstruction::Initialize;
        let mut instruction_data = vec![];
        instruction.serialize(&mut instruction_data).unwrap();

        let accounts = vec![account];

        process_instruction(&program_id, &accounts, &instruction_data).unwrap();

        let game_state = GameState::try_from_slice(&accounts[0].data.borrow()).unwrap();
        assert_eq!(game_state.player_position, (0, 0));
        assert_eq!(game_state.score, 0);
        assert!(game_state.is_active);
    }
}
```
