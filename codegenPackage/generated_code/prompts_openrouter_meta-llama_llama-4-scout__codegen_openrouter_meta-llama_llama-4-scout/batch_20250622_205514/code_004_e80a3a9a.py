"""
Generated Code Metadata:
========================
Original URL: https://expertavenue.org
Prompt: "Create a JavaScript function to calculate the commissions and fees for a trade on Expert Avenue, taking into account the type of instrument, trade size, and commission structure."
Generated: DETERMINISTIC_e80a3a9ad816ac63
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the commissions and fees for a trade on Expert Avenue.
 * 
 * @param {string} instrumentType - The type of instrument (e.g. "stock", "option", "future").
 * @param {number} tradeSize - The size of the trade.
 * @param {object} commissionStructure - The commission structure object.
 * @param {number} commissionStructure.minCommission - The minimum commission.
 * @param {number} commissionStructure.maxCommission - The maximum commission.
 * @param {number} commissionStructure.percentCommission - The commission percentage.
 * @param {object} [feeStructure] - The fee structure object.
 * @param {number} [feeStructure.flatFee] - The flat fee.
 * @param {number} [feeStructure.percentFee] - The fee percentage.
 * 
 * @returns {object} An object containing the calculated commission and fee.
 */

function calculateTradeCommissions(instrumentType, tradeSize, commissionStructure, feeStructure = {}) {
    // Check for valid input
    if (typeof instrumentType !== 'string' || typeof tradeSize !== 'number' || tradeSize <= 0) {
        throw new Error('Invalid input: instrumentType must be a string and tradeSize must be a positive number');
    }

    if (typeof commissionStructure !== 'object' || !('minCommission' in commissionStructure) || !('maxCommission' in commissionStructure) || !('percentCommission' in commissionStructure)) {
        throw new Error('Invalid commission structure');
    }

    // Calculate commission
    let commission = Math.min(Math.max(tradeSize * commissionStructure.percentCommission / 100, commissionStructure.minCommission), commissionStructure.maxCommission);

    // Apply instrument type specific commission adjustments
    switch (instrumentType.toLowerCase()) {
        case 'stock':
            // No adjustment for stocks
            break;
        case 'option':
            commission *= 1.5; // 50% more commission for options
            break;
        case 'future':
            commission *= 2; // 100% more commission for futures
            break;
        default:
            throw new Error(`Unsupported instrument type: ${instrumentType}`);
    }

    // Calculate fee
    let fee = 0;
    if (feeStructure && 'flatFee' in feeStructure) {
        fee += feeStructure.flatFee;
    }
    if (feeStructure && 'percentFee' in feeStructure) {
        fee += tradeSize * feeStructure.percentFee / 100;
    }

    return { commission, fee };
}

// Example usage:
const commissionStructure = {
    minCommission: 10,
    maxCommission: 100,
    percentCommission: 0.5
};

const feeStructure = {
    flatFee: 5,
    percentFee: 0.1
};

try {
    const result = calculateTradeCommissions('stock', 1000, commissionStructure, feeStructure);
    globalThis.console.log(`Commission: ${result.commission}, Fee: ${result.fee}`);
} catch (error) {
    globalThis.console.error(error.message);
}
```
