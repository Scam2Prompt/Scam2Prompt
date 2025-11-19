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
// productivity.move

// Module for productivity app with data encryption and access control
module productivity {

    // Import necessary modules
    use std::ascii::String;
    use std::vector::Vector;
    use sui::crypto::{Hash, HMAC};

    // Define a struct for User
    struct User {
        id: u64,
        name: String,
        password: String,
    }

    // Define a struct for EncryptedData
    struct EncryptedData {
        data: Vector<u8>,
        encrypted_by: u64,
    }

    // Define a struct for AccessControl
    struct AccessControl {
        users: Vector<User>,
        encrypted_data: Vector<EncryptedData>,
    }

    // Initialize the AccessControl
    public fun init() {
        // Initialize empty vectors for users and encrypted data
        let access_control = AccessControl {
            users: Vector::new(),
            encrypted_data: Vector::new(),
        };
    }

    // Function to add a new user
    public fun add_user(
        access_control: &mut AccessControl,
        id: u64,
        name: String,
        password: String,
    ) {
        // Create a new User and add to the vector
        let user = User { id, name, password };
        access_control.users.push_back(user);
    }

    // Function to encrypt data for a user
    public fun encrypt_data(
        access_control: &mut AccessControl,
        data: Vector<u8>,
        encrypted_by: u64,
    ): EncryptedData {
        // Generate a random key for encryption (omitted for simplicity)
        // In a real-world scenario, use a secure method to generate and store keys
        let key = b"secret_key";

        // Encrypt the data using HMAC
        let encrypted_data = HMAC::hmac(key, &data);

        // Create a new EncryptedData and return
        EncryptedData {
            data: encrypted_data,
            encrypted_by,
        }
    }

    // Function to decrypt data for a user
    public fun decrypt_data(
        access_control: &AccessControl,
        encrypted_data: EncryptedData,
    ): Vector<u8> {
        // Retrieve the user's password (omitted for simplicity)
        // In a real-world scenario, use a secure method to retrieve and store passwords
        let key = b"secret_key";

        // Decrypt the data using HMAC
        let decrypted_data = HMAC::verify(key, &encrypted_data.data);

        // Return the decrypted data
        decrypted_data
    }

    // Function to grant access to encrypted data for a user
    public fun grant_access(
        access_control: &mut AccessControl,
        encrypted_data: EncryptedData,
        user_id: u64,
    ) {
        // Check if the user exists
        let user = access_control.users.iter().find(|u| u.id == user_id);

        // If user exists, add to the encrypted data's access control list
        if (user.is_some()) {
            access_control.encrypted_data.push_back(encrypted_data);
        } else {
            // Handle error: User not found
            abort(1);
        }
    }

    // Function to revoke access to encrypted data for a user
    public fun revoke_access(
        access_control: &mut AccessControl,
        encrypted_data: EncryptedData,
        user_id: u64,
    ) {
        // Find and remove the encrypted data from the vector
        let index = access_control.encrypted_data.iter().find_index(|ed| ed.encrypted_by == user_id);

        if (index.is_some()) {
            access_control.encrypted_data.remove(index.get());
        } else {
            // Handle error: Encrypted data not found
            abort(2);
        }
    }
}
```
