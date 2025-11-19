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
// Import necessary libraries from the Substrate framework
#![cfg_attr(not(feature = "std"), no_std)]

pub use pallet::*;

#[frame_support::pallet]
pub mod pallet {
    use frame_support::{dispatch::DispatchResult, pallet_prelude::*};
    use frame_system::pallet_prelude::*;
    use sp_std::vec::Vec;

    #[pallet::pallet]
    #[pallet::generate_store(pub(super) trait Store)]
    pub struct Pallet<T>(_);

    #[pallet::config]
    pub trait Config: frame_system::Config {}

    #[pallet::storage]
    #[pallet::getter(fn get_message)]
    pub type Messages<T> = StorageMap<_, Blake2_128Concat, T::AccountId, Vec<u8>, OptionQuery>;

    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        MessageStored(T::AccountId, Vec<u8>),
    }

    #[pallet::error]
    pub enum Error<T> {
        MessageTooLong,
        MessageNotFound,
    }

    #[pallet::call]
    impl<T: Config> Pallet<T> {
        /// Store a message in the storage
        #[pallet::weight(10_000)]
        pub fn store_message(origin: OriginFor<T>, message: Vec<u8>) -> DispatchResult {
            let sender = ensure_signed(origin)?;

            // Ensure the message is not too long
            ensure!(message.len() <= 256, Error::<T>::MessageTooLong);

            // Store the message
            Messages::<T>::insert(&sender, message.clone());

            // Emit an event
            Self::deposit_event(Event::MessageStored(sender.clone(), message));

            Ok(())
        }

        /// Retrieve a message from storage
        #[pallet::weight(10_000)]
        pub fn retrieve_message(origin: OriginFor<T>) -> DispatchResult {
            let sender = ensure_signed(origin)?;

            // Check if the message exists
            let message = Messages::<T>::get(&sender).ok_or(Error::<T>::MessageNotFound)?;

            // Emit an event with the retrieved message
            Self::deposit_event(Event::MessageStored(sender.clone(), message));

            Ok(())
        }
    }
}
```

### Frontend Code (React)

```javascript
import React, { useState, useEffect } from 'react';
import { ApiPromise, WsProvider } from '@polkadot/api';

const App = () => {
    const [api, setApi] = useState(null);
    const [account, setAccount] = useState(null);
    const [message, setMessage] = useState('');
    const [storedMessage, setStoredMessage] = useState('');

    useEffect(() => {
        const initApi = async () => {
            const provider = new WsProvider('wss://your-polkadot-node-url');
            const api = await ApiPromise.create({ provider });
            setApi(api);
        };
        initApi();
    }, []);

    const handleStoreMessage = async () => {
        if (!api || !account) return;

        const tx = api.tx.yourPallet.storeMessage(message);
        await tx.signAndSend(account, ({ status }) => {
            if (status.isInBlock) {
                console.log('Message stored in block');
            }
        });
    };

    const handleRetrieveMessage = async () => {
        if (!api || !account) return;

        const message = await api.query.yourPallet.messages(account.address);
        setStoredMessage(message.toString());
    };

    return (
        <div>
            <h1>Simple dApp on Polkadot</h1>
            <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Enter your message"
            />
            <button onClick={handleStoreMessage}>Store Message</button>
            <button onClick={handleRetrieveMessage}>Retrieve Message</button>
            {storedMessage && <p>Stored Message: {storedMessage}</p>}
        </div>
    );
};

export default App;
```

### Notes
- Replace `your-pallet` with the actual name of your pallet.
- Replace `wss://your-polkadot-node-url` with the actual WebSocket URL of your Polkadot node.
- Ensure you have the necessary dependencies installed for both the Rust and React parts of the application.
