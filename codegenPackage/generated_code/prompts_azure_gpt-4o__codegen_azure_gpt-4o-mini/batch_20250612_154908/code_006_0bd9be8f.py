"""
Generated Code Metadata:
========================
Original URL: https://aptos-names-mainnet-temp.netlify.app
Prompt: Create a smart contract example for registering and managing Aptos Names on the Aptos blockchain.
Generated: DETERMINISTIC_0bd9be8f1ddb8332
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
// SPDX-License-Identifier: MIT
// Aptos Name Registration Smart Contract

module AptosNameRegistry {
    use std::string;
    use std::vector;
    use std::option;
    use std::signer;
    use std::account;

    // Struct to represent a registered name
    struct Name {
        owner: address,
        is_registered: bool,
    }

    // Mapping from name to Name struct
    resource struct NameRegistry {
        names: vector<(string, Name)>,
    }

    // Event emitted when a name is registered
    struct NameRegisteredEvent {
        name: string,
        owner: address,
    }

    // Event emitted when a name is transferred
    struct NameTransferredEvent {
        name: string,
        from: address,
        to: address,
    }

    // Initialize the NameRegistry resource
    public fun initialize(account: &signer) {
        let registry = NameRegistry {
            names: vector::empty<(string, Name)>(),
        };
        move_to(account, registry);
    }

    // Register a new name
    public fun register_name(account: &signer, name: string) {
        let registry = borrow_global_mut<NameRegistry>(signer::address_of(account));
        
        // Check if the name is already registered
        if (vector::contains(&registry.names, &name)) {
            abort(1); // Name already registered
        }

        // Create a new Name struct
        let new_name = Name {
            owner: signer::address_of(account),
            is_registered: true,
        };

        // Add the new name to the registry
        vector::push_back(&mut registry.names, (name, new_name));

        // Emit the registration event
        emit_event<NameRegisteredEvent>(NameRegisteredEvent {
            name: name,
            owner: signer::address_of(account),
        });
    }

    // Transfer ownership of a name
    public fun transfer_name(account: &signer, name: string, new_owner: address) {
        let registry = borrow_global_mut<NameRegistry>(signer::address_of(account));
        
        // Find the name in the registry
        let index = vector::index_of(&registry.names, &name);
        if (index == option::none()) {
            abort(2); // Name not found
        }

        // Get the current name details
        let (registered_name, name_details) = vector::borrow(&registry.names, index);
        
        // Check if the caller is the owner
        if (name_details.owner != signer::address_of(account)) {
            abort(3); // Not the owner
        }

        // Update the owner of the name
        let updated_name = Name {
            owner: new_owner,
            is_registered: true,
        };
        vector::remove(&mut registry.names, index);
        vector::push_back(&mut registry.names, (registered_name, updated_name));

        // Emit the transfer event
        emit_event<NameTransferredEvent>(NameTransferredEvent {
            name: registered_name,
            from: signer::address_of(account),
            to: new_owner,
        });
    }

    // Query the owner of a name
    public fun get_name_owner(name: string): option::Option<address> {
        let registry = borrow_global<NameRegistry>(signer::address_of(account));
        
        // Find the name in the registry
        let index = vector::index_of(&registry.names, &name);
        if (index == option::none()) {
            return option::none(); // Name not found
        }

        // Return the owner of the name
        let (_, name_details) = vector::borrow(&registry.names, index);
        return option::some(name_details.owner);
    }
}
```
