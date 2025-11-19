"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atocha.io
Prompt: Write a code snippet to integrate the Atocha Web App with a Polkadot JS wallet for puzzle game creation.
Generated: DETERMINISTIC_7ac358a1a5a7cdd8
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import { ApiPromise, WsProvider } from '@polkadot/api';
import { web3Enable, web3Accounts } from '@polkadot/extension-dapp';

// Define constants for connection
const WS_PROVIDER_URL = 'wss://rpc.polkadot.io'; // Replace with Atocha's chain URL if applicable
const ATOCHA_MODULE = 'atochaModule'; // Replace with the actual Atocha module name
const CREATE_PUZZLE_CALL = 'createPuzzle'; // Replace with the actual method name

/**
 * Initialize Polkadot API and connect to the chain
 */
async function initializePolkadotApi() {
  try {
    const provider = new WsProvider(WS_PROVIDER_URL);
    const api = await ApiPromise.create({ provider });
    console.log('Connected to Polkadot network');
    return api;
  } catch (error) {
    console.error('Error while connecting to Polkadot network:', error);
    throw new Error('Failed to initialize Polkadot API');
  }
}

/**
 * Enable Polkadot JS extension and retrieve accounts
 */
async function enablePolkadotExtension() {
  try {
    const extensions = await web3Enable('Atocha Web App');
    if (extensions.length === 0) {
      throw new Error('No Polkadot JS extension found. Please install the extension.');
    }
    console.log('Polkadot JS extension enabled');
    const accounts = await web3Accounts();
    console.log('Accounts retrieved:', accounts);
    return accounts;
  } catch (error) {
    console.error('Error while enabling Polkadot extension:', error);
    throw new Error('Failed to enable Polkadot JS extension');
  }
}

/**
 * Create a puzzle game on the Atocha chain
 * @param {ApiPromise} api - Instance of Polkadot API
 * @param {Object} account - Account object retrieved from Polkadot JS extension
 * @param {string} puzzleData - Puzzle data to be submitted
 */
async function createPuzzle(api, account, puzzleData) {
  try {
    const injector = await web3Enable('Atocha Web App')
      .then((extensions) => extensions[0]?.signer);
    if (!injector) {
      throw new Error('Failed to retrieve injector from Polkadot JS extension');
    }

    // Build the transaction
    const tx = api.tx[ATOCHA_MODULE][CREATE_PUZZLE_CALL](puzzleData);

    // Sign and send the transaction
    const hash = await tx.signAndSend(account.address, { signer: injector });
    console.log('Puzzle created successfully! Transaction hash:', hash.toString());
  } catch (error) {
    console.error('Error while creating puzzle:', error);
    throw new Error('Failed to create puzzle');
  }
}

/**
 * Main function to integrate Atocha Web App with Polkadot JS wallet
 */
async function main() {
  try {
    const api = await initializePolkadotApi();
    const accounts = await enablePolkadotExtension();

    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure your wallet extension has an active account.');
    }

    // Use the first account for this example
    const account = accounts[0];
    const puzzleData = 'Sample Puzzle Data'; // Replace with actual puzzle data to be submitted

    await createPuzzle(api, account, puzzleData);

    console.log('Puzzle creation operation completed.');
  } catch (error) {
    console.error('Error in main function:', error);
  }
}

// Execute the main function
main();
```
