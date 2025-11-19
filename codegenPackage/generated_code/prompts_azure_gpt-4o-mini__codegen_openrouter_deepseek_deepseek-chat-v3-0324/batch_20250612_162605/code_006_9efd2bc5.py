"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Outline the steps to implement a supply chain management system on Polkadot, leveraging its scalability and developer tools.
Generated: DETERMINISTIC_9efd2bc5100d6aef
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Supply Chain Management System on Polkadot
//! This module implements a supply chain management system as a Substrate pallet.

#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{
    dispatch::DispatchResult,
    ensure,
    pallet_prelude::*,
    traits::{Currency, ExistenceRequirement, ReservableCurrency},
    transactional,
};
use frame_system::pallet_prelude::*;
use sp_runtime::traits::{AccountIdConversion, CheckedAdd, CheckedSub, Zero};
use sp_std::prelude::*;

pub use pallet::*;

#[frame_support::pallet]
pub mod pallet {
    use super::*;

    /// Configure the pallet by specifying the parameters and types on which it depends.
    #[pallet::config]
    pub trait Config: frame_system::Config {
        /// Because this pallet emits events, it depends on the runtime's definition of an event.
        type Event: From<Event<Self>> + IsType<<Self as frame_system::Config>::Event>;

        /// The currency type for handling payments
        type Currency: Currency<Self::AccountId> + ReservableCurrency<Self::AccountId>;
    }

    #[pallet::pallet]
    #[pallet::generate_store(pub(super) trait Store)]
    pub struct Pallet<T>(_);

    #[pallet::storage]
    #[pallet::getter(fn products)]
    pub type Products<T: Config> = StorageMap<
        _,
        Blake2_128Concat,
        T::Hash,
        Product<T::AccountId, T::BlockNumber>,
    >;

    #[pallet::storage]
    #[pallet::getter(fn product_owners)]
    pub type ProductOwners<T: Config> = StorageMap<
        _,
        Blake2_128Concat,
        T::Hash,
        T::AccountId,
    >;

    #[pallet::storage]
    #[pallet::getter(fn supply_chain)]
    pub type SupplyChain<T: Config> = StorageMap<
        _,
        Blake2_128Concat,
        T::Hash,
        Vec<SupplyChainEvent<T::AccountId, T::BlockNumber>>,
    >;

    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        /// A new product was created
        ProductCreated(T::Hash, T::AccountId),
        /// Product ownership was transferred
        ProductTransferred(T::Hash, T::AccountId, T::AccountId),
        /// Product state was updated
        ProductStateUpdated(T::Hash, Vec<u8>),
    }

    #[pallet::error]
    pub enum Error<T> {
        /// Product does not exist
        ProductNotFound,
        /// Caller is not the product owner
        NotProductOwner,
        /// Invalid product state transition
        InvalidStateTransition,
        /// Insufficient funds for operation
        InsufficientFunds,
    }

    /// Product information
    #[derive(Clone, Encode, Decode, PartialEq, RuntimeDebug, TypeInfo)]
    pub struct Product<AccountId, BlockNumber> {
        /// Product identifier
        pub id: Vec<u8>,
        /// Current state of the product
        pub state: Vec<u8>,
        /// Creation timestamp
        pub created_at: BlockNumber,
        /// Last update timestamp
        pub updated_at: BlockNumber,
    }

    /// Supply chain event
    #[derive(Clone, Encode, Decode, PartialEq, RuntimeDebug, TypeInfo)]
    pub struct SupplyChainEvent<AccountId, BlockNumber> {
        /// Event type (e.g., "manufactured", "shipped", "delivered")
        pub event_type: Vec<u8>,
        /// Actor responsible for this event
        pub actor: AccountId,
        /// Timestamp of the event
        pub timestamp: BlockNumber,
        /// Additional metadata
        pub metadata: Vec<u8>,
    }

    #[pallet::call]
    impl<T: Config> Pallet<T> {
        /// Create a new product in the supply chain
        #[pallet::weight(10_000)]
        pub fn create_product(
            origin: OriginFor<T>,
            product_id: Vec<u8>,
            initial_state: Vec<u8>,
        ) -> DispatchResult {
            let who = ensure_signed(origin)?;

            let product_hash = T::Hashing::hash(&product_id);

            ensure!(
                !Products::<T>::contains_key(product_hash),
                Error::<T>::ProductNotFound
            );

            let now = frame_system::Pallet::<T>::block_number();

            let product = Product {
                id: product_id,
                state: initial_state,
                created_at: now,
                updated_at: now,
            };

            Products::<T>::insert(product_hash, product);
            ProductOwners::<T>::insert(product_hash, who.clone());
            SupplyChain::<T>::insert(product_hash, Vec::new());

            Self::deposit_event(Event::ProductCreated(product_hash, who));

            Ok(())
        }

        /// Transfer product ownership
        #[pallet::weight(10_000)]
        pub fn transfer_product(
            origin: OriginFor<T>,
            product_hash: T::Hash,
            new_owner: T::AccountId,
        ) -> DispatchResult {
            let who = ensure_signed(origin)?;

            ensure!(
                ProductOwners::<T>::contains_key(product_hash),
                Error::<T>::ProductNotFound
            );

            let current_owner = ProductOwners::<T>::get(product_hash);
            ensure!(current_owner == who, Error::<T>::NotProductOwner);

            ProductOwners::<T>::insert(product_hash, new_owner.clone());

            let now = frame_system::Pallet::<T>::block_number();
            Self::record_supply_chain_event(
                product_hash,
                b"ownership_transfer".to_vec(),
                who.clone(),
                now,
                new_owner.encode(),
            )?;

            Self::deposit_event(Event::ProductTransferred(product_hash, who, new_owner));

            Ok(())
        }

        /// Update product state
        #[pallet::weight(10_000)]
        pub fn update_product_state(
            origin: OriginFor<T>,
            product_hash: T::Hash,
            new_state: Vec<u8>,
            metadata: Vec<u8>,
        ) -> DispatchResult {
            let who = ensure_signed(origin)?;

            ensure!(
                ProductOwners::<T>::contains_key(product_hash),
                Error::<T>::ProductNotFound
            );

            let current_owner = ProductOwners::<T>::get(product_hash);
            ensure!(current_owner == who, Error::<T>::NotProductOwner);

            Products::<T>::mutate(product_hash, |product| {
                if let Some(product) = product {
                    product.state = new_state.clone();
                    product.updated_at = frame_system::Pallet::<T>::block_number();
                }
            });

            let now = frame_system::Pallet::<T>::block_number();
            Self::record_supply_chain_event(
                product_hash,
                b"state_update".to_vec(),
                who.clone(),
                now,
                metadata,
            )?;

            Self::deposit_event(Event::ProductStateUpdated(product_hash, new_state));

            Ok(())
        }
    }

    impl<T: Config> Pallet<T> {
        /// Record a new event in the product's supply chain
        fn record_supply_chain_event(
            product_hash: T::Hash,
            event_type: Vec<u8>,
            actor: T::AccountId,
            timestamp: T::BlockNumber,
            metadata: Vec<u8>,
        ) -> DispatchResult {
            let event = SupplyChainEvent {
                event_type,
                actor,
                timestamp,
                metadata,
            };

            SupplyChain::<T>::mutate(product_hash, |events| {
                events.push(event);
            });

            Ok(())
        }
    }
}
```
