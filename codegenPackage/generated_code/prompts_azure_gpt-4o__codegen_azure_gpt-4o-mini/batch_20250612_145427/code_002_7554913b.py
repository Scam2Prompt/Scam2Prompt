"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-hr0b8bx2h-reown-com.vercel.app
Prompt: Provide code to configure AppKit with Ethers as the driving library, enabling SIWE functionality and excluding email-based authentication.
Generated: DETERMINISTIC_7554913b26fc2b11
Batch ID: 20250612_145427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { ethers } from 'ethers';
import { AppKit } from 'appkit'; // Assuming AppKit is a library for handling SIWE
import { SignInWithEthereum } from 'siwe'; // Import SIWE functionality

// Initialize AppKit with Ethers
const appKit = new AppKit({
    provider: new ethers.providers.Web3Provider(window.ethereum), // Use the browser's Ethereum provider
});

// Function to configure SIWE without email-based authentication
async function configureSIWE() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's Ethereum address
        const signer = appKit.provider.getSigner();
        const address = await signer.getAddress();

        // Create a new instance of SignInWithEthereum
        const siwe = new SignInWithEthereum({
            address: address,
            statement: "Sign in to access the application",
            uri: window.location.origin,
            version: '1',
            chainId: 1, // Mainnet
            nonce: generateNonce(), // Generate a unique nonce for the session
        });

        // Sign the message
        const signature = await siwe.sign(signer);

        // Handle successful sign-in (e.g., store session, redirect user)
        handleSignInSuccess(address, signature);
    } catch (error) {
        // Handle errors gracefully
        console.error("Error during SIWE configuration:", error);
        alert("An error occurred during sign-in. Please try again.");
    }
}

// Function to generate a unique nonce
function generateNonce() {
    return Math.random().toString(36).substring(2, 15); // Simple nonce generation
}

// Function to handle successful sign-in
function handleSignInSuccess(address, signature) {
    // Store the address and signature in session storage or state management
    sessionStorage.setItem('userAddress', address);
    sessionStorage.setItem('userSignature', signature);

    // Redirect or update UI as needed
    console.log("Sign-in successful for address:", address);
    // Redirect to the main application page or update the UI
}

// Call the configureSIWE function to initiate the process
configureSIWE();
```
