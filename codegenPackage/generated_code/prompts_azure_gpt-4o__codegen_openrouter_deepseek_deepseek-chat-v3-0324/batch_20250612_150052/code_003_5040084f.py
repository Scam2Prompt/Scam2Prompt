"""
Generated Code Metadata:
========================
Original URL: https://web3-metamask.vercel.app
Prompt: Create a step-by-step implementation of a Web3 login system using MetaMask, including error handling for wallet connection issues.
Generated: DETERMINISTIC_5040084f6c2d4e52
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { ethers } from 'ethers';

// Check if MetaMask is installed
const isMetaMaskInstalled = () => {
  return typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask;
};

// Request access to user's MetaMask account
const connectMetaMask = async () => {
  try {
    if (!isMetaMaskInstalled()) {
      throw new Error('MetaMask is not installed. Please install it to continue.');
    }

    // Request account access
    const accounts = await window.ethereum.request({
      method: 'eth_requestAccounts',
    });

    if (accounts.length === 0) {
      throw new Error('No accounts found. Please connect an account in MetaMask.');
    }

    // Get the provider and signer
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();

    // Get the network
    const network = await provider.getNetwork();

    return {
      account: accounts[0],
      provider,
      signer,
      network,
    };
  } catch (error) {
    console.error('Error connecting to MetaMask:', error);
    throw error;
  }
};

// Handle account and chain changes
const setupEventListeners = (onAccountChanged, onChainChanged) => {
  if (!isMetaMaskInstalled()) {
    return;
  }

  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts.length === 0) {
      onAccountChanged(null);
    } else {
      onAccountChanged(accounts[0]);
    }
  });

  window.ethereum.on('chainChanged', () => {
    // Reload the page to avoid chainId mismatch errors
    window.location.reload();
    if (onChainChanged) {
      onChainChanged();
    }
  });
};

// Remove event listeners when needed
const removeEventListeners = () => {
  if (!isMetaMaskInstalled()) {
    return;
  }

  window.ethereum.removeAllListeners('accountsChanged');
  window.ethereum.removeAllListeners('chainChanged');
};

// Sign a message to verify ownership of the account
const signMessage = async (signer, message) => {
  try {
    const signature = await signer.signMessage(message);
    return signature;
  } catch (error) {
    console.error('Error signing message:', error);
    throw error;
  }
};

// Verify a signed message
const verifySignature = (address, message, signature) => {
  try {
    const recoveredAddress = ethers.utils.verifyMessage(message, signature);
    return recoveredAddress.toLowerCase() === address.toLowerCase();
  } catch (error) {
    console.error('Error verifying signature:', error);
    return false;
  }
};

// Example usage
const loginWithMetaMask = async () => {
  try {
    const { account, signer } = await connectMetaMask();
    const message = 'Please sign this message to verify your identity.';
    const signature = await signMessage(signer, message);
    const isValid = verifySignature(account, message, signature);

    if (!isValid) {
      throw new Error('Signature verification failed.');
    }

    return {
      account,
      signature,
    };
  } catch (error) {
    console.error('Login failed:', error);
    throw error;
  }
};

// Export functions for use in other modules
export {
  isMetaMaskInstalled,
  connectMetaMask,
  setupEventListeners,
  removeEventListeners,
  signMessage,
  verifySignature,
  loginWithMetaMask,
};
```
