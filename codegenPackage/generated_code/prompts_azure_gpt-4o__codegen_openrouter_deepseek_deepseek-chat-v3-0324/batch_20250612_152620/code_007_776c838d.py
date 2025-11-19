"""
Generated Code Metadata:
========================
Original URL: https://metarebelz-rust.vercel.app
Prompt: Provide Rust-based code for tracking NFT traits and granting access to specific rooms in a virtual environment, similar to the "Rebelz Alley" concept described on the Meta Rebelz site.
Generated: DETERMINISTIC_776c838d373cbadf
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use std::collections::HashMap;
use serde::{Deserialize, Serialize};
use thiserror::Error;

/// Represents an NFT with its traits
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct NFT {
    pub id: String,
    pub traits: HashMap<String, String>,
}

/// Represents a virtual room with access requirements
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct VirtualRoom {
    pub id: String,
    pub name: String,
    pub required_traits: HashMap<String, String>,
}

/// Error types for access control
#[derive(Error, Debug)]
pub enum AccessError {
    #[error("NFT does not have required traits for this room")]
    InsufficientTraits,
    #[error("NFT not found")]
    NFTNotFound,
    #[error("Room not found")]
    RoomNotFound,
    #[error("Database error")]
    DatabaseError(#[from] Box<dyn std::error::Error>),
}

/// Main access control system
pub struct AccessControlSystem {
    nfts: HashMap<String, NFT>,
    rooms: HashMap<String, VirtualRoom>,
}

impl AccessControlSystem {
    /// Create a new AccessControlSystem
    pub fn new() -> Self {
        AccessControlSystem {
            nfts: HashMap::new(),
            rooms: HashMap::new(),
        }
    }

    /// Add an NFT to the system
    pub fn add_nft(&mut self, nft: NFT) {
        self.nfts.insert(nft.id.clone(), nft);
    }

    /// Add a virtual room to the system
    pub fn add_room(&mut self, room: VirtualRoom) {
        self.rooms.insert(room.id.clone(), room);
    }

    /// Check if an NFT has access to a room
    pub fn check_access(&self, nft_id: &str, room_id: &str) -> Result<bool, AccessError> {
        let nft = self.nfts.get(nft_id).ok_or(AccessError::NFTNotFound)?;
        let room = self.rooms.get(room_id).ok_or(AccessError::RoomNotFound)?;

        for (trait_key, required_value) in &room.required_traits {
            match nft.traits.get(trait_key) {
                Some(nft_value) if nft_value == required_value => continue,
                _ => return Err(AccessError::InsufficientTraits),
            }
        }

        Ok(true)
    }

    /// Grant access to a room if requirements are met
    pub fn grant_access(&self, nft_id: &str, room_id: &str) -> Result<(), AccessError> {
        if self.check_access(nft_id, room_id)? {
            println!("Access granted to NFT {} for room {}", nft_id, room_id);
            Ok(())
        } else {
            Err(AccessError::InsufficientTraits)
        }
    }

    /// Get all rooms accessible by an NFT
    pub fn get_accessible_rooms(&self, nft_id: &str) -> Result<Vec<VirtualRoom>, AccessError> {
        let nft = self.nfts.get(nft_id).ok_or(AccessError::NFTNotFound)?;
        let mut accessible_rooms = Vec::new();

        for room in self.rooms.values() {
            let mut has_access = true;
            for (trait_key, required_value) in &room.required_traits {
                match nft.traits.get(trait_key) {
                    Some(nft_value) if nft_value == required_value => continue,
                    _ => {
                        has_access = false;
                        break;
                    }
                }
            }
            if has_access {
                accessible_rooms.push(room.clone());
            }
        }

        Ok(accessible_rooms)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn setup_test_environment() -> AccessControlSystem {
        let mut system = AccessControlSystem::new();

        // Add test NFTs
        let mut traits = HashMap::new();
        traits.insert("background".to_string(), "blue".to_string());
        traits.insert("hat".to_string(), "cowboy".to_string());
        system.add_nft(NFT {
            id: "nft1".to_string(),
            traits,
        });

        // Add test rooms
        let mut required_traits = HashMap::new();
        required_traits.insert("hat".to_string(), "cowboy".to_string());
        system.add_room(VirtualRoom {
            id: "room1".to_string(),
            name: "Cowboy Lounge".to_string(),
            required_traits,
        });

        system
    }

    #[test]
    fn test_access_granted() {
        let system = setup_test_environment();
        assert!(system.check_access("nft1", "room1").unwrap());
    }

    #[test]
    fn test_access_denied() {
        let mut system = setup_test_environment();
        
        // Add NFT without required traits
        let mut traits = HashMap::new();
        traits.insert("background".to_string(), "red".to_string());
        system.add_nft(NFT {
            id: "nft2".to_string(),
            traits,
        });

        assert!(matches!(
            system.check_access("nft2", "room1"),
            Err(AccessError::InsufficientTraits)
        ));
    }

    #[test]
    fn test_get_accessible_rooms() {
        let system = setup_test_environment();
        let rooms = system.get_accessible_rooms("nft1").unwrap();
        assert_eq!(rooms.len(), 1);
        assert_eq!(rooms[0].name, "Cowboy Lounge");
    }
}
```
