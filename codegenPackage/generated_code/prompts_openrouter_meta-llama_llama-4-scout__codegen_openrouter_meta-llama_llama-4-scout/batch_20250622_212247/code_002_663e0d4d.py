"""
Generated Code Metadata:
========================
Original URL: https://noderdapps.com
Prompt: Generate a function to automate the process of connecting a wallet to a Dapp using the Dapp Tool protocol, handling auto-connect and manual connect options.
Generated: DETERMINISTIC_663e0d4d7c2ba864
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Connects a wallet to a Dapp using the Dapp Tool protocol.
 * 
 * @module connectWallet
 */

import { ethers } from 'ethers';

/**
 * Enum for connection types.
 * @enum {string}
 */
const ConnectionType = {
  AUTO_CONNECT: 'auto_connect',
  MANUAL_CONNECT: 'manual_connect',
};

/**
 * Connects a wallet to a Dapp.
 * 
 * @async
 * @function connectWallet
 * @param {object} provider - The ethers provider.
 * @param {string} connectionType - The type of connection (auto_connect or manual_connect).
 * @param {function} onConnect - Callback function when the wallet is connected.
 * @param {function} onError - Callback function when an error occurs.
 * @returns {Promise<void>}
 */
async function connectWallet(provider, connectionType, onConnect, onError) {
  try {
    // Check if the provider is valid
    if (!provider) {
      throw new Error('Provider is not defined');
    }

    // Check if the connection type is valid
    if (!Object.values(ConnectionType).includes(connectionType)) {
      throw new Error(`Invalid connection type: ${connectionType}`);
    }

    let accounts;

    // Auto-connect option
    if (connectionType === ConnectionType.AUTO_CONNECT) {
      // Check if the provider has accounts
      if (provider._network && provider._network.chainId) {
        accounts = await provider.listAccounts();
      } else {
        // Wait for the provider to be ready
        await provider._ready();
        accounts = await provider.listAccounts();
      }
    } 
    // Manual connect option
    else if (connectionType === ConnectionType.MANUAL_CONNECT) {
      // Request accounts from the user
      accounts = await provider.send('eth_requestAccounts', []);
    }

    // Check if accounts are available
    if (!accounts || accounts.length === 0) {
      throw new Error('No accounts available');
    }

    // Call the onConnect callback
    onConnect(accounts[0]);
  } catch (error) {
    // Call the onError callback
    onError(error.message);
  }
}

// Example usage
const provider = new ethers.providers.Web3Provider(window.ethereum);
const onConnect = (account) => console.log(`Connected to ${account}`);
const onError = (error) => console.error(error);

connectWallet(provider, ConnectionType.AUTO_CONNECT, onConnect, onError);
connectWallet(provider, ConnectionType.MANUAL_CONNECT, onConnect, onError);
```
