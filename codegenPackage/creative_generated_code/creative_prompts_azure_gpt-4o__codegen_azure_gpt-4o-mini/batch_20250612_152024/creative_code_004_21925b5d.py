"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aicryptoexm.com
Prompt: Write a JavaScript function to calculate profit and loss for crypto derivatives trades based on input parameters like entry price, exit price, and leverage.
Generated: DETERMINISTIC_21925b5d9442fcb0
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the profit or loss for crypto derivatives trades.
 * 
 * @param {number} entryPrice - The price at which the asset was bought.
 * @param {number} exitPrice - The price at which the asset was sold.
 * @param {number} quantity - The amount of the asset traded.
 * @param {number} leverage - The leverage used in the trade (e.g., 2 for 2x leverage).
 * @returns {object} - An object containing the profit/loss and the percentage of profit/loss.
 * @throws {Error} - Throws an error if any parameter is invalid.
 */
function calculateProfitLoss(entryPrice, exitPrice, quantity, leverage) {
    // Validate input parameters
    if (typeof entryPrice !== 'number' || entryPrice <= 0) {
        throw new Error('Invalid entry price. It must be a positive number.');
    }
    if (typeof exitPrice !== 'number' || exitPrice <= 0) {
        throw new Error('Invalid exit price. It must be a positive number.');
    }
    if (typeof quantity !== 'number' || quantity <= 0) {
        throw new Error('Invalid quantity. It must be a positive number.');
    }
    if (typeof leverage !== 'number' || leverage <= 0) {
        throw new Error('Invalid leverage. It must be a positive number.');
    }

    // Calculate total invested amount
    const totalInvestment = entryPrice * quantity;
    
    // Calculate total exit value
    const totalExitValue = exitPrice * quantity;

    // Calculate profit/loss
    const profitLoss = (totalExitValue - totalInvestment) * leverage;

    // Calculate percentage profit/loss
    const percentageProfitLoss = (profitLoss / totalInvestment) * 100;

    return {
        profitLoss: profitLoss,
        percentageProfitLoss: percentageProfitLoss.toFixed(2) + '%'
    };
}

// Example usage:
try {
    const result = calculateProfitLoss(100, 120, 1, 10);
    console.log(`Profit/Loss: $${result.profitLoss}, Percentage: ${result.percentageProfitLoss}`);
} catch (error) {
    console.error('Error:', error.message);
}
```
