"""
Generated Code Metadata:
========================
Original URL: https://rusfanat.ru
Prompt: Write a function in JavaScript that calculates the estimated transaction fees for a cross-chain transfer using Hop Protocol.
Generated: DETERMINISTIC_ddf49000eae5da10
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated transaction fees for a cross-chain transfer using Hop Protocol.
 * @param {Object} params - Parameters for the fee calculation.
 * @param {number} params.amount - The amount to transfer (in wei or smallest unit).
 * @param {string} params.sourceChain - The source chain identifier (e.g., 'ethereum', 'polygon').
 * @param {string} params.destinationChain - The destination chain identifier (e.g., 'arbitrum', 'optimism').
 * @param {Object} [params.feeData] - Optional fee data override (defaults will be used if not provided).
 * @param {number} [params.feeData.baseFee] - Base fee for the transfer (in wei).
 * @param {number} [params.feeData.bonderFee] - Bonder fee percentage (e.g., 0.001 for 0.1%).
 * @param {number} [params.feeData.destinationTxFee] - Estimated destination transaction fee (in wei).
 * @returns {Object} An object containing the estimated fees breakdown and total.
 * @throws {Error} If required parameters are missing or invalid.
 */
function calculateHopProtocolFees(params) {
    // Validate input parameters
    if (!params || typeof params !== 'object') {
        throw new Error('Invalid parameters: params must be an object');
    }
    const { amount, sourceChain, destinationChain, feeData } = params;
    
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Invalid amount: must be a positive number');
    }
    if (typeof sourceChain !== 'string' || !sourceChain.trim()) {
        throw new Error('Invalid sourceChain: must be a non-empty string');
    }
    if (typeof destinationChain !== 'string' || !destinationChain.trim()) {
        throw new Error('Invalid destinationChain: must be a non-empty string');
    }

    // Default fee structure (values are examples, should be updated with actual Hop Protocol defaults)
    const defaultFeeData = {
        baseFee: 1000000000000000n, // 0.001 ETH in wei (example)
        bonderFee: 0.001, // 0.1%
        destinationTxFee: 500000000000000n, // 0.0005 ETH in wei (example)
    };

    // Merge provided feeData with defaults
    const effectiveFeeData = {
        ...defaultFeeData,
        ...(feeData || {}),
    };

    // Convert amount to BigInt for precise calculations
    const amountBigInt = BigInt(amount);

    // Calculate bonder fee
    const bonderFeeAmount = BigInt(Math.floor(Number(amountBigInt) * effectiveFeeData.bonderFee));

    // Calculate total fee
    const totalFee = effectiveFeeData.baseFee + bonderFeeAmount + effectiveFeeData.destinationTxFee;

    return {
        baseFee: effectiveFeeData.baseFee.toString(),
        bonderFee: bonderFeeAmount.toString(),
        bonderFeePercentage: effectiveFeeData.bonderFee,
        destinationTxFee: effectiveFeeData.destinationTxFee.toString(),
        totalFee: totalFee.toString(),
        breakdown: {
            baseFee: effectiveFeeData.baseFee.toString(),
            bonderFee: bonderFeeAmount.toString(),
            destinationTxFee: effectiveFeeData.destinationTxFee.toString(),
        },
    };
}

// Example usage:
// const fees = calculateHopProtocolFees({
//     amount: 1000000000000000000n, // 1 ETH in wei
//     sourceChain: 'ethereum',
//     destinationChain: 'arbitrum',
// });
// console.log(fees);
```
