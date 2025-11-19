"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Outline the steps to implement a supply chain management system on Polkadot, leveraging its scalability and developer tools.
Generated: DETERMINISTIC_9efd2bc5100d6aef
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Supply Chain Management System on Polkadot
// This code outlines a basic implementation using Substrate, the framework for building Polkadot-compatible blockchains.

// Import necessary crates and modules
use frame_support::{dispatch::DispatchResult, pallet_prelude::*};
use frame_system::pallet_prelude::*;
use sp_std::vec::Vec;

// Define the pallet
#[frame_support::pallet]
pub mod pallet {
    use super::*;

    #[pallet::pallet]
    #[pallet::generate_store(pub(super) trait Store)]
    pub struct Pallet<T>(_);

    // Define configuration trait for the pallet
    #[pallet::config]
    pub trait Config: frame_system::Config {
        // Define associated types, such as events
        type Event: From<Event<Self>> + IsType<<Self as frame_system::Config>::Event>;
    }

    // Define the pallet's storage
    #[pallet::storage]
    #[pallet::getter(fn get_item)]
    pub type Items<T> = StorageMap<_, Blake2_128Concat, u32, SupplyItem<T>>;

    #[pallet::type_value]
    pub fn DefaultItemId<T: Config>() -> u32 {
        1
    }
    #[pallet::storage]
    #[pallet::getter(fn next_item_id)]
    pub type NextItemId<T> = StorageValue<_, u32, ValueQuery, DefaultItemId<T>>;

    // Struct to represent a supply item
    #[derive(Encode, Decode, Clone, PartialEq, Eq, RuntimeDebug, TypeInfo)]
    pub struct SupplyItem<T: Config> {
        pub id: u32,
        pub name: Vec<u8>,
        pub owner: T::AccountId,
        pub location: Vec<u8>,
    }

    // Define pallet events
    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        // Event emitted when a new item is added
        ItemCreated(u32, T::AccountId),
        // Event emitted when an item is updated
        ItemUpdated(u32, Vec<u8>),
    }

    // Define callable pallet functions
    #[pallet::call]
    impl<T: Config> Pallet<T> {
        // Function to create a new supply item
        #[pallet::weight(10_000)]
        pub fn create_item(
            origin: OriginFor<T>,
            name: Vec<u8>,
            location: Vec<u8>,
        ) -> DispatchResult {
            let sender = ensure_signed(origin)?;

            let item_id = Self::next_item_id();
            let new_item = SupplyItem::<T> {
                id: item_id,
                name: name.clone(),
                owner: sender.clone(),
                location: location.clone(),
            };

            Items::<T>::insert(item_id, new_item);
            NextItemId::<T>::set(item_id + 1);

            Self::deposit_event(Event::ItemCreated(item_id, sender));
            Ok(())
        }

        // Function to update an item's location
        #[pallet::weight(10_000)]
        pub fn update_item(
            origin: OriginFor<T>,
            item_id: u32,
            new_location: Vec<u8>,
        ) -> DispatchResult {
            let sender = ensure_signed(origin)?;

            ensure!(Items::<T>::contains_key(item_id), "Item does not exist");
            let mut item = Items::<T>::get(item_id).unwrap();

            ensure!(item.owner == sender, "Only the owner can update the item");

            item.location = new_location.clone();
            Items::<T>::insert(item_id, item);

            Self::deposit_event(Event::ItemUpdated(item_id, new_location));
            Ok(())
        }
    }
}
```
