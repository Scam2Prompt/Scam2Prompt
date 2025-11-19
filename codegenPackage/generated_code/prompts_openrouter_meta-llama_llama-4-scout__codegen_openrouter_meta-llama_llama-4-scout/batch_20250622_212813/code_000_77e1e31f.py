"""
Generated Code Metadata:
========================
Original URL: https://dappsdexprotocols.xyz
Prompt: Write a code snippet to establish a secure connection between a Bitcoin wallet and a dapp using the WalletConnect protocol.
Generated: DETERMINISTIC_77e1e31fd4bb533a
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { WalletConnect } from '@walletconnect/node';
import { Bitcoin } from 'bitcoinjs-lib';

// Define constants
const RELAY_URL = 'wss://relay.walletconnect.org';
const CHAIN_ID = 'bitcoin';

// Initialize WalletConnect
const walletConnect = new WalletConnect({
  bridge: RELAY_URL,
});

// Define a function to establish a connection
async function connectToWallet() {
  try {
    // Check if a session exists
    if (!walletConnect.session) {
      // Create a new session
      await walletConnect.createSession();
    }

    // Handle session request
    walletConnect.on('session_request', (error, payload) => {
      if (error) {
        console.error('Session request error:', error);
      } else {
        console.log('Session request payload:', payload);
      }
    });

    // Handle session update
    walletConnect.on('session_update', (error, payload) => {
      if (error) {
        console.error('Session update error:', error);
      } else {
        console.log('Session update payload:', payload);
      }
    });

    // Handle disconnect
    walletConnect.on('disconnect', (error) => {
      if (error) {
        console.error('Disconnect error:', error);
      } else {
        console.log('Disconnected from wallet');
      }
    });
  } catch (error) {
    console.error('Connection error:', error);
  }
}

// Define a function to request accounts
async function requestAccounts() {
  try {
    // Check if a session exists
    if (walletConnect.session) {
      // Request accounts
      const accounts = await walletConnect.request({
        method: 'eth_accounts',
      });

      console.log('Accounts:', accounts);
    } else {
      console.error('No session exists');
    }
  } catch (error) {
    console.error('Request accounts error:', error);
  }
}

// Define a function to sign a transaction
async function signTransaction() {
  try {
    // Create a sample transaction
    const tx = {
      to: 'bc1p...',
      value: '0.1',
      satoshis: 10000000,
      changeAddress: 'bc1p...',
    };

    // Sign the transaction
    const signedTx = await walletConnect.request({
      method: 'signTransaction',
      params: [tx],
    });

    console.log('Signed transaction:', signedTx);
  } catch (error) {
    console.error('Sign transaction error:', error);
  }
}

// Establish a connection
connectToWallet();

// Request accounts
requestAccounts();

// Sign a transaction
signTransaction();
```
