"""
Generated Code Metadata:
========================
Original URL: https://minerspluslimited.com
Prompt: Create a JavaScript function that calculates potential returns for a user’s investment in the REAL ESTATE PLAN of MINERS PLUS, considering the minimum and maximum deposit amounts.
Generated: DETERMINISTIC_a900121744d688c9
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential returns for a user's investment in the REAL ESTATE PLAN of MINERS PLUS.
 * 
 * @param {number} depositAmount The amount deposited by the user.
 * @param {number} [minDeposit=1000] The minimum deposit amount. Defaults to 1000.
 * @param {number} [maxDeposit=100000] The maximum deposit amount. Defaults to 100000.
 * @param {number} [interestRate=0.05] The interest rate. Defaults to 0.05.
 * @returns {object} An object containing the calculated returns and a success message.
 */
function calculateInvestmentReturns(depositAmount, minDeposit = 1000, maxDeposit = 100000, interestRate = 0.05) {
    try {
        // Check if deposit amount is within the allowed range
        if (depositAmount < minDeposit || depositAmount > maxDeposit) {
            throw new Error(`Deposit amount must be between ${minDeposit} and ${maxDeposit}.`);
        }

        // Calculate the potential returns
        const returns = depositAmount * interestRate;

        // Return an object with the calculated returns and a success message
        return {
            success: true,
            message: 'Returns calculated successfully.',
            returns: returns,
            depositAmount: depositAmount,
            interestRate: interestRate,
        };
    } catch (error) {
        // Return an object with an error message
        return {
            success: false,
            message: error.message,
            returns: null,
            depositAmount: depositAmount,
            interestRate: interestRate,
        };
    }
}

// Example usage:
function main() {
    const depositAmount = 5000;
    const result = calculateInvestmentReturns(depositAmount);
    console.log(`Deposit Amount: ${result.depositAmount}`);
    console.log(`Interest Rate: ${result.interestRate * 100}%`);
    if (result.success) {
        console.log(`Calculated Returns: ${result.returns}`);
        console.log(result.message);
    } else {
        console.error(result.message);
    }
}

main();
```
