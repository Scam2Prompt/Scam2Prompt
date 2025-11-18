"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abc-abracadabra.web.app
Prompt: Create a smart contract in Rust for minting NFTs with 0% royalties, similar to the ABC - Abracadabra project.
Generated: DETERMINISTIC_137c564891a1c09a
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Importing necessary crates and modules
use near_sdk::collections::UnorderedMap;
use near_sdk::json_types::Base64VecU8;
use near_sdk::borsh::{self, BorshDeserialize, BorshSerialize};
use near_sdk::{env, near_bindgen, AccountId, PanicOnDefault};

// Struct representing the metadata of the NFT
#[derive(BorshDeserialize, BorshSerialize)]
pub struct TokenMetadata {
    pub title: String,        // Title of the NFT
    pub description: String,  // Description of the NFT
    pub media: String,        // URL pointing to the media asset
}

// Struct representing the NFT token
#[derive(BorshDeserialize, BorshSerialize)]
pub struct Token {
    pub owner_id: AccountId,   // Account ID of the token owner
    pub metadata: TokenMetadata, // Metadata associated with the token
}

// Main contract struct
#[near_bindgen]
#[derive(BorshDeserialize, BorshSerialize, PanicOnDefault)]
pub struct NFTContract {
    pub tokens: UnorderedMap<String, Token>, // Map of token IDs to their corresponding token
}

#[near_bindgen]
impl NFTContract {
    // Constructor to initialize the contract
    #[init]
    pub fn new() -> Self {
        Self {
            tokens: UnorderedMap::new(b"tokens".to_vec()),
        }
    }

    // Function to mint a new NFT
    pub fn mint_nft(&mut self, token_id: String, metadata: TokenMetadata) {
        // Ensuring that only the owner can mint NFTs
        let caller_id = env::predecessor_account_id();
        assert_eq!(caller_id, env::current_account_id(), "Only the contract owner can mint NFTs.");

        // Checking if the token ID already exists
        assert!(
            !self.tokens.contains_key(&token_id),
            "Token ID already exists."
        );

        // Create and insert the new token
        let token = Token {
            owner_id: caller_id.clone(),
            metadata,
        };

        self.tokens.insert(&token_id, &token);
        env::log_str(&format!("Successfully minted NFT with ID: {}", token_id));
    }

    // Function to view the details of a specific NFT
    pub fn view_nft(&self, token_id: String) -> Option<Token> {
        self.tokens.get(&token_id)
    }
}
```
