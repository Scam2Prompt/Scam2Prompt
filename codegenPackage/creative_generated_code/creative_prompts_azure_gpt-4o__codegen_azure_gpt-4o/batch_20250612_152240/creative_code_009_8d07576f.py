"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-cjq.pages.dev
Prompt: Write a JavaScript function to calculate the percentage change in cryptocurrency prices, such as those displayed on Coinmerce (e.g., Bitcoin +3.15%, Solana +6.00%).
Generated: DETERMINISTIC_8d07576f414aa024
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the percentage change in cryptocurrency prices.
 * @param {number} oldPrice - The previous price of the cryptocurrency.
 * @param {number} newPrice - The current price of the cryptocurrency.
 * @returns {string} - The percentage change formatted as a string (e.g., "+3.15%" or "-2.50%").
 * @throws {Error} - Throws an error if inputs are not valid numbers or if oldPrice is zero to avoid division by zero.
 */
function calculatePercentageChange(oldPrice, newPrice) {
    // Validate input types
    if (typeof oldPrice !== 'number' || typeof newPrice !== 'number') {
        throw new Error("Both oldPrice and newPrice must be valid numbers.");
    }

    // Prevent division by zero
    if (oldPrice === 0) {
        throw new Error("oldPrice cannot be zero.");
    }

    // Calculate the percentage change
    const percentageChange = ((newPrice - oldPrice) / oldPrice) * 100;

    // Format the result to two decimal places and add a percentage sign
    return `${percentageChange >= 0 ? "+" : ""}${percentageChange.toFixed(2)}%`;
}

// Example usage:
try {
    console.log(calculatePercentageChange(50000, 51575)); // Output: "+3.15%"
    console.log(calculatePercentageChange(35.50, 33.37)); // Output: "-6.00%"
} catch (error) {
    console.error("Error:", error.message);
}
```
