"""
Generated Code Metadata:
========================
Original URL: https://xrp-mixer.com
Prompt: Create a function in JavaScript that calculates the total amount of XRP sent after applying a random commission fee between 1% and 5%, as described by the XRP mixer service.
Generated: DETERMINISTIC_3c8f3e779ea62621
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total amount of XRP sent after applying a random commission fee.
 * The commission fee is randomly selected between 1% and 5%.
 *
 * @param {number} amount - The initial amount of XRP to be sent.
 * @returns {number} - The total amount of XRP sent after applying the commission fee.
 * @throws {Error} - Throws an error if the input amount is not a positive number.
 */
function calculateXrpSent(amount) {
    // Validate the input amount
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Invalid amount: Amount must be a positive number.');
    }

    // Generate a random commission fee between 1% and 5%
    const commissionPercentage = Math.random() * (0.05 - 0.01) + 0.01;

    // Calculate the commission fee
    const commissionFee = amount * commissionPercentage;

    // Calculate the total amount sent after deducting the commission fee
    const totalSent = amount - commissionFee;

    // Return the total amount sent
    return totalSent;
}

// Example usage
try {
    const initialAmount = 100; // Example initial amount of XRP
    const totalXrpSent = calculateXrpSent(initialAmount);
    console.log(`Total XRP sent after commission: ${totalXrpSent.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
