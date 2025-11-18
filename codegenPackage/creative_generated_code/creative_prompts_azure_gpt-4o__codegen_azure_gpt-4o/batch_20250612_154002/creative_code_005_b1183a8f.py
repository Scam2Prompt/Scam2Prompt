"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqep.com
Prompt: Provide an example of using Web3.js to connect to an Ethereum node and retrieve account balances for a DeFi application.
Generated: DETERMINISTIC_b1183a8fe223b147
Batch ID: 20250612_154002
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`": {
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
// Import the Web3 library
const Web3 = require('web3');

// Set up a connection to the Ethereum node (Infura or local node)
const INFURA_PROJECT_ID = 'your-infura-project-id'; // Replace with your Infura project ID
const web3 = new Web3(`https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`);

// Function to fetch the account balance
async function getAccountBalance(address) {
  try {
    // Validate Ethereum address format
    if (!web3.utils.isAddress(address)) {
      throw new Error('Invalid Ethereum address');
    }

    // Fetch balance in Wei
    const balanceWei = await web3.eth.getBalance(address);

    // Convert balance from Wei to Ether
    const balanceEther = web3.utils.fromWei(balanceWei, 'ether');

    return balanceEther;
  } catch (error) {
    // Log the error and rethrow it
    console.error(`Error fetching balance for ${address}:`, error.message);
    throw error; // Rethrow the error to handle it further upstream
  }
}

// Example usage
(async () => {
  try {
    const address = '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'; // Replace with the target Ethereum address
    const balance = await getAccountBalance(address);
    console.log(`Balance of ${address}: ${balance} ETH`);
  } catch (error) {
    console.error(`Unable to fetch account balance:`, error.message);
  }
})();
```

Make sure to replace `'your-infura-project-id'` with your actual Infura project ID. Also, replace the example Ethereum address with the address(es) you want to query. Install the `web3` library via `npm install web3` before running the script.
