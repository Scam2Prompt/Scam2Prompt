"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smogtokenairdrop.pages.dev
Prompt: Generate a JavaScript function that calculates the airdrop points based on the number of $SMOG tokens held, as described in the Smog Token documentation.
Generated: DETERMINISTIC_2f62317d91cdb258
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates airdrop points based on the number of $SMOG tokens held.
 * 
 * @param {number} smogTokens - The number of $SMOG tokens held by the user.
 * @returns {number} - The calculated airdrop points.
 * @throws {Error} - Throws an error if the input is not a valid number or is negative.
 */
function calculateAirdropPoints(smogTokens) {
    // Validate input
    if (typeof smogTokens !== 'number') {
        throw new Error('Invalid input: The number of $SMOG tokens must be a number.');
    }
    
    if (smogTokens < 0) {
        throw new Error('Invalid input: The number of $SMOG tokens cannot be negative.');
    }

    // Airdrop points calculation logic based on $SMOG tokens
    let airdropPoints = 0;

    // Define the thresholds and corresponding points
    if (smogTokens >= 1000) {
        airdropPoints = smogTokens * 1.5; // 1.5 points per token for 1000 or more
    } else if (smogTokens >= 500) {
        airdropPoints = smogTokens * 1.2; // 1.2 points per token for 500-999
    } else if (smogTokens >= 100) {
        airdropPoints = smogTokens * 1.1; // 1.1 points per token for 100-499
    } else {
        airdropPoints = smogTokens; // 1 point per token for less than 100
    }

    return airdropPoints;
}

// Example usage:
try {
    const tokensHeld = 750; // Example input
    const points = calculateAirdropPoints(tokensHeld);
    console.log(`Airdrop points for holding ${tokensHeld} $SMOG tokens: ${points}`);
} catch (error) {
    console.error(`Error calculating airdrop points: ${error.message}`);
}
```
