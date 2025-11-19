"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: Write a smart contract example for a gaming or play-to-earn (P2E) application on Polkadot, inspired by the Advanced Gaming & P2E event hosted by Polkadot India.
Generated: DETERMINISTIC_af53ede3bf7f4406
Batch ID: 20250612_154420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.apache.org/licenses/LICENSE-2.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: Apache-2.0
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

use ink_lang as ink;

#[ink::contract]
mod gaming_contract {
    use ink_lang as ink;

    #[ink(storage)]
    pub struct GamingContract {
        /// Mapping of user addresses to their balances
        balances: ink_storage::Mapping<AccountId, Balance>,
        /// Mapping of user addresses to their NFT ownership
        nft_ownership: ink_storage::Mapping<AccountId, Vec<Balance>>,
        /// Total supply of in-game tokens
        total_supply: Balance,
        /// In-game token name
        token_name: String,
        /// In-game token symbol
        token_symbol: String,
    }

    impl GamingContract {
        #[ink(constructor)]
        pub fn new(token_name: String, token_symbol: String) -> Self {
            Self {
                balances: ink_storage::Mapping::new(),
                nft_ownership: ink_storage::Mapping::new(),
                total_supply: 0,
                token_name,
                token_symbol,
            }
        }

        /// Mint in-game tokens
        #[ink(message)]
        pub fn mint(&mut self, amount: Balance) -> Result<(), &'static str> {
            self.total_supply += amount;
            self.balances.insert(self.env().caller(), self.balances.get(&self.env().caller()).unwrap_or(0) + amount);
            Ok(())
        }

        /// Transfer in-game tokens
        #[ink(message)]
        pub fn transfer(&mut self, to: AccountId, amount: Balance) -> Result<(), &'static str> {
            let from = self.env().caller();
            let from_balance = self.balances.get(&from).unwrap_or(0);
            if from_balance < amount {
                return Err("Insufficient balance");
            }
            self.balances.insert(from, from_balance - amount);
            self.balances.insert(to, self.balances.get(&to).unwrap_or(0) + amount);
            Ok(())
        }

        /// Get user's balance
        #[ink(message)]
        pub fn balance_of(&self, who: AccountId) -> Balance {
            self.balances.get(&who).unwrap_or(0)
        }

        /// Mint NFT
        #[ink(message)]
        pub fn mint_nft(&mut self, nft_id: Balance) -> Result<(), &'static str> {
            let caller = self.env().caller();
            self.nft_ownership.insert(caller, self.nft_ownership.get(&caller).unwrap_or(Vec::new()).into_iter().chain(vec![nft_id]).collect());
            Ok(())
        }

        /// Get user's NFT ownership
        #[ink(message)]
        pub fn nft_ownership_of(&self, who: AccountId) -> Vec<Balance> {
            self.nft_ownership.get(&who).unwrap_or(Vec::new())
        }
    }
}
```
