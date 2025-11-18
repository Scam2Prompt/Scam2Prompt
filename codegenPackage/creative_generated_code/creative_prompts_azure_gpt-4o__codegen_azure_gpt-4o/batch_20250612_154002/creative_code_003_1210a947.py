"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqed.com
Prompt: Write a script to fetch real-time data from an Ethereum DeFi protocol using JavaScript and display it on a webpage.
Generated: DETERMINISTIC_1210a94735981c34
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
// We'll use ethers.js for interacting with Ethereum blockchain and its smart contracts
import { ethers } from 'ethers';

// Define constants
const INFURA_PROJECT_ID = 'your-infura-project-id'; // Replace with your Infura Project ID
const PROTOCOL_CONTRACT_ADDRESS = '0xYourProtocolContractAddress'; // Replace with the DeFi protocol's contract address

// ABI (Application Binary Interface) specific to the DeFi protocol's contract
const PROTOCOL_CONTRACT_ABI = [
  // Add the relevant ABI here for the contract methods you need to call
  // For example, if you're calling a method named 'getPoolData':
  {
    "constant": true,
    "inputs": [],
    "name": "getPoolData",
    "outputs": [
      { "name": "totalLiquidity", "type": "uint256" },
      { "name": "poolAPY", "type": "uint256" }
    ],
    "type": "function"
  }
];

// Function to fetch real-time data from the protocol
async function fetchProtocolData() {
  try {
    // Set up a provider using Infura
    const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);

    // Instantiate the protocol contract
    const protocolContract = new ethers.Contract(
      PROTOCOL_CONTRACT_ADDRESS,
      PROTOCOL_CONTRACT_ABI,
      provider
    );

    // Call the contract method to fetch data (assuming getPoolData method exists)
    const poolData = await protocolContract.getPoolData();

    // Process the data (convert BigNumber to readable format)
    const totalLiquidity = ethers.utils.formatEther(poolData.totalLiquidity); // Convert to Ether
    const poolAPY = parseFloat(poolData.poolAPY) / 100; // Assuming APY is returned as a scaled integer

    // Return the processed data
    return { totalLiquidity, poolAPY };
  } catch (error) {
    console.error('Error fetching protocol data:', error);
    throw new Error('Failed to fetch protocol data.');
  }
}

// Function to update the webpage with fetched data
async function updateWebpage() {
  try {
    // Fetch data from the protocol
    const { totalLiquidity, poolAPY } = await fetchProtocolData();

    // Update the DOM with the fetched data
    document.getElementById('totalLiquidity').innerText = `Total Liquidity: ${totalLiquidity} ETH`;
    document.getElementById('poolAPY').innerText = `Pool APY: ${poolAPY}%`;
  } catch (error) {
    // Handle errors gracefully
    document.getElementById('errorMessage').innerText = 'Failed to load data. Please try again later.';
  }
}

// Add event listener to fetch and display data when the page loads
document.addEventListener('DOMContentLoaded', () => {
  updateWebpage();
});

// HTML structure (for reference)
// <div id="app">
//   <p id="totalLiquidity">Loading...</p>
//   <p id="poolAPY">Loading...</p>
//   <p id="errorMessage" style="color: red;"></p>
// </div>
```

**Note:** Make sure to install ethers.js (`npm install ethers`) and replace placeholders like `your-infura-project-id` and `0xYourProtocolContractAddress` with actual values. You'll also need to provide the correct ABI for the DeFi protocol's smart contract you're interacting with.
