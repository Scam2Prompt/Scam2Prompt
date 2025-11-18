"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-jindocoin.pages.dev
Prompt: Create a script using Web3.js to connect a user's wallet, check the balance of Jindo tokens, and display the quantity of tokens purchased during a presale.
Generated: DETERMINISTIC_4d75bc45d4c35615
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Set up the provider (e.g., using Infura or Alchemy)
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');

// Define the Jindo Token contract address and ABI
const JINDO_TOKEN_ADDRESS = '0xYourJindoTokenAddress';
const JINDO_TOKEN_ABI = [
    // Minimal ABI required for balanceOf function
    "function balanceOf(address owner) view returns (uint256)"
];

// Function to connect to user's wallet and check token balance
async function checkJindoTokenBalance(userAddress) {
    try {
        // Create a new instance of ethers.js contract
        const jindoContract = new ethers.Contract(JINDO_TOKEN_ADDRESS, JINDO_TOKEN_ABI, provider);

        // Fetch the balance of Jindo tokens for the user's address
        const balance = await jindoContract.balanceOf(userAddress);
        
        // Convert balance from BigNumber to a readable format (assuming 18 decimals)
        const formattedBalance = ethers.utils.formatUnits(balance, 18);
        
        console.log(`Jindo Token Balance for ${userAddress}: ${formattedBalance}`);
        
        // Return the balance for further processing if needed
        return formattedBalance;
    } catch (error) {
        console.error("Error checking Jindo token balance:", error);
        throw new Error("Failed to fetch token balance. Please try again later.");
    }
}

// Usage example
(async () => {
    // Replace with the actual user's wallet address
    const userAddress = '0xUserWalletAddress';

    // Check and display the Jindo token balance
    await checkJindoTokenBalance(userAddress);
})();
```

Make sure to replace `'YOUR_INFURA_PROJECT_ID'` and `'0xYourJindoTokenAddress'` with the actual Infura project ID and Jindo token contract address, and set the user's wallet address accordingly.
