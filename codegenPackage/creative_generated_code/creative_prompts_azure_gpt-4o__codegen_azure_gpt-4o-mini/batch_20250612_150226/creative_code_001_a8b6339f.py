"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://root69.pages.dev
Prompt: Using ethers.js, create a script to connect an Ethereum wallet and retrieve token balances for the CENNZ to Root Network swap process described on root69.pages.dev.
Generated: DETERMINISTIC_a8b6339f2d2cef06
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require('ethers');

// Constants
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const CENNZ_CONTRACT_ADDRESS = '0xCENNZ_CONTRACT_ADDRESS'; // Replace with the actual CENNZ token contract address
const ROOT_NETWORK_CONTRACT_ADDRESS = '0xROOT_NETWORK_CONTRACT_ADDRESS'; // Replace with the actual Root Network contract address

// ABI for ERC20 token to interact with token contracts
const ERC20_ABI = [
    "function balanceOf(address owner) view returns (uint256)",
    "function decimals() view returns (uint8)"
];

// Connect to Ethereum network via Infura
async function connectToNetwork() {
    const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
    return provider;
}

// Get the token balance for a given address
async function getTokenBalance(provider, tokenAddress, walletAddress) {
    try {
        // Create a contract instance
        const tokenContract = new ethers.Contract(tokenAddress, ERC20_ABI, provider);
        
        // Retrieve the balance
        const balance = await tokenContract.balanceOf(walletAddress);
        const decimals = await tokenContract.decimals();
        
        // Convert balance to a human-readable format
        return ethers.utils.formatUnits(balance, decimals);
    } catch (error) {
        console.error(`Error retrieving balance: ${error.message}`);
        throw error; // Rethrow error for further handling if necessary
    }
}

// Main function to execute the script
async function main() {
    // Replace with the wallet address you want to check
    const walletAddress = '0xYOUR_WALLET_ADDRESS'; // Replace with your wallet address

    // Connect to the Ethereum network
    const provider = await connectToNetwork();

    // Fetch and display token balances
    try {
        const cennzBalance = await getTokenBalance(provider, CENNZ_CONTRACT_ADDRESS, walletAddress);
        console.log(`CENNZ Balance: ${cennzBalance}`);
        
        const rootNetworkBalance = await getTokenBalance(provider, ROOT_NETWORK_CONTRACT_ADDRESS, walletAddress);
        console.log(`Root Network Balance: ${rootNetworkBalance}`);
    } catch (error) {
        console.error('Failed to retrieve token balances:', error);
    }
}

// Execute the main function
main().catch((error) => {
    console.error('Error in main function:', error);
});
```

**Note:** 
- Please make sure to replace placeholder values like `YOUR_INFURA_PROJECT_ID`, `0xCENNZ_CONTRACT_ADDRESS`, `0xROOT_NETWORK_CONTRACT_ADDRESS`, and `0xYOUR_WALLET_ADDRESS` with actual values before running the script. 
- Ensure that you have installed the `ethers` library via npm (i.e., `npm install ethers`).
