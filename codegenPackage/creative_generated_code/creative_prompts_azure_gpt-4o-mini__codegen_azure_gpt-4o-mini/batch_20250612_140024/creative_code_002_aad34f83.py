"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craves.io
Prompt: Create a function in JavaScript that calculates potential winnings based on Angkah's bonus structure for new members and daily cash back offers.
Generated: DETERMINISTIC_aad34f836071bc1e
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the potential winnings based on Angkah's bonus structure for new members
 * and daily cash back offers.
 * 
 * @param {number} initialDeposit - The initial deposit amount by the new member.
 * @param {number} dailyCashbackRate - The daily cash back rate as a percentage (e.g., 5 for 5%).
 * @param {number} numberOfDays - The number of days the cashback is calculated for.
 * @returns {number} - The total potential winnings including bonuses and cashback.
 * @throws {Error} - Throws an error if any input is invalid (negative values).
 */
function calculatePotentialWinnings(initialDeposit, dailyCashbackRate, numberOfDays) {
    // Validate inputs
    if (initialDeposit < 0) {
        throw new Error("Initial deposit must be a non-negative value.");
    }
    if (dailyCashbackRate < 0 || dailyCashbackRate > 100) {
        throw new Error("Daily cashback rate must be between 0 and 100.");
    }
    if (numberOfDays < 0) {
        throw new Error("Number of days must be a non-negative value.");
    }

    // Calculate the bonus for new members (assuming a fixed bonus structure)
    const newMemberBonus = initialDeposit * 0.10; // 10% bonus on initial deposit

    // Calculate daily cashback
    const dailyCashback = (initialDeposit * (dailyCashbackRate / 100));
    const totalCashback = dailyCashback * numberOfDays;

    // Calculate total potential winnings
    const totalWinnings = initialDeposit + newMemberBonus + totalCashback;

    return parseFloat(totalWinnings.toFixed(2)); // Return the total winnings rounded to two decimal places
}

// Example usage:
// const winnings = calculatePotentialWinnings(1000, 5, 30);
// console.log("Total Potential Winnings: $" + winnings);
```
