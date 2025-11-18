"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vestings-scapesmania.pages.dev
Prompt: Create a script using Web3.js or ethers.js to facilitate the public sale of $MANIA tokens, ensuring compliance with ScapesMania's vesting schedule.
Generated: DETERMINISTIC_d69f8e30bda13b6a
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const ethers = require('ethers');

// Define constants
const TOKEN_ADDRESS = '0xYourTokenAddress'; // Replace with the actual token contract address
const SALE_CONTRACT_ADDRESS = '0xYourSaleContractAddress'; // Replace with the public sale contract address
const VESTING_START_TIMESTAMP = 1635681600; // Example timestamp for vesting start
const VESTING_DURATION = 31536000; // Vesting duration in seconds (1 year)
const AMOUNT_PER_PURCHASE = ethers.utils.parseUnits('100', 18); // Amount of tokens to purchase

// Set up provider and signer
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID'); // Replace with your Infura project ID
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider); // Replace with your wallet private key

// Create contract instances
const tokenContract = new ethers.Contract(TOKEN_ADDRESS, [
    // Minimal ABI for ERC20 token
    'function transfer(address to, uint amount)',
], wallet);

const saleContract = new ethers.Contract(SALE_CONTRACT_ADDRESS, [
    // Minimal ABI for the sale contract
    'function buyTokens(uint256 amount)',
], wallet);

/**
 * Function to purchase $MANIA tokens
 */
async function purchaseTokens() {
    try {
        // Get the current timestamp
        const currentTimestamp = Math.floor(Date.now() / 1000);

        // Check if the vesting period is active
        if (currentTimestamp < VESTING_START_TIMESTAMP) {
            throw new Error('Vesting period has not started yet.');
        }

        // Calculate tokens to purchase based on the vesting schedule
        const elapsedTime = currentTimestamp - VESTING_START_TIMESTAMP;
        const vestingPercentage = Math.min(elapsedTime / VESTING_DURATION, 1);
        const allowableTokens = AMOUNT_PER_PURCHASE.mul(vestingPercentage);

        // Execute the purchase
        console.log(`Attempting to purchase ${ethers.utils.formatUnits(allowableTokens, 18)} $MANIA tokens...`);
        
        const tx = await saleContract.buyTokens(allowableTokens);
        
        // Wait for the transaction to be confirmed
        await tx.wait();
        console.log(`Successfully purchased ${ethers.utils.formatUnits(allowableTokens, 18)} $MANIA tokens!`);
    } catch (error) {
        console.error('Error purchasing tokens:', error.message);
    }
}

// Execute the purchase function
purchaseTokens();
```

Make sure to fill in the necessary addresses and credentials before running the script. Don't forget to install ethers.js with `npm install ethers` if you haven't already.
