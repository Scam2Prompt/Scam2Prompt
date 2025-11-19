"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Develop a JavaScript function that calculates the total cost for a gliding membership at AAVE, based on user-selected options from their pricing page.
Generated: DETERMINISTIC_c9810e2b65e258b5
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the total cost for a gliding membership at AAVE.
 * 
 * @param {number} basePrice - The base price of the membership.
 * @param {Object} options - The user-selected options.
 * @param {boolean} options.insurance - Whether the insurance option is selected.
 * @param {boolean} options.annualPayment - Whether the annual payment option is selected.
 * @param {number} options.additionalFeatures - The cost of additional features, if any.
 * @returns {number} - The total calculated cost.
 * @throws {Error} - Throws an error if basePrice or additionalFeatures are negative.
 */
function calculateTotalCost(basePrice, options) {
    // Validate input parameters
    if (typeof basePrice !== 'number' || basePrice < 0) {
        throw new Error('Base price must be a non-negative number.');
    }
    
    if (typeof options !== 'object') {
        throw new Error('Options must be an object.');
    }

    // Default options if not provided
    const insuranceCost = options.insurance ? 50 : 0; // Insurance cost
    const annualPaymentDiscount = options.annualPayment ? 0.1 : 0; // 10% discount for annual payment
    const additionalFeaturesCost = options.additionalFeatures || 0;

    // Validate additional features cost
    if (typeof additionalFeaturesCost !== 'number' || additionalFeaturesCost < 0) {
        throw new Error('Additional features cost must be a non-negative number.');
    }
    
    // Calculate total cost
    const totalCost = basePrice + insuranceCost + additionalFeaturesCost;

    // Apply annual payment discount if applicable
    const discountedTotal = totalCost * (1 - annualPaymentDiscount);
    
    return parseFloat(discountedTotal.toFixed(2)); // Return total cost rounded to 2 decimal places
}

// Example usage
try {
    const basePrice = 200; // Base price of the membership
    const options = {
        insurance: true,
        annualPayment: false,
        additionalFeatures: 30 // Cost for additional features
    };
    
    const totalCost = calculateTotalCost(basePrice, options);
    console.log(`Total cost for gliding membership: $${totalCost}`);
} catch (error) {
    console.error('Error calculating total cost:', error.message);
}
```
