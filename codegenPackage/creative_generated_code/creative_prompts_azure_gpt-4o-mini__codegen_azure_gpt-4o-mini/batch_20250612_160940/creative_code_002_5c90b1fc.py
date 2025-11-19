"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiha7aew6cnrfx323nbkbwheqhy7qp4rdsogs3bqahgzfex7vgmlya.ipfs.dweb.link
Prompt: Create a JavaScript function that calculates the amount of BCKR tokens a user receives based on their ETH contribution during the presale.
Generated: DETERMINISTIC_5c90b1fcbc5ffa36
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the amount of BCKR tokens a user receives based on their ETH contribution.
 * 
 * @param {number} ethContribution - The amount of ETH contributed by the user.
 * @param {number} exchangeRate - The rate of exchange from ETH to BCKR tokens (tokens per ETH).
 * @returns {number} The amount of BCKR tokens the user receives.
 * @throws {Error} If the ethContribution or exchangeRate is not a positive number.
 */
function calculateBCKRTokens(ethContribution, exchangeRate) {
    // Validate input values
    if (typeof ethContribution !== 'number' || typeof exchangeRate !== 'number') {
        throw new Error('Invalid input: ethContribution and exchangeRate must be numbers.');
    }
    if (ethContribution <= 0) {
        throw new Error('Invalid input: ethContribution must be a positive number.');
    }
    if (exchangeRate <= 0) {
        throw new Error('Invalid input: exchangeRate must be a positive number.');
    }

    // Calculate the amount of BCKR tokens
    const bckrTokens = ethContribution * exchangeRate;

    // Return the calculated tokens
    return bckrTokens;
}

// Example usage
try {
    const userEthContribution = 2; // The amount of ETH contributed
    const currentExchangeRate = 1000; // 1000 BCKR tokens per ETH

    const tokensReceived = calculateBCKRTokens(userEthContribution, currentExchangeRate);
    console.log(`The user receives ${tokensReceived} BCKR tokens.`);
} catch (error) {
    console.error(error.message);
}
```
