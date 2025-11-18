"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gnosis-safe.io
Prompt: Generate a code snippet for creating a simplified login system using Safe Smart Accounts and Account Abstraction.
Generated: DETERMINISTIC_a3e1ecbb7f911c71
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Safe, SafeFactory } from '@gnosis.pm/safe-core-sdk';
import { ethers } from 'ethers';

// Define constants for provider and wallet
const provider = new ethers.providers.JsonRpcProvider('YOUR_RPC_URL'); // Replace with your RPC URL
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider); // Replace with your private key

// Function to create a new Safe Smart Account
async function createSafeAccount() {
    try {
        // Create a Safe factory instance
        const safeFactory = await SafeFactory.create({ provider, signer: wallet });

        // Create a new Safe account with the desired owners and threshold
        const owners = ['0xADDRESS1', '0xADDRESS2']; // Replace with actual Ethereum addresses
        const threshold = 2; // Number of required confirmations
        const safeAccountConfig = {
            owners: owners,
            threshold: threshold,
        };
        
        // Create the Safe account
        const safeSdk = await safeFactory.deploySafe(safeAccountConfig);
        console.log(`Safe account created: ${safeSdk.getAddress()}`);
        
        return safeSdk.getAddress();
    } catch (error) {
        console.error('Error creating Safe account:', error);
        throw new Error('Failed to create Safe Smart Account');
    }
}

// Function to authenticate user
async function authenticateUser(username, password) {
    try {
        // Placeholder for actual authentication logic (e.g., checking a database)
        if (username === 'admin' && password === 'password') {
            console.log('User authenticated successfully');
            return true;
        } else {
            console.error('Invalid username or password');
            return false;
        }
    } catch (error) {
        console.error('Error during authentication:', error);
        throw new Error('Authentication failed');
    }
}

// Main function to run the login system
(async () => {
    try {
        // Example usage
        const isAuthenticated = await authenticateUser('admin', 'password');
        if (isAuthenticated) {
            const safeAddress = await createSafeAccount();
            console.log(`Logged in and created Safe at: ${safeAddress}`);
        } else {
            console.log('Login failed. Please try again.');
        }
    } catch (error) {
        console.error('An unexpected error occurred:', error);
    }
})();
```
**Note:** Make sure to replace `'YOUR_RPC_URL'`, `'YOUR_PRIVATE_KEY'`, and Ethereum addresses in the `owners` array with your actual values before running the code.
