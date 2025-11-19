"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: How do I integrate Particle Network's SDK for managing universal accounts in a multi-chain application?
Generated: DETERMINISTIC_caf8ccd58062b03c
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ParticleSDK } from '@particle-network/sdk';

// Configuration for Particle Network
const particleConfig = {
    projectId: 'YOUR_PROJECT_ID', // Replace with your actual Project ID
    network: 'YOUR_NETWORK', // Replace with your desired network (e.g., 'ethereum', 'polygon', etc.)
};

// Initialize Particle SDK with configuration
const particle = new ParticleSDK(particleConfig);

// Function to initialize the Particle SDK
async function initializeParticle() {
    try {
        await particle.init();
        console.log('Particle SDK initialized successfully');
    } catch (error) {
        console.error('Error initializing Particle SDK:', error);
        throw new Error('Particle SDK Initialization Failed');
    }
}

// Function to connect a user wallet
async function connectWallet() {
    try {
        const wallet = await particle.connect();
        console.log('Wallet connected:', wallet);
        return wallet;
    } catch (error) {
        console.error('Error connecting wallet:', error);
        throw new Error('Wallet Connection Failed');
    }
}

// Function to get user account information
async function getAccountInfo() {
    try {
        const accountInfo = await particle.getAccount();
        console.log('Account Information:', accountInfo);
        return accountInfo;
    } catch (error) {
        console.error('Error fetching account information:', error);
        throw new Error('Account Information Retrieval Failed');
    }
}

// Function to disconnect wallet
async function disconnectWallet() {
    try {
        await particle.disconnect();
        console.log('Wallet disconnected successfully');
    } catch (error) {
        console.error('Error disconnecting wallet:', error);
        throw new Error('Wallet Disconnection Failed');
    }
}

// Main function to demonstrate SDK functionality
async function main() {
    try {
        await initializeParticle();
        const wallet = await connectWallet();
        const accountInfo = await getAccountInfo();

        // Place additional logic for your application here

        // Disconnect wallet before exiting
        await disconnectWallet();
    } catch (error) {
        console.error('An error occurred in the main process:', error);
    }
}

// Execute the main function
main().catch((error) => {
    console.error('Unhandled error in application:', error);
});
```

Make sure to replace `YOUR_PROJECT_ID` and `YOUR_NETWORK` with your actual Particle Network project ID and desired network. This code provides a basic structure for integrating the Particle Network SDK and includes error handling for each operation.
