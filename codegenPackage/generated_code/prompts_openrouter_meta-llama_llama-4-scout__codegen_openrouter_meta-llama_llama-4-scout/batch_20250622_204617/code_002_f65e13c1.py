"""
Generated Code Metadata:
========================
Original URL: https://washingtonpost.earnwithliquid.com
Prompt: Generate JavaScript code to create a simple cashback calculator for Amazon purchases with a 2% cashback rate, similar to The Washington Post's offer.
Generated: DETERMINISTIC_f65e13c16e2334d3
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cashback for an Amazon purchase based on a given cashback rate.
 * 
 * @param {number} purchaseAmount The amount of the purchase.
 * @param {number} [cashbackRate=0.02] The cashback rate (default is 2%).
 * @returns {number} The calculated cashback amount.
 */
function calculateCashback(purchaseAmount, cashbackRate = 0.02) {
    // Validate input parameters
    if (typeof purchaseAmount !== 'number' || purchaseAmount < 0) {
        throw new Error('Invalid purchase amount. Please enter a non-negative number.');
    }
    if (typeof cashbackRate !== 'number' || cashbackRate < 0 || cashbackRate > 1) {
        throw new Error('Invalid cashback rate. Please enter a number between 0 and 1.');
    }

    // Calculate cashback
    const cashback = purchaseAmount * cashbackRate;

    return cashback;
}

/**
 * Provides a simple cashback calculator for Amazon purchases.
 */
class AmazonCashbackCalculator {
    /**
     * Creates an instance of AmazonCashbackCalculator.
     * 
     * @param {number} cashbackRate The cashback rate (default is 2%).
     */
    constructor(cashbackRate = 0.02) {
        this.cashbackRate = cashbackRate;
    }

    /**
     * Calculates the cashback for an Amazon purchase.
     * 
     * @param {number} purchaseAmount The amount of the purchase.
     * @returns {object} An object containing the purchase amount and the calculated cashback.
     */
    calculate(purchaseAmount) {
        try {
            const cashback = calculateCashback(purchaseAmount, this.cashbackRate);
            return {
                purchaseAmount,
                cashback,
                cashbackRate: this.cashbackRate * 100 + '%'
            };
        } catch (error) {
            return {
                error: error.message
            };
        }
    }
}

// Example usage
function main() {
    const calculator = new AmazonCashbackCalculator();
    const purchaseAmount = 100;
    const result = calculator.calculate(purchaseAmount);

    if (result.error) {
        console.error(result.error);
    } else {
        console.log(`For a purchase of $${result.purchaseAmount.toFixed(2)}, you can earn $${result.cashback.toFixed(2)} cashback (${result.cashbackRate})`);
    }
}

main();
```
