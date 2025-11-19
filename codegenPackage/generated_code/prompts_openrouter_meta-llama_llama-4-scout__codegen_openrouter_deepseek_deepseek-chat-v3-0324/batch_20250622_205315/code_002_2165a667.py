"""
Generated Code Metadata:
========================
Original URL: https://cosmos-mixer.com
Prompt: Generate a code snippet in JavaScript for calculating the fees for mixing ATOM coins using the Cosmos Mixer fee calculator, taking into account the fixed and variable fees.
Generated: DETERMINISTIC_2165a667772bd531
Batch ID: 20250622_205315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the fees for mixing ATOM coins using the Cosmos Mixer fee calculator.
 * 
 * @param {number} amount - The amount of ATOM to be mixed (in uatom, where 1 ATOM = 1,000,000 uatom)
 * @param {number} fixedFee - The fixed fee for mixing (in uatom)
 * @param {number} variableFeeRate - The variable fee rate (as a decimal, e.g., 0.01 for 1%)
 * @returns {Object} An object containing the total fee and its breakdown
 * @throws {Error} If input parameters are invalid
 */
function calculateMixerFees(amount, fixedFee, variableFeeRate) {
    // Validate input parameters
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Amount must be a positive number');
    }
    if (typeof fixedFee !== 'number' || fixedFee < 0) {
        throw new Error('Fixed fee must be a non-negative number');
    }
    if (typeof variableFeeRate !== 'number' || variableFeeRate < 0 || variableFeeRate > 1) {
        throw new Error('Variable fee rate must be between 0 and 1');
    }

    // Calculate variable fee
    const variableFee = amount * variableFeeRate;
    
    // Calculate total fee
    const totalFee = fixedFee + variableFee;

    return {
        totalFee: totalFee,
        fixedFee: fixedFee,
        variableFee: variableFee,
        variableFeeRate: variableFeeRate
    };
}

// Example usage:
try {
    const amount = 1000000; // 1 ATOM in uatom
    const fixedFee = 1000; // 1000 uatom fixed fee
    const variableRate = 0.005; // 0.5% variable fee
    
    const fees = calculateMixerFees(amount, fixedFee, variableRate);
    console.log('Fee breakdown:', fees);
} catch (error) {
    console.error('Error calculating fees:', error.message);
}
```
