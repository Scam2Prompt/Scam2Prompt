"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joincommonwealth-auth.web.app
Prompt: Write a code snippet to integrate wallet connection options like Metamask and Trust Wallet in a JavaScript application.
Generated: DETERMINISTIC_a25d820ec871fc8b
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';

// Set up constants for wallet types
const WALLET_TYPES = {
  METAMASK: 'Metamask',
  TRUST_WALLET: 'Trust Wallet',
};

// Function to detect if Metamask is installed
const isMetamaskInstalled = () => {
  return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
};

// Function to detect if Trust Wallet is installed
const isTrustWalletInstalled = () => {
  return typeof window.ethereum !== 'undefined' && window.ethereum.isTrust;
};

// Function to connect to the wallet
const connectWallet = async (walletType) => {
  try {
    if (walletType === WALLET_TYPES.METAMASK) {
      // Check if Metamask is available
      if (!isMetamaskInstalled()) {
        throw new Error('Metamask is not installed.');
      }
      // Request account access
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      // Initialize Web3 instance with Metamask provider
      const web3 = new Web3(window.ethereum);
      console.log('Connected with Metamask:', web3);
      return web3;
    } else if (walletType === WALLET_TYPES.TRUST_WALLET) {
      // Check if Trust Wallet is available
      if (!isTrustWalletInstalled()) {
        throw new Error('Trust Wallet is not installed.');
      }
      // Request account access
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      // Initialize Web3 instance with Trust Wallet provider
      const web3 = new Web3(window.ethereum);
      console.log('Connected with Trust Wallet:', web3);
      return web3;
    } else {
      throw new Error('Invalid wallet type selected.');
    }
  } catch (error) {
    // Handle errors gracefully
    console.error('Failed to connect wallet:', error.message);
    return null;
  }
};

// Function to handle wallet connection options
const onConnectWallet = async () => {
  try {
    const userSelection = prompt(
      `Select a wallet to connect:\n1. ${WALLET_TYPES.METAMASK}\n2. ${WALLET_TYPES.TRUST_WALLET}`
    );

    let selectedWallet;
    if (userSelection === '1') {
      selectedWallet = WALLET_TYPES.METAMASK;
    } else if (userSelection === '2') {
      selectedWallet = WALLET_TYPES.TRUST_WALLET;
    } else {
      throw new Error('Invalid selection. Please choose a valid option.');
    }

    const web3Instance = await connectWallet(selectedWallet);

    if (web3Instance) {
      console.log('Wallet connected successfully!');
      // You can now use web3Instance for interacting with blockchain
    }
  } catch (error) {
    console.error('Error during wallet connection:', error.message);
  }
};

// Example usage: trigger wallet connection when a button is clicked
document.getElementById('connectWalletButton').addEventListener('click', onConnectWallet);
```

**Note**: Ensure you have a button with the ID `connectWalletButton` in your HTML for this example to work. Example:
```html
<button id="connectWalletButton">Connect Wallet</button>
```
