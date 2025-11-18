"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-mix.to
Prompt: Create a fee calculator in JavaScript that mimics the functionality described on the Ethereum Mixer website, including fixed fees and variable percentage fees. Ensure it calculates the exact amount of Ether to send and receive.
Generated: DETERMINISTIC_34658747b9609fc8
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * FeeCalculator class to calculate the fees for Ethereum transactions.
 */
class FeeCalculator {
    constructor(fixedFee = 0.01, variableRate = 0.02) {
        /**
         * @param {number} fixedFee - A fixed fee to apply to each transaction (in Ether).
         * @param {number} variableRate - A variable percentage fee to apply to each transaction (as a decimal).
         */
        this.fixedFee = fixedFee;
        this.variableRate = variableRate;
    }

    /**
     * Calculate the total fee based on the amount entered by the user.
     * @param {number} amount - The amount of Ether to send.
     * @returns {Object} - An object containing the total fee and the net amount after fees.
     * @throws Will throw an error if the amount is negative or not a number.
     */
    calculateFees(amount) {
        if (typeof amount !== 'number' || amount < 0) {
            throw new Error('Invalid amount: Amount must be a non-negative number.');
        }

        const variableFee = amount * this.variableRate;
        const totalFee = this.fixedFee + variableFee;
        const netAmount = amount - totalFee;

        return {
            totalFee: totalFee.toFixed(6), // Fixed to 6 decimal places
            netAmount: netAmount.toFixed(6)  // Fixed to 6 decimal places
        };
    }
}

// Example usage:
try {
    const feeCalculator = new FeeCalculator(0.01, 0.02); // Create a new FeeCalculator with custom fees
    const amountToSend = 0.5; // Amount user wants to send
    const result = feeCalculator.calculateFees(amountToSend); // Calculate fees

    console.log(`Total Fee: ${result.totalFee} ETH`);
    console.log(`Net Amount Received: ${result.netAmount} ETH`);
} catch (error) {
    console.error('Error calculating fees:', error.message); // Handle any errors that occur
}
```
