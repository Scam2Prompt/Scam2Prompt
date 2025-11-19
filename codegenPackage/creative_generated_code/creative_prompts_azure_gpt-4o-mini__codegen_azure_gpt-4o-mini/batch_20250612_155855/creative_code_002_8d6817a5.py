"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: Generate a JavaScript function that calculates the number of BDOGITO tokens received based on the input value during the swap process.
Generated: DETERMINISTIC_8d6817a5b23140d5
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the number of BDOGITO tokens received based on the input value during the swap process.
 * 
 * @param {number} inputValue - The amount of tokens being swapped.
 * @param {number} exchangeRate - The rate at which the input tokens are exchanged for BDOGITO tokens.
 * @returns {number} - The amount of BDOGITO tokens received.
 * @throws {Error} - Throws an error if inputValue or exchangeRate are not positive numbers.
 */
function calculateBDOGITOTokens(inputValue, exchangeRate) {
    // Validate input parameters
    if (typeof inputValue !== 'number' || typeof exchangeRate !== 'number') {
        throw new Error('Both inputValue and exchangeRate must be numbers.');
    }
    
    if (inputValue <= 0) {
        throw new Error('inputValue must be a positive number.');
    }

    if (exchangeRate <= 0) {
        throw new Error('exchangeRate must be a positive number.');
    }

    // Calculate BDOGITO tokens received
    const bdogitoTokens = inputValue * exchangeRate;

    // Return the calculated amount of BDOGITO tokens
    return bdogitoTokens;
}

// Example usage:
try {
    const inputValue = 100; // Amount of tokens being swapped
    const exchangeRate = 1.5; // Rate for the swap
    const receivedTokens = calculateBDOGITOTokens(inputValue, exchangeRate);
    console.log(`BDOGITO tokens received: ${receivedTokens}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
