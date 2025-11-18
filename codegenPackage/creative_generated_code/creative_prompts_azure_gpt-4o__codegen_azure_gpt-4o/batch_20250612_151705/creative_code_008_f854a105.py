"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.org
Prompt: Generate a step-by-step tutorial for integrating deBridge's cross-chain bridging functionality into a Solana-based DeFi protocol.
Generated: DETERMINISTIC_f854a105b9a58a2c
Batch ID: 20250612_151705
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.debridge.finance/v1/transaction/fee": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.debridge.finance/v1/chain/list": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.debridge.finance/v1/transaction/create": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/*
Tutorial: Integrating deBridge's Cross-Chain Bridging Functionality into a Solana-based DeFi Protocol

Below is a step-by-step implementation to integrate deBridge's functionality in JavaScript. 
Ensure you have a Solana wallet and access to deBridge API keys for this integration to work.

Pre-requisites:
1. Install the required dependencies:
   npm install @solana/web3.js axios dotenv

2. Add a .env file to your project with the following constants:
   DEBRIDGE_API_KEY=<your_deBridge_API_key>
   SOLANA_RPC_URL=<your_Solana_RPC_URL>
   WALLET_PRIVATE_KEY=<your_wallet_private_key>
*/

require('dotenv').config();
const { Connection, Keypair, PublicKey, Transaction, SystemProgram } = require('@solana/web3.js');
const axios = require('axios');

// Load environment variables
const DEBRIDGE_API_KEY = process.env.DEBRIDGE_API_KEY;
const SOLANA_RPC_URL = process.env.SOLANA_RPC_URL;
const WALLET_PRIVATE_KEY = process.env.WALLET_PRIVATE_KEY;

// Initialize Solana connection and wallet
const connection = new Connection(SOLANA_RPC_URL, 'confirmed');
const wallet = Keypair.fromSecretKey(Buffer.from(JSON.parse(WALLET_PRIVATE_KEY)));

/*
Step 1: Fetch deBridge-supported chains and tokens
Use deBridge's API to fetch supported chains and token information.
This will help you identify the appropriate destination chain and token for bridging.
*/
async function fetchSupportedChainsAndTokens() {
  try {
    const response = await axios.get('https://api.debridge.finance/v1/chain/list', {
      headers: { Authorization: `Bearer ${DEBRIDGE_API_KEY}` },
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching supported chains and tokens:', error.message);
    throw error;
  }
}

/*
Step 2: Get deBridge fee estimation
Fetch fees required for performing a cross-chain transfer via deBridge.
*/
async function fetchCrossChainTransferFee(sourceChainId, destinationChainId, tokenAddress, amount) {
  try {
    const response = await axios.post(
      'https://api.debridge.finance/v1/transaction/fee',
      {
        sourceChainId,
        destinationChainId,
        tokenAddress,
        amount,
      },
      {
        headers: { Authorization: `Bearer ${DEBRIDGE_API_KEY}` },
      }
    );
    return response.data;
  } catch (error) {
    console.error('Error fetching cross-chain transfer fee:', error.message);
    throw error;
  }
}

/*
Step 3: Execute cross-chain transfer
Construct and send the transaction to deBridge for cross-chain bridging.
*/
async function executeCrossChainTransfer(destinationChainId, tokenAddress, amount, recipientAddress) {
  try {
    const response = await axios.post(
      'https://api.debridge.finance/v1/transaction/create',
      {
        sourceChainId: 101, // Solana chain ID
        destinationChainId,
        tokenAddress,
        amount,
        recipientAddress,
      },
      {
        headers: { Authorization: `Bearer ${DEBRIDGE_API_KEY}` },
      }
    );
    return response.data;
  } catch (error) {
    console.error('Error executing cross-chain transfer:', error.message);
    throw error;
  }
}

/*
Step 4: Submit the signed transaction to Solana blockchain
Sign and send a transaction from the Solana wallet to deBridge's contract.
*/
async function submitTransactionToSolana(amount, recipientAddress) {
  try {
    // Construct the transaction
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: wallet.publicKey,
        toPubkey: new PublicKey(recipientAddress),
        lamports: amount, // Amount in lamports
      })
    );

    // Sign and send the transaction
    const signedTransaction = await connection.sendTransaction(transaction, [wallet]);
    return signedTransaction;
  } catch (error) {
    console.error('Error submitting transaction to Solana blockchain:', error.message);
    throw error;
  }
}

// Example Workflow
(async () => {
  try {
    console.log('Fetching supported chains and tokens...');
    const supportedChainsAndTokens = await fetchSupportedChainsAndTokens();
    console.log('Supported chains and tokens:', supportedChainsAndTokens);

    console.log('Fetching cross-chain transfer fee...');
    const feeData = await fetchCrossChainTransferFee(101, 56, '<token_address>', 1000); // Example values
    console.log('Fee data:', feeData);

    console.log('Executing cross-chain transfer...');
    const transferData = await executeCrossChainTransfer(56, '<token_address>', 1000, '<recipient_address>'); // Example values
    console.log('Transfer data:', transferData);

    console.log('Submitting transaction to Solana blockchain...');
    const transactionId = await submitTransactionToSolana(1000, '<recipient_address>'); // Example value
    console.log('Transaction submitted successfully:', transactionId);
  } catch (error) {
    console.error('Workflow failed:', error.message);
  }
})();

/*
Final Notes:
- Replace placeholder values (<token_address>, <recipient_address>, etc.) with actual values.
- Implement additional validation to ensure proper format for addresses and amounts.
- Use production-grade monitoring and logging for error tracking when deploying to production.
*/
```
