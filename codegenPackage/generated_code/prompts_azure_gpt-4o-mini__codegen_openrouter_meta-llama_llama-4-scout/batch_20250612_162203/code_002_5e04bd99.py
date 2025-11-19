"""
Generated Code Metadata:
========================
Original URL: https://lermlinstrate.pages.dev
Prompt: Create a JavaScript function that calculates the token price for $MP in relation to BTC and M-BTC based on the details provided by MerlinSwap.
Generated: DETERMINISTIC_5e04bd997b30d437
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the token price for $MP in relation to BTC and M-BTC based on the details provided by MerlinSwap.
 * 
 * @param {Object} merlinSwapData - Data provided by MerlinSwap.
 * @param {number} merlinSwapData.btcPriceInSats - The current price of BTC in sats.
 * @param {number} merlinSwapData.mpPriceInSats - The current price of $MP in sats.
 * @param {number} [merlinSwapData.mBtcReserve=0] - The reserve of M-BTC.
 * @param {number} [merlinSwapData.mpReserve=0] - The reserve of $MP.
 * 
 * @returns {Object} An object containing the calculated token prices.
 * @returns {number} return.btcPrice - The price of $MP in BTC.
 * @returns {number} return.mBtcPrice - The price of $MP in M-BTC.
 */
function calculateTokenPrice(merlinSwapData) {
    try {
        // Check if required parameters are provided
        if (!merlinSwapData || typeof merlinSwapData.btcPriceInSats !== 'number' || typeof merlinSwapData.mpPriceInSats !== 'number') {
            throw new Error('Invalid MerlinSwap data provided');
        }

        // Calculate $MP price in BTC
        const btcPrice = merlinSwapData.mpPriceInSats / 1e8; // Convert sats to BTC

        // Calculate $MP price in M-BTC
        let mBtcPrice;
        if (merlinSwapData.mBtcReserve > 0 && merlinSwapData.mpReserve > 0) {
            // Use the reserves to calculate the price
            mBtcPrice = merlinSwapData.mpReserve / merlinSwapData.mBtcReserve;
        } else {
            // Default to 1:1 if reserves are not provided
            mBtcPrice = 1;
        }

        return {
            btcPrice,
            mBtcPrice,
        };
    } catch (error) {
        // Log and rethrow the error
        // console.error('Error calculating token price:', error); // Commented out for production
        throw error;
    }
}

// Example usage:
const merlinSwapData = {
    btcPriceInSats: 40000000,
    mpPriceInSats: 200,
    mBtcReserve: 100,
    mpReserve: 500,
};

const tokenPrices = calculateTokenPrice(merlinSwapData);
// console.log('Token prices:', tokenPrices); // Commented out for production
```
