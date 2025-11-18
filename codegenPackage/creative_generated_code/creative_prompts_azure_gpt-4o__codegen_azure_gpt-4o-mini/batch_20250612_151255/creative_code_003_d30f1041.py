"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethoq.xyz
Prompt: Provide an example of querying Ethereum blockchain data for DeFi transactions using Web3.js or Ethers.js.
Generated: DETERMINISTIC_d30f1041c5c7c315
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const { ethers } = require("ethers");

// Define the provider to connect to the Ethereum network
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');

// Define the address of the DeFi contract (example: Uniswap V2)
const deFiContractAddress = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6'; // Uniswap V2 Router

// Define the ABI for the DeFi contract to interact with (simplified for example)
const deFiContractABI = [
    "event Swap(address indexed sender, uint amountIn, uint amountOut, address indexed to)",
    "function getPair(address tokenA, address tokenB) external view returns (address pair)",
];

// Create a contract instance
const deFiContract = new ethers.Contract(deFiContractAddress, deFiContractABI, provider);

// Function to fetch recent swap events from the DeFi contract
async function fetchRecentSwaps(fromBlock, toBlock) {
    try {
        // Define the filter for the Swap event
        const filter = {
            address: deFiContractAddress,
            fromBlock: fromBlock,
            toBlock: toBlock,
            topics: [ethers.utils.id("Swap(address,uint256,uint256,address)")]
        };

        // Fetch the logs for the swap events
        const logs = await provider.getLogs(filter);

        // Parse the logs to readable format
        const swaps = logs.map(log => {
            const parsedLog = deFiContract.interface.parseLog(log);
            return {
                sender: parsedLog.args.sender,
                amountIn: parsedLog.args.amountIn.toString(),
                amountOut: parsedLog.args.amountOut.toString(),
                to: parsedLog.args.to,
                transactionHash: log.transactionHash,
                blockNumber: log.blockNumber,
            };
        });

        // Return the parsed swap events
        return swaps;
    } catch (error) {
        console.error("Error fetching swap events:", error);
        throw new Error("Failed to fetch swap events");
    }
}

// Example usage: Fetch recent swaps from block 15000000 to current block
(async () => {
    const currentBlock = await provider.getBlockNumber();
    const fromBlock = currentBlock - 1000; // Fetch the last 1000 blocks
    try {
        const recentSwaps = await fetchRecentSwaps(fromBlock, currentBlock);
        console.log("Recent Swap Events:", recentSwaps);
    } catch (error) {
        console.error("Error in fetching recent swaps:", error.message);
    }
})();
```

Make sure to replace `'YOUR_INFURA_PROJECT_ID'` with your actual Infura project ID. This code connects to the Ethereum mainnet and retrieves swap events from a DeFi contract like Uniswap V2. It includes error handling and logs any issues that may arise during execution.
