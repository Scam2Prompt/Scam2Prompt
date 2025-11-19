"""
Generated Code Metadata:
========================
Original URL: https://appmasks.pages.dev
Prompt: Generate code to connect a cryptocurrency wallet to a dApp, enabling users to interact with the platform.
Generated: DETERMINISTIC_6ced043ab1f2103b
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Web3 from 'web3';
import Web3Modal from 'web3modal';
import WalletConnectProvider from '@walletconnect/web3-provider';

// Configuration for Web3Modal
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: 'YOUR_INFURA_PROJECT_ID', // Replace with your Infura Project ID
    }
  }
};

const web3Modal = new Web3Modal({
  cacheProvider: true, // Optional
  providerOptions, // Required
  theme: 'dark', // Optional
});

// Initialize Web3 instance
let web3;
let currentAccount = null;

/**
 * Connect to wallet using Web3Modal
 * @returns {Promise<void>}
 */
async function connectWallet() {
  try {
    const provider = await web3Modal.connect();
    web3 = new Web3(provider);

    // Subscribe to accounts change
    provider.on('accountsChanged', (accounts) => {
      currentAccount = accounts[0];
      console.log(`Account changed to: ${currentAccount}`);
      // Update UI or emit event
    });

    // Subscribe to chainId change
    provider.on('chainChanged', (chainId) => {
      console.log(`Chain changed to: ${chainId}`);
      // Handle chain change (e.g., reload page)
      window.location.reload();
    });

    // Subscribe to provider disconnect
    provider.on('disconnect', (error) => {
      console.log('Provider disconnected', error);
      disconnectWallet();
    });

    // Get current account
    const accounts = await web3.eth.getAccounts();
    currentAccount = accounts[0];
    return currentAccount;

  } catch (error) {
    console.error('Error connecting wallet:', error);
    throw error;
  }
}

/**
 * Disconnect wallet and clean up
 */
function disconnectWallet() {
  if (web3 && web3.currentProvider && web3.currentProvider.close) {
    web3.currentProvider.close();
  }
  web3 = null;
  currentAccount = null;
  web3Modal.clearCachedProvider();
  // Update UI or emit event
}

/**
 * Get current connected account
 * @returns {string|null} Current account address or null if not connected
 */
function getCurrentAccount() {
  return currentAccount;
}

/**
 * Get current chain ID
 * @returns {Promise<number>} Current chain ID
 */
async function getChainId() {
  if (!web3) {
    throw new Error('Web3 not initialized');
  }
  return await web3.eth.getChainId();
}

/**
 * Execute a contract transaction
 * @param {Object} contract - Web3 contract instance
 * @param {string} methodName - Contract method name
 * @param {Array} params - Method parameters
 * @param {Object} options - Transaction options (gas, value, etc.)
 * @returns {Promise<Object>} Transaction receipt
 */
async function executeContractTransaction(contract, methodName, params, options = {}) {
  if (!web3 || !currentAccount) {
    throw new Error('Wallet not connected');
  }

  try {
    const method = contract.methods[methodName](...params);
    const gas = options.gas || await method.estimateGas({ from: currentAccount });
    const tx = await method.send({
      from: currentAccount,
      gas,
      ...options
    });
    return tx;
  } catch (error) {
    console.error('Transaction failed:', error);
    throw error;
  }
}

// Export functions for use in your dApp
export {
  connectWallet,
  disconnectWallet,
  getCurrentAccount,
  getChainId,
  executeContractTransaction
};
```
