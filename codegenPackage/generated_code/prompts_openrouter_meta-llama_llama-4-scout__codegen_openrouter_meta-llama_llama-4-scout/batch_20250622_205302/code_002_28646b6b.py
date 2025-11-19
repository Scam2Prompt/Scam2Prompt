"""
Generated Code Metadata:
========================
Original URL: https://starknetvietnam.wordpress.com
Prompt: Generate a Cairo code example for a simple NFT game on StarkNet, inspired by the Starknet Vietnam Community.
Generated: DETERMINISTIC_28646b6b5b5860fa
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cairo
// SPDX-License-Identifier: MIT
// This contract is an example of a simple NFT game on StarkNet.

use starknet::Contract;
use starknet::ContractError;
use starknet::Event;

#[starknet::contract]
mod simple_nft_game {
    #[contract::storage]
    struct Storage {
        owner: starknet::Felt,
        nft_count: u128,
        nft_owners: Mapping<starknet::Felt, starknet::Felt>,
    }

    #[contract::event]
    enum Event {
        NftMinted {
            token_id: starknet::Felt,
            owner: starknet::Felt,
        },
        NftTransferred {
            token_id: starknet::Felt,
            from: starknet::Felt,
            to: starknet::Felt,
        },
    }

    impl SimpleNftGame {
        fn new() -> Self {
            Self {
                owner: starknet::Felt::from(0u8),
                nft_count: 0,
                nft_owners: Mapping::new(),
            }
        }

        #[contract::function]
        fn mint_nft(self, token_id: starknet::Felt) -> Result<(), ContractError> {
            // Check if token_id already exists
            if self.nft_owners.get(&token_id).is_some() {
                return Err(ContractError::TokenIdAlreadyExists);
            }

            // Mint NFT
            self.nft_owners.insert(&token_id, &self.owner);
            self.nft_count += 1;

            // Emit event
            self.emit_event(Event::NftMinted { token_id, owner: self.owner });

            Ok(())
        }

        #[contract::function]
        fn transfer_nft(self, token_id: starknet::Felt, to: starknet::Felt) -> Result<(), ContractError> {
            // Check if token_id exists
            let from = self.nft_owners.get(&token_id).ok_or(ContractError::TokenIdDoesNotExist)?;

            // Check if caller is owner
            if from != starknet::Felt::from_selector(self.caller()) {
                return Err(ContractError::NotOwner);
            }

            // Transfer NFT
            self.nft_owners.insert(&token_id, &to);

            // Emit event
            self.emit_event(Event::NftTransferred { token_id, from, to });

            Ok(())
        }

        #[contract::function]
        fn get_nft_owner(self, token_id: starknet::Felt) -> Result<starknet::Felt, ContractError> {
            self.nft_owners.get(&token_id).ok_or(ContractError::TokenIdDoesNotExist)
        }
    }
}
```
