"""
Generated Code Metadata:
========================
Original URL: https://web3modal.com
Prompt: Create a script to integrate embedded smart wallets with social and email login using Reown's AppKit, ensuring compatibility with EVM, Solana, and Bitcoin chains.
Generated: DETERMINISTIC_64fc39343af463df
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { AppKit, ChainId, Wallet } = require('@reown/appkit');
const { ethers } = require('ethers');
const axios = require('axios');

// Define supported chains
const supportedChains = [
  ChainId.Ethereum,
  ChainId.Solana,
  ChainId.Bitcoin,
];

// Define social and email login providers
const loginProviders = [
  'google',
  'facebook',
  'twitter',
  'email',
];

// Initialize AppKit
const appKit = new AppKit({
  // Replace with your Reown AppKit API key
  apiKey: 'YOUR_API_KEY',
});

/**
 * Generates a random wallet
 * @returns {Promise<Wallet>} A promise resolving to a Wallet object
 */
async function generateWallet() {
  try {
    const wallet = await Wallet.generate();
    return wallet;
  } catch (error) {
    console.error('Error generating wallet:', error);
    throw error;
  }
}

/**
 * Connects a social or email login provider
 * @param {string} provider - The login provider to connect
 * @param {string} idToken - The ID token from the login provider
 * @returns {Promise<string>} A promise resolving to the user's address
 */
async function connectLoginProvider(provider, idToken) {
  try {
    if (!loginProviders.includes(provider)) {
      throw new Error(`Unsupported login provider: ${provider}`);
    }

    const userAddress = await appKit.connectSocialLogin({
      provider,
      idToken,
    });

    return userAddress;
  } catch (error) {
    console.error('Error connecting login provider:', error);
    throw error;
  }
}

/**
 * Links a wallet to a user's social or email login
 * @param {Wallet} wallet - The wallet to link
 * @param {string} userAddress - The user's address from the social or email login
 * @param {ChainId} chainId - The chain ID of the wallet
 * @returns {Promise<void>} A promise resolving when the wallet is linked
 */
async function linkWallet(wallet, userAddress, chainId) {
  try {
    if (!supportedChains.includes(chainId)) {
      throw new Error(`Unsupported chain ID: ${chainId}`);
    }

    await appKit.linkWallet({
      wallet,
      userAddress,
      chainId,
    });
  } catch (error) {
    console.error('Error linking wallet:', error);
    throw error;
  }
}

/**
 * Authenticates a user with a social or email login and returns their linked wallets
 * @param {string} provider - The login provider to authenticate with
 * @param {string} idToken - The ID token from the login provider
 * @returns {Promise<Wallet[]>} A promise resolving to an array of the user's linked wallets
 */
async function authenticateUser(provider, idToken) {
  try {
    const userAddress = await connectLoginProvider(provider, idToken);
    const linkedWallets = await appKit.getLinkedWallets(userAddress);

    return linkedWallets;
  } catch (error) {
    console.error('Error authenticating user:', error);
    throw error;
  }
}

// Example usage:
async function main() {
  try {
    // Generate a random wallet
    const wallet = await generateWallet();
    console.log('Generated wallet:', wallet.address);

    // Authenticate a user with Google login
    const googleIdToken = 'YOUR_GOOGLE_ID_TOKEN';
    const userAddress = await connectLoginProvider('google', googleIdToken);
    console.log('Authenticated user address:', userAddress);

    // Link the wallet to the user's social login
    const chainId = ChainId.Ethereum;
    await linkWallet(wallet, userAddress, chainId);
    console.log('Linked wallet to user address');

    // Authenticate the user and retrieve their linked wallets
    const linkedWallets = await authenticateUser('google', googleIdToken);
    console.log('Linked wallets:', linkedWallets.map((wallet) => wallet.address));
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
