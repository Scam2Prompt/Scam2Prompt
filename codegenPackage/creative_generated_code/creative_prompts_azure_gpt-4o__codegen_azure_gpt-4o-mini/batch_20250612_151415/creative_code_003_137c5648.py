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
// Import necessary libraries and traits
use ink_lang as ink;

// Define the NFT contract
#[ink::contract]
mod nft_contract {
    use ink_storage::collections::HashMap as StorageHashMap;

    #[ink(storage)]
    pub struct NftContract {
        // Mapping from token ID to owner address
        owners: StorageHashMap<u64, AccountId>,
        // Mapping from owner address to their token count
        balances: StorageHashMap<AccountId, u64>,
        // Total supply of minted tokens
        total_supply: u64,
    }

    impl NftContract {
        // Constructor to initialize the contract state
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                owners: StorageHashMap::new(),
                balances: StorageHashMap::new(),
                total_supply: 0,
            }
        }

        // Function to mint a new NFT
        #[ink(message)]
        pub fn mint(&mut self) -> Result<u64, &'static str> {
            // Get the caller's account ID
            let caller = self.env().caller();

            // Increment total supply to get the new token ID
            self.total_supply += 1;
            let token_id = self.total_supply;

            // Assign the token to the caller
            self.owners.insert(token_id, caller);
            let balance = self.balances.entry(caller).or_insert(0);
            *balance += 1;

            // Return the new token ID
            Ok(token_id)
        }

        // Function to get the owner of a specific token ID
        #[ink(message)]
        pub fn owner_of(&self, token_id: u64) -> Result<AccountId, &'static str> {
            // Check if the token ID exists
            match self.owners.get(&token_id) {
                Some(&owner) => Ok(owner),
                None => Err("Token does not exist"),
            }
        }

        // Function to get the balance of a specific account
        #[ink(message)]
        pub fn balance_of(&self, owner: AccountId) -> Result<u64, &'static str> {
            // Retrieve the balance from the storage map
            match self.balances.get(&owner) {
                Some(&balance) => Ok(balance),
                None => Ok(0), // Return 0 if the owner has no tokens
            }
        }
    }

    // Implement the default trait for the contract (optional)
    impl Default for NftContract {
        fn default() -> Self {
            Self::new()
        }
    }
}
```
