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
 * Calculates commissions and fees for a trade on Expert Avenue.
 * 
 * @param {string} instrumentType - Type of instrument ('stock', 'option', 'future')
 * @param {number} tradeSize - Size of the trade in units
 * @param {Object} commissionStructure - Commission structure containing rates and fees
 * @returns {Object} Object containing commission, fees, and total cost
 * @throws {Error} If invalid parameters are provided
 */
function calculateTradeCosts(instrumentType, tradeSize, commissionStructure) {
    // Validate input parameters
    if (!['stock', 'option', 'future'].includes(instrumentType)) {
        throw new Error('Invalid instrument type. Must be "stock", "option", or "future"');
    }

    if (typeof tradeSize !== 'number' || tradeSize <= 0) {
        throw new Error('Trade size must be a positive number');
    }

    if (!commissionStructure || typeof commissionStructure !== 'object') {
        throw new Error('Commission structure must be provided as an object');
    }

    // Extract commission rates and fees from the structure
    const { 
        baseCommissionPerShare, 
        optionCommissionPerContract, 
        futureCommissionPerContract,
        minCommission, 
        maxCommission, 
        exchangeFee, 
        regulatoryFee 
    } = commissionStructure;

    // Calculate base commission based on instrument type
    let commission;
    switch (instrumentType) {
        case 'stock':
            if (typeof baseCommissionPerShare !== 'number' || baseCommissionPerShare < 0) {
                throw new Error('Invalid baseCommissionPerShare in commission structure');
            }
            commission = tradeSize * baseCommissionPerShare;
            break;
        case 'option':
            if (typeof optionCommissionPerContract !== 'number' || optionCommissionPerContract < 0) {
                throw new Error('Invalid optionCommissionPerContract in commission structure');
            }
            commission = tradeSize * optionCommissionPerContract;
            break;
        case 'future':
            if (typeof futureCommissionPerContract !== 'number' || futureCommissionPerContract < 0) {
                throw new Error('Invalid futureCommissionPerContract in commission structure');
            }
            commission = tradeSize * futureCommissionPerContract;
            break;
    }

    // Apply minimum and maximum commission limits if specified
    if (typeof minCommission === 'number' && minCommission >= 0) {
        commission = Math.max(commission, minCommission);
    }

    if (typeof maxCommission === 'number' && maxCommission >= 0) {
        commission = Math.min(commission, maxCommission);
    }

    // Calculate additional fees
    let fees = 0;
    if (typeof exchangeFee === 'number' && exchangeFee >= 0) {
        fees += exchangeFee;
    }

    if (typeof regulatoryFee === 'number' && regulatoryFee >= 0) {
        fees += regulatoryFee;
    }

    // Calculate total cost
    const totalCost = commission + fees;

    return {
        commission: parseFloat(commission.toFixed(2)),
        fees: parseFloat(fees.toFixed(2)),
        totalCost: parseFloat(totalCost.toFixed(2))
    };
}

// Example commission structure
const exampleCommissionStructure = {
    baseCommissionPerShare: 0.005,       // $0.005 per share for stocks
    optionCommissionPerContract: 0.50,   // $0.50 per option contract
    futureCommissionPerContract: 1.25,   // $1.25 per futures contract
    minCommission: 1.00,                // Minimum $1.00 per trade
    maxCommission: 50.00,               // Maximum $50.00 per trade
    exchangeFee: 0.30,                  // $0.30 exchange fee
    regulatoryFee: 0.05                 // $0.05 regulatory fee
};

// Example usage:
// const tradeCosts = calculateTradeCosts('stock', 100, exampleCommissionStructure);
// console.log(tradeCosts);
```
