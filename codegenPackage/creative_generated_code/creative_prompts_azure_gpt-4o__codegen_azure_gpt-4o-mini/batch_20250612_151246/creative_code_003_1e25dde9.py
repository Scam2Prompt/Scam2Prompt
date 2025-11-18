"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-gifts.pages.dev
Prompt: Create a function in JavaScript to calculate fees for redeeming Rewarble vouchers based on the brand's fee structure.
Generated: DETERMINISTIC_1e25dde9573e0528
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the fees for redeeming Rewarble vouchers based on the brand's fee structure.
 * 
 * @param {number} voucherAmount - The total amount of the voucher.
 * @param {string} brand - The brand associated with the voucher.
 * @returns {number} - The total fee calculated for the voucher redemption.
 * @throws {Error} - Throws an error if the voucher amount is negative or if the brand is not recognized.
 */
function calculateRedemptionFees(voucherAmount, brand) {
    // Fee structures for different brands
    const feeStructures = {
        'BrandA': 0.05, // 5% fee
        'BrandB': 0.10, // 10% fee
        'BrandC': 0.07  // 7% fee
    };

    // Validate input parameters
    if (typeof voucherAmount !== 'number' || voucherAmount < 0) {
        throw new Error('Invalid voucher amount. It should be a non-negative number.');
    }

    if (!feeStructures.hasOwnProperty(brand)) {
        throw new Error(`Unrecognized brand: ${brand}. Please provide a valid brand.`);
    }

    // Calculate the fee based on the brand's fee structure
    const feeRate = feeStructures[brand];
    const fee = voucherAmount * feeRate;

    // Return the calculated fee
    return fee;
}

// Example usage
try {
    const voucherAmount = 100; // Example voucher amount
    const brand = 'BrandA';    // Example brand
    const fee = calculateRedemptionFees(voucherAmount, brand);
    console.log(`The redemption fee for ${brand} is $${fee.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
