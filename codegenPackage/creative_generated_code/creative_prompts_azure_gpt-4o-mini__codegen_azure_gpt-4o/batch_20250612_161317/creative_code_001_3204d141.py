"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-sea-web3-app.vercel.app
Prompt: Write code to integrate wallet connection functionality in a web3 app using Metamask.
Generated: DETERMINISTIC_3204d141b9a56001
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// web3-wallet-connection.js

// Import the ethers library for interacting with the blockchain
import { ethers } from 'ethers';

// Helper function to connect to Metamask wallet
async function connectWallet() {
  try {
    // Check if the MetaMask extension is installed
    if (!window.ethereum) {
      throw new Error('MetaMask is not installed. Please install MetaMask to use this feature.');
    }

    // Request connection to the wallet
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    
    // If accounts exist, return the first account (default behavior of Metamask)
    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure you have an active account in MetaMask.');
    }

    const selectedAccount = accounts[0]; // Get the first account from the list
    console.log(`Connected wallet address: ${selectedAccount}`);

    // Create a provider using the connected wallet
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Return wallet and provider information
    return { selectedAccount, provider };
  } catch (error) {
    console.error('Error connecting to wallet:', error.message);
    throw error; // Propagate the error further
  }
}

// Helper function to get the current wallet's network information
async function getNetwork(provider) {
  try {
    if (!provider) {
      throw new Error('Provider is missing. Please ensure the wallet is connected.');
    }

    const network = await provider.getNetwork(); // Get network details
    console.log(`Connected to network: ${network.name} (chainId: ${network.chainId})`);
    return network;
  } catch (error) {
    console.error('Error fetching network information:', error.message);
    throw error; // Propagate the error further
  }
}

// Example usage
async function main() {
  try {
    // Connect wallet and get provider
    const { selectedAccount, provider } = await connectWallet();

    // Display connected wallet address
    console.log(`Wallet address: ${selectedAccount}`);

    // Fetch and display network information
    const network = await getNetwork(provider);
    console.log(`Network name: ${network.name}`);
    console.log(`Network chainId: ${network.chainId}`);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
}

// Call main function to initiate wallet connection
main();

export { connectWallet, getNetwork };
```
