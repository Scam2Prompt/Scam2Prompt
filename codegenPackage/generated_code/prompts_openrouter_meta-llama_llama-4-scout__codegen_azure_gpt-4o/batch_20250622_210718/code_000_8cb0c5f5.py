"""
Generated Code Metadata:
========================
Original URL: https://atocha.io
Prompt: "Write a smart contract for a decentralized puzzle game on the NEAR blockchain, incorporating Atocha protocol features."
Generated: DETERMINISTIC_8cb0c5f579ade24c
Batch ID: 20250622_210718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Smart Contract for a Decentralized Puzzle Game on the NEAR Blockchain
// Incorporating Atocha Protocol Features

// Import necessary libraries and modules
use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::{env, near_bindgen, AccountId, Balance, PanicOnDefault};
use near_sdk::collections::UnorderedMap;

// Define the Puzzle struct
#[derive(BorshDeserialize, BorshSerialize)]
pub struct Puzzle {
    creator: AccountId,
    question: String,
    answer_hash: String, // Hash of the answer for verification
    reward: Balance,     // Reward for solving the puzzle
    solved: bool,        // Status of the puzzle
}

// Define the PuzzleGame contract
#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct PuzzleGame {
    puzzles: UnorderedMap<u64, Puzzle>, // Map of puzzle ID to Puzzle struct
    next_puzzle_id: u64,                // Auto-incrementing puzzle ID
}

#[near_bindgen]
impl PuzzleGame {
    // Constructor to initialize the contract
    #[init]
    pub fn new() -> Self {
        Self {
            puzzles: UnorderedMap::new(b"puzzles".to_vec()),
            next_puzzle_id: 0,
        }
    }

    // Function to create a new puzzle
    pub fn create_puzzle(&mut self, question: String, answer_hash: String, reward: Balance) {
        // Ensure the reward is greater than zero
        assert!(reward > 0, "Reward must be greater than zero");

        // Ensure the creator has enough balance to fund the reward
        assert!(
            env::attached_deposit() >= reward,
            "Attached deposit must be equal to or greater than the reward"
        );

        // Create a new puzzle
        let puzzle = Puzzle {
            creator: env::predecessor_account_id(),
            question,
            answer_hash,
            reward,
            solved: false,
        };

        // Store the puzzle in the map
        self.puzzles.insert(&self.next_puzzle_id, &puzzle);

        // Increment the puzzle ID for the next puzzle
        self.next_puzzle_id += 1;
    }

    // Function to solve a puzzle
    pub fn solve_puzzle(&mut self, puzzle_id: u64, answer: String) {
        // Retrieve the puzzle
        let mut puzzle = self
            .puzzles
            .get(&puzzle_id)
            .expect("Puzzle not found");

        // Ensure the puzzle is not already solved
        assert!(!puzzle.solved, "Puzzle has already been solved");

        // Verify the answer hash
        let answer_hash = env::sha256(answer.as_bytes());
        let answer_hash_hex = hex::encode(answer_hash);
        assert_eq!(
            answer_hash_hex, puzzle.answer_hash,
            "Incorrect answer"
        );

        // Mark the puzzle as solved
        puzzle.solved = true;

        // Update the puzzle in the map
        self.puzzles.insert(&puzzle_id, &puzzle);

        // Transfer the reward to the solver
        Promise::new(env::predecessor_account_id()).transfer(puzzle.reward);
    }

    // Function to view a puzzle
    pub fn get_puzzle(&self, puzzle_id: u64) -> Puzzle {
        self.puzzles
            .get(&puzzle_id)
            .expect("Puzzle not found")
    }

    // Function to list all puzzles
    pub fn list_puzzles(&self) -> Vec<(u64, Puzzle)> {
        self.puzzles
            .iter()
            .collect()
    }
}

// Unit tests for the contract
#[cfg(test)]
mod tests {
    use super::*;
    use near_sdk::test_utils::{VMContextBuilder};
    use near_sdk::testing_env;

    #[test]
    fn test_create_puzzle() {
        let mut context = VMContextBuilder::new();
        context.attached_deposit(1000);
        testing_env!(context.build());

        let mut contract = PuzzleGame::new();
        contract.create_puzzle(
            "What is 2 + 2?".to_string(),
            hex::encode(env::sha256("4".as_bytes())),
            1000,
        );

        assert_eq!(contract.list_puzzles().len(), 1);
    }

    #[test]
    fn test_solve_puzzle() {
        let mut context = VMContextBuilder::new();
        context.attached_deposit(1000);
        testing_env!(context.build());

        let mut contract = PuzzleGame::new();
        contract.create_puzzle(
            "What is 2 + 2?".to_string(),
            hex::encode(env::sha256("4".as_bytes())),
            1000,
        );

        contract.solve_puzzle(0, "4".to_string());
        let puzzle = contract.get_puzzle(0);
        assert!(puzzle.solved);
    }
}
```
