"""
Generated Code Metadata:
========================
Original URL: https://peaq-network.pages.dev
Prompt: "How can developers use peaq's testnet and krest Block Explorer for testing and debugging their dApps?"
Generated: DETERMINISTIC_c4240a99082de66e
Batch ID: 20250622_210053
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://krest-block-explorer.peaq.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://testnet.peaq.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const axios = require('axios');
const { PeaqTestnet, KrestBlockExplorer } = require('./peaq-libs');

// Set up Peaq testnet and Krest Block Explorer URLs
const peaqTestnetUrl = 'https://testnet.peaq.network';
const krestBlockExplorerUrl = 'https://krest-block-explorer.peaq.network';

/**
 * Initialize Peaq testnet and Krest Block Explorer clients
 */
const peaqTestnet = new PeaqTestnet(peaqTestnetUrl);
const krestBlockExplorer = new KrestBlockExplorer(krestBlockExplorerUrl);

/**
 * Function to test dApp on Peaq testnet
 * @param {string} dAppId - ID of the dApp to test
 * @returns {Promise} Promise resolving to test results
 */
async function testDappOnPeaqTestnet(dAppId) {
  try {
    // Get testnet account balance
    const balance = await peaqTestnet.getAccountBalance(dAppId);
    console.log(`Account balance: ${balance}`);

    // Send test transaction
    const txHash = await peaqTestnet.sendTransaction(dAppId, '0.1');
    console.log(`Transaction hash: ${txHash}`);

    // Verify transaction on Krest Block Explorer
    const tx = await krestBlockExplorer.getTransaction(txHash);
    console.log(`Transaction status: ${tx.status}`);

    return { balance, txHash, txStatus: tx.status };
  } catch (error) {
    console.error('Error testing dApp on Peaq testnet:', error);
    throw error;
  }
}

/**
 * Function to debug dApp using Krest Block Explorer API
 * @param {string} dAppId - ID of the dApp to debug
 * @returns {Promise} Promise resolving to debug results
 */
async function debugDappWithKrestBlockExplorer(dAppId) {
  try {
    // Get dApp's contract code
    const contractCode = await krestBlockExplorer.getContractCode(dAppId);
    console.log(`Contract code: ${contractCode}`);

    // Get dApp's events
    const events = await krestBlockExplorer.getEvents(dAppId);
    console.log(`Events: ${JSON.stringify(events)}`);

    return { contractCode, events };
  } catch (error) {
    console.error('Error debugging dApp with Krest Block Explorer:', error);
    throw error;
  }
}

// Example usage
async function main() {
  const dAppId = 'my-dapp-id';

  try {
    const testResults = await testDappOnPeaqTestnet(dAppId);
    console.log('Test results:', testResults);

    const debugResults = await debugDappWithKrestBlockExplorer(dAppId);
    console.log('Debug results:', debugResults);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
