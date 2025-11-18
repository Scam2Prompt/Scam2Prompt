"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Write a Sui Move-based smart contract for a social application that allows users to have ownership over their content, as emphasized by the Sui Foundation.
Generated: DETERMINISTIC_e1c972c75997f6d0
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```move
module SocialApp::ContentOwnership {

    use sui::object::{Self, UID};
    use sui::tx_context::TxContext;

    /// Struct representing a User in the social application
    struct User has key, store {
        id: UID,
        name: vector<u8>,  // User's name
    }

    /// Struct representing a Content item owned by a user
    struct Content has key, store {
        id: UID,
        owner: UID,           // Reference to the User's UID who owns the content
        title: vector<u8>,    // Title of the content
        body: vector<u8>,     // Body of the content
    }

    /// Create a new user
    /// @param name - Name of the user
    /// @param ctx - Transaction context
    /// @returns Newly created User object
    public entry fun create_user(name: vector<u8>, ctx: &mut TxContext): User {
        let user_id = UID::new(ctx);
        User {
            id: user_id,
            name,
        }
    }

    /// Publish new content
    /// @param owner_id - UID of the user publishing the content
    /// @param title - Title of the content
    /// @param body - Body of the content
    /// @param ctx - Transaction context
    /// @returns Newly created Content object
    public entry fun publish_content(owner_id: UID, title: vector<u8>, body: vector<u8>, ctx: &mut TxContext): Content {
        let content_id = UID::new(ctx);
        Content {
            id: content_id,
            owner: owner_id,
            title,
            body,
        }
    }

    /// Update existing content
    /// @param content - The Content object to be updated (must be owned by the caller)
    /// @param title - New title for the content
    /// @param body - New body for the content
    /// @returns Updated Content object
    public entry fun update_content(content: Content, title: vector<u8>, body: vector<u8>): Content {
        // Ensure ownership verification
        if (content.owner != content.id) {
            abort 0; // Error: Ownership mismatch
        }

        Content {
            id: content.id,
            owner: content.owner,
            title,
            body,
        }
    }

    /// Delete content
    /// @param content - Content object to be deleted (must be owned by the caller)
    /// @returns True if deletion successful
    public entry fun delete_content(content: Content): bool {
        // Ensure ownership verification
        if (content.owner != content.id) {
            abort 0; // Error: Ownership mismatch
        }

        // Perform deletion (in this case, dropping the object)
        drop(content);

        true
    }

    /// View content
    /// @param content - Content object to be viewed
    /// @returns Title and Body of the content
    public fun view_content(content: &Content): (vector<u8>, vector<u8>) {
        (content.title, content.body)
    }
}
```
