"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Write a code snippet that demonstrates how to implement a parachain using the Substrate SDK in Polkadot.
Generated: DETERMINISTIC_083d36efb79faafa
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary modules from Substrate
use frame_support::{decl_module, decl_storage, decl_event, dispatch::DispatchResult, ensure};
use frame_system::ensure_signed;
use sp_std::vec::Vec;

/// The runtime module for the parachain
pub trait Config: frame_system::Config {
    /// Event type for this module
    type Event: From<Event<Self>> + Into<<Self as frame_system::Config>::Event>;
}

/// Struct for the module's storage
decl_storage! {
    trait Store for Module<T: Config> as ParachainModule {
        // Store the parachain data
        ParachainData get(fn parachain_data): map hasher(blake2_128_concat) T::AccountId => Vec<u8>;
    }
}

/// Events that this module can emit
decl_event! {
    pub enum Event<T> where AccountId = <T as frame_system::Config>::AccountId {
        /// Event emitted when parachain data is added
        DataAdded(AccountId, Vec<u8>),
    }
}

/// The main module for the parachain
decl_module! {
    pub struct Module<T: Config> for enum Call where origin: T::Origin {
        // Emit events
        fn deposit_event() = default;

        /// Function to add data to the parachain
        #[weight = 10_000]
        fn add_data(origin, data: Vec<u8>) -> DispatchResult {
            // Ensure the caller is a signed user
            let who = ensure_signed(origin)?;
            
            // Validate the data length
            ensure!(!data.is_empty(), "Data cannot be empty");

            // Store the parachain data
            ParachainData::<T>::insert(&who, data.clone());

            // Emit the DataAdded event
            Self::deposit_event(RawEvent::DataAdded(who, data));

            Ok(())
        }
    }
}

/// Implementing the parachain functionality
impl<T: Config> Module<T> {
    /// This function retrieves the parachain data for a given account
    pub fn get_parachain_data(account: T::AccountId) -> Option<Vec<u8>> {
        ParachainData::<T>::get(account)
    }
}
```
