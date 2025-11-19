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

```rust
// This is an example of a simple Substrate-based blockchain for the African market.
// It includes basic functionality, runtime configuration, and error handling.

#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{decl_module, decl_storage, decl_event, ensure};
use frame_system::ensure_signed;
use sp_runtime::traits::Hash;
use sp_std::prelude::*;

// Defining the module's configuration trait.
pub trait Config: frame_system::Config {
    type Event: From<Event<Self>> + Into<<Self as frame_system::Config>::Event>;
}

// Declaring the storage items.
decl_storage! {
    trait Store for Module<T: Config> as ExampleStorage {
        // Store a mapping between user accounts and their balances.
        Balances get(fn balances): map hasher(blake2_128_concat) T::AccountId => u64;
    }
}

// Declaring the events.
decl_event! {
    pub enum Event<T> where AccountId = <T as frame_system::Config>::AccountId {
        // Event for successful fund transfer.
        FundsTransferred(AccountId, AccountId, u64),
    }
}

// Declaring the module.
decl_module! {
    pub struct Module<T: Config> for enum Call where origin: T::Origin {
        // This function is called when the module is being initialized.
        fn deposit_event() = default;

        // Function for transferring funds between accounts.
        #[weight = 10_000]
        fn transfer(origin, to: T::AccountId, amount: u64) -> dispatch::DispatchResult {
            // Ensure the caller is a signed user.
            let sender = ensure_signed(origin)?;

            // Ensure the sender has enough balance.
            let sender_balance = Self::balances(&sender);
            ensure!(sender_balance >= amount, "Insufficient balance");

            // Perform the transfer.
            <Balances<T>>::insert(&sender, sender_balance - amount);
            let recipient_balance = Self::balances(&to);
            <Balances<T>>::insert(&to, recipient_balance + amount);
            
            // Emit an event for the transfer.
            Self::deposit_event(RawEvent::FundsTransferred(sender, to, amount));
            Ok(())
        }

        // Initialize the balance for a user.
        #[weight = 10_000]
        fn initialize_balance(origin, amount: u64) -> dispatch::DispatchResult {
            let sender = ensure_signed(origin)?;

            // Ensure that the sender's balance is uninitialized (zero).
            ensure!(Self::balances(&sender) == 0, "Balance already initialized");

            // Set the initial balance.
            <Balances<T>>::insert(&sender, amount);
            Ok(())
        }
    }
}

// Unit tests for the module.
#[cfg(test)]
mod tests {
    use super::*;
    use frame_support::{assert_ok, assert_noop};

    #[test]
    fn test_initialize_balance() {
        // Mock initialization and assert balance.
        let account: u64 = 1;
        let initial_balance = 100;

        assert_ok!(Module::<Test>::initialize_balance(Origin::signed(account), initial_balance));
        assert_eq!(Balances::<Test>::get(account), initial_balance);
    }

    #[test]
    fn test_transfer_funds() {
        // Mock initialization of balances for two different accounts.
        let sender: u64 = 1;
        let receiver: u64 = 2;
        let amount = 50;
        
        Module::<Test>::initialize_balance(Origin::signed(sender), 100).unwrap();
        Module::<Test>::initialize_balance(Origin::signed(receiver), 0).unwrap();

        // Transfer funds and assert balances.
        assert_ok!(Module::<Test>::transfer(Origin::signed(sender), receiver, amount));
        assert_eq!(Balances::<Test>::get(sender), 50);
        assert_eq!(Balances::<Test>::get(receiver), amount);
    }

    #[test]
    fn test_transfer_insufficient_balance() {
        // Attempt to transfer more than available balance.
        let sender: u64 = 1;
        let receiver: u64 = 2;
        
        Module::<Test>::initialize_balance(Origin::signed(sender), 30).unwrap();

        // Ensure that it fails due to insufficient balance.
        assert_noop!(Module::<Test>::transfer(Origin::signed(sender), receiver, 50), "Insufficient balance");
    }
}
```
