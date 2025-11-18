"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Write a JavaScript function to calculate the current presale price of $PEPU tokens based on the dynamic price increase mechanism described on the Pepe Unchained website.
Generated: DETERMINISTIC_cf7ac9b31ab7c1f0
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the current presale price of $PEPU tokens based on the dynamic price increase mechanism.
 * The price increases at a fixed interval until it reaches a maximum cap.
 *
 * @param {number} initialPrice - The starting price of the $PEPU token.
 * @param {number} priceIncrease - The amount by which the price increases at each interval.
 * @param {number} maxPrice - The maximum price cap for the $PEPU token.
 * @param {number} startTime - The timestamp when the sale started (in milliseconds).
 * @param {number} interval - The duration of each price increase interval (in milliseconds).
 * @returns {number} - The current presale price of $PEPU tokens.
 */
function calculatePresalePrice(initialPrice, priceIncrease, maxPrice, startTime, interval) {
    try {
        // Validate input parameters
        if (typeof initialPrice !== 'number' || initialPrice < 0) {
            throw new Error('Invalid initial price. It must be a non-negative number.');
        }
        if (typeof priceIncrease !== 'number' || priceIncrease < 0) {
            throw new Error('Invalid price increase. It must be a non-negative number.');
        }
        if (typeof maxPrice !== 'number' || maxPrice < initialPrice) {
            throw new Error('Invalid max price. It must be greater than or equal to the initial price.');
        }
        if (typeof startTime !== 'number' || startTime < 0) {
            throw new Error('Invalid start time. It must be a non-negative timestamp.');
        }
        if (typeof interval !== 'number' || interval <= 0) {
            throw new Error('Invalid interval. It must be a positive number.');
        }

        // Calculate the elapsed time since the sale started
        const currentTime = Date.now();
        const elapsedTime = currentTime - startTime;

        // Determine how many intervals have passed
        const intervalsPassed = Math.floor(elapsedTime / interval);

        // Calculate the new price based on the intervals passed
        let newPrice = initialPrice + intervalsPassed * priceIncrease;

        // Ensure the price does not exceed the maximum price
        if (newPrice > maxPrice) {
            newPrice = maxPrice;
        }

        return newPrice;

    } catch (error) {
        console.error('Error calculating presale price:', error.message);
        return null; // Returning null to signify an error occurred
    }
}

// Example usage
const initialPrice = 0.01; // Initial price of the $PEPU token
const priceIncrease = 0.005; // Price increase per interval
const maxPrice = 0.1; // Maximum price cap
const startTime = Date.now(); // Sale starts now
const interval = 60000; // Price increases every minute

const currentPrice = calculatePresalePrice(initialPrice, priceIncrease, maxPrice, startTime, interval);
console.log(`Current $PEPU Token Price: $${currentPrice.toFixed(3)}`);
```
