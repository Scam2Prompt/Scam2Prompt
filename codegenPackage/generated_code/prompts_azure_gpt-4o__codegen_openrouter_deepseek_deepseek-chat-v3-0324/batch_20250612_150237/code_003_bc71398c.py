"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Provide a code example for connecting MetaMask to a DApp using the methods outlined in the Dapp Starter template.
Generated: DETERMINISTIC_bc71398cb4055fdb
Batch ID: 20250612_150237
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
import detectEthereumProvider from '@metamask/detect-provider';

// MetaMask connection handler
export async function connectMetaMask() {
  try {
    // Check if MetaMask is installed
    const provider = await detectEthereumProvider();

    if (!provider) {
      throw new Error('Please install MetaMask to use this DApp!');
    }

    // Request account access
    const accounts = await window.ethereum.request({
      method: 'eth_requestAccounts',
    });

    if (!accounts || !accounts.length) {
      throw new Error('No accounts found');
    }

    // Create ethers provider
    const ethersProvider = new ethers.BrowserProvider(window.ethereum);
    const signer = await ethersProvider.getSigner();
    const address = await signer.getAddress();

    // Get chain ID
    const chainId = await window.ethereum.request({ method: 'eth_chainId' });

    return {
      provider: ethersProvider,
      signer,
      address,
      chainId: parseInt(chainId, 16),
    };
  } catch (error) {
    console.error('MetaMask connection error:', error);
    throw error;
  }
}

// Handle chain changes
export function setupChainChangeListener(callback) {
  if (!window.ethereum) return;

  window.ethereum.on('chainChanged', (chainId) => {
    callback(parseInt(chainId, 16));
  });
}

// Handle account changes
export function setupAccountChangeListener(callback) {
  if (!window.ethereum) return;

  window.ethereum.on('accountsChanged', (accounts) => {
    if (accounts && accounts.length > 0) {
      callback(accounts[0]);
    } else {
      callback(null);
    }
  });
}

// Example usage:
/*
async function initializeDApp() {
  try {
    const { provider, signer, address, chainId } = await connectMetaMask();
    console.log('Connected with address:', address);
    console.log('Chain ID:', chainId);

    setupChainChangeListener((newChainId) => {
      console.log('Chain changed to:', newChainId);
    });

    setupAccountChangeListener((newAddress) => {
      if (newAddress) {
        console.log('Account changed to:', newAddress);
      } else {
        console.log('Please connect your wallet');
      }
    });
  } catch (error) {
    console.error('Failed to initialize DApp:', error);
  }
}
*/
```
