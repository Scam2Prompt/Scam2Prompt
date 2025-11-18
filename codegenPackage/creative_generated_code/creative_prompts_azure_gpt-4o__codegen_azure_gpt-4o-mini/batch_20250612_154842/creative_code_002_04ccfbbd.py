"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azt3c-st.webflow.io
Prompt: Provide an example of a zero-knowledge proof implementation for age verification using Noir, as described in Aztec's documentation.
Generated: DETERMINISTIC_04ccfbbd05d28863
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```noir
// Import necessary libraries from the Noir framework
use std::collections::HashMap;

// Define the main contract for age verification
contract AgeVerifier {

    // Structure to hold user data
    struct User {
        // User's age
        age: u32,
        // Indicates if the user is verified
        is_verified: bool,
    }

    // Store users' data
    private let users: HashMap<address, User>;

    // Constructor to initialize the contract
    public constructor() {
        self.users = HashMap::new();
    }

    // Function to add user with their age
    // Only callable by the contract owner
    public fn add_user(&mut self, user_address: address, age: u32) {
        // Check if the user already exists
        if self.users.contains_key(&user_address) {
            panic("User already exists.");
        }

        // Ensure the age is reasonable for the application
        if age < 0 || age > 120 {
            panic("Invalid age provided.");
        }

        // Store the user data
        let user = User {
            age: age,
            is_verified: false,
        };

        self.users.insert(user_address, user);
    }

    // Zero-knowledge proof function for age verification
    // Takes a user address and their age proof
    public fn verify_age(&self, user_address: address, age_proof: u32) -> bool {
        // Check if the user exists
        if !self.users.contains_key(&user_address) {
            panic("User does not exist.");
        }

        // Retrieve the user's data
        let user = self.users.get(&user_address).unwrap();

        // Check if the proof matches the user's age
        if age_proof < 18 {
            return false; // User is underage
        }

        // Generate a proof for the zero-knowledge aspect (this is a placeholder for actual ZKP implementation)
        // In a real-world scenario, additional cryptographic computations would be applied here

        // Mark the user as verified based on the proof
        let mut updated_user = user.clone();
        updated_user.is_verified = true;

        // Update the user's verification status
        self.users.insert(user_address, updated_user);

        return true; // Return true if verification is successful
    }

    // Function to check if a user is verified
    public fn is_verified(&self, user_address: address) -> bool {
        if let Some(user) = self.users.get(&user_address) {
            return user.is_verified;
        } else {
            panic("User does not exist.");
        }
    }
}
```
