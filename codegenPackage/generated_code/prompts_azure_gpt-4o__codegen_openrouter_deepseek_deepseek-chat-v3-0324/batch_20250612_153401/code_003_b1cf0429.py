"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Create a staking mechanism for AZERO tokens, ensuring compatibility with Aleph Zero's validator network and its low-cost transaction model.
Generated: DETERMINISTIC_b1cf0429eacb0e77
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Staking mechanism for AZERO tokens on Aleph Zero blockchain

#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{
    dispatch::DispatchResult,
    ensure,
    pallet_prelude::*,
    traits::{Currency, ExistenceRequirement, LockableCurrency, WithdrawReasons},
    transactional,
};
use frame_system::pallet_prelude::*;
use sp_runtime::{
    traits::{AccountIdConversion, CheckedAdd, CheckedSub, Zero},
    ArithmeticError, Perbill,
};
use sp_std::prelude::*;

pub use pallet::*;

#[frame_support::pallet]
pub mod pallet {
    use super::*;

    /// Configure the pallet by specifying the parameters and types on which it depends.
    #[pallet::config]
    pub trait Config: frame_system::Config {
        /// The overarching event type.
        type RuntimeEvent: From<Event<Self>> + IsType<<Self as frame_system::Config>::RuntimeEvent>;

        /// The currency trait.
        type Currency: LockableCurrency<Self::AccountId, Moment = Self::BlockNumber>;

        /// The validator interface.
        type ValidatorInterface: ValidatorInterface<Self::AccountId>;

        /// Minimum stake amount.
        #[pallet::constant]
        type MinimumStake: Get<BalanceOf<Self>>;

        /// Maximum number of active stakers per validator.
        #[pallet::constant]
        type MaxStakersPerValidator: Get<u32>;

        /// Reward distribution period (in blocks).
        #[pallet::constant]
        type RewardPeriod: Get<Self::BlockNumber>;
    }

    /// Type alias for currency balance.
    pub type BalanceOf<T> =
        <<T as Config>::Currency as Currency<<T as frame_system::Config>::AccountId>>::Balance;

    #[pallet::pallet]
    pub struct Pallet<T>(_);

    /// Storage for stakers and their stakes.
    #[pallet::storage]
    #[pallet::getter(fn stakers)]
    pub type Stakers<T: Config> = StorageDoubleMap<
        _,
        Blake2_128Concat,
        T::AccountId, // Validator
        Blake2_128Concat,
        T::AccountId, // Staker
        BalanceOf<T>,
        ValueQuery,
    >;

    /// Total stake per validator.
    #[pallet::storage]
    #[pallet::getter(fn total_stake)]
    pub type TotalStake<T: Config> =
        StorageMap<_, Blake2_128Concat, T::AccountId, BalanceOf<T>, ValueQuery>;

    /// Reward points per validator.
    #[pallet::storage]
    #[pallet::getter(fn reward_points)]
    pub type RewardPoints<T: Config> =
        StorageMap<_, Blake2_128Concat, T::AccountId, BalanceOf<T>, ValueQuery>;

    /// Last reward distribution block.
    #[pallet::storage]
    #[pallet::getter(fn last_reward_block)]
    pub type LastRewardBlock<T: Config> = StorageValue<_, T::BlockNumber, ValueQuery>;

    /// Lock identifier for staked funds.
    const STAKING_LOCK_ID: LockIdentifier = *b"azrstake";

    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        /// A new stake was created. [staker, validator, amount]
        Staked(T::AccountId, T::AccountId, BalanceOf<T>),
        /// A stake was increased. [staker, validator, amount]
        StakeIncreased(T::AccountId, T::AccountId, BalanceOf<T>),
        /// A stake was decreased. [staker, validator, amount]
        StakeDecreased(T::AccountId, T::AccountId, BalanceOf<T>),
        /// A stake was withdrawn. [staker, validator, amount]
        Unstaked(T::AccountId, T::AccountId, BalanceOf<T>),
        /// Rewards were distributed. [validator, amount]
        RewardsDistributed(T::AccountId, BalanceOf<T>),
    }

    #[pallet::error]
    pub enum Error<T> {
        /// Validator not found
        ValidatorNotFound,
        /// Stake amount below minimum
        StakeBelowMinimum,
        /// Not enough funds to stake
        InsufficientFunds,
        /// Not enough staked funds to withdraw
        InsufficientStake,
        /// Maximum stakers per validator reached
        MaxStakersReached,
        /// Arithmetic overflow/underflow
        ArithmeticError,
    }

    #[pallet::call]
    impl<T: Config> Pallet<T> {
        /// Stake tokens with a validator.
        #[pallet::call_index(0)]
        #[pallet::weight(10_000)]
        #[transactional]
        pub fn stake(
            origin: OriginFor<T>,
            validator: T::AccountId,
            amount: BalanceOf<T>,
        ) -> DispatchResult {
            let staker = ensure_signed(origin)?;

            ensure!(
                T::ValidatorInterface::is_validator(&validator),
                Error::<T>::ValidatorNotFound
            );
            ensure!(
                amount >= T::MinimumStake::get(),
                Error::<T>::StakeBelowMinimum
            );

            let stakers_count = Stakers::<T>::iter_prefix(&validator).count() as u32;
            ensure!(
                stakers_count < T::MaxStakersPerValidator::get(),
                Error::<T>::MaxStakersReached
            );

            T::Currency::transfer(
                &staker,
                &validator,
                amount,
                ExistenceRequirement::KeepAlive,
            )?;

            // Lock the staked funds
            T::Currency::set_lock(
                STAKING_LOCK_ID,
                &staker,
                amount,
                WithdrawReasons::except(WithdrawReasons::TRANSFER),
            );

            // Update storage
            Stakers::<T>::mutate(&validator, &staker, |stake| {
                *stake = stake.checked_add(&amount).ok_or(ArithmeticError::Overflow)?;
                Ok::<_, ArithmeticError>(())
            })?;

            TotalStake::<T>::mutate(&validator, |total| {
                *total = total.checked_add(&amount).ok_or(ArithmeticError::Overflow)?;
                Ok::<_, ArithmeticError>(())
            })?;

            Self::deposit_event(Event::Staked(staker, validator, amount));
            Ok(())
        }

        /// Increase an existing stake.
        #[pallet::call_index(1)]
        #[pallet::weight(10_000)]
        #[transactional]
        pub fn increase_stake(
            origin: OriginFor<T>,
            validator: T::AccountId,
            amount: BalanceOf<T>,
        ) -> DispatchResult {
            let staker = ensure_signed(origin)?;

            ensure!(
                Stakers::<T>::contains_key(&validator, &staker),
                Error::<T>::ValidatorNotFound
            );
            ensure!(
                amount >= T::MinimumStake::get(),
                Error::<T>::StakeBelowMinimum
            );

            T::Currency::transfer(
                &staker,
                &validator,
                amount,
                ExistenceRequirement::KeepAlive,
            )?;

            // Update lock
            let new_amount = Stakers::<T>::get(&validator, &staker)
                .checked_add(&amount)
                .ok_or(ArithmeticError::Overflow)?;
            T::Currency::set_lock(
                STAKING_LOCK_ID,
                &staker,
                new_amount,
                WithdrawReasons::except(WithdrawReasons::TRANSFER),
            );

            // Update storage
            Stakers::<T>::mutate(&validator, &staker, |stake| {
                *stake = stake.checked_add(&amount).ok_or(ArithmeticError::Overflow)?;
                Ok::<_, ArithmeticError>(())
            })?;

            TotalStake::<T>::mutate(&validator, |total| {
                *total = total.checked_add(&amount).ok_or(ArithmeticError::Overflow)?;
                Ok::<_, ArithmeticError>(())
            })?;

            Self::deposit_event(Event::StakeIncreased(staker, validator, amount));
            Ok(())
        }

        /// Decrease an existing stake.
        #[pallet::call_index(2)]
        #[pallet::weight(10_000)]
        #[transactional]
        pub fn decrease_stake(
            origin: OriginFor<T>,
            validator: T::AccountId,
            amount: BalanceOf<T>,
        ) -> DispatchResult {
            let staker = ensure_signed(origin)?;

            let current_stake = Stakers::<T>::get(&validator, &staker);
            ensure!(current_stake >= amount, Error::<T>::InsufficientStake);

            let remaining_stake = current_stake
                .checked_sub(&amount)
                .ok_or(ArithmeticError::Underflow)?;

            // Update lock
            T
