"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Provide an example of a decentralized finance (DeFi) application that can be built on Polkadot, detailing the use of parachains and shared security.
Generated: DETERMINISTIC_dc4e75ec0fb4ecec
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! A simple decentralized finance (DeFi) application built on Polkadot using Substrate.
//! This example demonstrates a basic lending protocol leveraging Polkadot's parachains and shared security.

#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{
    decl_error, decl_event, decl_module, decl_storage,
    dispatch::DispatchResult,
    ensure,
    traits::{Currency, ExistenceRequirement, Get, ReservableCurrency},
    weights::Weight,
};
use frame_system::{self as system, ensure_signed};
use sp_runtime::{
    traits::{AccountIdConversion, CheckedAdd, CheckedSub, Zero},
    ArithmeticError, DispatchError,
};
use sp_std::prelude::*;

// Re-export pallet items for runtime
pub use pallet::*;

#[frame_support::pallet]
pub mod pallet {
    use super::*;

    /// Configure the pallet by specifying the parameters and types on which it depends.
    #[pallet::config]
    pub trait Config: frame_system::Config {
        /// The overarching event type.
        type Event: From<Event<Self>> + IsType<<Self as frame_system::Config>::Event>;

        /// The currency trait for handling deposits and withdrawals.
        type Currency: Currency<Self::AccountId> + ReservableCurrency<Self::AccountId>;

        /// The parachain ID for cross-chain messaging.
        #[pallet::constant]
        type ParachainId: Get<u32>;

        /// The minimum deposit required to create a loan.
        #[pallet::constant]
        type MinimumDeposit: Get<BalanceOf<Self>>;
    }

    #[pallet::pallet]
    #[pallet::generate_store(pub(super) trait Store)]
    pub struct Pallet<T>(_);

    // Type aliases for cleaner code
    type BalanceOf<T> =
        <<T as Config>::Currency as Currency<<T as frame_system::Config>::AccountId>>::Balance;
    type AccountIdOf<T> = <T as frame_system::Config>::AccountId;

    /// Storage for the total amount deposited by users.
    #[pallet::storage]
    #[pallet::getter(fn total_deposits)]
    pub type TotalDeposits<T: Config> = StorageValue<_, BalanceOf<T>, ValueQuery>;

    /// Storage for individual user deposits.
    #[pallet::storage]
    #[pallet::getter(fn user_deposits)]
    pub type UserDeposits<T: Config> =
        StorageMap<_, Blake2_128Concat, AccountIdOf<T>, BalanceOf<T>, ValueQuery>;

    /// Storage for loans created by users.
    #[pallet::storage]
    #[pallet::getter(fn loans)]
    pub type Loans<T: Config> = StorageMap<
        _,
        Blake2_128Concat,
        AccountIdOf<T>,
        (BalanceOf<T>, BalanceOf<T>), // (principal, interest)
        OptionQuery,
    >;

    /// Events emitted by the pallet.
    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        /// A user has deposited funds.
        Deposited(AccountIdOf<T>, BalanceOf<T>),
        /// A user has withdrawn funds.
        Withdrawn(AccountIdOf<T>, BalanceOf<T>),
        /// A loan has been created.
        LoanCreated(AccountIdOf<T>, BalanceOf<T>, BalanceOf<T>),
        /// A loan has been repaid.
        LoanRepaid(AccountIdOf<T>, BalanceOf<T>, BalanceOf<T>),
    }

    /// Errors that can occur in the pallet.
    #[pallet::error]
    pub enum Error<T> {
        /// Deposit amount is below the minimum.
        DepositTooSmall,
        /// Insufficient funds for withdrawal.
        InsufficientFunds,
        /// User already has an active loan.
        LoanAlreadyExists,
        /// No active loan found for user.
        NoLoanExists,
        /// Arithmetic overflow occurred.
        ArithmeticOverflow,
    }

    #[pallet::hooks]
    impl<T: Config> Hooks<BlockNumberFor<T>> for Pallet<T> {}

    #[pallet::call]
    impl<T: Config> Pallet<T> {
        /// Deposit funds into the protocol.
        #[pallet::weight(10_000)]
        pub fn deposit(
            origin: OriginFor<T>,
            amount: BalanceOf<T>,
        ) -> DispatchResultWithPostInfo {
            let who = ensure_signed(origin)?;

            ensure!(
                amount >= T::MinimumDeposit::get(),
                Error::<T>::DepositTooSmall
            );

            // Transfer funds from user to protocol
            T::Currency::transfer(&who, &Self::account_id(), amount, ExistenceRequirement::KeepAlive)?;

            // Update storage
            UserDeposits::<T>::mutate(&who, |balance| *balance += amount);
            TotalDeposits::<T>::mutate(|total| *total += amount);

            Self::deposit_event(Event::Deposited(who, amount));
            Ok(().into())
        }

        /// Withdraw funds from the protocol.
        #[pallet::weight(10_000)]
        pub fn withdraw(
            origin: OriginFor<T>,
            amount: BalanceOf<T>,
        ) -> DispatchResultWithPostInfo {
            let who = ensure_signed(origin)?;

            let user_balance = UserDeposits::<T>::get(&who);
            ensure!(user_balance >= amount, Error::<T>::InsufficientFunds);

            // Update storage before transfer to prevent re-entrancy
            UserDeposits::<T>::mutate(&who, |balance| *balance -= amount);
            TotalDeposits::<T>::mutate(|total| *total -= amount);

            // Transfer funds back to user
            T::Currency::transfer(&Self::account_id(), &who, amount, ExistenceRequirement::AllowDeath)?;

            Self::deposit_event(Event::Withdrawn(who, amount));
            Ok(().into())
        }

        /// Create a new loan.
        #[pallet::weight(10_000)]
        pub fn create_loan(
            origin: OriginFor<T>,
            principal: BalanceOf<T>,
            interest: BalanceOf<T>,
        ) -> DispatchResultWithPostInfo {
            let who = ensure_signed(origin)?;

            ensure!(!Loans::<T>::contains_key(&who), Error::<T>::LoanAlreadyExists);

            let total_deposits = TotalDeposits::<T>::get();
            ensure!(principal <= total_deposits, Error::<T>::InsufficientFunds);

            // Store the loan
            Loans::<T>::insert(&who, (principal, interest));

            Self::deposit_event(Event::LoanCreated(who, principal, interest));
            Ok(().into())
        }

        /// Repay an existing loan.
        #[pallet::weight(10_000)]
        pub fn repay_loan(
            origin: OriginFor<T>,
            amount: BalanceOf<T>,
        ) -> DispatchResultWithPostInfo {
            let who = ensure_signed(origin)?;

            let (principal, interest) = Loans::<T>::get(&who).ok_or(Error::<T>::NoLoanExists)?;
            let total_repayment = principal.checked_add(&interest).ok_or(Error::<T>::ArithmeticOverflow)?;

            ensure!(amount >= total_repayment, Error::<T>::InsufficientFunds);

            // Transfer repayment from user to protocol
            T::Currency::transfer(&who, &Self::account_id(), amount, ExistenceRequirement::KeepAlive)?;

            // Remove the loan
            Loans::<T>::remove(&who);

            Self::deposit_event(Event::LoanRepaid(who, principal, interest));
            Ok(().into())
        }
    }

    impl<T: Config> Pallet<T> {
        /// The account ID of the protocol's treasury.
        pub fn account_id() -> T::AccountId {
            T::ParachainId::get().into_account()
        }
    }
}

// Cross-chain messaging would be implemented using XCMP (Cross-Chain Message Passing)
// This would allow interaction with other parachains in the Polkadot ecosystem
// Note: Actual XCMP implementation would require additional configuration and runtime setup
```
