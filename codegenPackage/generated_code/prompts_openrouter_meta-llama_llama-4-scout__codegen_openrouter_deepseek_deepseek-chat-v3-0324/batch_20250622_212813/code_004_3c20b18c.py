"""
Generated Code Metadata:
========================
Original URL: https://guardian-associates.com
Prompt: "Create a function in Node.js that takes transaction data and calculates the optimal Rolling Reserve percentage for a business, considering factors discussed in the Guardian Associates' risk assessment process."
Generated: DETERMINISTIC_3c20b18c34287e2c
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the optimal Rolling Reserve percentage based on transaction data and risk factors.
 * 
 * @param {Object} transactionData - The transaction data object
 * @param {Array} transactionData.transactions - Array of transaction amounts
 * @param {number} transactionData.averageTransactionValue - Average transaction value
 * @param {number} transactionData.chargebackRate - Chargeback rate (percentage)
 * @param {number} transactionData.refundRate - Refund rate (percentage)
 * @param {number} transactionData.businessAgeMonths - Age of business in months
 * @param {string} transactionData.industryRisk - Industry risk level ('low', 'medium', 'high')
 * @param {number} transactionData.fraudRate - Fraud rate (percentage)
 * @returns {number} Optimal rolling reserve percentage (0-100)
 * @throws {Error} If input validation fails
 */
function calculateOptimalRollingReserve(transactionData) {
    // Validate input
    if (!transactionData || typeof transactionData !== 'object') {
        throw new Error('Invalid transaction data: must be an object');
    }

    const requiredFields = [
        'transactions', 
        'averageTransactionValue', 
        'chargebackRate', 
        'refundRate', 
        'businessAgeMonths', 
        'industryRisk', 
        'fraudRate'
    ];

    for (const field of requiredFields) {
        if (!(field in transactionData)) {
            throw new Error(`Missing required field: ${field}`);
        }
    }

    if (!Array.isArray(transactionData.transactions)) {
        throw new Error('transactions must be an array');
    }

    // Calculate base factors
    const baseReserve = calculateBaseReserve(
        transactionData.chargebackRate,
        transactionData.refundRate,
        transactionData.fraudRate
    );

    // Apply modifiers based on business profile
    const businessModifier = calculateBusinessModifier(
        transactionData.businessAgeMonths,
        transactionData.industryRisk,
        transactionData.transactions.length
    );

    // Calculate final reserve percentage (clamped between 5% and 30%)
    const reservePercentage = Math.min(Math.max(baseReserve + businessModifier, 5), 30);

    return parseFloat(reservePercentage.toFixed(2));
}

/**
 * Calculates base reserve percentage based on chargeback, refund and fraud rates
 */
function calculateBaseReserve(chargebackRate, refundRate, fraudRate) {
    // Normalize rates (ensure they're between 0-100)
    const normalizedChargeback = Math.min(Math.max(chargebackRate, 0), 100);
    const normalizedRefund = Math.min(Math.max(refundRate, 0), 100);
    const normalizedFraud = Math.min(Math.max(fraudRate, 0), 100);

    // Weighted calculation
    const base = (normalizedChargeback * 0.5) + (normalizedRefund * 0.3) + (normalizedFraud * 0.2);
    
    // Scale to typical reserve range (5-30%)
    return 5 + (base * 0.25);
}

/**
 * Calculates business modifier based on business profile factors
 */
function calculateBusinessModifier(businessAgeMonths, industryRisk, transactionCount) {
    let modifier = 0;

    // Business age modifier (older businesses get lower reserves)
    const ageModifier = Math.max(0, (24 - businessAgeMonths) / 24) * 5;
    modifier += ageModifier;

    // Industry risk modifier
    const riskModifiers = {
        low: -3,
        medium: 0,
        high: 5
    };
    modifier += riskModifiers[industryRisk.toLowerCase()] || 0;

    // Transaction volume modifier (more transactions = lower reserve)
    const volumeModifier = -Math.min(5, transactionCount / 1000);
    modifier += volumeModifier;

    return modifier;
}

module.exports = { calculateOptimalRollingReserve };
```
