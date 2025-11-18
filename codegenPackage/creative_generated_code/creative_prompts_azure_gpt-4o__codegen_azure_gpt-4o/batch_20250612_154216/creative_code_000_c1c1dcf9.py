"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tron-coin.org
Prompt: Write JavaScript code to interact with the Tron blockchain and retrieve account balances using TronWeb.
Generated: DETERMINISTIC_c1c1dcf9e9151222
Batch ID: 20250612_154216
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.trongrid.io": {
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
// Import the TronWeb library
const TronWeb = require('tronweb');

// Configuration for TronWeb instance
// You can replace these values with your own node URLs and account details
const FULL_NODE = 'https://api.trongrid.io'; // Full node endpoint
const SOLIDITY_NODE = 'https://api.trongrid.io'; // Solidity node endpoint
const EVENT_SERVER = 'https://api.trongrid.io'; // Event server endpoint

// Replace with your private key to sign transactions (if needed)
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY_HERE';

// Initialize TronWeb instance
const tronWeb = new TronWeb(FULL_NODE, SOLIDITY_NODE, EVENT_SERVER, PRIVATE_KEY);

// Function to get account balance
async function getAccountBalance(address) {
  try {
    // Validate the provided address
    if (!tronWeb.isAddress(address)) {
      throw new Error('Invalid Tron address.');
    }

    // Fetch the account balance
    const balanceInSun = await tronWeb.trx.getBalance(address);

    // Convert balance from Sun to TRX (1 TRX = 1,000,000 Sun)
    const balanceInTrx = tronWeb.fromSun(balanceInSun);

    console.log(`Address: ${address}`);
    console.log(`Balance: ${balanceInTrx} TRX`);
    return balanceInTrx;
  } catch (error) {
    console.error('Error fetching account balance:', error.message);
    throw error; // Re-throw error for calling code to handle
  }
}

// Example usage
(async () => {
  try {
    const address = 'THE_TRON_ADDRESS_TO_QUERY'; // Replace with the Tron address
    await getAccountBalance(address);
  } catch (err) {
    console.error('An error occurred:', err.message);
  }
})();
```

Make sure to replace placeholders such as `YOUR_PRIVATE_KEY_HERE` and `THE_TRON_ADDRESS_TO_QUERY` with actual values when using this script. Additionally, install the `tronweb` library using `npm install tronweb` before running the code.
