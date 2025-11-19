"""
Generated Code Metadata:
========================
Original URL: https://magic.link
Prompt: "Design a user-friendly onboarding process for a new user to interact with an on-chain application using Magic Labs' wallet abstraction tools."
Generated: DETERMINISTIC_2b9f0f4125632dbd
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { Magic } from '@magic-sdk/admin';
import { ethers } from 'ethers';

// Initialize Magic instance
const magic = new Magic('YOUR_API_KEY', {
  // Optional configuration
  network: 'testnet', // or 'mainnet'
});

// Function to handle user onboarding
async function onboardUser() {
  try {
    // Step 1: Get user email
    const email = await getUserEmail();

    // Step 2: Create a new Magic user
    const user = await magic.users.createUser({
      email,
    });

    // Step 3: Get user's Ethereum wallet
    const wallet = await magic.users.getWallet(user.id);

    // Step 4: Display wallet address to user
    console.log(`Your Ethereum wallet address is: ${wallet.address}`);

    // Step 5: Provide next steps for user to interact with on-chain application
    console.log('Please proceed to connect your wallet to our on-chain application.');

    return user;
  } catch (error) {
    console.error('Error during onboarding:', error);
    throw error;
  }
}

// Helper function to get user email
async function getUserEmail() {
  return new Promise((resolve, reject) => {
    // Implement your preferred method to get user email
    // For example, using a prompt in a browser environment
    const email = prompt('Please enter your email address:');
    if (email) {
      resolve(email);
    } else {
      reject(new Error('Email address is required'));
    }
  });
}

// Function to connect wallet to on-chain application
async function connectWalletToApp(userId) {
  try {
    // Get user's Ethereum wallet
    const wallet = await magic.users.getWallet(userId);

    // Connect wallet to on-chain application
    // Replace with your on-chain application's connection logic
    const appProvider = new ethers.providers.JsonRpcProvider('YOUR_APP_RPC_URL');
    const appSigner = new ethers.Wallet(wallet.privateKey, appProvider);

    // Verify connection
    const balance = await appSigner.getBalance();
    console.log(`Connected to on-chain application with wallet balance: ${balance}`);

    return appSigner;
  } catch (error) {
    console.error('Error connecting wallet to on-chain application:', error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    const user = await onboardUser();
    const appSigner = await connectWalletToApp(user.id);
    // Continue with on-chain application interaction using appSigner
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
