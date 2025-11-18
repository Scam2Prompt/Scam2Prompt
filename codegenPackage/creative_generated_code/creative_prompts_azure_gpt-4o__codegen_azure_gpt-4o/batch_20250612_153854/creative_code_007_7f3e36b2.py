"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mega-rabbit.com
Prompt: Write a script using ethers.js to query the Ethereum blockchain for details about the MegaRabbit NFT collection, including mint groups and their respective limits.
Generated: DETERMINISTIC_7f3e36b2bc3be30c
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js library
const { ethers } = require("ethers");

// RPC Provider URL (use an Ethereum node provider like Infura or Alchemy)
const RPC_URL = "<YOUR_RPC_PROVIDER_URL>"; // Replace with your Ethereum node provider URL

// MegaRabbit NFT contract address (replace with actual contract address)
const CONTRACT_ADDRESS = "<MEGA_RABBIT_CONTRACT_ADDRESS>"; // Replace with MegaRabbit NFT contract address

// ABI for MegaRabbit NFT contract (replace with actual ABI)
const CONTRACT_ABI = [
  // Add the relevant ABI methods for querying mint groups and their limits.
  "function getMintGroupCount() view returns (uint256)",
  "function getMintGroupDetails(uint256 groupId) view returns (string name, uint256 limit)"
];

// Initialize ethers.js provider and contract instance
async function main() {
  try {
    // Create a provider instance
    const provider = new ethers.JsonRpcProvider(RPC_URL);

    // Create a contract instance
    const megaRabbitContract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, provider);

    console.log("Connected to Ethereum blockchain and MegaRabbit NFT contract.");

    // Query total number of mint groups
    const totalMintGroups = await megaRabbitContract.getMintGroupCount();
    console.log(`Total Mint Groups: ${totalMintGroups}`);

    // Loop through each mint group and fetch details
    for (let i = 0; i < totalMintGroups; i++) {
      const mintGroupDetails = await megaRabbitContract.getMintGroupDetails(i);
      console.log(`Mint Group ${i}:`);
      console.log(`  Name: ${mintGroupDetails.name}`);
      console.log(`  Limit: ${mintGroupDetails.limit}`);
    }

    console.log("Successfully retrieved mint group details.");
  } catch (error) {
    // Handle any errors that occur during execution
    console.error("An error occurred while querying the blockchain:", error.message);
  }
}

// Execute the script
main();
```

Make sure to replace `<YOUR_RPC_PROVIDER_URL>` and `<MEGA_RABBIT_CONTRACT_ADDRESS>` with the appropriate values for your setup. Also, ensure that the ABI matches the actual contract's interface.
