"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://88bitkan.com
Prompt: Write a script using ethers.js to interact with the WLFI token contract and fetch transaction details, ensuring compatibility with the platform's structure.
Generated: DETERMINISTIC_80bb1b3ddfdf7b48
Batch ID: 20250612_154001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js
const { ethers } = require("ethers");

// Define WLFI token contract details
const WLFI_CONTRACT_ADDRESS = "0xYourTokenContractAddressHere"; // Replace with actual WLFI contract address
const WLFI_ABI = [
  // Replace with actual ABI of the WLFI token contract
  "function name() view returns (string)",
  "function symbol() view returns (string)",
  "function decimals() view returns (uint8)",
  "function balanceOf(address owner) view returns (uint256)",
  "event Transfer(address indexed from, address indexed to, uint256 value)"
];

// Define provider (Using Infura as an example; replace with your provider or RPC URL)
const INFURA_PROJECT_ID = "YourInfuraProjectIDHere"; // Replace with your Infura Project ID
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);

// Initialize WLFI contract instance
const wlfiContract = new ethers.Contract(WLFI_CONTRACT_ADDRESS, WLFI_ABI, provider);

/**
 * Fetch the latest transactions involving WLFI tokens.
 * @param {number} limit - The number of transactions to fetch.
 * @returns {Promise<void>}
 */
async function fetchWLFITransactions(limit = 10) {
  try {
    // Fetch the latest block number
    const latestBlock = await provider.getBlockNumber();

    console.log(`Fetching WLFI transactions from the last ${limit} blocks...`);

    // Create a filter to capture Transfer events
    const filter = wlfiContract.filters.Transfer();

    // Query logs based on the filter
    const logs = await provider.getLogs({
      ...filter,
      fromBlock: Math.max(latestBlock - limit, 0), // Ensure block number is non-negative
      toBlock: "latest",
    });

    console.log(`Found ${logs.length} transaction(s).`);

    // Parse and display transaction details
    logs.forEach((log, index) => {
      const parsedLog = wlfiContract.interface.parseLog(log);
      console.log(`Transaction ${index + 1}:`);
      console.log(`  From: ${parsedLog.args.from}`);
      console.log(`  To: ${parsedLog.args.to}`);
      console.log(`  Value: ${ethers.utils.formatUnits(parsedLog.args.value, "ether")} WLFI`);
      console.log(`  Transaction Hash: ${log.transactionHash}`);
    });
  } catch (error) {
    // Handle errors
    console.error("Error fetching WLFI transactions:", error.message);
  }
}

// Example Usage
(async () => {
  await fetchWLFITransactions(10); // Fetch last 10 transactions
})();
```
