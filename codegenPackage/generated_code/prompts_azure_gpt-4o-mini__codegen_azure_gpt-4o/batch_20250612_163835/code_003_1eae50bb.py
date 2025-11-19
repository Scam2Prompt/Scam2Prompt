"""
Generated Code Metadata:
========================
Original URL: https://polkadot.africa
Prompt: Provide an example of using Substrate to build a custom blockchain for the African market.
Generated: DETERMINISTIC_1eae50bb4e181905
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary Substrate crates
use frame_support::{decl_module, decl_storage, decl_event, decl_error, dispatch};
use frame_system::ensure_signed;
use sp_std::vec::Vec;

// Define the module for the custom blockchain
pub trait Config: frame_system::Config {
    // Define the event type for the module
    type Event: From<Event<Self>> + Into<<Self as frame_system::Config>::Event>;
}

// Define the storage for the module
decl_storage! {
    trait Store for Module<T: Config> as AfricanMarketModule {
        // Storage to hold product listings
        Products get(fn products): map hasher(blake2_128_concat) u32 => Option<Product>;
        // Storage to hold the next product ID
        NextProductId get(fn next_product_id): u32;
    }
}

// Define the structure for a product
#[derive(Clone, Encode, Decode, Default, PartialEq)]
pub struct Product {
    pub name: Vec<u8>,
    pub price: u32,
    pub owner: T::AccountId,
}

// Define the events for the module
decl_event! {
    pub enum Event<T> where AccountId = <T as frame_system::Config>::AccountId {
        // Event emitted when a product is listed
        ProductListed(u32, Vec<u8>, u32, AccountId),
        // Event emitted when a product is purchased
        ProductPurchased(u32, AccountId),
    }
}

// Define the errors for the module
decl_error! {
    pub enum Error for Module<T: Config> {
        // Error when a product does not exist
        ProductNotFound,
        // Error when the buyer does not have enough funds
        InsufficientFunds,
    }
}

// Define the module's dispatchable functions
decl_module! {
    pub struct Module<T: Config> for enum Call where origin: T::Origin {
        // Initialize the module with default events
        fn deposit_event() = default;

        // Function to list a new product
        #[weight = 10_000]
        pub fn list_product(origin, name: Vec<u8>, price: u32) -> dispatch::DispatchResult {
            let sender = ensure_signed(origin)?;

            // Get the next product ID
            let product_id = Self::next_product_id();

            // Create the product
            let product = Product {
                name: name.clone(),
                price,
                owner: sender.clone(),
            };

            // Store the product in storage
            Products::insert(product_id, product);

            // Update the next product ID
            NextProductId::put(product_id + 1);

            // Emit the ProductListed event
            Self::deposit_event(RawEvent::ProductListed(product_id, name, price, sender));

            Ok(())
        }

        // Function to purchase a product
        #[weight = 10_000]
        pub fn purchase_product(origin, product_id: u32) -> dispatch::DispatchResult {
            let buyer = ensure_signed(origin)?;

            // Ensure the product exists
            let product = Products::get(product_id).ok_or(Error::<T>::ProductNotFound)?;

            // Ensure the buyer has enough funds (mock check for simplicity)
            // In a real implementation, this would involve checking balances
            if product.price > 1000 {
                return Err(Error::<T>::InsufficientFunds.into());
            }

            // Transfer ownership of the product
            Products::mutate(product_id, |p| {
                if let Some(prod) = p {
                    prod.owner = buyer.clone();
                }
            });

            // Emit the ProductPurchased event
            Self::deposit_event(RawEvent::ProductPurchased(product_id, buyer));

            Ok(())
        }
    }
}
```

This code provides a basic implementation of a custom blockchain module using Substrate for an African market. It includes functionality for listing and purchasing products, with proper error handling and event emission.
