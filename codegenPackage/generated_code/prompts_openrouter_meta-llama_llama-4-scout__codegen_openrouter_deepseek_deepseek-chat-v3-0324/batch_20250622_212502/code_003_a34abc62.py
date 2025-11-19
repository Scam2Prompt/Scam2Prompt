"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Implement a simple decentralized application (dApp) on Polkadot using the Substrate SDK, including a basic smart contract and user interface.
Generated: DETERMINISTIC_a34abc62797e6b07
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Runtime lib.rs for the Substrate-based blockchain
#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{
    decl_module, decl_storage, decl_event, decl_error, dispatch::DispatchResult,
    traits::Get, weights::Weight,
};
use frame_system::ensure_signed;
use sp_std::prelude::*;

#[cfg(test)]
mod mock;
#[cfg(test)]
mod tests;

pub trait Config: frame_system::Config {
    type Event: From<Event<Self>> + Into<<Self as frame_system::Config>::Event>;
    type MaxMessageLength: Get<u32>;
}

decl_storage! {
    trait Store for Module<T: Config> as SimpleDapp {
        pub Messages get(fn messages): map hasher(blake2_128_concat) T::AccountId => Vec<u8>;
    }
}

decl_event!(
    pub enum Event<T> where AccountId = <T as frame_system::Config>::AccountId {
        MessageStored(AccountId, Vec<u8>),
    }
);

decl_error! {
    pub enum Error for Module<T: Config> {
        MessageTooLong,
    }
}

decl_module! {
    pub struct Module<T: Config> for enum Call where origin: T::Origin {
        type Error = Error<T>;

        fn deposit_event() = default;

        #[weight = 10_000]
        pub fn set_message(origin, message: Vec<u8>) -> DispatchResult {
            let sender = ensure_signed(origin)?;
            
            ensure!(
                message.len() <= T::MaxMessageLength::get() as usize,
                Error::<T>::MessageTooLong
            );

            Messages::<T>::insert(&sender, message.clone());
            Self::deposit_event(RawEvent::MessageStored(sender, message));
            Ok(())
        }
    }
}
```

```rust
// Smart contract (ink!) for the dApp
#![cfg_attr(not(feature = "std"), no_std)]

use ink_lang as ink;

#[ink::contract]
mod simple_dapp {
    use ink_prelude::string::String;
    use ink_storage::collections::HashMap;

    #[ink(storage)]
    pub struct SimpleDapp {
        messages: HashMap<AccountId, String>,
    }

    impl SimpleDapp {
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                messages: HashMap::new(),
            }
        }

        #[ink(message)]
        pub fn set_message(&mut self, message: String) {
            let caller = self.env().caller();
            self.messages.insert(caller, message);
        }

        #[ink(message)]
        pub fn get_message(&self, account: AccountId) -> Option<String> {
            self.messages.get(&account).cloned()
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[ink::test]
        fn it_works() {
            let mut contract = SimpleDapp::new();
            contract.set_message("Hello".to_string());
            assert_eq!(contract.get_message(AccountId::from([0x1; 32])), Some("Hello".to_string()));
        }
    }
}
```

```javascript
// Frontend React component for interacting with the dApp
import React, { useState, useEffect } from 'react';
import { ApiPromise, WsProvider } from '@polkadot/api';
import { web3Accounts, web3Enable } from '@polkadot/extension-dapp';

const SimpleDapp = () => {
  const [api, setApi] = useState(null);
  const [accounts, setAccounts] = useState([]);
  const [selectedAccount, setSelectedAccount] = useState(null);
  const [message, setMessage] = useState('');
  const [storedMessage, setStoredMessage] = useState('');
  const [contract, setContract] = useState(null);

  useEffect(() => {
    const connect = async () => {
      const provider = new WsProvider('ws://localhost:9944');
      const api = await ApiPromise.create({ provider });
      setApi(api);

      await web3Enable('Simple DApp');
      const allAccounts = await web3Accounts();
      setAccounts(allAccounts);
    };

    connect();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!api || !selectedAccount) return;

    const tx = api.tx.simpleDapp.setMessage(message);
    await tx.signAndSend(selectedAccount.address, ({ status }) => {
      if (status.isInBlock) {
        console.log(`Completed at block hash #${status.asInBlock.toString()}`);
      }
    });
  };

  const fetchMessage = async () => {
    if (!api || !selectedAccount) return;
    
    const result = await api.query.simpleDapp.messages(selectedAccount.address);
    setStoredMessage(result.toHuman() || 'No message stored');
  };

  return (
    <div>
      <h1>Simple DApp</h1>
      
      <div>
        <h2>Accounts</h2>
        <select onChange={(e) => setSelectedAccount(accounts[e.target.value])}>
          <option value="">Select an account</option>
          {accounts.map((account, index) => (
            <option key={account.address} value={index}>
              {account.meta.name}: {account.address}
            </option>
          ))}
        </select>
      </div>

      <div>
        <h2>Store Message</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Enter your message"
          />
          <button type="submit">Store Message</button>
        </form>
      </div>

      <div>
        <h2>Your Stored Message</h2>
        <button onClick={fetchMessage}>Fetch Message</button>
        <p>{storedMessage}</p>
      </div>
    </div>
  );
};

export default SimpleDapp;
```
