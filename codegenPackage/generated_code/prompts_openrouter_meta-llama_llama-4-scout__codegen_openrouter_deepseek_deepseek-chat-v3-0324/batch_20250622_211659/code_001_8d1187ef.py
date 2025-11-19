"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: What are the benefits of Common Good Parachains in the Polkadot ecosystem, and how can they be used for governance-allocated parachains?
Generated: DETERMINISTIC_8d1187ef055fce6f
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// This code demonstrates the concept of Common Good Parachains in Polkadot
// and how they can be used for governance-allocated parachains.

use sp_runtime::traits::{IdentifyAccount, Verify};
use sp_runtime::MultiSignature;
use frame_support::{
    dispatch::DispatchResult,
    traits::{Currency, Get},
    Parameter,
};
use frame_system::Config as SystemConfig;
use parity_scale_codec::{Decode, Encode};
use scale_info::TypeInfo;
use sp_std::prelude::*;

/// Common Good Parachain configuration trait
pub trait Config: SystemConfig {
    /// The currency type for staking
    type Currency: Currency<Self::AccountId>;
    /// The runtime event type
    type Event: From<Event<Self>> + Into<<Self as SystemConfig>::Event>;
    /// Minimum stake required to propose a common good parachain
    type MinimumStake: Get<BalanceOf<Self>>;
}

/// Balance type alias
type BalanceOf<T> = <<T as Config>::Currency as Currency<<T as SystemConfig>::AccountId>>::Balance;

/// Parachain identifier
#[derive(Encode, Decode, Clone, PartialEq, Eq, Debug, TypeInfo)]
pub struct ParaId(pub u32);

/// Common Good Parachain proposal
#[derive(Encode, Decode, Clone, PartialEq, Eq, Debug, TypeInfo)]
pub struct Proposal<AccountId, Balance> {
    /// The account proposing the parachain
    proposer: AccountId,
    /// The parachain ID being proposed
    para_id: ParaId,
    /// Stake amount locked for this proposal
    stake: Balance,
    /// Description of the common good purpose
    description: Vec<u8>,
}

/// Storage for active Common Good Parachain proposals
#[frame_support::pallet]
pub mod pallet {
    use super::*;
    use frame_support::pallet_prelude::*;
    use frame_system::pallet_prelude::*;

    #[pallet::config]
    pub trait Config: frame_system::Config {
        type Event: From<Event<Self>> + IsType<<Self as frame_system::Config>::Event>;
        type Currency: Currency<Self::AccountId>;
        type MinimumStake: Get<BalanceOf<Self>>;
    }

    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        /// A new Common Good Parachain has been proposed
        Proposed(ParaId, T::AccountId),
        /// A Common Good Parachain has been approved
        Approved(ParaId),
        /// A Common Good Parachain has been rejected
        Rejected(ParaId),
    }

    #[pallet::error]
    pub enum Error<T> {
        /// Proposal already exists for this parachain ID
        ProposalExists,
        /// Insufficient stake for proposal
        InsufficientStake,
        /// Proposal doesn't exist
        ProposalNotFound,
    }

    #[pallet::storage]
    #[pallet::getter(fn proposals)]
    pub type Proposals<T: Config> = StorageMap<
        _,
        Blake2_128Concat,
        ParaId,
        Proposal<T::AccountId, BalanceOf<T>>,
        OptionQuery,
    >;

    #[pallet::pallet]
    pub struct Pallet<T>(_);

    #[pallet::call]
    impl<T: Config> Pallet<T> {
        /// Propose a new Common Good Parachain
        #[pallet::weight(10_000)]
        pub fn propose(
            origin: OriginFor<T>,
            para_id: ParaId,
            description: Vec<u8>,
        ) -> DispatchResult {
            let proposer = ensure_signed(origin)?;

            // Ensure proposal doesn't already exist
            ensure!(!Proposals::<T>::contains_key(&para_id), Error::<T>::ProposalExists);

            // Lock stake
            let stake = T::MinimumStake::get();
            T::Currency::reserve(&proposer, stake)?;

            // Create and store proposal
            let proposal = Proposal {
                proposer: proposer.clone(),
                para_id,
                stake,
                description,
            };
            Proposals::<T>::insert(&para_id, proposal);

            Self::deposit_event(Event::Proposed(para_id, proposer));
            Ok(())
        }

        /// Approve a Common Good Parachain (governance function)
        #[pallet::weight(10_000)]
        pub fn approve(origin: OriginFor<T>, para_id: ParaId) -> DispatchResult {
            // In production, this would be restricted to governance (e.g., council or referendum)
            ensure_root(origin)?;

            // Get and remove proposal
            let proposal = Proposals::<T>::take(&para_id)
                .ok_or(Error::<T>::ProposalNotFound)?;

            // Unreserve stake (in production, might be held until parachain is onboarded)
            T::Currency::unreserve(&proposal.proposer, proposal.stake);

            Self::deposit_event(Event::Approved(para_id));
            Ok(())
        }

        /// Reject a Common Good Parachain (governance function)
        #[pallet::weight(10_000)]
        pub fn reject(origin: OriginFor<T>, para_id: ParaId) -> DispatchResult {
            // In production, this would be restricted to governance
            ensure_root(origin)?;

            // Get and remove proposal
            let proposal = Proposals::<T>::take(&para_id)
                .ok_or(Error::<T>::ProposalNotFound)?;

            // Slash or unreserve stake based on governance decision
            T::Currency::unreserve(&proposal.proposer, proposal.stake);

            Self::deposit_event(Event::Rejected(para_id));
            Ok(())
        }
    }
}

// Example of integrating with Polkadot's governance system
mod governance_integration {
    use super::*;
    use frame_support::traits::OriginTrait;

    /// A function that could be called by Polkadot's governance system
    /// to allocate a Common Good Parachain slot
    pub fn allocate_common_good_parachain<T: Config>(
        origin: T::Origin,
        para_id: ParaId,
    ) -> DispatchResult {
        // Verify the origin is from governance
        // (implementation depends on your governance system)
        ensure_root(origin)?;

        // Call the approve function
        pallet::Pallet::<T>::approve(
            frame_system::RawOrigin::Root.into(),
            para_id,
        )
    }
}
```
