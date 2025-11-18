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
// SPDX-License-Identifier: Apache-2.0
// Sui Move contract for a Legal Data Management System

module legal_data_management {

    // Structure to hold legal document information
    struct Document has key, store {
        // Unique identifier for the document
        id: u64,
        // Owner of the document
        owner: address,
        // Creation timestamp
        created_at: timestamp,
        // Metadata of the document
        metadata: vector<u8>,
    }

    // Event emitted when a new document is created
    struct DocumentCreatedEvent has copy, drop {
        document_id: u64,
        owner: address,
        timestamp: timestamp,
    }

    // Resource to hold the owner of documents
    resource Owner {
        // Vector of document IDs owned by the user
        documents: vector<u64>,
    }

    // Function to create a new document
    public fun create_document(
        id: u64,
        owner: address,
        metadata: vector<u8>,
    ) {
        // Ensure the owner address is valid
        assert!(is_valid_address(owner), 0);

        // Create a new document instance
        let new_document = Document {
            id: id,
            owner: owner,
            created_at: current_time(),
            metadata: metadata,
        };

        // Store document in the global state
        move_to_sender(new_document);

        // Emit a document created event
        emit DocumentCreatedEvent {
            document_id: id,
            owner: owner,
            timestamp: current_time(),
        };
    }

    // Function to retrieve document by ID
    public fun get_document(id: u64): Document {
        let doc = borrow_global<Document>(id);
        return doc;
    }

    // Function to transfer ownership of a document
    public fun transfer_document(doc_id: u64, new_owner: address) {
        // Ensure the new owner address is valid
        assert!(is_valid_address(new_owner), 1);

        // Borrow the document from global storage
        let doc_ref = borrow_global_mut<Document>(doc_id);

        // Transfer ownership
        doc_ref.owner = new_owner;

        // Update the owner resource
        let owner_ref = borrow_global_mut<Owner>(doc_ref.owner);
        remove_document_from_owner(owner_ref, doc_id);
        add_document_to_owner(owner_ref, doc_id);
    }

    // Helper function to remove a document ID from the owner's resource
    fun remove_document_from_owner(owner: &mut Owner, doc_id: u64) {
        let index = vector::index_of(&owner.documents, doc_id);
        assert!(index != vector::length(&owner.documents), 2);
        vector::remove(&mut owner.documents, index);
    }

    // Helper function to add a document ID to the owner's resource
    fun add_document_to_owner(owner: &mut Owner, doc_id: u64) {
        vector::push_back(&mut owner.documents, doc_id);
    }

    // Utility function to validate an address
    fun is_valid_address(addr: address): bool {
        return addr != 0x00000000000000000000000000000000;
    }

    // Utility function to get the current timestamp
    fun current_time(): timestamp {
        // Return the current timestamp (placeholder)
        return 0;
    }
}
```
