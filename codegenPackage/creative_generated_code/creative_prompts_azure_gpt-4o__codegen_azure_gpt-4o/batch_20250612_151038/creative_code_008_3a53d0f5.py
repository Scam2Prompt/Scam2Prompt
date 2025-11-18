"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://or-22s.pages.dev
Prompt: Using the $ENTS contract address, write a script to monitor token transactions and log them in real-time using ethers.js.
Generated: DETERMINISTIC_3a53d0f5b6fd95fe
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers"); // Ethers.js library for interacting with the blockchain
const fs = require("fs"); // File system module for logging transactions

// Configuration
const INFURA_PROJECT_ID = "your_infura_project_id"; // Replace with your Infura Project ID
const NETWORK = "mainnet"; // Ethereum network to connect to
const ENTS_CONTRACT_ADDRESS = "0xYour_ENTS_Contract_Address"; // Replace with the $ENTS contract address
const LOG_FILE = "transactions.log"; // File where transactions will be logged

// Initialize provider (Infura)
const provider = new ethers.providers.InfuraProvider(NETWORK, INFURA_PROJECT_ID);

// ABI (Application Binary Interface) for ERC-20 token standard
const ERC20_ABI = [
  "event Transfer(address indexed from, address indexed to, uint256 value)"
];

// Initialize contract instance
const entsContract = new ethers.Contract(ENTS_CONTRACT_ADDRESS, ERC20_ABI, provider);

// Function to log transactions to a file
function logTransaction(transaction) {
  const logEntry = `${new Date().toISOString()} | From: ${transaction.from} | To: ${transaction.to} | Value: ${transaction.value.toString()}\n`;

  // Append transaction log to the file
  fs.appendFile(LOG_FILE, logEntry, (err) => {
    if (err) {
      console.error("Error writing to log file:", err);
    }
  });
}

// Function to monitor token transactions
function monitorTransactions() {
  console.log(`Monitoring $ENTS token transactions on address: ${ENTS_CONTRACT_ADDRESS}`);

  // Listen for "Transfer" events
  entsContract.on("Transfer", (from, to, value, event) => {
    // Log the transaction details
    console.log("New transaction detected:");
    console.log(`  From: ${from}`);
    console.log(`  To: ${to}`);
    console.log(`  Value: ${ethers.utils.formatUnits(value, 18)} $ENTS`);

    // Create a transaction object
    const transaction = {
      from,
      to,
      value
    };

    // Log the transaction to the file
    logTransaction(transaction);
  });
}

// Error handling for provider
provider.on("error", (error) => {
  console.error("Provider error:", error);
});

// Start monitoring transactions
monitorTransactions();
```
