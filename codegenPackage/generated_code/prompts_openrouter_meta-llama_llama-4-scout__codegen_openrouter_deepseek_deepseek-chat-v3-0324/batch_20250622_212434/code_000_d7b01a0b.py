"""
Generated Code Metadata:
========================
Original URL: https://cyclicmainnet.vercel.app
Prompt: "Write a code snippet for integrating a wallet authentication system into a dApp using a decentralized protocol."
Generated: DETERMINISTIC_d7b01a0b70f78b8f
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const ethers = require('ethers');
const Web3Modal = require('web3modal');

// Configuration for Web3Modal
const providerOptions = {
  walletconnect: {
    package: require('@walletconnect/web3-provider'),
    options: {
      infuraId: 'YOUR_INFURA_PROJECT_ID', // Replace with your Infura ID
    }
  }
};

const web3Modal = new Web3Modal({
  network: 'mainnet', // Change to appropriate network
  cacheProvider: true, // Enable caching
  providerOptions // Add provider options
});

// Function to connect wallet
async function connectWallet() {
  try {
    // Open Web3Modal to prompt user to select wallet
    const instance = await web3Modal.connect();
    
    // Create a Web3Provider instance
    const provider = new ethers.providers.Web3Provider(instance);
    
    // Get the signer (user's wallet)
    const signer = provider.getSigner();
    
    // Get user's address
    const address = await signer.getAddress();
    
    // Get user's balance
    const balance = await provider.getBalance(address);
    
    // Format balance in ETH
    const formattedBalance = ethers.utils.formatEther(balance);
    
    console.log('Connected wallet:', address);
    console.log('Balance:', formattedBalance, 'ETH');
    
    return {
      provider,
      signer,
      address,
      balance: formattedBalance
    };
  } catch (error) {
    console.error('Error connecting wallet:', error);
    throw new Error('Failed to connect wallet');
  }
}

// Function to disconnect wallet
async function disconnectWallet() {
  try {
    if (web3Modal.cachedProvider) {
      web3Modal.clearCachedProvider();
      console.log('Wallet disconnected');
    }
  } catch (error) {
    console.error('Error disconnecting wallet:', error);
    throw new Error('Failed to disconnect wallet');
  }
}

// Function to sign a message
async function signMessage(signer, message) {
  try {
    if (!signer || !message) {
      throw new Error('Signer and message are required');
    }
    
    const signature = await signer.signMessage(message);
    console.log('Message signed:', signature);
    return signature;
  } catch (error) {
    console.error('Error signing message:', error);
    throw new Error('Failed to sign message');
  }
}

// Example usage
(async () => {
  try {
    // Connect wallet
    const { signer, address } = await connectWallet();
    
    // Sign a message
    await signMessage(signer, 'Hello, dApp!');
    
    // Disconnect wallet (optional)
    // await disconnectWallet();
  } catch (error) {
    console.error('Application error:', error.message);
  }
})();
```
