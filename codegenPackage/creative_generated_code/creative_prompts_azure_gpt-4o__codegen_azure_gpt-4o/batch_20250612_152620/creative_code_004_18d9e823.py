"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metarebelz-rust.vercel.app
Prompt: Write a Rust program to manage dynamic NFT versions, including functionality for matching and distributing rare 1/1 NFTs, as described in the Meta Rebelz rewards phase.
Generated: DETERMINISTIC_18d9e8234a2a7cc2
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use std::collections::HashMap;

// Define a struct for an NFT
#[derive(Debug, Clone)]
struct NFT {
    id: u64,
    name: String,
    rarity: Rarity,
}

// Enum to represent NFT rarity
#[derive(Debug, Clone, PartialEq)]
enum Rarity {
    Common,
    Rare,
    Epic,
    Legendary,
    OneOfOne, // Rare 1/1 NFTs
}

// Struct to manage the NFT collection
struct NFTManager {
    nfts: Vec<NFT>,
    distributed_nfts: HashMap<u64, NFT>, // Track distributed NFTs
}

impl NFTManager {
    // Create a new NFT manager
    fn new() -> Self {
        NFTManager {
            nfts: Vec::new(),
            distributed_nfts: HashMap::new(),
        }
    }

    // Add an NFT to the collection
    fn add_nft(&mut self, nft: NFT) {
        self.nfts.push(nft);
    }

    // Distribute NFTs based on rarity
    fn distribute_nft(&mut self, rarity: Rarity) -> Result<NFT, String> {
        // Find an NFT matching the desired rarity
        if let Some(index) = self.nfts.iter().position(|n| n.rarity == rarity) {
            let nft = self.nfts.remove(index); // Remove from collection
            self.distributed_nfts.insert(nft.id, nft.clone()); // Track it as distributed
            Ok(nft)
        } else {
            Err(format!("No NFTs of rarity {:?} available for distribution.", rarity))
        }
    }

    // Retrieve a distributed NFT by ID
    fn get_distributed_nft(&self, id: u64) -> Option<&NFT> {
        self.distributed_nfts.get(&id)
    }
}

fn main() {
    // Initialize the NFT Manager
    let mut manager = NFTManager::new();

    // Add some sample NFTs to the collection
    manager.add_nft(NFT {
        id: 1,
        name: String::from("Meta Rebel #1"),
        rarity: Rarity::Common,
    });
    manager.add_nft(NFT {
        id: 2,
        name: String::from("Meta Rebel #2"),
        rarity: Rarity::Rare,
    });
    manager.add_nft(NFT {
        id: 3,
        name: String::from("Meta Rebel #3"),
        rarity: Rarity::OneOfOne,
    });

    // Distribute a rare NFT
    match manager.distribute_nft(Rarity::Rare) {
        Ok(nft) => println!("Distributed NFT: {:?}", nft),
        Err(e) => println!("Error distributing NFT: {}", e),
    }

    // Distribute a 1/1 NFT
    match manager.distribute_nft(Rarity::OneOfOne) {
        Ok(nft) => println!("Distributed 1/1 NFT: {:?}", nft),
        Err(e) => println!("Error distributing NFT: {}", e),
    }

    // Attempt to distribute a non-existent NFT
    match manager.distribute_nft(Rarity::Legendary) {
        Ok(nft) => println!("Distributed NFT: {:?}", nft),
        Err(e) => println!("Error distributing NFT: {}", e),
    }

    // Retrieve a distributed NFT
    if let Some(nft) = manager.get_distributed_nft(2) {
        println!("Retrieved distributed NFT: {:?}", nft);
    } else {
        println!("NFT with ID 2 not found in distributed collection.");
    }
}
```
