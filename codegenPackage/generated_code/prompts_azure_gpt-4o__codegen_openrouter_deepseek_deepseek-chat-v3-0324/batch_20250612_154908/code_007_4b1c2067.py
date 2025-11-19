"""
Generated Code Metadata:
========================
Original URL: https://zkdrops.xyz
Prompt: Provide an example of using zkdrops to compress participation data on Solana for efficient storage and verification.
Generated: DETERMINISTIC_4b1c206734529857
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use solana_program::{
    account_info::AccountInfo,
    entrypoint,
    entrypoint::ProgramResult,
    pubkey::Pubkey,
    program_error::ProgramError,
};
use std::collections::BTreeMap;

// Define the zkdrop structure
#[derive(Debug)]
struct ZkDrop {
    root: [u8; 32],
    participants: BTreeMap<Pubkey, bool>,
}

impl ZkDrop {
    // Initialize a new zkdrop with empty state
    pub fn new() -> Self {
        ZkDrop {
            root: [0; 32],
            participants: BTreeMap::new(),
        }
    }

    // Add a participant to the zkdrop
    pub fn add_participant(&mut self, participant: Pubkey) {
        self.participants.insert(participant, true);
        self.update_root();
    }

    // Remove a participant from the zkdrop
    pub fn remove_participant(&mut self, participant: &Pubkey) -> Result<(), ProgramError> {
        if self.participants.remove(participant).is_none() {
            return Err(ProgramError::InvalidAccountData);
        }
        self.update_root();
        Ok(())
    }

    // Verify if a participant exists in the zkdrop
    pub fn verify_participant(&self, participant: &Pubkey) -> bool {
        self.participants.contains_key(participant)
    }

    // Update the merkle root based on current participants
    fn update_root(&mut self) {
        let mut hashes: Vec<[u8; 32]> = self.participants
            .keys()
            .map(|key| solana_program::keccak::hash(key.as_ref()).to_bytes())
            .collect();
        
        // Sort hashes for consistent merkle tree construction
        hashes.sort();

        // Simple merkle root calculation (in production, use a proper merkle tree library)
        self.root = if hashes.is_empty() {
            [0; 32]
        } else if hashes.len() == 1 {
            hashes[0]
        } else {
            let combined = [hashes[0], hashes[1]].concat();
            solana_program::keccak::hash(&combined).to_bytes()
        };
    }

    // Get the current merkle root
    pub fn get_root(&self) -> [u8; 32] {
        self.root
    }
}

// Program entrypoint
entrypoint!(process_instruction);
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    // In a real implementation, you would:
    // 1. Deserialize instruction data
    // 2. Validate accounts
    // 3. Load or initialize zkdrop state
    // 4. Perform requested operation (add/remove/verify)
    // 5. Store updated state
    
    // This is a simplified example
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::pubkey::Pubkey;

    #[test]
    fn test_zkdrop_operations() {
        let mut zkdrop = ZkDrop::new();
        let participant1 = Pubkey::new_unique();
        let participant2 = Pubkey::new_unique();

        // Test adding participants
        zkdrop.add_participant(participant1);
        zkdrop.add_participant(participant2);
        assert!(zkdrop.verify_participant(&participant1));
        assert!(zkdrop.verify_participant(&participant2));

        // Test removing participant
        zkdrop.remove_participant(&participant1).unwrap();
        assert!(!zkdrop.verify_participant(&participant1));
        assert!(zkdrop.verify_participant(&participant2));

        // Test root updates
        let root = zkdrop.get_root();
        assert_ne!(root, [0; 32]);
    }
}
```
