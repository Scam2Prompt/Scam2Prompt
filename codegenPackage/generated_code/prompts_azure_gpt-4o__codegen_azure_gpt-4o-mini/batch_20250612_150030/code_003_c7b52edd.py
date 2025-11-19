"""
Generated Code Metadata:
========================
Original URL: https://web3-dapp.vercel.app
Prompt: Generate a code snippet to configure Web3Modal with multiple wallet providers in a Web3 application.
Generated: DETERMINISTIC_c7b52eddfd69fad4
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3Modal from 'web3modal';
import { ethers } from 'ethers';

// Define the configuration for the Web3Modal
const providerOptions = {
  // Example provider: WalletConnect
  walletconnect: {
    package: require('@walletconnect/web3-provider'), // Required
    options: {
      infuraId: 'YOUR_INFURA_ID', // Required
    },
  },
  // Example provider: Fortmatic
  fortmatic: {
    package: require('fortmatic'), // Required
    options: {
      key: 'YOUR_FORTMATIC_KEY', // Required
    },
  },
  // Example provider: Portis
  portis: {
    package: require('@portis/web3'), // Required
    options: {
      id: 'YOUR_PORTIS_ID', // Required
    },
  },
  // Add more providers as needed
};

// Create a new instance of Web3Modal
const web3Modal = new Web3Modal({
  cacheProvider: true, // Set to true to cache the provider
  providerOptions, // Pass the provider options
});

// Function to connect to the wallet
async function connectWallet() {
  try {
    // Open the modal to select a wallet provider
    const provider = await web3Modal.connect();
    
    // Create an ethers provider from the selected wallet
    const ethersProvider = new ethers.providers.Web3Provider(provider);
    
    // Get the signer for transactions
    const signer = ethersProvider.getSigner();
    
    // Log the connected account
    const address = await signer.getAddress();
    console.log('Connected account:', address);
    
    // Return the provider and signer for further use
    return { ethersProvider, signer };
  } catch (error) {
    console.error('Failed to connect wallet:', error);
    throw new Error('Wallet connection failed');
  }
}

// Example usage of the connectWallet function
document.getElementById('connectButton').addEventListener('click', async () => {
  try {
    const { ethersProvider, signer } = await connectWallet();
    // You can now use ethersProvider and signer for further interactions
  } catch (error) {
    alert(error.message); // Notify the user of the error
  }
});
```

Make sure to replace `'YOUR_INFURA_ID'`, `'YOUR_FORTMATIC_KEY'`, and `'YOUR_PORTIS_ID'` with your actual keys for the respective wallet providers.
