"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.web.app
Prompt: "Create a Sui Move module for a productivity app, including functions for data encryption and access control, and explain its key features and benefits."
Generated: DETERMINISTIC_21c7d08c0a283759
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```move
/// Module: productivity_app
/// A Sui Move module for a productivity app with data encryption and access control features.
module productivity_app::productivity {
    use std::vector;
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};
    use sui::sui::SUI;
    use sui::dynamic_field;
    use sui::crypto;

    /// Error codes
    const E_NOT_AUTHORIZED: u64 = 0;
    const E_INVALID_ENCRYPTION_KEY: u64 = 1;
    const E_DATA_NOT_FOUND: u64 = 2;

    /// Struct representing encrypted data
    struct EncryptedData has key, store {
        id: UID,
        encrypted_content: vector<u8>,
        owner: address
    }

    /// Struct representing access control permissions
    struct AccessControl has key, store {
        id: UID,
        owner: address,
        authorized_users: vector<address>
    }

    /// Initialize a new AccessControl object
    public fun new_access_control(owner: &signer, ctx: &mut TxContext): AccessControl {
        AccessControl {
            id: object::new(ctx),
            owner: tx_context::sender(ctx),
            authorized_users: vector::empty()
        }
    }

    /// Grant access to a user
    public fun grant_access(
        access_control: &mut AccessControl,
        user: address,
        _: &signer
    ) {
        assert!(tx_context::sender(_) == access_control.owner, E_NOT_AUTHORIZED);
        vector::push_back(&mut access_control.authorized_users, user);
    }

    /// Revoke access from a user
    public fun revoke_access(
        access_control: &mut AccessControl,
        user: address,
        _: &signer
    ) {
        assert!(tx_context::sender(_) == access_control.owner, E_NOT_AUTHORIZED);
        let index = vector::index_of(&access_control.authorized_users, &user);
        if (option::is_some(&index)) {
            vector::remove(&mut access_control.authorized_users, option::destroy_some(index));
        }
    }

    /// Check if a user has access
    public fun has_access(access_control: &AccessControl, user: address): bool {
        user == access_control.owner || vector::contains(&access_control.authorized_users, &user)
    }

    /// Encrypt data with a key
    public fun encrypt_data(
        content: vector<u8>,
        encryption_key: vector<u8>,
        owner: &signer,
        ctx: &mut TxContext
    ): EncryptedData {
        assert!(vector::length(&encryption_key) > 0, E_INVALID_ENCRYPTION_KEY);
        
        let encrypted_content = crypto::blake2b256(&content);
        // In production, use proper encryption instead of hash
        // let encrypted_content = crypto::encrypt(&content, &encryption_key);

        EncryptedData {
            id: object::new(ctx),
            encrypted_content,
            owner: tx_context::sender(ctx)
        }
    }

    /// Decrypt data with a key
    public fun decrypt_data(
        encrypted_data: &EncryptedData,
        encryption_key: vector<u8>,
        access_control: &AccessControl,
        _: &signer
    ): vector<u8> {
        assert!(has_access(access_control, tx_context::sender(_)), E_NOT_AUTHORIZED);
        assert!(vector::length(&encryption_key) > 0, E_INVALID_ENCRYPTION_KEY);

        // In production, use proper decryption instead
        // let decrypted_content = crypto::decrypt(&encrypted_data.encrypted_content, &encryption_key);
        encrypted_data.encrypted_content
    }

    /// Transfer ownership of encrypted data
    public fun transfer_encrypted_data(
        encrypted_data: EncryptedData,
        recipient: address,
        _: &signer
    ) {
        assert!(tx_context::sender(_) == encrypted_data.owner, E_NOT_AUTHORIZED);
        transfer::transfer(encrypted_data, recipient);
    }

    /// Share encrypted data with another user
    public entry fun share_data(
        encrypted_data: &mut EncryptedData,
        access_control: &mut AccessControl,
        recipient: address,
        _: &signer
    ) {
        assert!(tx_context::sender(_) == encrypted_data.owner, E_NOT_AUTHORIZED);
        grant_access(access_control, recipient, _);
    }

    /// Delete encrypted data
    public entry fun delete_data(
        encrypted_data: EncryptedData,
        _: &signer
    ) {
        assert!(tx_context::sender(_) == encrypted_data.owner, E_NOT_AUTHORIZED);
        let EncryptedData { id, encrypted_content: _, owner: _ } = encrypted_data;
        object::delete(id);
    }

    /// Get encrypted data content (for testing purposes)
    public fun get_encrypted_content(encrypted_data: &EncryptedData): &vector<u8> {
        &encrypted_data.encrypted_content
    }
}
```
