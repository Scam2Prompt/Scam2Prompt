"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dai2dai.github.io
Prompt: Using Dai.js, write code to check the balance of Dai stablecoins in a wallet and validate whether the wallet has completed at least 5 transactions in the past 30 days.
Generated: DETERMINISTIC_ba7518a1d90fc8d8
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
const { Maker } = require('@makerdao/dai'); // Dai.js library
const ethers = require('ethers'); // Ether.js library for blockchain interactions

// Function to check Dai balance and validate transaction count
async function checkWallet(walletAddress) {
  try {
    // Validate wallet address
    if (!ethers.utils.isAddress(walletAddress)) {
      throw new Error('Invalid wallet address.');
    }

    // Initialize the Maker instance
    const maker = await Maker.create('mainnet', {
      privateKey: process.env.PRIVATE_KEY, // Replace with your private key or use environment variables
    });

    // Connect to the Ethereum network
    const service = maker.service('token');
    const dai = service.getToken('DAI'); // Get Dai contract instance

    // Fetch Dai balance
    const daiBalance = await dai.balanceOf(walletAddress);

    // Fetch transaction history from etherscan API or another provider
    const etherscanProvider = new ethers.providers.EtherscanProvider(); // Set up Etherscan provider
    const history = await etherscanProvider.getHistory(walletAddress);

    // Filter transactions in the last 30 days
    const thirtyDaysAgo = new Date();
    thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);

    const recentTransactions = history.filter((tx) => {
      const txDate = new Date(tx.timestamp * 1000); // Convert UNIX timestamp to Date
      return txDate >= thirtyDaysAgo;
    });

    // Check transaction count
    const hasCompletedFiveTransactions = recentTransactions.length >= 5;

    // Return results
    return {
      wallet: walletAddress,
      daiBalance: daiBalance.toString(),
      hasCompletedFiveTransactions,
    };
  } catch (error) {
    // Handle errors gracefully
    console.error('Error while checking wallet:', error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const walletAddress = '0xYourWalletAddressHere'; // Replace with the actual wallet address
    const result = await checkWallet(walletAddress);
    console.log('Wallet Details:', result);
  } catch (error) {
    console.error('Failed to fetch wallet details:', error.message);
  }
})();
```
