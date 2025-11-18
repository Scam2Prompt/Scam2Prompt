"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Write code using Particle Network's SDK to implement a universal account system that supports multi-chain asset management and account abstraction.
Generated: DETERMINISTIC_e0a314c70277a981
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies and libraries
const { ParticleNetwork, ParticleProvider, ParticleWallet } = require('@particle-network/provider');
const ethers = require('ethers');

// Configuration for Particle Network
const particleNetworkConfig = {
  projectId: 'your-project-id', // Replace with your Particle Network project ID
  clientKey: 'your-client-key', // Replace with your Particle Network client key
  appId: 'your-app-id', // Replace with your Particle Network app ID
  chainIds: ['1', '137', '56'], // Ethereum, Polygon, Binance Smart Chain (multi-chain support)
};

// Initialize Particle Network instance
const particleNetwork = new ParticleNetwork(particleNetworkConfig);

// Function to create or retrieve a universal account
async function initializeAccount() {
  try {
    // Log in user via Particle Network (supports social login, email, etc.)
    const user = await particleNetwork.auth.login({
      preferredAuthType: 'social', // Example: social login; can be customized
      loginOptions: { provider: 'google' }, // Example: Google login; other providers can be used
    });

    console.log('User logged in successfully:', user);
    return user;
  } catch (error) {
    console.error('Error during login:', error.message);
    throw new Error('Failed to initialize account');
  }
}

// Function to get wallet provider (supports account abstraction)
async function getWalletProvider() {
  try {
    const provider = new ParticleProvider(particleNetwork);
    console.log('Wallet provider initialized.');
    return provider;
  } catch (error) {
    console.error('Error initializing wallet provider:', error.message);
    throw new Error('Failed to get wallet provider');
  }
}

// Function to manage multi-chain assets
async function manageMultiChainAssets() {
  try {
    const provider = await getWalletProvider();

    // Create an ethers.js signer instance from provider
    const signer = new ethers.Wallet(particleNetwork.auth.privateKey, provider);

    // Query Ethereum balance
    const ethereumBalance = await provider.getBalance(signer.address, '1'); // Chain ID 1 (Ethereum)
    console.log(`Ethereum balance: ${ethers.utils.formatEther(ethereumBalance)} ETH`);

    // Query Polygon balance
    const polygonBalance = await provider.getBalance(signer.address, '137'); // Chain ID 137 (Polygon)
    console.log(`Polygon balance: ${ethers.utils.formatEther(polygonBalance)} MATIC`);

    // Query Binance Smart Chain balance
    const bscBalance = await provider.getBalance(signer.address, '56'); // Chain ID 56 (BSC)
    console.log(`Binance Smart Chain balance: ${ethers.utils.formatEther(bscBalance)} BNB`);

    // Example Transaction: Transfer assets (abstracted for universal account)
    const transaction = {
      to: 'recipient-address', // Replace with recipient address
      value: ethers.utils.parseEther('0.1'), // Specify amount to send
      chainId: '1', // Specify chain ID for transaction
    };

    const txResponse = await signer.sendTransaction(transaction);
    console.log('Transaction sent:', txResponse.hash);

    const receipt = await txResponse.wait();
    console.log('Transaction confirmed:', receipt);
  } catch (error) {
    console.error('Error managing multi-chain assets:', error.message);
    throw new Error('Failed to manage multi-chain assets');
  }
}

// Main function to demonstrate universal account system
async function main() {
  try {
    // Step 1: Initialize universal account
    const user = await initializeAccount();

    // Step 2: Manage multi-chain assets using account abstraction
    await manageMultiChainAssets();

    console.log('Universal account system implementation completed successfully.');
  } catch (error) {
    console.error('Error in universal account system:', error.message);
  }
}

// Execute the main function
main();
```
