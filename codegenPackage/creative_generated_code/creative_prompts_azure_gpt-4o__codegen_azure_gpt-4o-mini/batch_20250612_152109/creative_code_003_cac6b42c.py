"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-a.pages.dev
Prompt: Create a JavaScript function to calculate the potential returns of DOGE20 tokens based on the presale price of `$0.000158` and a hypothetical future price.
Generated: DETERMINISTIC_cac6b42ca75d96b6
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential returns of DOGE20 tokens.
 * 
 * @param {number} tokens - The number of DOGE20 tokens purchased.
 * @param {number} futurePrice - The hypothetical future price of DOGE20 token in USD.
 * @returns {object} An object containing the initial investment, potential returns, and profit.
 * @throws {Error} Will throw an error if the number of tokens or future price is not a positive number.
 */
function calculateDoge20Returns(tokens, futurePrice) {
    // Define the presale price of DOGE20 token
    const presalePrice = 0.000158; // in USD

    // Input validation
    if (typeof tokens !== 'number' || tokens <= 0) {
        throw new Error("The number of tokens must be a positive number.");
    }
    if (typeof futurePrice !== 'number' || futurePrice <= 0) {
        throw new Error("The future price must be a positive number.");
    }

    // Calculate initial investment
    const initialInvestment = tokens * presalePrice;

    // Calculate potential value at future price
    const potentialValue = tokens * futurePrice;

    // Calculate profit
    const profit = potentialValue - initialInvestment;

    // Return an object with all necessary information
    return {
        initialInvestment: initialInvestment.toFixed(6), // format to 6 decimal places
        potentialValue: potentialValue.toFixed(6),       // format to 6 decimal places
        profit: profit.toFixed(6)                         // format to 6 decimal places
    };
}

// Example usage:
try {
    const result = calculateDoge20Returns(10000, 0.01); // Calculate returns for 10,000 tokens at a future price of $0.01
    console.log(result);
} catch (error) {
    console.error(error.message);
}
```
