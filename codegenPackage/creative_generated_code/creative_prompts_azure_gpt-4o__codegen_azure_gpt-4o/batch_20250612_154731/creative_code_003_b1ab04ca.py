"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghsttoken.co
Prompt: Write a code snippet in JavaScript to fetch the total supply of GHST tokens from its Ethereum contract address `0x3F382DbD960E3a9bbCeaE22651E88158d2791550` using Ethers.js.
Generated: DETERMINISTIC_b1ab04caafb6cc04
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers from the Ethers.js library
const { ethers } = require("ethers");

// Define the Ethereum provider (using Infura as an example)
const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");

// GHST token contract address
const ghstContractAddress = "0x3F382DbD960E3a9bbCeaE22651E88158d2791550";

// ERC-20 Token ABI (only the "totalSupply" function is required for this example)
const erc20Abi = [
  "function totalSupply() view returns (uint256)"
];

// Create a contract instance
const ghstContract = new ethers.Contract(ghstContractAddress, erc20Abi, provider);

// Function to fetch the total supply of GHST tokens
const fetchTotalSupply = async () => {
  try {
    // Call the `totalSupply` method on the contract
    const totalSupply = await ghstContract.totalSupply();
    
    // Convert the result from BigNumber to a human-readable format (assuming 18 decimals)
    const totalSupplyFormatted = ethers.utils.formatUnits(totalSupply, 18);

    // Log the total supply to the console
    console.log(`Total Supply of GHST Tokens: ${totalSupplyFormatted}`);
  } catch (error) {
    // Log any errors encountered during the process
    console.error("Error fetching total supply:", error);
  }
};

// Execute the function
fetchTotalSupply();
```

**Note**: Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID to connect to the Ethereum mainnet.
