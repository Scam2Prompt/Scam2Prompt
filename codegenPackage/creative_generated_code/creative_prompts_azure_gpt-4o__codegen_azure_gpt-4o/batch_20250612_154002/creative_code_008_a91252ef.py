"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqwp.com
Prompt: Write a script to monitor Ethereum blockchain events, such as token transfers or liquidity pool updates, using JavaScript.
Generated: DETERMINISTIC_a91252ef69671ba9
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
// Import required libraries
const Web3 = require('web3');

// Constants
const INFURA_PROJECT_ID = 'your_infura_project_id'; // Replace with your Infura Project ID
const CONTRACT_ADDRESS = '0xYourContractAddress'; // Replace with the contract you want to monitor
const ABI = [/* Contract ABI goes here */]; // Replace with the ABI of the contract

// Initialize Web3
const web3 = new Web3(`https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`);

// Create contract instance
const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);

// Function to monitor 'Transfer' events (example for ERC-20 token transfers)
const monitorTransferEvents = () => {
  console.log('Listening for Transfer events...');

  try {
    contract.events.Transfer({
      fromBlock: 'latest' // Listen from the latest block
    })
    .on('data', event => {
      console.log('Transfer Event Detected:');
      console.log(`From: ${event.returnValues.from}`);
      console.log(`To: ${event.returnValues.to}`);
      console.log(`Value: ${event.returnValues.value}`);
      console.log(`Transaction Hash: ${event.transactionHash}`);
    })
    .on('error', error => {
      console.error('Error listening for Transfer events:', error.message);
    });
  } catch (error) {
    console.error('Failed to set up event listener:', error.message);
  }
};

// Function to monitor all events from a contract
const monitorAllEvents = () => {
  console.log('Listening for all events...');
  
  try {
    contract.events.allEvents({
      fromBlock: 'latest' // Listen from the latest block
    })
    .on('data', event => {
      console.log('Event Detected:', event.event);
      console.log('Event Data:', event.returnValues);
      console.log(`Transaction Hash: ${event.transactionHash}`);
    })
    .on('error', error => {
      console.error('Error listening for events:', error.message);
    });
  } catch (error) {
    console.error('Failed to set up event listener:', error.message);
  }
};

// Main function
const main = () => {
  console.log('Ethereum Event Monitor Started');
  
  // Start monitoring events
  monitorTransferEvents(); // Example: Monitor 'Transfer' events
  monitorAllEvents(); // Monitor all events
};

// Run the script
main();
```

- Replace `your_infura_project_id` with your actual Infura project ID.
- Replace `0xYourContractAddress` with the address of the contract you want to monitor.
- Replace the `ABI` array with the actual ABI of the contract. You can obtain the ABI from the contract source code or tools like Etherscan.

Make sure you install the `web3` library via npm before running the script:

```bash
npm install web3
```
