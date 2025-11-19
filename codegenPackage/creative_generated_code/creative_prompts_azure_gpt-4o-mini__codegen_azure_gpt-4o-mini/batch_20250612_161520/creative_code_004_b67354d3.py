"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbot-8m4.pages.dev
Prompt: Create a function in JavaScript that utilizes Bitbot's automated trading tools to manage both small and large investments effectively.
Generated: DETERMINISTIC_b67354d3f989759f
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Bitbot Trading Manager
 * This function automates trading actions based on investment size.
 * It utilizes Bitbot's trading tools to manage both small and large investments.
 * 
 * @param {number} investment - The amount of money to invest.
 * @param {string} asset - The asset to trade (e.g., 'BTC', 'ETH').
 * @throws Will throw an error if the investment amount is negative or if the asset is not valid.
 */

async function manageInvestment(investment, asset) {
    // Validate input parameters
    if (typeof investment !== 'number' || investment < 0) {
        throw new Error('Investment must be a positive number.');
    }
    
    const validAssets = ['BTC', 'ETH', 'LTC', 'XRP']; // List of valid assets
    if (!validAssets.includes(asset)) {
        throw new Error(`Invalid asset. Please choose from the following: ${validAssets.join(', ')}`);
    }

    try {
        // Determine trading strategy based on investment size
        let tradeType;
        if (investment < 1000) {
            tradeType = 'smallInvestment';
        } else {
            tradeType = 'largeInvestment';
        }

        // Execute trading action using Bitbot's API
        const response = await executeTrade(tradeType, investment, asset);
        
        // Log successful trade
        console.log(`Trade successful: ${response.message}. Investment: ${investment} in ${asset}`);
        
        return response.data; // Return trade details
    } catch (error) {
        // Handle specific errors from the trading API
        console.error('Error during trading operation:', error);
        throw new Error('Trading operation failed. Please try again later.');
    }
}

/**
 * Simulated API call to execute a trade based on trade type.
 * This function would normally interact with the Bitbot API.
 * 
 * @param {string} tradeType - Type of trade ('smallInvestment' or 'largeInvestment').
 * @param {number} investment - Amount to invest.
 * @param {string} asset - The asset to trade.
 * @returns {Promise<object>} - Returns a promise that resolves with trade details.
 */

async function executeTrade(tradeType, investment, asset) {
    // This is a mock implementation. Replace with actual API call to Bitbot.
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                message: `${tradeType} executed`,
                data: {
                    tradeId: Math.floor(Math.random() * 100000),
                    asset: asset,
                    investment: investment,
                    timestamp: new Date().toISOString(),
                },
            });
        }, 1000);
    });
}

// Example usage:
// manageInvestment(500, 'BTC').then(console.log).catch(console.error);
```
