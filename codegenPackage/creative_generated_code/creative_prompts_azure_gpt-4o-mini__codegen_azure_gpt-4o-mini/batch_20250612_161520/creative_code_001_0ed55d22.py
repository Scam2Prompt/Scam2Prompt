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
 * Calculates the total amount of JESSE tokens received based on the BASE input during the presale.
 * 
 * @param {number} baseAmount - The amount of BASE input.
 * @param {number} tokenRate - The conversion rate of BASE to JESSE tokens.
 * @returns {number} - The total amount of JESSE tokens received.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateJesseTokens(baseAmount, tokenRate) {
    // Validate input parameters
    if (typeof baseAmount !== 'number' || typeof tokenRate !== 'number') {
        throw new Error('Both baseAmount and tokenRate must be numbers.');
    }
    if (baseAmount < 0) {
        throw new Error('baseAmount cannot be negative.');
    }
    if (tokenRate <= 0) {
        throw new Error('tokenRate must be a positive number.');
    }

    // Calculate the total amount of JESSE tokens received
    const jesseTokens = baseAmount * tokenRate;

    // Return the calculated amount
    return jesseTokens;
}

// Example usage
try {
    const baseInput = 100; // Example BASE amount
    const rate = 10;       // Example conversion rate
    const totalJesseTokens = calculateJesseTokens(baseInput, rate);
    console.log(`Total JESSE tokens received: ${totalJesseTokens}`);
} catch (error) {
    console.error(`Error calculating JESSE tokens: ${error.message}`);
}
```
