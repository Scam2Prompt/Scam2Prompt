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
use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::collections::{LookupMap, UnorderedSet};
use near_sdk::json_types::U128;
use near_sdk::{
    env, near_bindgen, AccountId, Balance, BorshStorageKey, PanicOnDefault, Promise, PromiseOrValue,
};
use std::collections::HashMap;

#[derive(BorshSerialize, BorshStorageKey)]
enum StorageKey {
    Players,
    Puzzles,
    Solutions,
    Rewards,
}

#[derive(BorshSerialize, BorshDeserialize, Debug, Clone)]
pub struct Puzzle {
    id: u64,
    creator: AccountId,
    description: String,
    reward: Balance,
    solution_hash: String,
    is_solved: bool,
}

#[derive(BorshSerialize, BorshDeserialize, Debug, Clone)]
pub struct Solution {
    solver: AccountId,
    puzzle_id: u64,
    solution: String,
    timestamp: u64,
}

#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct PuzzleGame {
    players: UnorderedSet<AccountId>,
    puzzles: LookupMap<u64, Puzzle>,
    solutions: LookupMap<u64, Solution>,
    rewards: LookupMap<AccountId, Balance>,
    next_puzzle_id: u64,
}

#[near_bindgen]
impl PuzzleGame {
    #[init]
    pub fn new() -> Self {
        Self {
            players: UnorderedSet::new(StorageKey::Players),
            puzzles: LookupMap::new(StorageKey::Puzzles),
            solutions: LookupMap::new(StorageKey::Solutions),
            rewards: LookupMap::new(StorageKey::Rewards),
            next_puzzle_id: 1,
        }
    }

    pub fn create_puzzle(
        &mut self,
        description: String,
        solution_hash: String,
        reward: U128,
    ) -> u64 {
        let creator = env::predecessor_account_id();
        let puzzle_id = self.next_puzzle_id;
        self.next_puzzle_id += 1;

        let puzzle = Puzzle {
            id: puzzle_id,
            creator: creator.clone(),
            description,
            reward: reward.0,
            solution_hash,
            is_solved: false,
        };

        self.puzzles.insert(&puzzle_id, &puzzle);
        self.players.insert(&creator);
        puzzle_id
    }

    pub fn solve_puzzle(&mut self, puzzle_id: u64, solution: String) -> bool {
        let solver = env::predecessor_account_id();
        let puzzle = self.puzzles.get(&puzzle_id).expect("Puzzle not found");

        assert!(!puzzle.is_solved, "Puzzle already solved");
        assert_eq!(
            env::sha256(solution.as_bytes()),
            puzzle.solution_hash.as_bytes(),
            "Incorrect solution"
        );

        let solution_entry = Solution {
            solver: solver.clone(),
            puzzle_id,
            solution,
            timestamp: env::block_timestamp(),
        };

        self.solutions.insert(&puzzle_id, &solution_entry);
        self.players.insert(&solver);

        let mut puzzle = puzzle.clone();
        puzzle.is_solved = true;
        self.puzzles.insert(&puzzle_id, &puzzle);

        let reward = puzzle.reward;
        if reward > 0 {
            let current_reward = self.rewards.get(&solver).unwrap_or(0);
            self.rewards.insert(&solver, &(current_reward + reward));
        }

        true
    }

    pub fn claim_reward(&mut self) -> Promise {
        let account_id = env::predecessor_account_id();
        let amount = self.rewards.get(&account_id).expect("No rewards to claim");

        self.rewards.remove(&account_id);

        Promise::new(account_id).transfer(amount)
    }

    pub fn get_puzzle(&self, puzzle_id: u64) -> Option<Puzzle> {
        self.puzzles.get(&puzzle_id)
    }

    pub fn get_solution(&self, puzzle_id: u64) -> Option<Solution> {
        self.solutions.get(&puzzle_id)
    }

    pub fn get_player_reward(&self, account_id: AccountId) -> U128 {
        U128(self.rewards.get(&account_id).unwrap_or(0))
    }

    pub fn get_total_puzzles(&self) -> u64 {
        self.next_puzzle_id - 1
    }

    pub fn get_solved_puzzles(&self) -> Vec<Puzzle> {
        (1..self.next_puzzle_id)
            .filter_map(|id| {
                self.puzzles
                    .get(&id)
                    .filter(|puzzle| puzzle.is_solved)
            })
            .collect()
    }
}
```
