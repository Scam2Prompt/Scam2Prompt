"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Write a function in JavaScript that calculates the total amount of $JESSE tokens received based on the BASE input during the presale.
Generated: DETERMINISTIC_0ed55d22fe6137e0
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
 * Function to calculate the total amount of JESSE tokens received during the presale.
 * 
 * @param {number} baseAmount - The amount of BASE tokens input by the user.
 * @param {number} rate - The exchange rate (BASE to JESSE tokens).
 * @returns {number} - The total JESSE tokens received.
 * @throws Will throw an error if the input is invalid or if the rate is non-positive.
 */
function calculateJesseTokens(baseAmount, rate) {
    // Input validation
    if (typeof baseAmount !== 'number' || baseAmount <= 0) {
        throw new Error("Invalid baseAmount: Must be a positive number.");
    }
    if (typeof rate !== 'number' || rate <= 0) {
        throw new Error("Invalid rate: Must be a positive number.");
    }

    // Calculate JESSE tokens based on the rate
    const jesseTokens = baseAmount * rate;

    // Return result rounded to 6 decimal places for precision
    return parseFloat(jesseTokens.toFixed(6));
}

/**
 * Example Usage:
 */
try {
    const baseInput = 100; // Amount of BASE tokens provided by the user
    const exchangeRate = 2.5; // Exchange rate: 1 BASE = 2.5 JESSE tokens

    const totalJesseTokens = calculateJesseTokens(baseInput, exchangeRate);
    console.log(`Total JESSE tokens received: ${totalJesseTokens}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
