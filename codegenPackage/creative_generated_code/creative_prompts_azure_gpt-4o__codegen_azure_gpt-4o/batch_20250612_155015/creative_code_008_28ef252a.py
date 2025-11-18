"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.web.app
Prompt: Write a Sui Move contract for a legal data management system that aligns with the Sui Foundation's mission of enabling ownership over data.
Generated: DETERMINISTIC_28ef252ae6aa7be7
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
module LegalDataManagement {

    use sui::errors;
    use sui::transfer;

    /// Structure to represent legal data owned by a user.
    struct LegalData has key, store {
        id: UID,               // Unique identifier for the LegalData instance
        owner: address,        // The owner of this legal data
        data_title: String,    // A title describing the legal data
        content_hash: String,  // Hash representing the content (ensures immutability)
        metadata: String,      // Additional metadata about the legal data
    }

    /// Event emitted when legal data is created.
    struct LegalDataCreated has store {
        id: UID,               // Unique identifier for the LegalData
        owner: address,        // Owner of the LegalData
        data_title: String,    // Data Title
    }

    /// Event emitted when legal data ownership is transferred.
    struct LegalDataOwnershipTransferred has store {
        id: UID,               // Unique identifier for the LegalData
        old_owner: address,    // Previous owner of the LegalData
        new_owner: address,    // New owner of the LegalData
    }

    /// Function to create new legal data.
    public fun create_legal_data(
        owner: address,
        data_title: String,
        content_hash: String,
        metadata: String
    ): LegalData {
        // Generate a unique identifier for this LegalData
        let id = sui::object::new_uid();

        // Create the LegalData object
        let legal_data = LegalData {
            id,
            owner,
            data_title: data_title.clone(),
            content_hash: content_hash.clone(),
            metadata: metadata.clone(),
        };

        // Emit an event for the creation of the LegalData
        emit LegalDataCreated {
            id,
            owner,
            data_title,
        };

        // Return the newly created LegalData object
        legal_data
    }

    /// Function to transfer ownership of legal data.
    public fun transfer_legal_data(
        legal_data: &mut LegalData, 
        new_owner: address
    ) {
        let old_owner = legal_data.owner;

        // Update the owner field in the LegalData object
        legal_data.owner = new_owner;

        // Emit an event for the ownership transfer
        emit LegalDataOwnershipTransferred {
            id: legal_data.id,
            old_owner,
            new_owner,
        };
    }

    /// Function to validate content hash (basic integrity check example).
    public fun validate_content_hash(
        legal_data: &LegalData, 
        expected_hash: String
    ): bool {
        // Compare the current content hash with the expected hash
        legal_data.content_hash == expected_hash
    }

    /// Function to retrieve metadata for a legal data object.
    public fun get_metadata(legal_data: &LegalData): String {
        legal_data.metadata.clone()
    }

    /// Function to transfer ownership of a LegalData object to another address.
    /// This function ensures proper ownership and handles errors.
    public entry fun transfer_ownership_entry(
        legal_data: LegalData, 
        new_owner: address
    ) {
        // Ensure the caller is the current owner of the LegalData object
        if (sui::tx_context::sender() != legal_data.owner) {
            // Abort with an error if the caller is not the owner
            abort errors::unauthorized_error();
        }

        // Use the transfer module to transfer ownership
        transfer::object(legal_data.id, new_owner);
    }

    /// Function to retrieve the owner of the legal data.
    public fun get_owner(legal_data: &LegalData): address {
        legal_data.owner
    }
}
```
