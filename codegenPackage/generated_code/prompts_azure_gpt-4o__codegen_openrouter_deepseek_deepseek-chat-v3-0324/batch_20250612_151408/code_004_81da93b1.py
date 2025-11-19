"""
Generated Code Metadata:
========================
Original URL: https://polkadot.africa
Prompt: Write a smart contract compatible with the Polkadot ecosystem to facilitate microtransactions for African businesses.
Generated: DETERMINISTIC_81da93b1686698ae
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{
    dispatch::DispatchResult,
    ensure,
    pallet_prelude::*,
    traits::{Currency, ExistenceRequirement, WithdrawReasons},
    transactional,
};
use frame_system::pallet_prelude::*;
use sp_runtime::{
    traits::{AccountIdConversion, CheckedAdd, CheckedSub, Saturating, Zero},
    ArithmeticError, DispatchError,
};
use sp_std::prelude::*;

pub use pallet::*;

#[frame_support::pallet]
pub mod pallet {
    use super::*;

    #[pallet::config]
    pub trait Config: frame_system::Config {
        /// The overarching event type.
        type RuntimeEvent: From<Event<Self>> + IsType<<Self as frame_system::Config>::RuntimeEvent>;

        /// The currency type for handling microtransactions.
        type Currency: Currency<Self::AccountId>;

        /// The minimum amount that can be sent in a microtransaction.
        #[pallet::constant]
        type MinMicroTxAmount: Get<BalanceOf<Self>>;

        /// The maximum amount that can be sent in a microtransaction.
        #[pallet::constant]
        type MaxMicroTxAmount: Get<BalanceOf<Self>>;
    }

    #[pallet::pallet]
    pub struct Pallet<T>(_);

    pub type BalanceOf<T> =
        <<T as Config>::Currency as Currency<<T as frame_system::Config>::AccountId>>::Balance;

    #[pallet::storage]
    #[pallet::getter(fn transaction_count)]
    pub type TransactionCount<T: Config> = StorageValue<_, u64, ValueQuery>;

    #[pallet::storage]
    #[pallet::getter(fn transactions)]
    pub type Transactions<T: Config> = StorageMap<
        _,
        Blake2_128Concat,
        u64,
        Transaction<T::AccountId, BalanceOf<T>>,
        OptionQuery,
    >;

    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        /// A microtransaction was sent
        MicroTransactionSent {
            from: T::AccountId,
            to: T::AccountId,
            amount: BalanceOf<T>,
            tx_id: u64,
        },
        /// A microtransaction was received
        MicroTransactionReceived {
            to: T::AccountId,
            from: T::AccountId,
            amount: BalanceOf<T>,
            tx_id: u64,
        },
        /// A microtransaction failed
        MicroTransactionFailed {
            from: T::AccountId,
            to: T::AccountId,
            amount: BalanceOf<T>,
            reason: DispatchError,
        },
    }

    #[pallet::error]
    pub enum Error<T> {
        /// Amount is below minimum microtransaction threshold
        AmountTooSmall,
        /// Amount exceeds maximum microtransaction threshold
        AmountTooLarge,
        /// Sender has insufficient funds
        InsufficientBalance,
        /// Arithmetic overflow occurred
        ArithmeticOverflow,
    }

    #[derive(Clone, Encode, Decode, PartialEq, RuntimeDebug, TypeInfo)]
    pub struct Transaction<AccountId, Balance> {
        pub from: AccountId,
        pub to: AccountId,
        pub amount: Balance,
        pub timestamp: T::BlockNumber,
    }

    #[pallet::call]
    impl<T: Config> Pallet<T> {
        /// Send a microtransaction to another account
        #[pallet::weight(10_000)]
        #[transactional]
        pub fn send_microtransaction(
            origin: OriginFor<T>,
            to: T::AccountId,
            amount: BalanceOf<T>,
        ) -> DispatchResult {
            let from = ensure_signed(origin)?;

            ensure!(
                amount >= T::MinMicroTxAmount::get(),
                Error::<T>::AmountTooSmall
            );
            ensure!(
                amount <= T::MaxMicroTxAmount::get(),
                Error::<T>::AmountTooLarge
            );

            let new_balance = T::Currency::free_balance(&from)
                .checked_sub(&amount)
                .ok_or(Error::<T>::InsufficientBalance)?;

            T::Currency::ensure_can_withdraw(
                &from,
                amount,
                WithdrawReasons::TRANSFER,
                new_balance,
            )?;

            T::Currency::transfer(
                &from,
                &to,
                amount,
                ExistenceRequirement::KeepAlive,
            )?;

            let tx_id = TransactionCount::<T>::get();
            let transaction = Transaction {
                from: from.clone(),
                to: to.clone(),
                amount,
                timestamp: frame_system::Pallet::<T>::block_number(),
            };

            Transactions::<T>::insert(tx_id, transaction);
            TransactionCount::<T>::put(tx_id.saturating_add(1));

            Self::deposit_event(Event::MicroTransactionSent {
                from,
                to: to.clone(),
                amount,
                tx_id,
            });

            Self::deposit_event(Event::MicroTransactionReceived {
                to,
                from,
                amount,
                tx_id,
            });

            Ok(())
        }
    }

    impl<T: Config> Pallet<T> {
        /// Helper function to get the current balance of an account
        pub fn get_balance(account: &T::AccountId) -> BalanceOf<T> {
            T::Currency::free_balance(account)
        }
    }
}
```
