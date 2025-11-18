"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogee1.pages.dev
Prompt: Create a JavaScript function using ethers.js to calculate the amount of DOGE20 tokens a user can purchase during the presale based on their ETH, BNB, or USDT balance.
Generated: DETERMINISTIC_ad845f84bfad6e13
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from ethers.js
const { ethers } = require('ethers');

/**
 * Calculates the amount of DOGE20 tokens a user can purchase during the presale.
 * 
 * @param {string} walletAddress - The wallet address of the user.
 * @param {string} tokenType - Type of token user wants to use for purchase ('ETH', 'BNB', 'USDT').
 * @param {number} tokenPriceInUSD - Price of 1 DOGE20 token in USD during the presale.
 * @param {Object} provider - An ethers.js provider instance (e.g., Infura or Alchemy).
 * @returns {Promise<number>} Amount of DOGE20 tokens the user can purchase.
 */
async function calculateDOGE20Purchase(walletAddress, tokenType, tokenPriceInUSD, provider) {
    try {
        // Validate input parameters
        if (!ethers.utils.isAddress(walletAddress)) {
            throw new Error('Invalid wallet address.');
        }
        if (!['ETH', 'BNB', 'USDT'].includes(tokenType)) {
            throw new Error('Unsupported token type. Valid options are ETH, BNB, or USDT.');
        }
        if (typeof tokenPriceInUSD !== 'number' || tokenPriceInUSD <= 0) {
            throw new Error('Invalid token price. Must be a positive number.');
        }

        let balanceInUSD;

        // Fetch and calculate balance in USD for different token types
        if (tokenType === 'ETH' || tokenType === 'BNB') {
            // Get native currency balance (ETH/BNB)
            const balance = await provider.getBalance(walletAddress);
            const balanceInNative = ethers.utils.formatEther(balance); // Convert balance to a readable format

            // Fetch current price of ETH/BNB in USD using an oracle or external API
            const nativePriceInUSD = await fetchNativeTokenPrice(tokenType); // Replace with an actual API call

            // Calculate balance in USD
            balanceInUSD = balanceInNative * nativePriceInUSD;

        } else if (tokenType === 'USDT') {
            // For USDT, use ERC20 token balance
            const usdtContractAddress = '0xdAC17F958D2ee523a2206206994597C13D831ec7'; // Mainnet USDT address
            const usdtAbi = [
                "function balanceOf(address owner) view returns (uint256)"
            ]; // Minimal ERC20 ABI
            const usdtContract = new ethers.Contract(usdtContractAddress, usdtAbi, provider);

            // Get USDT balance
            const balance = await usdtContract.balanceOf(walletAddress);
            balanceInUSD = parseFloat(ethers.utils.formatUnits(balance, 6)); // USDT uses 6 decimal places
        }

        // Calculate the amount of DOGE20 tokens based on the balance and token price
        const doge20Amount = balanceInUSD / tokenPriceInUSD;

        // Return the amount of DOGE20 tokens the user can purchase
        return doge20Amount;

    } catch (error) {
        // Handle errors gracefully
        console.error('Error calculating DOGE20 purchase:', error.message || error);
        throw error; // Rethrow error for proper error handling in calling code
    }
}

/**
 * Mock function to fetch the price of ETH/BNB in USD.
 * Replace this function with a real implementation using an oracle or external API.
 *
 * @param {string} tokenType - Type of native token ('ETH' or 'BNB').
 * @returns {Promise<number>} Price of the token in USD.
 */
async function fetchNativeTokenPrice(tokenType) {
    // Example hardcoded prices (replace with real API calls)
    const mockPrices = {
        ETH: 1800, // $1,800 per ETH
        BNB: 250   // $250 per BNB
    };

    return mockPrices[tokenType];
}

// Example usage:
// const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');
// calculateDOGE20Purchase('0xYourWalletAddress', 'ETH', 0.002, provider)
//     .then(amount => console.log('DOGE20 tokens purchasable:', amount))
//     .catch(error => console.error('Error:', error));
```
