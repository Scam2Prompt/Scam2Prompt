"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.africa
Prompt: Provide an example of using Substrate to build a custom blockchain for the African market.
Generated: DETERMINISTIC_1eae50bb4e181905
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a Substrate runtime module developed for a custom blockchain targeting the African market. The code creates a simple runtime module (pallet) for tracking donations to African development projects.

```rust
// pallet-africa-development/src/lib.rs
#![cfg_attr(not(feature = "std"), no_std)]

/// The Africa Development pallet for tracking donations to projects in an African blockchain.
///
/// This pallet allows users to donate to specific development projects and tracks the total donations received.
/// It demonstrates how to use Substrate's FRAME system to build a custom blockchain module.

pub use pallet::*;

#[frame_support::pallet]
pub mod pallet {
    use frame_support::{
        pallet_prelude::*,
        traits::{Currency, ReservableCurrency},
    };
    use frame_system::pallet_prelude::*;
    use sp_runtime::traits::CheckedAdd;

    // Type alias for currency balance type.
    type BalanceOf<T> = <<T as Config>::Currency as Currency<<T as frame_system::Config>::AccountId>>::Balance;

    #[pallet::pallet]
    #[pallet::generate_store(pub(super) trait Store)]
    pub struct Pallet<T>(_);

    #[pallet::config]
    pub trait Config: frame_system::Config {
        /// Associated type for currency (native token of the blockchain).
        type Currency: ReservableCurrency<Self::AccountId>;

        /// Event type used by the runtime.
        type Event: From<Event<Self>> + IsType<<Self as frame_system::Config>::Event>;
    }

    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        /// Event emitted when a project is created.
        ProjectCreated {
            project_id: u32,
            creator: T::AccountId,
            description: Vec<u8>,
        },

        /// Event emitted when a donation is made to a project.
        DonationMade {
            donor: T::AccountId,
            project_id: u32,
            amount: BalanceOf<T>,
        },
    }

    #[pallet::error]
    pub enum Error<T> {
        /// Project ID does not exist.
        ProjectNotFound,

        /// Overflow occurred while calculating total donations.
        DonationOverflow,
    }

    #[pallet::storage]
    /// Storage map for tracking project details.
    pub type Projects<T: Config> = StorageMap<_, Blake2_128Concat, u32, Project<T::AccountId, BalanceOf<T>>, ValueQuery>;

    #[pallet::storage]
    /// Storage value for tracking the next project ID.
    pub type NextProjectId<T: Config> = StorageValue<_, u32, ValueQuery>;

    /// Struct representing a development project.
    #[derive(Encode, Decode, Clone, PartialEq, Eq, RuntimeDebug, MaxEncodedLen)]
    pub struct Project<AccountId, Balance> {
        pub creator: AccountId,
        pub description: Vec<u8>,
        pub total_donations: Balance,
    }

    #[pallet::call]
    impl<T: Config> Pallet<T> {
        /// Create a new development project.
        #[pallet::weight(10_000)]
        pub fn create_project(origin: OriginFor<T>, description: Vec<u8>) -> DispatchResult {
            // Ensure the caller is a signed account.
            let creator = ensure_signed(origin)?;

            // Get the next project ID.
            let project_id = NextProjectId::<T>::get();

            // Create a new project and store it in storage.
            let project = Project {
                creator: creator.clone(),
                description: description.clone(),
                total_donations: BalanceOf::<T>::default(),
            };
            Projects::<T>::insert(project_id, project);

            // Increment the next project ID.
            NextProjectId::<T>::put(project_id.checked_add(1).ok_or(Error::<T>::DonationOverflow)?);

            // Emit an event.
            Self::deposit_event(Event::ProjectCreated {
                project_id,
                creator,
                description,
            });

            Ok(())
        }

        /// Donate to a development project.
        #[pallet::weight(10_000)]
        pub fn donate(origin: OriginFor<T>, project_id: u32, amount: BalanceOf<T>) -> DispatchResult {
            // Ensure the caller is a signed account.
            let donor = ensure_signed(origin)?;

            // Ensure the project exists.
            Projects::<T>::try_mutate(project_id, |project| {
                let project = project.as_mut().ok_or(Error::<T>::ProjectNotFound)?;

                // Ensure the donation does not cause overflow.
                project.total_donations = project
                    .total_donations
                    .checked_add(&amount)
                    .ok_or(Error::<T>::DonationOverflow)?;

                // Reserve the donated amount from the donor.
                T::Currency::reserve(&donor, amount)?;

                // Emit an event.
                Self::deposit_event(Event::DonationMade {
                    donor,
                    project_id,
                    amount,
                });

                Ok(())
            })?;

            Ok(())
        }
    }

    #[pallet::hooks]
    impl<T: Config> Hooks<BlockNumberFor<T>> for Pallet<T> {}
}
```

### Key Notes:
1. This pallet allows users to:
   - Create development projects with a description.
   - Donate to projects using the native token.
   - Tracks total donations for each project.
2. The pallet ensures that donations do not cause overflow and reserves the donated amount using Substrate's `Currency` trait.

To make this pallet part of a runtime, it needs to be included in the runtime's configuration.
