"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-wallet.org
Prompt: Build a JavaScript tool to create a raw Bitcoin transaction and display it, following the example on bitcoin-wallet.org.
Generated: DETERMINISTIC_0f7f663a08e05f2c
Batch ID: 20250612_145917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Bitcoin Raw Transaction Generator
// This script creates a raw Bitcoin transaction using the BitcoinJS library.
// Ensure you have BitcoinJS installed: `npm install bitcoinjs-lib`

const bitcoin = require('bitcoinjs-lib');

// Function to create a raw Bitcoin transaction
function createRawTransaction(senderPrivateKey, recipientAddress, amountSatoshis, inputTxId, inputVout, changeAddress, feeSatoshis) {
  try {
    // Validate input parameters
    if (!senderPrivateKey || !recipientAddress || !changeAddress || !inputTxId || typeof inputVout !== 'number') {
      throw new Error('Missing or invalid input parameters.');
    }
    if (amountSatoshis <= 0 || feeSatoshis <= 0) {
      throw new Error('Amount and fee must be positive integers.');
    }

    // Create a key pair from the sender's private key
    const keyPair = bitcoin.ECPair.fromWIF(senderPrivateKey);

    // Build the transaction
    const txb = new bitcoin.TransactionBuilder();

    // Add input (UTXO)
    txb.addInput(inputTxId, inputVout);

    // Add output (recipient)
    txb.addOutput(recipientAddress, amountSatoshis);

    // Calculate change and add output (change address)
    const changeSatoshis = inputVout - amountSatoshis - feeSatoshis;
    if (changeSatoshis > 0) {
      txb.addOutput(changeAddress, changeSatoshis);
    } else if (changeSatoshis < 0) {
      throw new Error('Insufficient funds to cover amount and fees.');
    }

    // Sign the input with the sender's private key
    txb.sign(0, keyPair);

    // Build and return the raw transaction hex
    const rawTransaction = txb.build().toHex();
    return rawTransaction;
  } catch (err) {
    console.error('Error creating raw transaction:', err.message);
    return null;
  }
}

// Example usage:
// Replace these values with actual data
const senderPrivateKey = 'cR7...'; // Sender's private key in WIF format
const recipientAddress = '1A1z...'; // Recipient's Bitcoin address
const amountSatoshis = 10000; // Amount to send in satoshis
const inputTxId = 'abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890'; // UTXO transaction ID
const inputVout = 0; // UTXO output index
const changeAddress = '1B2x...'; // Sender's change address
const feeSatoshis = 500; // Transaction fee in satoshis

const rawTransactionHex = createRawTransaction(senderPrivateKey, recipientAddress, amountSatoshis, inputTxId, inputVout, changeAddress, feeSatoshis);

if (rawTransactionHex) {
  console.log('Raw Transaction Hex:', rawTransactionHex);
}
```

### Notes:
- Before running this code, ensure you have the `bitcoinjs-lib` package installed using npm.
- Replace placeholder values in the example with actual wallet and transaction data from your setup.
- This code assumes familiarity with Bitcoin principles like UTXOs, addresses, and private keys. Use caution when handling private keys.
