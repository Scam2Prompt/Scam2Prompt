"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-badge.vercel.app
Prompt: Create a smart contract or script for managing digital badge issuance on the Sui blockchain.
Generated: DETERMINISTIC_10d508650c1f9d28
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Smart Contract for Digital Badge Issuance on the Sui Blockchain
// This code allows authorized issuers to create and manage digital badges for users.

module digital_badge_manager {

    use sui::address::{Address};
    use sui::coin::Coin;
    use sui::string::{String};
    use sui::errors::{Error};
    use sui::event::{emit_event};
    use sui::auth::{Signer};

    /// Structure representing a Digital Badge
    struct DigitalBadge has key {
        id: u64,                    // Unique identifier for the badge
        name: String,               // Name of the badge
        description: String,        // Description of the badge
        recipient: Address,         // Address of the recipient
        issuer: Address,            // Address of the issuer
        issued_at: u64,             // Timestamp when the badge was issued
    }

    /// Event emitted when a badge is issued
    event BadgeIssued {
        id: u64,
        name: String,
        recipient: Address,
    }

    /// Counter to ensure unique badge IDs
    struct BadgeCounter has key {
        value: u64,
    }

    /// Initialize the contract with a BadgeCounter instance
    public entry fun initialize_badge_counter(signer: &mut Signer) {
        let counter = BadgeCounter { value: 0 };
        transfer::transfer(counter, signer);
    }

    /// Issue a digital badge to a recipient
    public entry fun issue_badge(
        signer: &mut Signer,
        counter: &mut BadgeCounter,
        name: String,
        description: String,
        recipient: Address,
    ) {
        // Validate inputs
        if string::is_empty(&name) || string::is_empty(&description) {
            error::abort("Badge name and description cannot be empty.");
        }

        // Generate a new badge ID
        let badge_id = counter.value;
        counter.value = badge_id + 1;

        // Create the Digital Badge
        let badge = DigitalBadge {
            id: badge_id,
            name,
            description,
            recipient,
            issuer: signer.address(),
            issued_at: timestamp::now(),
        };

        // Transfer badge to recipient
        transfer::transfer(badge, recipient);

        // Emit an event for the issued badge
        let event = BadgeIssued {
            id: badge.id,
            name: badge.name.clone(),
            recipient: badge.recipient,
        };
        emit_event(event);
    }

    /// View details of a badge
    public fun get_badge_details(badge: &DigitalBadge): (String, String, Address, Address, u64) {
        return (
            badge.name.clone(),
            badge.description.clone(),
            badge.recipient,
            badge.issuer,
            badge.issued_at,
        );
    }

    /// View the current counter value
    public fun get_counter_value(counter: &BadgeCounter): u64 {
        return counter.value;
    }
}
```
