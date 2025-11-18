"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: Generate a code snippet to configure Web3Modal with multiple wallet providers in a Web3 application.
Generated: DETERMINISTIC_c7b52eddfd69fad4
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3Modal from 'web3modal';
import { ethers } from 'ethers';

// Define the provider options for various wallet providers
const providerOptions = {
  // Example of adding WalletConnect provider
  walletconnect: {
    package: require('@walletconnect/web3-provider'), // Required
    options: {
      infuraId: 'YOUR_INFURA_ID' // Required, use your Infura project ID
    }
  },
  // Example of adding Fortmatic provider
  fortmatic: {
    package: require('fortmatic'), // Required
    options: {
      key: 'YOUR_FORTMATIC_KEY' // Required, use your Fortmatic API key
    }
  },
  // Example of adding MetaMask provider
  metamask: {
    // MetaMask does not require any options
  }
};

// Create a Web3Modal instance
const web3Modal = new Web3Modal({
  cacheProvider: true, // Set to true to cache the provider
  providerOptions // Pass the provider options
});

// Function to connect to the wallet
async function connectWallet() {
  try {
    // Open the modal to select a wallet provider
    const provider = await web3Modal.connect();
    
    // Create an ethers provider instance
    const ethersProvider = new ethers.providers.Web3Provider(provider);

    // Get user's account information
    const signer = ethersProvider.getSigner();
    const address = await signer.getAddress();

    console.log('Connected address:', address);
    return { ethersProvider, signer, address };
  } catch (error) {
    console.error('Could not connect to wallet:', error);
    alert('Failed to connect to wallet. Please try again.');
  }
}

// Example usage: call the connectWallet function
document.getElementById('connectButton').addEventListener('click', connectWallet);
```

Make sure to replace `'YOUR_INFURA_ID'` and `'YOUR_FORTMATIC_KEY'` with your actual Infura project ID and Fortmatic API key, respectively. Additionally, ensure that you have the required packages installed in your project.
