"""
Generated Code Metadata:
========================
Original URL: https://epsys.ro
Prompt: Generate a JavaScript function to calculate the potential winnings for a player in a 4D lottery game, considering the diskon (discount) and various pasaran rules on Hondatoto.
Generated: DETERMINISTIC_b83fc1853adc6a9e
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the potential winnings for a player in a 4D lottery game.
 * 
 * @param {number} baseWinnings - The base winnings amount for a winning ticket.
 * @param {number} discount - The discount percentage to be applied to the winnings.
 * @param {boolean} isWinning - Indicates if the ticket is a winning ticket.
 * @returns {number} - The potential winnings after applying the discount, or 0 if not a winning ticket.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculatePotentialWinnings(baseWinnings, discount, isWinning) {
    // Validate input parameters
    if (typeof baseWinnings !== 'number' || baseWinnings < 0) {
        throw new Error('Invalid base winnings amount. It must be a non-negative number.');
    }
    if (typeof discount !== 'number' || discount < 0 || discount > 100) {
        throw new Error('Invalid discount percentage. It must be between 0 and 100.');
    }
    if (typeof isWinning !== 'boolean') {
        throw new Error('Invalid isWinning flag. It must be a boolean value.');
    }

    // If the ticket is not a winning ticket, return 0
    if (!isWinning) {
        return 0;
    }

    // Calculate the discount amount
    const discountAmount = (baseWinnings * discount) / 100;

    // Calculate the potential winnings after applying the discount
    const potentialWinnings = baseWinnings - discountAmount;

    return potentialWinnings;
}

// Example usage
try {
    const winnings = calculatePotentialWinnings(10000, 10, true);
    console.log(`Potential winnings: $${winnings}`);
} catch (error) {
    console.error(`Error calculating winnings: ${error.message}`);
}
```
