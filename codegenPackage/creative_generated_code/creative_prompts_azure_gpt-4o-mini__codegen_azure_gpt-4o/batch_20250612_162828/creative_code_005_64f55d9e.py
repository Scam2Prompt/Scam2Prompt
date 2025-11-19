"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-compound.com
Prompt: What are the security features of MetaMask, and how can I leverage them in my crypto project?
Generated: DETERMINISTIC_64f55d9eb488be27
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: metaMaskSecurityFeatures.js

/**
 * This script demonstrates how to leverage MetaMask's security features
 * in your crypto project. MetaMask provides secure account management,
 * hardware wallet integrations, and permission systems for dApps. This
 * example includes proper implementation using best practices.
 */

// Import Ethereum provider library
import detectEthereumProvider from '@metamask/detect-provider';

/**
 * Initialize MetaMask and check for availability.
 * @returns {Promise<MetaMask>}
 */
async function initializeMetaMask() {
  // Detect MetaMask provider
  const provider = await detectEthereumProvider();

  if (!provider) {
    throw new Error('MetaMask not installed. Please install MetaMask to use this feature.');
  }

  // Ensure the provider is the MetaMask provider
  if (provider !== window.ethereum) {
    throw new Error('Multiple Ethereum providers detected. Please ensure MetaMask is your primary provider.');
  }

  return provider;
}

/**
 * Request account access securely.
 * @param {Object} provider - MetaMask Ethereum provider.
 * @returns {Promise<Array<String>>} - List of connected accounts.
 */
async function requestAccountAccess(provider) {
  try {
    const accounts = await provider.request({ method: 'eth_requestAccounts' });

    if (!accounts || accounts.length === 0) {
      throw new Error('No accounts found. Ensure you have at least one account in MetaMask.');
    }

    console.log('Connected accounts:', accounts);
    return accounts;
  } catch (error) {
    console.error('Error requesting account access:', error);
    throw new Error('Failed to access accounts. Ensure MetaMask is configured properly.');
  }
}

/**
 * Subscribe to account changes securely.
 * @param {Object} provider - MetaMask Ethereum provider.
 * @param {Function} callback - Callback to handle account changes.
 */
function subscribeToAccountChanges(provider, callback) {
  provider.on('accountsChanged', (accounts) => {
    console.log('Accounts changed:', accounts);
    callback(accounts);
  });
}

/**
 * Subscribe to network changes securely.
 * @param {Object} provider - MetaMask Ethereum provider.
 * @param {Function} callback - Callback to handle network changes.
 */
function subscribeToNetworkChanges(provider, callback) {
  provider.on('chainChanged', (chainId) => {
    console.log('Network changed. New chain ID:', chainId);
    callback(chainId);
  });
}

/**
 * Example usage of MetaMask security features.
 */
(async function main() {
  try {
    // Initialize MetaMask provider
    const provider = await initializeMetaMask();

    // Request account access
    const accounts = await requestAccountAccess(provider);

    // Subscribe to account and network changes
    subscribeToAccountChanges(provider, (newAccounts) => {
      console.log('Updated accounts:', newAccounts);
    });

    subscribeToNetworkChanges(provider, (newChainId) => {
      console.log('Updated network ID:', newChainId);
    });

  } catch (error) {
    console.error('Error initializing MetaMask:', error);
  }
})();

```

This script demonstrates how to integrate MetaMask's security features into a crypto project using JavaScript. It includes error handling, logging, and best practices for using MetaMask's provider APIs.
