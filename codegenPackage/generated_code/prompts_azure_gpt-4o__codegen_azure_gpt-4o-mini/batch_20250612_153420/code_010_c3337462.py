"""
Generated Code Metadata:
========================
Original URL: https://hehe-verse.pages.dev
Prompt: Create a JavaScript function to calculate the amount of $HEHE tokens a user will receive based on their ETH contribution during presale.
Generated: DETERMINISTIC_c3337462a3aea16b
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the amount of $HEHE tokens a user will receive based on their ETH contribution during presale.
 * 
 * @param {number} ethContribution - The amount of ETH contributed by the user.
 * @param {number} tokenRate - The rate of $HEHE tokens per ETH.
 * @returns {number} - The amount of $HEHE tokens the user will receive.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateHeheTokens(ethContribution, tokenRate) {
    // Validate input parameters
    if (typeof ethContribution !== 'number' || typeof tokenRate !== 'number') {
        throw new Error('Both ethContribution and tokenRate must be numbers.');
    }
    if (ethContribution < 0) {
        throw new Error('ETH contribution cannot be negative.');
    }
    if (tokenRate <= 0) {
        throw new Error('Token rate must be greater than zero.');
    }

    // Calculate the amount of $HEHE tokens
    const heheTokens = ethContribution * tokenRate;

    // Return the calculated amount of tokens
    return heheTokens;
}

// Example usage
try {
    const ethContribution = 1.5; // Example ETH contribution
    const tokenRate = 1000; // Example token rate (1000 $HEHE per 1 ETH)
    const tokensReceived = calculateHeheTokens(ethContribution, tokenRate);
    console.log(`You will receive ${tokensReceived} $HEHE tokens.`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
