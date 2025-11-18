"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shiba-3.web.app
Prompt: Develop a Node.js script to subscribe to blockchain events related to Shiba 3.0 token transfers and log transaction details.
Generated: DETERMINISTIC_3ebea1142df2d35a
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const Web3 = require('web3'); // Web3.js library for interacting with blockchain
require('dotenv').config(); // For loading environment variables securely

// Load environment variables
const INFURA_URL = process.env.INFURA_URL; // Infura URL for connecting to an Ethereum node
const SHIBA_3_0_CONTRACT_ADDRESS = process.env.SHIBA_3_0_CONTRACT_ADDRESS; // Address of the Shiba 3.0 token contract
const SHIBA_3_0_ABI = JSON.parse(process.env.SHIBA_3_0_ABI); // ABI definition of the Shiba 3.0 token contract

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Create contract instance
const shibaContract = new web3.eth.Contract(SHIBA_3_0_ABI, SHIBA_3_0_CONTRACT_ADDRESS);

/**
 * Function to handle blockchain events for Shiba 3.0 token transfers.
 */
function subscribeToTokenTransfers() {
  try {
    console.log('Subscribing to Shiba 3.0 token transfer events...');
    
    // Subscribe to Transfer events (standard ERC20 event)
    shibaContract.events.Transfer({
      fromBlock: 'latest' // Start listening from the latest block
    })
    .on('data', (event) => {
      // Log transfer details
      console.log('Token Transfer Event Detected:');
      console.log(`From: ${event.returnValues.from}`);
      console.log(`To: ${event.returnValues.to}`);
      console.log(`Amount: ${web3.utils.fromWei(event.returnValues.value, 'ether')} tokens`);
    })
    .on('error', (error) => {
      // Handle errors gracefully
      console.error('Error while listening to Transfer events:', error);
    });
  } catch (err) {
    // Catch and log initialization errors
    console.error('Error during subscription initialization:', err);
  }
}

// Start the subscription
subscribeToTokenTransfers();
```

### Environment Variables (`.env` file):
```
INFURA_URL=<Your Infura Project URL>
SHIBA_3_0_CONTRACT_ADDRESS=<Shiba 3.0 Contract Address>
SHIBA_3_0_ABI=<Shiba 3.0 Contract ABI JSON>
```

### Notes:
1. Ensure the required libraries are installed using `npm install web3 dotenv`.
2. Replace placeholder values in the `.env` file with actual data (Infura URL, contract address, ABI).
3. Use this script in a secure environment; avoid exposing sensitive information like the Infura URL publicly.
