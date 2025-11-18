"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmints-6.vercel.app
Prompt: Develop a script using ethers.js to connect to the Ethereum Mainnet, retrieve transaction history for a wallet, and calculate total gas fees spent.
Generated: DETERMINISTIC_d6f44271b6cf4ec8
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
const { ethers } = require("ethers");

// Function to retrieve transaction history and calculate total gas fees
async function calculateTotalGasFees(walletAddress) {
    // Connect to the Ethereum Mainnet using Infura as the provider
    const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");

    try {
        // Fetch transaction history for the given wallet address
        const history = await provider.getHistory(walletAddress);

        // Initialize total gas fee
        let totalGasFees = ethers.BigNumber.from(0);

        // Iterate through each transaction to calculate gas fees
        for (const tx of history) {
            // Calculate gas fee for the transaction
            const gasFee = tx.gasPrice.mul(tx.gasLimit);
            totalGasFees = totalGasFees.add(gasFee);
        }

        // Convert total gas fees to Ether
        const totalGasFeesInEther = ethers.utils.formatEther(totalGasFees);

        console.log(`Total gas fees spent by ${walletAddress}: ${totalGasFeesInEther} ETH`);
    } catch (error) {
        console.error("Error retrieving transaction history:", error.message);
    }
}

// Replace with the wallet address you want to check
const walletAddress = "YOUR_WALLET_ADDRESS";

// Call the function to calculate total gas fees
calculateTotalGasFees(walletAddress);
```
