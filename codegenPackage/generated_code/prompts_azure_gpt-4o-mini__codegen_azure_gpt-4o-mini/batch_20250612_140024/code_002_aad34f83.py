"""
Generated Code Metadata:
========================
Original URL: https://craves.io
Prompt: Create a function in JavaScript that calculates potential winnings based on Angkah's bonus structure for new members and daily cash back offers.
Generated: DETERMINISTIC_aad34f836071bc1e
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential winnings based on Angkah's bonus structure for new members
 * and daily cash back offers.
 * 
 * @param {number} initialDeposit - The initial deposit made by the new member.
 * @param {number} dailyCashBackRate - The daily cash back rate as a percentage (e.g., 5 for 5%).
 * @param {number} days - The number of days the cash back is calculated for.
 * @returns {number} - The total potential winnings including bonuses and cash back.
 * @throws {Error} - Throws an error if any input is invalid (negative values).
 */
function calculatePotentialWinnings(initialDeposit, dailyCashBackRate, days) {
    // Validate inputs
    if (initialDeposit < 0) {
        throw new Error("Initial deposit must be a non-negative number.");
    }
    if (dailyCashBackRate < 0 || dailyCashBackRate > 100) {
        throw new Error("Daily cash back rate must be between 0 and 100.");
    }
    if (days < 0) {
        throw new Error("Number of days must be a non-negative integer.");
    }

    // Calculate the bonus for new members (assumed to be 100% of the initial deposit)
    const bonus = initialDeposit; // 100% bonus on the initial deposit

    // Calculate total cash back over the specified number of days
    const dailyCashBack = (initialDeposit * (dailyCashBackRate / 100));
    const totalCashBack = dailyCashBack * days;

    // Calculate total potential winnings
    const totalWinnings = initialDeposit + bonus + totalCashBack;

    return totalWinnings;
}

// Example usage
try {
    const winnings = calculatePotentialWinnings(1000, 5, 30);
    console.log(`Total potential winnings: $${winnings.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
