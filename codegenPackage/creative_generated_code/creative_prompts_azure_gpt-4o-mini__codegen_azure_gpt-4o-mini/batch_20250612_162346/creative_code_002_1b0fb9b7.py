"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-srunexyz.pages.dev
Prompt: Create a JavaScript function that calculates the amount of $SRUNE received for a given SOL investment based on the exchange rate of 1 SOL to 99,500 $SRUNE.
Generated: DETERMINISTIC_1b0fb9b759d5d198
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the amount of $SRUNE received for a given SOL investment.
 *
 * @param {number} solInvestment - The amount of SOL to invest.
 * @returns {number} - The amount of $SRUNE received.
 * @throws {Error} - Throws an error if the input is not a positive number.
 */
function calculateSRUNE(solInvestment) {
    // Define the exchange rate from SOL to $SRUNE
    const exchangeRate = 99500;

    // Validate the input to ensure it is a positive number
    if (typeof solInvestment !== 'number' || solInvestment <= 0) {
        throw new Error('Invalid input: solInvestment must be a positive number');
    }

    // Calculate the amount of $SRUNE received
    const sruneReceived = solInvestment * exchangeRate;

    // Return the calculated amount of $SRUNE
    return sruneReceived;
}

// Example usage:
try {
    const solInvestment = 1; // Amount of SOL to invest
    const sruneAmount = calculateSRUNE(solInvestment);
    console.log(`For an investment of ${solInvestment} SOL, you will receive ${sruneAmount} $SRUNE.`);
} catch (error) {
    console.error(error.message);
}
```
