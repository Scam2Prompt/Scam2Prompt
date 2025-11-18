"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saita.pages.dev
Prompt: Create a JavaScript function to calculate and display token swap values, including slippage percentage adjustments, as described in the SaitaSwap interface.
Generated: DETERMINISTIC_ee82fd8eb2e3ae11
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the expected output of a token swap given the input amount, 
 * exchange rate, and slippage percentage. 
 * 
 * @param {number} inputAmount - The amount of input tokens to swap.
 * @param {number} exchangeRate - The rate at which input tokens are exchanged for output tokens.
 * @param {number} slippagePercentage - The acceptable slippage percentage for the swap.
 * @returns {Object} An object containing the calculated output value and adjusted output with slippage.
 * @throws {Error} Throws an error if the input values are not valid.
 */
function calculateTokenSwap(inputAmount, exchangeRate, slippagePercentage) {
    // Validate input parameters
    if (typeof inputAmount !== 'number' || inputAmount <= 0) {
        throw new Error('Input amount must be a positive number.');
    }
    if (typeof exchangeRate !== 'number' || exchangeRate <= 0) {
        throw new Error('Exchange rate must be a positive number.');
    }
    if (typeof slippagePercentage !== 'number' || slippagePercentage < 0) {
        throw new Error('Slippage percentage must be a non-negative number.');
    }

    // Calculate the expected output amount before slippage
    const expectedOutput = inputAmount * exchangeRate;

    // Calculate the slippage adjustment
    const slippageAdjustment = (expectedOutput * slippagePercentage) / 100;
    
    // Calculate the final output value considering slippage
    const finalOutput = expectedOutput - slippageAdjustment;

    // Return the results as an object
    return {
        expectedOutput: expectedOutput.toFixed(4), // Round to 4 decimal places for display
        finalOutput: finalOutput.toFixed(4) // Round to 4 decimal places for display
    };
}

/**
 * Displays the results of the token swap calculation in the console.
 * 
 * @param {number} inputAmount - The amount of input tokens to swap.
 * @param {number} exchangeRate - The rate at which input tokens are exchanged for output tokens.
 * @param {number} slippagePercentage - The acceptable slippage percentage for the swap.
 */
function displayTokenSwap(inputAmount, exchangeRate, slippagePercentage) {
    try {
        const result = calculateTokenSwap(inputAmount, exchangeRate, slippagePercentage);
        console.log(`Expected Output: ${result.expectedOutput} tokens`);
        console.log(`Final Output after Slippage: ${result.finalOutput} tokens`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

// Example usage
displayTokenSwap(100, 0.5, 1); // Example input: swapping 100 tokens at an exchange rate of 0.5 with 1% slippage
```
