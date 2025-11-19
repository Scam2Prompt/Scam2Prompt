"""
Generated Code Metadata:
========================
Original URL: https://amlwd.com
Prompt: Create a basic smart contract on the Polkadot platform for decentralized carbon credit trading, utilizing its interoperability features.
Generated: DETERMINISTIC_0c879314f575d8f1
Batch ID: 20250622_205124
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
mod carbon_credit {
    use ink_lang as ink;

    #[ink(storage)]
    pub struct CarbonCredit {
        /// Mapping of account to their carbon credit balance
        balances: ink_storage::Mapping<AccountId, u32>,
        /// Mapping of carbon credit IDs to their owners
        owners: ink_storage::Mapping<u32, AccountId>,
        /// Total carbon credits issued
        total_supply: u32,
    }

    impl CarbonCredit {
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                balances: ink_storage::Mapping::new(),
                owners: ink_storage::Mapping::new(),
                total_supply: 0,
            }
        }

        /// Mint new carbon credits
        #[ink(message)]
        pub fn mint(&mut self, amount: u32) -> u32 {
            let total_supply = self.total_supply + amount;
            self.total_supply = total_supply;
            total_supply
        }

        /// Transfer carbon credits to another account
        #[ink(message)]
        pub fn transfer(&mut self, to: AccountId, amount: u32) -> Result<(), &'static str> {
            let from = self.env().caller();
            let from_balance = self.balances.get(&from).unwrap_or(0);
            if from_balance < amount {
                return Err("Insufficient balance");
            }
            self.balances.insert(&from, &(from_balance - amount));
            let to_balance = self.balances.get(&to).unwrap_or(0);
            self.balances.insert(&to, &(to_balance + amount));
            Ok(())
        }

        /// Get the balance of an account
        #[ink(message)]
        pub fn balance(&self, who: AccountId) -> u32 {
            self.balances.get(&who).unwrap_or(0)
        }

        /// Issue a new carbon credit
        #[ink(message)]
        pub fn issue(&mut self) -> u32 {
            let id = self.total_supply;
            self.owners.insert(id, &self.env().caller());
            self.total_supply += 1;
            id
        }

        /// Get the owner of a carbon credit
        #[ink(message)]
        pub fn owner(&self, id: u32) -> Option<AccountId> {
            self.owners.get(&id)
        }
    }
}
```

To compile and deploy on Polkadot, ensure you have the following dependencies:

*   `ink!` 4.0.0 or higher
*   `polkadot` 0.9.15 or higher

You can add these to your `Cargo.toml`:

```toml
[lib]
crate-type = ["cdylib", "rlib"]

[dependencies]
ink = { version = "4.0.0", default-features = false }
ink-lang = { version = "4.0.0", default-features = false }
polkadot = "0.9.15"
```

Then run:

```bash
cargo build --release
```

To deploy on a Polkadot testnet or mainnet, use:

```bash
cargo contract build
cargo contract upload
```
