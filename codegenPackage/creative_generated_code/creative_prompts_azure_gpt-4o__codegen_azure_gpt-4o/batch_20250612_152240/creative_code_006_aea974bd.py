"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fight2maga-claimreward.pages.dev
Prompt: Using the $FIGHT token contract address, write a script in Node.js to fetch token details such as name, symbol, and decimals using the Ethereum blockchain.
Generated: DETERMINISTIC_aea974bd1f4f28eb
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const { ethers } = require("ethers");

// Define constants
const INFURA_PROJECT_ID = "your_infura_project_id"; // Replace with your Infura Project ID
const FIGHT_TOKEN_CONTRACT_ADDRESS = "0xYourTokenContractAddress"; // Replace with the $FIGHT token contract address
const ERC20_ABI = [
  // Minimal ABI to interact with an ERC-20 contract
  "function name() view returns (string)",
  "function symbol() view returns (string)",
  "function decimals() view returns (uint8)"
];

// Function to fetch token details
async function fetchTokenDetails() {
  try {
    // Set up an Ethereum provider using Infura
    const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);

    // Create a contract instance for the $FIGHT token
    const fightTokenContract = new ethers.Contract(FIGHT_TOKEN_CONTRACT_ADDRESS, ERC20_ABI, provider);

    // Fetch the token details
    const name = await fightTokenContract.name(); // Token name
    const symbol = await fightTokenContract.symbol(); // Token symbol
    const decimals = await fightTokenContract.decimals(); // Token decimals

    // Log the token details
    console.log("Token Details:");
    console.log(`Name: ${name}`);
    console.log(`Symbol: ${symbol}`);
    console.log(`Decimals: ${decimals}`);
  } catch (error) {
    // Handle errors gracefully
    console.error("Error fetching token details:", error.message);
  }
}

// Execute the function
fetchTokenDetails();
```

### Notes:
- Ensure you replace `your_infura_project_id` with your actual Infura Project ID.
- Replace `0xYourTokenContractAddress` with the actual $FIGHT token contract address.
- Install the required `ethers` package using `npm install ethers` before running the script.
