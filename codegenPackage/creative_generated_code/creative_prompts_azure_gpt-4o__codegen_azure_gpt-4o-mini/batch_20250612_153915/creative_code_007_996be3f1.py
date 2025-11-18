"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonbrowser.ru
Prompt: Generate code for integrating TON wallet functionality into a web application, including support for Toncoin transactions.
Generated: DETERMINISTIC_996be3f13f205e6c
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for the TON wallet integration
import { TONClient } from 'ton-client-node-js'; // TON Client SDK
import { Api } from 'ton-client-core'; // Core API for TON Client

// Configuration for the TON Client
const clientConfig = {
  network: {
    server: 'net.ton.dev', // TON network server
  },
};

// Initialize the TON Client
const tonClient = new TONClient(clientConfig);

// Function to create a new wallet address
async function createWallet() {
  try {
    const { keys, address } = await tonClient.crypto.generateRandomKeys();
    console.log('Wallet address:', address);
    return { keys, address };
  } catch (error) {
    console.error('Error creating wallet:', error);
    throw new Error('Failed to create wallet');
  }
}

// Function to get the balance of the given wallet address
async function getBalance(address) {
  try {
    const balance = await tonClient.net.query({
      method: 'getAccount',
      params: {
        address: address,
      },
    });
    return balance.balance; // Return the balance in nanoton
  } catch (error) {
    console.error('Error fetching balance:', error);
    throw new Error('Failed to fetch wallet balance');
  }
}

// Function to transfer Toncoin from one wallet to another
async function transferToncoin(senderAddress, senderKeys, recipientAddress, amount) {
  try {
    const transferParams = {
      from: senderAddress,
      to: recipientAddress,
      amount: amount, // Amount in nanoton
      payload: '', // Optional payload
      keys: senderKeys,
    };

    const result = await tonClient.abi.encodeMessage({
      abi: { type: 'Transfer', value: transferParams },
      signer: { type: 'Keys', keys: senderKeys },
    });

    const transaction = await tonClient.net.sendRawTransaction(result);
    console.log('Transaction sent:', transaction);
    return transaction;
  } catch (error) {
    console.error('Error transferring Toncoin:', error);
    throw new Error('Failed to transfer Toncoin');
  }
}

// Example usage
(async () => {
  try {
    // Create a new wallet
    const { keys, address } = await createWallet();

    // Get balance for the new wallet
    const balance = await getBalance(address);
    console.log('Wallet balance:', balance);

    // Transfer Toncoin to another address (replace with actual recipient address and amount)
    const recipientAddress = 'recipient_wallet_address_here';
    const transferAmount = 1000000; // Amount in nanoton (1 TON = 1,000,000,000 nanoton)
    const transaction = await transferToncoin(address, keys, recipientAddress, transferAmount);
    
    console.log('Transaction details:', transaction);
  } catch (error) {
    console.error('Error in example usage:', error.message);
  }
})();
```
