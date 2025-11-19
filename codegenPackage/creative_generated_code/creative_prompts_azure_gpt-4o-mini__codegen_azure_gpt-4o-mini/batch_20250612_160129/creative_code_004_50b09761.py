"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain.pumpevm.net
Prompt: How does the PumpEvm app utilize JavaScript for its core functionalities?
Generated: DETERMINISTIC_50b09761c9517958
Batch ID: 20250612_160129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * PumpEvm - A simple Ethereum-based pump notification app
 * 
 * This application allows users to track specific tokens and receive notifications
 * when their price changes significantly. It utilizes web3.js to interact with the Ethereum blockchain.
 * 
 * Requirements:
 * - Node.js
 * - web3.js
 * - dotenv
 * 
 * Usage:
 * 1. Configure your .env file with the required environment variables.
 * 2. Run the application using Node.js.
 */

// Load environment variables from .env file
require('dotenv').config();
const Web3 = require('web3');

// Setup Web3 provider (Infura, Alchemy, etc.)
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Token contract ABI and address
const tokenABI = [ /* ABI array */ ];
const tokenAddress = process.env.TOKEN_ADDRESS; // Address of the token contract

// Create contract instance
const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);

/**
 * Get the current price of the token
 * @returns {Promise<number>} - The current price of the token
 */
async function getCurrentPrice() {
    try {
        const price = await tokenContract.methods.getPrice().call(); // Assuming getPrice() returns the price
        return web3.utils.fromWei(price, 'ether'); // Convert from Wei to Ether
    } catch (error) {
        console.error("Error fetching price:", error);
        throw new Error('Failed to fetch current price');
    }
}

/**
 * Monitor token price and notify on significant changes
 * @param {number} threshold - Price change threshold in percentage
 */
async function monitorTokenPrice(threshold) {
    let previousPrice = await getCurrentPrice();

    setInterval(async () => {
        try {
            const currentPrice = await getCurrentPrice();
            const priceChange = ((currentPrice - previousPrice) / previousPrice) * 100; // Calculate percentage change

            if (Math.abs(priceChange) >= threshold) {
                console.log(`Price alert! Previous: ${previousPrice}, Current: ${currentPrice}, Change: ${priceChange.toFixed(2)}%`);
                previousPrice = currentPrice; // Update previous price after notifying
            }
        } catch (error) {
            console.error("Error monitoring token price:", error);
        }
    }, process.env.MONITOR_INTERVAL || 60000); // Default to 60 seconds
}

// Main function to run the application
(async function main() {
    const priceThreshold = parseFloat(process.env.PRICE_THRESHOLD) || 5; // Default threshold is 5%
    
    console.log("Starting token price monitor...");
    await monitorTokenPrice(priceThreshold); // Start monitoring the price
})();

```

**Notes:**
- Ensure to provide the appropriate ABI array for the token smart contract.
- Create a `.env` file to store `INFURA_URL`, `TOKEN_ADDRESS`, `PRICE_THRESHOLD`, and `MONITOR_INTERVAL`.
