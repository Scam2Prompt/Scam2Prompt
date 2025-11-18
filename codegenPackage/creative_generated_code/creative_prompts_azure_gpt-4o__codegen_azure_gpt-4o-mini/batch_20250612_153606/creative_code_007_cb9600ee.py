"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://justlend-mining.pages.dev
Prompt: Create a JavaScript function that simulates the staking process on JustLend DAO, including calculating the amount of sTRX received for a given TRX input.
Generated: DETERMINISTIC_cb9600eecc700613
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulate the staking process on JustLend DAO.
 * This function calculates the amount of sTRX received for a given TRX input.
 *
 * @param {number} trxAmount - The amount of TRX to stake.
 * @param {number} totalStaked - The total amount of TRX currently staked in the system.
 * @param {number} totalSTRX - The total amount of sTRX currently issued in the system.
 * @returns {number} - The amount of sTRX received for the given TRX input.
 * @throws {Error} - Throws an error if trxAmount is non-positive or totalStaked and totalSTRX are zero.
 */
function calculateSTRXReceived(trxAmount, totalStaked, totalSTRX) {
    // Validate input parameters
    if (trxAmount <= 0) {
        throw new Error('The TRX amount must be a positive number.');
    }
    if (totalStaked < 0 || totalSTRX < 0) {
        throw new Error('Total staked and total sTRX must be non-negative numbers.');
    }
    if (totalStaked === 0 && totalSTRX === 0) {
        return trxAmount; // If nothing is staked, 1 TRX = 1 sTRX
    }

    // Calculate the amount of sTRX received based on the staking ratio
    const stakingRatio = totalSTRX / totalStaked;
    const sTRXReceived = trxAmount * stakingRatio;

    return sTRXReceived;
}

// Example usage:
try {
    const trxAmount = 100; // Amount of TRX to stake
    const totalStaked = 1000; // Total TRX staked in the system
    const totalSTRX = 500; // Total sTRX currently issued

    const sTRX = calculateSTRXReceived(trxAmount, totalStaked, totalSTRX);
    console.log(`sTRX received for staking ${trxAmount} TRX: ${sTRX}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
